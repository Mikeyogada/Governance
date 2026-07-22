import json

from config.settings import (
    SPLUNK_INDEX,
    SPLUNK_SOURCE,
    SPLUNK_SOURCETYPE,
)

def build_payload(event):
    """
    Build the payload for Splunk HEC.
    """
    payload = {
        "index": SPLUNK_INDEX,
        "source": SPLUNK_SOURCE,
        "sourcetype": SPLUNK_SOURCETYPE,
        "host": event.repo,
        "event": event.__dict__
    }
    
    return payload
#payload etl to fit splunk hec format. The build_payload function takes a SupplyChainEvent object as input and returns a dictionary that represents the payload to be sent to Splunk HEC. The payload includes the timestamp, host (repository), source, sourcetype, and the event data itself. 


def send_to_splunk(event):

    print("Sending event to Splunk")

    payload = build_payload(event)

    print(json.dumps(payload, indent=2)) #print the payload as a JSON object

