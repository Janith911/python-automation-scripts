from fluent import sender
from fluent import event
import argparse
import json

def cli_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname",help="Hostname of the Fluentd")
    parser.add_argument("port",help="Port of the Fluentd")
    parser.add_argument("logger",help="Logger for the Fluentd")
    parser.add_argument("environment",help="Environment")
    parser.add_argument("data",help="JSON file")
    args = parser.parse_args()
    sender.setup(args.logger, host=args.hostname, port=int(args.port))
    with open(args.data) as json_file:
        data = json.load(json_file)
        for i in range(0,len(data)):
            event.Event(args.environment, data[i])
    json_file.close()

cli_arguments()