import requests

# Zendesk API to fetch tickets
zendesk_url = "https://yourcompany.zendesk.com/api/v2/tickets.json"
zendesk_headers = {
    "Authorization": "Bearer your_zendesk_api_token"
}

response = requests.get(zendesk_url, headers=zendesk_headers)
tickets = response.json()

# Salesforce API to create/update cases
salesforce_url = "https://your_instance.salesforce.com/services/data/vXX.0/sobjects/Case/"
salesforce_headers = {
    "Authorization": "Bearer your_salesforce_access_token",
    "Content-Type": "application/json"
}

for ticket in tickets['tickets']:
    case_data = {
        "Subject": ticket['subject'],
        "Description": ticket['description'],
        "Origin": "Zendesk",
        "Status": "New"  # Mapping example
    }
    response = requests.post(salesforce_url, headers=salesforce_headers, json=case_data)
    if response.status_code == 201:
        print("Case created in Salesforce")
