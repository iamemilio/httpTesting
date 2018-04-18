#! /usr/bin/env/ python3
# Reflects the requests from HTTP methods GET, POST, PUT, and DELETE
# Written by Nathan Hamiel (2010)
# https://gist.github.com/huyng/814831

from http.server import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser
from Auth import Auth


class RequestHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        request_path = self.path

        print("\n----- Request Start ----->\n")
        #print(request_path)
        print(self.headers)
        print("<----- Request End -----\n")

        headers = self.headers
        self.authorizeStuff()


    def do_POST(self):
        request_path = self.path

        print("\n----- Request Start ----->\n")
        print(request_path)

        request_headers = self.headers
        length = 0
        if "Content-Length" in self.headers:
            length = self.headers['Content-Length']

        print(request_headers)
        print(self.rfile.read(int(length)))
        print("<----- Request End -----\n")

        self.authorizeStuff()


    def authorizeStuff(self):
        auth = Auth('http', 'pfioh_config.cfg')
        allowed, error = auth.authorizeClientRequest(self.headers)
        print('\n\nAUTH: %s' % str(allowed))

        if allowed:
            self.send_response(200, "Authentication Successful!")
        else:
            print('%s: %s %s' % error)
            self.send_error(error[0], error[1], error[2])


    do_PUT = do_POST
    do_DELETE = do_GET


def main():
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("Creates an http-server that will echo out any GET or POST parameters\n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()
    main()