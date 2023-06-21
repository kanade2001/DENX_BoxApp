import http.server

def RUN():
    http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler)
