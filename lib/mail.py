from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from bs4 import BeautifulSoup 


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def main():
    apps = {'apps':[]}
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    # pylint: disable=no-member
    results = service.users().messages().list(userId='me',labelIds = ['INBOX', 'UNREAD']).execute()
    messages = results.get('messages', [])

    if not messages:
        return None
    else:
        for message in messages:
            msg = service.users().messages().modify(userId='me', id=message['id'], body={'removeLabelIds': ['UNREAD']}).execute()
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            subject = (msg['payload']['headers'][17]['value'])
            if subject == "Guild Application":
                data = msg['payload']['parts'][0]['body']['data']
                data = base64.urlsafe_b64decode(data)
                body = BeautifulSoup(data, 'lxml').body
                body = str(body)[9:].split('----')[0]
                apps['apps'].append(body)
        return apps
if __name__ == '__main__':
    main()