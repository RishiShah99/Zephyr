import datetime as dt
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def test():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        # Code to create new event 
        event = {
            'summary': 'My Python Event',
            'location': 'Test Location',
            'description': 'Test Description',
            'colorId': '6',
            'start': {
                'dateTime': '2024-07-05T09:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': '2024-07-05T10:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            }, 
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=2'
            ],
            'attendees': [
                {'email': 'rishishah994@gmail.com'},
            ]
        }
        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f'Event created: {event.get("htmlLink")}')

       
        # now = dt.datetime.now().isoformat() + 'Z'

        # # Code to list all events in the next 10 days
        # event_result = service.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
        # events = event_result.get('items', [])

        # if not events:
        #     print('No upcoming events found.')
        # for event in events:
        #     start = event['start'].get('dateTime', event['start'].get('date'))
        #     print(f"Event: {event['summary']} starts at {start}")
    except HttpError as error:
        print(f'An error occurred: {error}')


test()
