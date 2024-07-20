import datetime as dt
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_creds():
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
    return creds

def create_event(name, location=None, description=None, color=6):
    creds = get_creds()
    try:
        service = build('calendar', 'v3', credentials=creds)
        event = {
            'summary': name if name else 'My Python Event',
            'location': location,
            'description': description,
            'colorId': color,
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
    except HttpError as error:
        print(f'An error occurred: {error}')

def see_future_events():
    creds = get_creds()
    try:
        service = build('calendar', 'v3', credentials=creds)
        now = dt.datetime.now().isoformat() + 'Z'
        event_result = service.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = event_result.get('items', [])
        if not events:
            return 'No upcoming events found.'
        events_list = []
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            events_list.append(f"Event: {event['summary']} starts at {start}")
        return "\n".join(events_list)
    except HttpError as error:
        print(f'An error occurred: {error}')
        return 'Failed to fetch events.'
