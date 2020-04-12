#!/usr/bin/python

import socket
import time, io, sys, os.path, re

if len(sys.argv) != 3:
    print("Usage: ./streaming_server.py <filename> <port>")
    exit(0)
else:
    filename=sys.argv[1]
    if not (os.path.isfile(filename)):
        print("File ",filename," does not exist!")
        exit(0)
    port=int(sys.argv[2])
    if (port < 9700) or (port > 9800):
        print("Port number should be between 9700 and 9800")
        exit(0)

host = ''
address = (host, port)

# setup TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(address)
sock.listen(5)

numlines = sum(1 for line in open(filename,'rt'))  # get number of lines in file

# get line of a file
def get_line(line):
    with open(filename,'rt') as fp:
        for i, l in enumerate(fp):
            if i == line:
                clean_line = re.sub(r"[^a-z0-9\s+]","",l.lower())
                return clean_line

# main loop
while True:
    try:
        print("Listening for client . . .")
        conn, client = sock.accept()
        print("Connected to client at ", client)
        print("Sending file ",filename," with ",numlines," lines")
        currline = 0
        while currline < numlines:
            print("Sending line: ",currline)
            conn.send(get_line(currline).encode())
            currline += 1
            time.sleep(1)
        conn.close()
        print("File ended and closing connection....")
    except KeyboardInterrupt:
        print("Keyboard interrupt occurred.")
        print("Closing client and server...")
        conn.close()
        sock.close()
       # sock.shutdown(socket.SHUT_WR)
