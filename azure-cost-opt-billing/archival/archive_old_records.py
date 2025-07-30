from datetime import datetime, timedelta
import azure.cosmos.cosmos_client as cosmos_client
from azure.storage.blob import BlobServiceClient
import json

COSMOS_ENDPOINT = "<cosmos_endpoint>"
COSMOS_KEY = "<cosmos_key>"
DATABASE_NAME = "BillingDB"
CONTAINER_NAME = "Records"
BLOB_CONNECTION_STRING = "<blob_connection_string>"
BLOB_CONTAINER = "archived-billing"

cutoff_date = (datetime.utcnow() - timedelta(days=90)).isoformat()

def archive_old_records():
    client = cosmos_client.CosmosClient(COSMOS_ENDPOINT, {'masterKey': COSMOS_KEY})
    container = client.get_database_client(DATABASE_NAME).get_container_client(CONTAINER_NAME)
    query = f"SELECT * FROM c WHERE c.timestamp < '{cutoff_date}'"
    old_records = list(container.query_items(query=query, enable_cross_partition_query=True))
    blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
    blob_container_client = blob_service_client.get_container_client(BLOB_CONTAINER)

    for record in old_records:
        blob_name = f"{record['id']}.json"
        blob_container_client.upload_blob(name=blob_name, data=json.dumps(record), overwrite=True)
        container.delete_item(record, partition_key=record['partitionKey'])
