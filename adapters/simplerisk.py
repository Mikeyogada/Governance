import json

def send_to_simplerisk(event):

    print("Sending event to SimpleRisk")

    print(json.dumps(event.__dict__, indent=2))  #print the event as a JSON object