#!/usr/bin/python3

import argparse
import socket
import sys

def check_port(hostname, port):
    s = socket.socket()
    s.settimeout(5)

    try:
        s.connect((hostname, port))
        print(f'Connected to {hostname} on the port {port}')
    except socket.error as e:
        print(f'Connection to {hostname} failed on the port {port}: {e}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python script to check port is open or not",
                                     usage="%(prog)s -a hostname -p port",
                                    epilog="Example %(prog)s --host example.com --port 443" )

    parser.add_argument(
                    "-a",
                    help="Destination server hostname",
                    dest="hostname",
                    default="localhost",
                    metavar="Hostname or IP")

    parser.add_argument("-p",
                    help="Destination server port",
                    dest="port",
                    default=80,
                    metavar="Port")

    args = parser.parse_args()


    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)

check_open_port = check_port(args.hostname, int(args.port))