import socket
import sys
import mimetypes
import os

def response_ok(body, mimetype):
    """returns a basic HTTP response"""
    resp = []
    resp.append("HTTP/1.1 200 OK")
    resp.append("Content-Type: %s" %mimetype)
    resp.append("")
    resp.append("%s" % body)
    return "\r\n".join(resp)


def response_method_not_allowed():
    """returns a 405 Method Not Allowed response"""
    resp = []
    resp.append("HTTP/1.1 405 Method Not Allowed")
    resp.append("")
    return "\r\n".join(resp)


def parse_request(request):
    first_line = request.split("\r\n", 1)[0]
    method, uri, protocol = first_line.split()
    if method != "GET":
        raise NotImplementedError("We only accept GET")
    print >>sys.stderr, 'request is okay'
    return uri

def resolve_uri(uri):
    home_directory = "./webroot"
    requested_uri = uri
    resource_path = home_directory + requested_uri
    if os.path.exists(resource_path):
        if os.path.isdir(resource_path):
            dir_contents = os.listdir(resource_path)
            dir_contents_joined = "\r\n".join(dir_contents)
            return (dir_contents_joined, "text/plain")
        elif os.path.isfile(resource_path):
            content_type = mimetypes.guess_type(resource_path)[0]
            with file(resource_path, "rb") as f:
                file_data = f.read()
            return (file_data, content_type) 
        else:
            print "What is this thing you are asking me for?"
    else:
        raise ValueError



def response_not_found():
    response_404 = "HTTP/1.1 404 Not Found\r\n\r\n"
    return response_404
    




def server():
    address = ('127.0.0.1', 10000)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print >>sys.stderr, "making a server on %s:%s" % address
    sock.bind(address)
    sock.listen(1)
    
    try:
        while True:
            print >>sys.stderr, 'waiting for a connection'
            conn, addr = sock.accept() # blocking
            try:
                print >>sys.stderr, 'connection - %s:%s' % addr
                request = ""
                while True:
                    data = conn.recv(1024)
                    request += data
                    if len(data) < 1024 or not data:
                        break

                try:
                    uri = parse_request(request)

                except NotImplementedError:
                    response = response_method_not_allowed()
                else:
                    try:
                        body, mimetype = resolve_uri(uri)
                    except ValueError:
                        response = response_not_found()
                    else:
                        response = response_ok(body, mimetype)

                print >>sys.stderr, 'sending response'
                conn.sendall(response)
            finally:
                conn.close()
            
    except KeyboardInterrupt:
        sock.close()
        return


if __name__ == '__main__':
    server()
    sys.exit(0)
