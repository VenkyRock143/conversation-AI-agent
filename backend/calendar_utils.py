# import os
# import pickle
# import datetime
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from googleapiclient.discovery import build
# from dateutil.parser import parse

# SCOPES = ['https://www.googleapis.com/auth/calendar']


# def get_calendar_service():
#     creds = None
#     token_file = os.getenv("token_file", "token.json")
#     if os.path.exists(token_file):
#         with open(token_file, 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_config({
#                 "installed": {
#                     "client_id": os.getenv("GOOGLE_CLIENT_ID"),
#                     "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
#                     # "redirect_uris": [os.getenv("GOOGLE_REDIRECT_URI")],
#                     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#                     "token_uri": "https://oauth2.googleapis.com/token"
#                 }
#             }, SCOPES)
#             creds = flow.run_local_server(port=8000)
#         with open(token_file, 'wb') as token:
#             pickle.dump(creds, token)
#     return build('calendar', 'v3', credentials=creds)


# def check_availability(start_time, end_time):
#     service = get_calendar_service()
#     body = {
#         "timeMin": start_time.isoformat() + 'Z',
#         "timeMax": end_time.isoformat() + 'Z',
#         "items": [{"id": os.getenv("calendar_id", "primary")}]
#     }
#     events = service.freebusy().query(body=body).execute()
#     return not events['calendars'][os.getenv("calendar_id", "primary")]['busy']


# def create_event(summary, start_time, end_time):
#     service = get_calendar_service()
#     event = {
#         'summary': summary,
#         'start': {'dateTime': start_time.isoformat(), 'timeZone': 'UTC'},
#         'end': {'dateTime': end_time.isoformat(), 'timeZone': 'UTC'}
#     }
#     return service.events().insert(calendarId=os.getenv("calendar_id", "primary"), body=event).execute()

import os
import pickle
import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None
    token_file = os.getenv("token_file", "token.json")

    if os.path.exists(token_file):
        with open(token_file, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config({
                "installed": {
                    "client_id": os.getenv("GOOGLE_CLIENT_ID"),
                    "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token"
                }
            }, SCOPES)
            creds = flow.run_local_server(port=8080)

        with open(token_file, 'wb') as token:
            pickle.dump(creds, token)

    return build('calendar', 'v3', credentials=creds)

def check_availability(start_time, end_time):
    service = get_calendar_service()
    body = {
        "timeMin": start_time.isoformat() + 'Z',
        "timeMax": end_time.isoformat() + 'Z',
        "items": [{"id": os.getenv("calendar_id", "primary")}]
    }
    events = service.freebusy().query(body=body).execute()
    return not events['calendars'][os.getenv("calendar_id", "primary")]['busy']

def create_event(summary, start_time, end_time):
    service = get_calendar_service()
    event = {
        'summary': summary,
        'start': {'dateTime': start_time.isoformat(), 'timeZone': 'UTC'},
        'end': {'dateTime': end_time.isoformat(), 'timeZone': 'UTC'}
    }
    return service.events().insert(calendarId=os.getenv("calendar_id", "primary"), body=event).execute()
