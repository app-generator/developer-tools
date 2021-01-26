# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: https://github.com/app-generator/license-eula
"""

import io, os, sys, htmlmin, shutil, pprint, json, fnmatch, re, bs4, copy, configparser
from bs4 import BeautifulSoup as bs, NavigableString, Tag, ResultSet

from api.common import COMMON, BS_TAG, ASSETS_MAP
from api.util   import is_int, is_str, is_list

def update_path( aObj ):

    if not aObj:
        return ''

    # print (' >> Input  [' + aObj.href + ']' )

    for key in ASSETS_MAP.keys(): 

        # print ( 'Compare key = [' + key + '] with [' + aObj.href + ']'  )
        if key in aObj.href:
            # print ( '   ---->  MATCH key = [' + key + '] on [' + aObj.href + '] -> ' + ASSETS_MAP[ key ] )
            return aObj.href.replace( key, ASSETS_MAP[ key ] )

    if aObj.is_link:
        #print ( ' ------------------> LINK: TRUE')
        if aObj.href == "#":
            return aObj.href
    # else:
    #    print ( ' ------------------> LINK: FALSE')

    # if len( aObj.href ) > 0:  
    #    print (' >> Output [' + aObj.href + ']' )

    return aObj.href


def node_info( aTag ):
    
    if not aTag:
        return None

    obj = BS_TAG( aTag )

    if aTag.has_attr('src'):

        # Process value
        if is_list( aTag['src'] ):
            obj.href = ''.join(aTag['src'])    
        else:
            obj.href = aTag['src']
        
        # We have a string
        #print(' > href = ' + obj.href )

        # Check for remote resource
        if obj.href.startswith('http') or obj.href.lower().startswith('//'):
            #print(' > WWW object ' )
            obj.is_local = False
        #else:
        #    print(' > LOCAL object ' )

        # Save file name
        obj.file = obj.href.split('/')[-1]
        #print(' > file = ' + obj.file )

        # Save extension
        obj.ext  = obj.href.split('.')[-1]
        #print(' > ext = ' + obj.ext )

    if aTag.has_attr('href'):

        # Process value
        if is_list( aTag['href'] ):
            obj.href = ''.join(aTag['href'])    
        else:
            obj.href = aTag['href']
        
        # We have a string
        #print(' > href = ' + obj.href )

        # Check for remote resource
        if obj.href.startswith('http') or obj.href.lower().startswith('//'):
            obj.is_local = False

        # Save file name
        obj.file = obj.href.split('/')[-1]
        #print(' > file = ' + obj.file )

        # Save extension
        obj.ext  = obj.href.split('.')[-1]
        #print(' > ext = ' + obj.ext )

    if aTag.has_attr('rel'):

        if is_list( aTag['rel'] ):
            obj.rel = ''.join(aTag['rel'])    
        else:
            obj.rel = aTag['rel']

        #print(' > rel = ' + obj.rel )

    if aTag.has_attr('type'):
        obj.type = aTag['type']
        
        #print(' > type = ' + obj.type )

    if obj.ext in ['js']:
        obj.is_js = True    

    if obj.ext in ['jpg', 'jpeg', 'png', 'svg']:
        obj.is_img = True    

    if obj.rel == 'stylesheet':
        obj.is_css = True

    if obj.rel == 'canonical':
        obj.is_canonical  = True
        obj.is_local      = False

    if 'icon' in obj.rel:
        obj.is_icon = True

    if 'manifest' in obj.rel:
        obj.is_manifest = True        

    if obj.is_local and not obj.is_link:
        obj.path = update_path( obj ) # we might need context information
    else: 
        # For remote products paths are identical
        obj.path = obj.href

    return obj

'''
Deprecated
'''
def update_path2( aObj ):

    if not aObj:
        return ''

    ret = aObj.href
    #print (' >> Input  [' + aObj.href + ']' )

    ## Deep paths first !!!

    if '../../../assets' in aObj.href:
        return aObj.href.replace('../../../assets', '/static/assets')

    if '../../assets' in aObj.href:
        return aObj.href.replace('../../assets', '/static/assets')

    if '../assets' in aObj.href:
        return aObj.href.replace('../assets', '/static/assets')

    if './assets' in aObj.href:
        return aObj.href.replace('./assets', '/static/assets')

    if '../../../css' in aObj.href:
        return aObj.href.replace('../../../css', '/static/assets/css')

    if '../../css' in aObj.href:
        return aObj.href.replace('../../css', '/static/assets/css')

    if '../css' in aObj.href:
        return aObj.href.replace('../css', '/static/assets/css')

    if './css' in aObj.href:
        return aObj.href.replace('./css', '/static/assets/css')

    if '../../../vendor' in aObj.href:
        return aObj.href.replace('../../../vendor', '/static/assets/vendor')

    if '../../vendor' in aObj.href:
        return aObj.href.replace('../../vendor', '/static/assets/vendor')

    if '../vendor' in aObj.href:
        return aObj.href.replace('../vendor', '/static/assets/vendor')

    if './vendor' in aObj.href:
        return aObj.href.replace('./vendor', '/static/assets/vendor')

    if '../../../lib' in aObj.href:
        return aObj.href.replace('../../../lib', '/static/assets/lib')

    if '../../lib' in aObj.href:
        return aObj.href.replace('../../lib', '/static/assets/lib')

    if '../lib' in aObj.href:
        return aObj.href.replace('../lib', '/static/assets/lib')

    if './lib' in aObj.href:
        return aObj.href.replace('./lib', '/static/assets/lib')

    if 'lib/' in aObj.href:
        return aObj.href.replace('lib/', '/static/assets/lib/')

    if '../../js' in aObj.href:
        return aObj.href.replace('../../js', '/static/assets/js')

    if '../js' in aObj.href:
        return aObj.href.replace('../js', '/static/assets/js')

    if './js' in aObj.href:
        return aObj.href.replace('./js', '/static/assets/js')

    if '../../../img' in aObj.href:
        return aObj.href.replace('../../../img', '/static/assets/img')

    if '../../img' in aObj.href:
        return aObj.href.replace('../../img', '/static/assets/img')

    if '../img' in aObj.href:
        return aObj.href.replace('../img', '/static/assets/img')

    if './img' in aObj.href:
        return aObj.href.replace('./img', '/static/assets/img')

    if '../../node_modules' in aObj.href:
        return aObj.href.replace('../../node_modules', '/static/assets/node_modules')

    if '../node_modules' in aObj.href:
        return aObj.href.replace('../node_modules', '/static/assets/node_modules')

    if './node_modules' in aObj.href:
        return aObj.href.replace('./node_modules', '/static/assets/node_modules')

    if len(ret) > 0:  
        print (' >> Output [' + ret + ']' )

    return ret

