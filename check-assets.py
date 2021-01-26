# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: https://github.com/app-generator/license-eula
"""

'''
information    : Scan a design/ui kit for missing assets
Status         : WIP
Usage          : python ./check-assets.py
Configuration  : 
- DIR_HTML: The directory the HTML files are located
- DIR_ASSETS: The parent directory for all assests (JS, images, CSS) 
'''

### Configuration ###
DIR_HTML   = '<FULL_PATH_HERE>'
DIR_ASSETS = '<FULL_PATH_HERE>'
### END Configuration ###

from os import walk
import sys, htmlmin
from bs4 import BeautifulSoup as bs, NavigableString, Tag, ResultSet, Comment

from api.common import COMMON, ASSETS_MAP
from api.util   import file_load, file_exists, get_files
from api.parser import node_info

FILES_LIST        = []
FILES_MAP         = {}
FILES_WITH_ERRORS = []

class TMPL:

    def __init__(self, aFile=''):

        self.file      = aFile
        self.title     = ''
        self.css       = []
        self.js        = []
        self.img       = []
        self.links     = []

        self.all_files = [] # used to fix the file internal links
        self.err       = [] # used to report missing assets

    def __repr__(self):
        return "TMPL() - " + self.file + ' css=' + str(len( self.css )) + ' / js=' + str(len( self.js )) + ' / img=' + str(len( self.img )) 

    def check_assets(self):

        self.err    = []

        print (' PROCESSING --> ' + self.file )

        for f in self.css:
            if not file_exists( DIR_ASSETS + f ) and ( f not in self.err ) and ( len( f ) > 0 ):
                print( ' ERR - Missing Asset -> ' + f )
                self.err.append( f )

        for f in self.js:
            if not file_exists( DIR_ASSETS + f ) and ( f not in self.err ) and ( len( f ) > 0 ):
                print( ' ERR - Missing Asset -> ' + f )
                self.err.append( f )

        for f in self.img:
            if not file_exists( DIR_ASSETS + f ) and ( f not in self.err ) and ( len( f ) > 0 ):
                print( ' ERR - Missing Asset -> ' + f )
                self.err.append( f )

def get_bs( aFile ):

  minified = htmlmin.minify( file_load( aFile ), remove_empty_space=True)
  return bs(minified,'html.parser')

def get_res( aBS, aNodeType ):

    page_res = []

    for link in aBS.find_all( aNodeType ):

        tag = node_info( link )
        
        # Remote resources are ignored 
        if tag and tag.is_local :
            page_res.append( tag.path )        

        #print ( tag.info() )

    return page_res

# Scan for CSS files
def get_css( aBS ):

    return get_res( aBS, 'link' )

# Scan for JS files
def get_js( aBS ):

    return get_res( aBS, 'script' )

# Scan for images
def get_img( aBS ):

    return get_res( aBS, 'img' )    

# Scan for links
def get_links( aBS ):

    page_links = []

    for link in aBS.find_all( 'a' ):

        tag = node_info( link )
        
        # Remote resources are ignored 
        if '../' in tag.path:
            page_links.append( tag.path )        

        #print ( tag.info() )

    return page_links

def l_to_map( aFileList ):

    ret_val = {}
    for f in aFileList:

        tmpl           = TMPL( f )
        tmpl.all_files = aFileList # used to fix the internal links 

        ret_val[ f ] = tmpl  

    return ret_val

def process_assets( aFileMap ):

    idx = 0
    for f in aFileMap:

        idx += 1

        print (' PROCESSING --> ' + f + ' | files (' + str( len(aFileMap) - idx ) + ') remaining' )
        tmpl = aFileMap[ f ]

        FULL_PATH = DIR_HTML + f     
        soup = get_bs( FULL_PATH )
        
        #print( soup.find('head') ) 

        # Scan for CSS files
        tmpl.css = get_css( soup )
        # print ('    |--- CSS   = ' + str( len(tmpl.css) ) + ' file(s)' )

        # Scan for JS files
        tmpl.js = get_js( soup ) 
        # print ('    |--- JS    = ' + str( len(tmpl.js) ) + ' file(s)' )

        # Scan for Images files
        tmpl.img = get_img( soup )
        # print ('    |--- IMG   = ' + str( len(tmpl.img) ) + ' file(s)' )

        # Scan for Links
        tmpl.links = get_links( soup )
        # print ('    |--- LINKS = ' + str( len(tmpl.links) ) + ' links' )

        aFileMap[ f ] = tmpl 

    return aFileMap

def check_assets( aFileMap ):

    idx = 0
    for f in aFileMap:

        aFileMap[ f ].check_assets()

        # We have errors    
        if len ( aFileMap[ f ].err ) > 0 :
            
            FILES_WITH_ERRORS.append( f )

# Entry point
if __name__ == "__main__":
    
    # print( 'HERE we go!' )
    
    files = get_files( DIR_HTML )
    print ( '\n Files (' + str(len( files )) + ')' )
    print ( files )

    FILES_MAP = l_to_map( files )
    # print ( FILES_MAP )

    print ( '\n ***** ***** ***** \n') 

    FILES_MAP = process_assets( FILES_MAP )
    # print ( FILES_MAP )

    check_assets( FILES_MAP )
    # print ( FILES_MAP )

    print('    | ' )
    print('    | ' )

    for k in FILES_MAP:
        
        f = FILES_MAP[k]

        print('    |  ' )
        print('    |  ' )
        print('    |- ' + f.file )
        print('    |    |')
        print('    |    |--- CSS: ' + str( len(f.css) ) + ' file(s)' )

        for i in f.css:
            print('    |    |     | ' + str( i ) )

        print('    |    |')
        print('    |    |--- JS: ' + str( len(f.js) ) + ' file(s)' )

        for i in f.js:
            print('    |    |     | ' + str( i ) )

        print('    |    |')
        print('    |    |--- IMG: ' + str( len(f.img) ) + ' file(s)' )

        for i in f.img:
            print('    |    |     | ' + str( i ) )

        print('    |    |')
        print('    |    |--- Links: ' + str( len(f.links) ) + ' (inner)' )

        for i in f.links:
            print('    |    |     | ' + str( i ) )

        print('    |    |')
        print('    |    |--- Errors: ' + str( len(f.err) ) )

        for i in f.err:
            print('    |    |     | ' + str( i ) )


    print ('\n\n')
    print ( 'Pages with errors: ' + str( len( FILES_WITH_ERRORS ) ) )

    for f in FILES_WITH_ERRORS:

        f = FILES_MAP[ f ]
        print('    |  ' )
        print('    |- ' + f.file )

        for i in f.err:
            print('    |    |     | ' + str( i ) )

    print ('\n\n')            
