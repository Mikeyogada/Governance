from adapters.splunk import send_to_splunk
from adapters.simplerisk import send_to_simplerisk


def route(event):
    print("Routing event...")

    send_to_splunk(event)
    send_to_simplerisk(event)

    print("Routing complete.")

#creat adapters for both splunk and simplerisk. The send_to_splunk function will send the event to Splunk, while the send_to_simplerisk function will send the event to SimpleRisk. You can implement these functions in their respective adapter files.
