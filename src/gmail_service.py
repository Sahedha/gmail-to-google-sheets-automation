import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from config import GMAIL_SCOPES

TOKEN_FILE = "credentials/gmail_token.pickle"

def get_gmail_service():
    creds = None

    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials/credentials.json",
                GMAIL_SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(creds, token)

    return build("gmail", "v1", credentials=creds)

def fetch_unread_emails(service):
    results = service.users().messages().list(
        userId="me",
        labelIds=["INBOX", "UNREAD"]
    ).execute()

    return results.get("messages", [])

