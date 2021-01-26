# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: https://github.com/app-generator/license-eula
"""

'''
Order is important - start with long paths 
'''
ASSETS_MAP = {
 '../../../assets'      : '/static/assets',
 '../../assets'         : '/static/assets',
 '../assets'            : '/static/assets',
 './assets'             : '/static/assets',
 '../../../css'         : '/static/assets/css',
 '../../css'            : '/static/assets/css',
 '../css'               : '/static/assets/css',
 './css'                : '/static/assets/css',
 '../../../vendor'      : '/static/assets/vendor',
 '../../vendor'         : '/static/assets/vendor',
 '../vendor'            : '/static/assets/vendor',
 './vendor'             : '/static/assets/vendor',
 '../../../lib'         : '/static/assets/lib',
 '../../lib'            : '/static/assets/lib',
 '../lib'               : '/static/assets/lib',
 './lib'                : '/static/assets/lib',
 'lib/'                 : '/static/assets/lib/',
 '../../js'             : '/static/assets/js',
 '../js'                : '/static/assets/js',
 './js'                 : '/static/assets/js',
 '../../../img'         : '/static/assets/img',
 '../../img'            : '/static/assets/img',
 '../img'               : '/static/assets/img',
 './img'                : '/static/assets/img',
 '../../node_modules'   : '/static/assets/node_modules',
 '../node_modules'      : '/static/assets/node_modules',
 './node_modules'       : '/static/assets/node_modules'
}

class COMMON:

    NULL  = None # not set
    NA    = -1   # not set
    OK    =  0   # all ok
    ERR   =  1   # not ok

class BS_TAG:

    def __init__(self, aTag):

        self._tag         = aTag 

        self.href         = ''
        self.rel          = ''
        self.type         = ''

        self.is_local     = True

        self.is_link      = False    
        self.is_canonical = False    
        self.is_css       = False
        self.is_img       = False
        self.is_js        = False
        self.is_icon      = False
        self.is_manifest  = False
        
        self.path         = ''
        self.file         = ''
        self.ext          = ''

        self.data         = {}

    def printme(self):

        print('>>> TAG Info')
        
        if self.is_css:
            print(' - Type = CSS' ) 

        if self.is_img:
            print(' - Type = IMAGE' ) 

        if self.is_js:
            print(' - Type = JS' ) 

        if self.is_icon:
            print(' - Type = ICON' ) 

        if self.is_manifest:
            print(' - Type = MANIFEST' ) 

        if self.is_local:
            print(' - Storage = LOCAL' ) 
        else:
            print(' - Storage = REMOTE' ) 

        print(' - HREF = ' + self.href ) 
        print(' - PATH = ' + self.path ) 
        print(' - FILE = ' + self.file ) 
        print(' - EXT  = ' + self.ext  ) 

    def info(self):
        ret = 'UNKN '
        
        if self.is_css:
            ret = 'CSS ' 

        if self.is_img:
            ret = 'IMAGE ' 

        if self.is_js:
            ret = 'JS ' 

        if self.is_link:
            ret = 'LINK ' 

        if self.is_canonical:
            ret = 'CANNONICAL ' 

        if self.is_icon:
            ret = 'ICON ' 

        if self.is_manifest:
            ret = 'MANIFEST ' 

        if self.is_local:
            ret += '(local) '  
        else:
            ret += '(www) ' 

        if self.is_canonical or self.is_link:
            ret += self.href
        else:    
            ret += '[' + self.file + '] ' + self.href + ' -> [' + str(self.path) + '] '

        return ret

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
        self.err_links = [] # used to report missing assets

    def __repr__(self):

        errors = len( self.err) + len( self.err_links) 
        return "" + self.file + ' | css=' + str(len( self.css )) + ' / js=' + str(len( self.js )) + ' / img=' + str(len( self.img )) + ' - ('+str(errors)+') ERRORS'
