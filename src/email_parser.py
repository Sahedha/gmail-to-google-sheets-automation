import base64

def parse_email(service, msg_id):
    message = service.users().messages().get(
        userId="me",
        id=msg_id,
        format="full"
    ).execute()

    headers = message["payload"]["headers"]
    payload = message["payload"]

    def get_header(name):
        for h in headers:
            if h["name"] == name:
                return h["value"]
        return ""

    body = ""

    # Plain text body
    if "data" in payload.get("body", {}):
        body = payload["body"]["data"]
    elif payload.get("parts"):
        for part in payload.get("parts"):
            if part["mimeType"] == "text/plain" and "data" in part["body"]:
                body = part["body"]["data"]
                break

    if body:
        body = base64.urlsafe_b64decode(body).decode("utf-8", errors="ignore")

    return {
        "from": get_header("From"),
        "subject": get_header("Subject"),
        "date": get_header("Date"),
        "content": body.strip()
    }
