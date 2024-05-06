import requests

# Get Databricks Host and Token:
# You need the Databricks host URL and a personal access token (PAT) to authenticate your requests.
# Generate a PAT from the Databricks workspace by navigating to User Settings > Access Tokens.

DATABRICKS_TOKEN = 'YOUR_TOKEN'
DATABRICKS_API_URL = 'https://<your-databricks-instance>.cloud.databricks.com/api/2.0/clusters/list'

headers = {
    'Authorization': f'Bearer {DATABRICKS_TOKEN}'
}

response = requests.get(DATABRICKS_API_URL, headers=headers)
print(response.json())
