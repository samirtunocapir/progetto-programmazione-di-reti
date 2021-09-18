from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        url = self.path
        print(f'url = {url}')

        path = ''

        #indirizzamento alla pagina in base all'url
        if url == '/':
            path = 'html/index.html'
            self.send_header('Content-type','text/html')
            self.send_response(200)

        elif url == '/orari':
            path = 'html/Orari.html'
            self.send_header('Content-type','text/html')
            self.send_response(200)

        elif url == '/personale':
            path = 'html/Personale.html'
            self.send_header('Content-type','text/html')
            self.send_response(200)

        elif url == '/prenota':
            path = 'html/Prenota.html'
            self.send_header('Content-type','text/html')
            self.send_response(200)

        elif url == '/file.pdf':
            path = 'file/file.pdf'
            self.send_header('Content-type','application/pdf')
            self.send_response(200)
        
        #in caso di errore
        else:
            self.send_response(404)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write('404 - Not Found'.encode())
            return


        self.end_headers()
        try:
            print(f'PATH = {path}')
            file = open(path, 'rb').read()
            self.wfile.write(file)
        except Exception as e:
            print(f"Error retrieving file {path}: {e}")


    
