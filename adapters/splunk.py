import json
import requests

from config.settings import (
    SPLUNK_HEC_URL,
    SPLUNK_HEC_TOKEN,
    SPLUNK_INDEX,
    SPLUNK_SOURCE,
    SPLUNK_SOURCETYPE,
)


def build_headers():
    return {
        "Authorization": f"Splunk {SPLUNK_HEC_TOKEN}",
        "Content-Type": "application/json",
    }


def build_payload(event):
    return {
        "index": SPLUNK_INDEX,
        "source": SPLUNK_SOURCE,
        "sourcetype": SPLUNK_SOURCETYPE,
        "host": event.repo,
        "event": event.__dict__,
    }


def send_to_splunk(event):

    payload = build_payload(event)

    print(json.dumps(payload, indent=2))

    response = requests.post(
        SPLUNK_HEC_URL,
        headers=build_headers(),
        json=payload,
        verify=False,
    )

    if response.status_code == 200:
        print("Event sent to Splunk successfully")
    else:
        print(f"Failed to send event: {response.text}")

    return response