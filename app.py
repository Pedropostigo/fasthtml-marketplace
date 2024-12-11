from datetime import datetime

from fasthtml.common import FastHTML, serve, RedirectResponse

from app_src.events.create_event import CreateEventForm, Event

from database.database import DataBase

app = FastHTML()

@app.get("/")
def home():
    return CreateEventForm().render()

@app.post("/create_event")
def create_event(event:Event):

    if CreateEventForm._validate_event(event):
        db = DataBase()
        date, time = event.event_date_time.split("T")
        year, month, day = date.split("-")
        hour, minute = time.split(":")
        db.insert_event(event_name = event.event_name, 
                        event_date_time = datetime(int(year), int(month), int(day), int(hour), int(minute), 0))

    return CreateEventForm().render_success_creating_event(event)

serve()