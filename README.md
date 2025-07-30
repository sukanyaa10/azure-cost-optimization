# azure-cost-optimization

# 🚀 Prompt Used with ChatGPT:

> **Cost Optimization Challenge: Managing Billing Records in Azure Serverless Architecture.We have a serverless architecture in Azure, where one of our services stores billing records in Azure Cosmos DB. The system is read-heavy, but records older than three months are rarely accessed.

Over the past few years, the database size has significantly grown, leading to increased costs. We need an efficient way to reduce costs while maintaining data availability.

### ✅ Response Summary:
I worked with ChatGPT to explore a cost-efficient, scalable solution using tiered storage (Cosmos DB + Blob Storage) without altering the existing APIs or causing downtime. I went beyond surface-level ideas by:

- Implementing fallback logic from Cosmos DB to Blob Storage in the API layer  
- Adding scheduled archival with Cosmos deletion logic  
- Highlighting production risks like schema drift, retry failures, or cold blob latency  
- Designing a modular repo with pseudocode and architecture details  

---



