# Email Spam Filter

This script is a simple email spam filter that connects to a Gmail account using IMAP, retrieves emails from the inbox, and moves any identified spam emails to the spam folder.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your machine
- The required dependencies installed: `imapclient`, `pyzmail`, `tqdm`

You can install the dependencies using `pip`:

```
pip install imapclient pyzmail tqdm
```

## Configuration

1. Open the script file in a text editor or integrated development environment (IDE).
2. Set the `spam_list` variable to include the names of known spammers. For example:

   ```python
   spam_list = ['Spammer1', 'Spammer2', 'Spammer3']
   ```

3. Replace `'your_gmail_account@gmail.com'` with your actual Gmail email address in the `server.login` function call.
4. Replace `'password'` with your Gmail password and two-step generated password in the `server.login` function call.

## Usage

1. Save the script with a `.py` extension (e.g., `spam_filter.py`).
2. Open a terminal or command prompt and navigate to the directory where the script is saved.
3. Run the script using the following command:

   ```
   python spam_filter.py
   ```

## Notes

- This script connects to Gmail's IMAP server (`imap.gmail.com`) using SSL encryption.
- If there is no internet connection, a message will be displayed.
- The script fetches all emails from the inbox and checks if the sender's address matches any entry in the `spam_list`.
- Any identified spam emails will be moved to the `[Gmail]/Spam` folder.

