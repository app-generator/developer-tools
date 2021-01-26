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

from api.common import COMMON, ASSETS_MAP, BS_TAG, TMPL
from api.util   import file_load, file_exists, get_files, get_tail
from api.parser import node_info

FILES_LIST        = []
FILES_MAP         = {}
FILES_WITH_ERRORS = []

# Initialized with all files manually renamed  
INNER_LINKS = {
    'error-404.html'      : 'page-404.html',
    'error-500.html'      : 'page-500.html',
    'flag-icons.html'     : 'icons-flag.html',
    'basic-table.html'    : 'table-basic.html',
    'data-table.html'     : 'table-data.html',
    'sortable-table.html' : 'table-sortable.html',
    'vector-map.html'     : 'maps-vector.html',
    'google-maps.html'    : 'maps-google.html',
    'lock-screen.html'    : 'page-lock.html'
}

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

        # extract the current template
        tmpl = aFileMap[ f ]

        # reset errors counter    
        tmpl.err = []

        print (' PROCESSING --> ' + tmpl.file )

        for css_file in tmpl.css:
            if not file_exists( DIR_ASSETS + css_file ) and ( css_file not in tmpl.err ) and ( len( css_file ) > 0 ):
                print( '\t ERR - Missing Asset -> ' + css_file )
                tmpl.err.append( css_file )

        for js_file in tmpl.js:
            if not file_exists( DIR_ASSETS + js_file ) and ( js_file not in tmpl.err ) and ( len( js_file ) > 0 ):
                print( '\t ERR - Missing Asset -> ' + js_file )
                tmpl.err.append( js_file )

        for img_file in tmpl.img:
            if not file_exists( DIR_ASSETS + img_file ) and ( img_file not in tmpl.err ) and ( len( img_file ) > 0 ):
                print( '\t  ERR - Missing Asset -> ' + img_file )
                tmpl.err.append( img_file )

        for link in tmpl.links:

            # Extract the file from full path:
            # ../whatever/index.html
            # ../../../aaa.html
            l_file = get_tail( link )

            # print( ' Search the inner link for ' + l_file ) 

            if l_file in INNER_LINKS.keys():

               #print( ' LINK: ' + l_file + ' -> ' + INNER_LINKS[ l_file ] )
               continue

            for link_file in aFileMap:

                if link_file.endswith(l_file):

                    # Save in map
                    INNER_LINKS[ l_file ] = link_file

                    print( ' LINK: ' + l_file + ' -> ' + INNER_LINKS[ l_file ] )
                    continue

            print( '\t ERR - Missing Inner Link -> ' + l_file )
            tmpl.err_links.append( l_file )

        # Update the template
        aFileMap[ f ] = tmpl

        # We have errors    
        if ( len ( aFileMap[ f ].err ) > 0 ) or ( len ( aFileMap[ f ].err_links ) > 0 ) :
            
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

    for k in FILES_MAP:
        
        f = FILES_MAP[k]

        print('    |- ' + str( f ) )

    print ('\n\n')
    print ( 'Pages with errors: ' + str( len( FILES_WITH_ERRORS ) ) )

    for f in FILES_WITH_ERRORS:

        f = FILES_MAP[ f ]
        print('    |  ' )
        print('    |- ' + f.file )

        if len ( f.err ) > 0: 

            for i in f.err:
                print('    |   | - asset -' + str( i ) )

        if len ( f.err_links ) > 0: 

            for i in f.err:
                print('    |   | - link -' + str( i ) )

    print ('\n\n')            
