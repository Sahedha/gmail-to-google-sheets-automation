#import sys
#import os

# Add project root to Python path
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from gmail_service import get_gmail_service

#if __name__ == "__main__":
#    service = get_gmail_service()
#    print("✅ Gmail authentication successful!")


#from sheets_service import get_sheets_service


#if __name__ == "__main__":
#    service = get_sheets_service()
#    print("✅ Google Sheets authentication successful!")



#from gmail_service import get_gmail_service, fetch_unread_emails

#if __name__ == "__main__":
#    service = get_gmail_service()
#    messages = fetch_unread_emails(service)

#    print(f"📩 Unread emails found: {len(messages)}")

#    if messages:
#        print("First email ID:", messages[0]["id"])



#from gmail_service import get_gmail_service, fetch_unread_emails
#from email_parser import parse_email

#if __name__ == "__main__":
#    service = get_gmail_service()
#    messages = fetch_unread_emails(service)

#    if not messages:
#        print("No unread emails.")
#        exit()

#    first_msg_id = messages[0]["id"]
#    email_data = parse_email(service, first_msg_id)

#    print("📧 Parsed Email:")
#    print("From:", email_data["from"])
#    print("Subject:", email_data["subject"])
#    print("Date:", email_data["date"])
#    print("Content (first 200 chars):")
#    print(email_data["content"][:200])

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gmail_service import get_gmail_service, fetch_unread_emails
from sheets_service import get_sheets_service, append_row
from email_parser import parse_email
from state import load_state, save_state

def main():
    gmail = get_gmail_service()
    sheets = get_sheets_service()

    processed_ids = load_state()
    messages = fetch_unread_emails(gmail)

    print(f"📩 Unread emails found: {len(messages)}")

    for msg in messages:
        msg_id = msg["id"]

        if msg_id in processed_ids:
            continue  # duplicate protection

        email = parse_email(gmail, msg_id)

        append_row(sheets, [
            email["from"],
            email["subject"],
            email["date"],
            email["content"]
        ])

        # Mark email as read ONLY after successful append
        gmail.users().messages().modify(
            userId="me",
            id=msg_id,
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()

        processed_ids.add(msg_id)

    save_state(processed_ids)
    print("✅ Processing complete")

if __name__ == "__main__":
    main()


