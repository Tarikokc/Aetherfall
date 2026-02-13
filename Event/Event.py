class Event:

    def trigger_event(event,*args):
        print("SPECIAL EVENT")
        event.triggered(args)