import os

# Splunk HEC connection
SPLUNK_HEC_URL = os.getenv("SPLUNK_HEC_URL")
SPLUNK_HEC_TOKEN = os.getenv("SPLUNK_HEC_TOKEN")

# Event metadata
SPLUNK_INDEX = os.getenv("SPLUNK_INDEX", "supply_chain")
SPLUNK_SOURCE = os.getenv("SPLUNK_SOURCE", "github-actions")
SPLUNK_SOURCETYPE = os.getenv("SPLUNK_SOURCETYPE", "_json")