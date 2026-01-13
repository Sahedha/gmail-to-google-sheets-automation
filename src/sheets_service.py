import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from config import SHEETS_SCOPES
from config import SPREADSHEET_ID, SHEET_NAME

TOKEN_FILE = "credentials/sheets_token.pickle"

def get_sheets_service():
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
                SHEETS_SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(creds, token)

    return build("sheets", "v4", credentials=creds)


def append_row(service, row):
    body = {
        "values": [row]
    }

    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_NAME,
        valueInputOption="RAW",
        body=body
    ).execute()

