#!/usr/bin/env python3
import sys
import lib.ical_parser

def main():
    if len(sys.argv) != 2 or sys.argv[1].startswith('-'):
        sys.stderr.write("Usage: %s <filename.ics>\n" % sys.argv[0])
        sys.exit(2)
    with open(sys.argv[1], 'r') as f:
        msg_str = f.read()
        ip = lib.ical_parser.IcalParser(msg_str)
        print(str(ip))

if __name__ == "__main__":
    main()
