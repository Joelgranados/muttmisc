#!/usr/bin/env python3
import sys
import lib.ical_parser
import lib.todoist_api
import json

def get_token():
    confi_file = "todoist_token.json"
    if len(sys.argv) > 1:
        config_file = sys.argv[1]

    with open(config_file, 'r') as f:
        config = json.load(f)
        return config['todoist_token']

def main():
    try:
        todoist_token = get_token()
    except:
        print ("Could not find the todoist token" )
        exit(1)

    try:
        msg_str = sys.stdin.read()
        ip = lib.ical_parser.IcalParser(msg_str)

        tt = lib.todoist_api.TodoistTask(todoist_token)
        response = tt.post(ip.to_json())

        if response.status_code >= 400 and response.status_cod < 600:
            print ("Received an http error %s" % response.status_code)
            print (response)
        else:
            print("Successfully POSTed to your todoist calendar")
    except:
        print ("It seems that the mail does not contain an event.")

if __name__ == "__main__":
    main()
