import socket
import sys


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print >>log_buffer, "making a server on {0}:{1}".format(*address)
    sock.bind(address)
    sock.listen(1)
    
    try:
        while True:
            print >>log_buffer, 'waiting for a connection'
            conn, addr = sock.accept() # blocking
            try:
                print >>log_buffer, 'connection - {0}:{1}'.format(*addr)
                request = ""
                while True:
                    data = conn.recv(1024)
                    request += data
                    if len(data) < 1024 or not data:
                        break
                parse_request(request)
                print >>log_buffer, 'sending response'
                response = response_ok()
                conn.sendall(response)

            finally:
                conn.close()
            
    except KeyboardInterrupt:
        sock.close()
        return

def response_ok():
    resp = []
    resp.append("HTTP/1.1 200 OK")
    resp.append("Content-Type: text/plain")
    resp.append("")
    resp.append("this is a pretty minimal response")
    return "\r\n".join(resp)

def parse_request(request):
    # In-class attempt:

    # parts = request.split(" ") # split the request on whitespace
    # if parts[0] != "GET":

    # Better:

    first_line = request.split("\r\n", 1)[0]
    method, uri, protocol = first_line.split()
    if method != "GET":
        raise NotImplementedError("Only GET requests, please.")
    print >>sys.stderr, 'request is okay'



if __name__ == '__main__':
    server()
    sys.exit(0)
