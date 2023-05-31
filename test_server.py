from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl


httpd = HTTPServer(('localhost', 8000), BaseHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket,
certfile='./certificate.pem', server_side=True, ssl_version=ssl.PROTOCOL_TLS

httpd.serve_forever()