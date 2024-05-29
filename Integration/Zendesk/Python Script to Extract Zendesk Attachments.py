import requests
import os

# Constants
ZENDESK_DOMAIN = 'your_zendesk_domain'
ZENDESK_EMAIL = 'your_email'
ZENDESK_TOKEN = 'your_api_token'

def zendesk_auth():
    """Returns HTTP basic authentication tuple."""
    return (ZENDESK_EMAIL + '/token', ZENDESK_TOKEN)

def fetch_tickets_with_attachments():
    """Fetch tickets and filter those with attachments."""
    tickets_url = f'https://{ZENDESK_DOMAIN}.zendesk.com/api/v2/tickets.json'
    response = requests.get(tickets_url, auth=zendesk_auth())
    tickets = response.json().get('tickets', [])
    
    # Filtering tickets that have attachments
    tickets_with_attachments = [ticket for ticket in tickets if ticket['has_attachments']]
    return tickets_with_attachments

def download_attachments(tickets):
    """Download attachments from given tickets."""
    for ticket in tickets:
        ticket_id = ticket['id']
        attachments_url = f'https://{ZENDESK_DOMAIN}.zendesk.com/api/v2/tickets/{ticket_id}/comments.json'
        response = requests.get(attachments_url, auth=zendesk_auth())
        comments = response.json().get('comments', [])
        
        for comment in comments:
            for attachment in comment.get('attachments', []):
                file_url = attachment['content_url']
                file_name = attachment['file_name']
                download_file(file_url, file_name)

def download_file(url, file_name):
    """Helper function to download a file from a given URL."""
    response = requests.get(url, auth=zendesk_auth(), stream=True)
    if response.status_code == 200:
        with open(file_name, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f'Downloaded {file_name}')

# Main Execution
if __name__ == '__main__':
    tickets = fetch_tickets_with_attachments()
    download_attachments(tickets)
