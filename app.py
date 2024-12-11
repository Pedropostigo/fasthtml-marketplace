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
        db.insert_event(event_name = event.event_name, event_date_time = event.event_date_time)

    return CreateEventForm().render_success_creating_event(event)

serve()