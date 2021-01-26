# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: https://github.com/app-generator/license-eula
"""

'''
information    : The script loads a design from a directory and serve the files in the browser
Status         : WIP
Usage          : python ./check-theme.py
Configuration  : 
- PORT: used to start the server
- UI_KIT_DIRECTORY: The source folder for the tested HTML files 
'''

### Configuration ###
PORT = 8080
UI_KIT_DIRECTORY = '<FULL_PATH_HERE>'
### END Configuration ###

import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler

def run():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

# Entry point
if __name__ == "__main__":
    print( 'HERE we go!' )
    run()
