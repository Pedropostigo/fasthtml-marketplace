from fasthtml.common import Table, Tr, Td, Th

from app_src.events.event import Event

from database.database import DataBase

class EventList():

    def __init__(self):
        pass
    
    @staticmethod
    def _render_event(event:Event):
        return Tr(
            Td(event.event_name),
            Td(event.event_date_time)
        )
    
    @staticmethod
    def _render_event_list():

        events = DataBase().get_events()
        events = [Event(**event) for event in events]

        print(events)

        return Table(
            Th("Event Name"),
            Th("Event Date"),
            id = "event_list_table"
        )
    
if __name__ == "__main__":

    event_list = EventList()
    event_list._render_event_list()