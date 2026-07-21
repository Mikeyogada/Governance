import json


def send_to_splunk(event):

    print("Sending event to Splunk")

    print(json.dumps(event.__dict__, indent=2)) #print the event as a JSON object