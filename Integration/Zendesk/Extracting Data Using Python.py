# Set Up: Install the necessary Python library and set up your API credentials.
# pip install Zendesk
# pip install zenpy

from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket
from datetime import datetime

# Credentials setup
creds = {
    'email' : 'your_email@example.com',
    'token' : 'your_api_token',
    'subdomain': 'your_subdomain'
}

# Initialize the Zenpy client
client = Zenpy(**creds)

# Function to fetch tickets and comments
def fetch_tickets_and_comments():
    tickets = client.tickets.list()  # This fetches all tickets; can be filtered
    for ticket in tickets:
        print(f"Ticket ID: {ticket.id}, Subject: '{ticket.subject}'")
        comments = client.tickets.comments(ticket=ticket)
        for comment in comments:
            print(f" - Comment by {comment.author_id}: {comment.body[:50]}...")  # Displaying first 50 chars

# Call the function
fetch_tickets_and_comments()

