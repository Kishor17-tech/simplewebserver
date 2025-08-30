from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<html>
    <head>
        <title>Sample</title>
    </head>
    <body>
        <center><font color=blue face="Arial" size="100">
            <b>List of Protocols in TCP/IP Model</b></font></center>
        <font color="red">
        <center>
        <h2>
            Application layer-HTP,FTP,DNS,TELNET<br>
            Transport layer-HTP,FTP,DNS,TELNET<br>
            Network layer-HTP,FTP,DNS,TELNET<br>
            Link layer-HTP,FTP,DNS,TELNET<br>
        </h2>
        </center>
        </font>
    </body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()