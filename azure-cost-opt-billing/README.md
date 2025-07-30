# Azure Cost Optimization for Billing Records

## Overview
Serverless architecture using Azure Cosmos DB and Blob Storage to reduce costs for billing records.

## Key Features
- Active records in Cosmos DB
- Archived records in Azure Blob Storage
- Seamless access through Azure Function

## Components
- API Layer
- Archival Function
- Blob Storage

## Setup Instructions
1. Set your Azure credentials.
2. Deploy infrastructure.
3. Set timers for archival.
4. Test the API.


## Production Considerations
- Retry and error handling in archival jobs
- Logging and monitoring with Azure Monitor
- Alerting on Blob access failures
- Secure secrets using Key Vault
- Schema evolution management
- Throttling and rate-limiting access to avoid cost spikes
