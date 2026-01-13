# Gmail to Google Sheets Automation

**Author:** Sahedha Shaik

## 📖 Project Overview
This project is a Python-based automation system that reads real unread emails from a Gmail inbox and logs them into a Google Sheet using official Google APIs.

## 🏗️ Architecture
Gmail Inbox → Gmail API → Email Parser → State Check → Google Sheets API → Google Sheet

## 🔐 Authentication
OAuth 2.0 Installed App flow is used to securely access Gmail and Google Sheets. User consent is required only on the first run, and access tokens are stored locally for reuse.

## ⚙️ Features
- Reads unread emails from Gmail Inbox
- Extracts sender, subject, date, and body
- Appends email data to Google Sheets
- Marks processed emails as read
- Prevents duplicate processing using local state
- Subject-based email filtering (Bonus)

## 🧠 Duplicate Prevention Logic
Each Gmail message has a unique and immutable message ID. Processed message IDs are stored in a local `state.json` file. On subsequent runs, emails with IDs already present in the state file are skipped, ensuring idempotent execution.

## 💾 State Persistence
State is stored locally in `state.json` as a list of processed email IDs. This lightweight approach avoids the need for a database while ensuring safe re-runs of the script.

## 🛠️ Setup Instructions
1. Clone the repository
2. Create and activate a Python virtual environment
3. Install dependencies using `pip install -r requirements.txt`
4. Create a Google Cloud project and enable Gmail & Sheets APIs
5. Configure OAuth consent screen and download `credentials.json`
6. Place `credentials.json` inside the `credentials/` folder
7. Run the script using `python src/main.py`

## 🚧 Challenges Faced
Handling duplicate email processing was challenging. This was solved by implementing state persistence using Gmail message IDs and adding defensive JSON handling to prevent crashes due to empty state files.

## ⚠️ Limitations
- Only plain text email bodies are fully supported
- API rate limits may apply for large inboxes
- Script processes only unread inbox emails

## 📸 Proof of Execution
Screenshots and execution proof are available in the `/proof` folder.

