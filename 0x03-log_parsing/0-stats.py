#!/usr/bin/python3
"""log parsing"""
import sys
import signal


def print_stats(total_size, status_codes):
    """status print function
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if isinstance(code, int):
            print("{}: {}".format(code, status_codes[code]))
        else:
            pass


def signal_handler(sig, frame):
    """signal handler
    """
    print_stats(total_size, status_codes)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
total_size = 0
status_codes = {}

try:
    for i, line in enumerate(sys.stdin, 1):
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size

            if status_code.isdigit() and int(status_code) in [
                    200, 301, 400, 401, 403, 404, 405, 500]:
                status_codes[
                        int(status_code)
                        ] = status_codes.get(int(status_code), 0) + 1

        if i % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    signal_handler(signal.SIGINT, None)
