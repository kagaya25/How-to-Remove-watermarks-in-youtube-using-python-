from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey

CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)

request = youtube.watermarks().unset(
        channelId="UCiBfuUreTbKvBKtQbb6SIWQ" # change this to your channels ids
    )
request.execute()

