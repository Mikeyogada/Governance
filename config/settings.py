import os



# Splunk HEC connection
SPLUNK_HEC_URL = os.getenv(
    "SPLUNK_HEC_URL",
    "https://localhost:8088/services/collector/event"
)

SPLUNK_HEC_TOKEN = os.getenv("SPLUNK_HEC_TOKEN" "55ec52a9-9f4c-424f-9061-ce390a859a27")#HEC token for Splunk HEC authentication. This token is used to authenticate the requests sent to the Splunk HEC endpoint. It is important to keep this token secure and not expose it in public repositories or logs.

# Event metadata
SPLUNK_INDEX = os.getenv("SPLUNK_INDEX", "supply_chain")
SPLUNK_SOURCE = os.getenv("SPLUNK_SOURCE", "github-actions")
SPLUNK_SOURCETYPE = os.getenv("SPLUNK_SOURCETYPE", "_json")