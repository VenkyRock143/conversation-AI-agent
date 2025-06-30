# from datetime import datetime, timedelta
# from dateutil import parser
# from app.calendar_utils import check_availability, create_event


# def interpret_message(message):
#     if "tomorrow" in message.lower():
#         start = datetime.utcnow() + timedelta(days=1, hours=15)
#         end = start + timedelta(hours=1)
#     elif "friday" in message.lower():
#         today = datetime.utcnow()
#         friday = today + timedelta((4 - today.weekday()) % 7)
#         start = friday.replace(hour=15, minute=0)
#         end = start + timedelta(hours=1)
#     else:
#         try:
#             start = parser.parse(message, fuzzy=True)
#             end = start + timedelta(hours=1)
#         except:
#             return "I'm sorry, I couldn't understand the time. Can you rephrase?"

#     available = check_availability(start, end)
#     if available:
#         create_event("User Booking", start, end)
#         return f"✅ Your appointment has been booked for {start.strftime('%A, %d %B %Y %I:%M %p UTC')}"
#     else:
#         return "Sorry, that time is already booked. Can you try another time?"

from datetime import datetime, timedelta
from dateutil import parser
from app.calendar_utils import check_availability, create_event

def interpret_message(message):
    try:
        if "tomorrow" in message.lower():
            start = datetime.utcnow() + timedelta(days=1, hours=15)
        elif "friday" in message.lower():
            today = datetime.utcnow()
            friday = today + timedelta((4 - today.weekday()) % 7)
            start = friday.replace(hour=15, minute=0)
        else:
            start = parser.parse(message, fuzzy=True)

        end = start + timedelta(hours=1)

        available = check_availability(start, end)
        if available:
            create_event("User Booking", start, end)
            return f"✅ Your appointment has been booked for {start.strftime('%A, %d %B %Y %I:%M %p UTC')}"
        else:
            return "❌ Sorry, that time is already booked. Can you try another time?"

    except Exception as e:
        return f"❌ Error: {str(e)}. Please try again with a clear time."