import os



# Splunk HEC connection
SPLUNK_HEC_URL = os.getenv("SPLUNK_HEC_URL")  # URL for Splunk HEC endpoint. This is the endpoint where events will be sent for indexing in Splunk. It should be in the format "https://<splunk-server>:8088/services/collector".
SPLUNK_HEC_TOKEN = os.getenv("SPLUNK_HEC_TOKEN")  # HEC token for Splunk HEC authentication. This token is used to authenticate the requests sent to the Splunk HEC endpoint. It is important to keep this token secure and not expose it in public repositories or logs.

# Event metadata
SPLUNK_INDEX = os.getenv("SPLUNK_INDEX", "supply_chain")
SPLUNK_SOURCE = os.getenv("SPLUNK_SOURCE", "github-actions")
SPLUNK_SOURCETYPE = os.getenv("SPLUNK_SOURCETYPE", "_json")