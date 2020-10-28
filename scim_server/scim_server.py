#!/usr/bin/python
import http.server
import socketserver

# This code is released to puplic domain
# https://creativecommons.org/publicdomain/zero/1.0/

#Author: Esa-Petri Tirkkonen (esa.petri.tirkkonen@csit.fi)

#sources used to create this app:
# https://stackabuse.com/serving-files-with-pythons-simplehttpserver-module/



#server variables:
PORT = 4555


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'main.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

my_server = socketserver.TCPServer(("", PORT), handler_object)

print("starting simple SCIM server at port: " + str(PORT) )
print("use ctrl-c to kill server")
# Star the server
my_server.serve_forever()
