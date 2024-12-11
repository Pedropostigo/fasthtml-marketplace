from fasthtml.common import Div, H3, P, Form, Input, Button

from app_src.styles.sucess_message_style import SUCCESS_MESSAGE_STYLE
from app_src.events.event import Event

class CreateEventForm():

    def __init__(self):
        pass
    
    @staticmethod
    def _validate_event(event:Event):
        return True
    
    def render_create_event_form(self):
        return Div(
            H3("Create Event", id = "create_event_title", hx_target="#create_event_form_content"),
            Form(
                Input(type="text", name="event_name", label="Event Name"),
                Input(type="datetime-local", name="event_date_time", label="Event Date"),
                Button("Create Event", type="submit"),
                hx_post="/create_event",
                hx_target="#create_event_form_content",
                hx_swap="innerHTML"

            )
        )
    
    def render_success_creating_event(self, event:Event):
        return Div(
            P(f"Event {event.event_name} created sucessfully!", style = SUCCESS_MESSAGE_STYLE)
        )

    def render(self):

        form = self.render_create_event_form()
        return Div(
            form,
            Div(id="create_event_form_content"),
            id = "create_event_div"
        )