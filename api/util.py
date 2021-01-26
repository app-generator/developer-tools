# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
License: https://github.com/app-generator/license-eula
"""

import io, os, sys, htmlmin, shutil, pprint, json, fnmatch, re, bs4, copy, configparser
from bs4 import BeautifulSoup as bs, NavigableString, Tag, ResultSet
from os import walk

from api.common import COMMON

CFG_FOLDER_NAME       = "mappings"
SUPPORTED_TRANSLATION = ['html', 'php', 'blade', 'j2', 'pug']
            
def pwd():
    return os.getcwd()

def p_print( aSoupDiv, aHtmlTag=None ):

    if not isinstance(aSoupDiv, Tag):
        print( 'ERR p_print(): wrong input' )
        return COMMON.ERR

    if not aHtmlTag:
        print ( aSoupDiv.prettify(formatter="html") )
        return 

    # style = special tag
    if aHtmlTag == 'style':
        for tag in aSoupDiv.findChildren( ):

            if aHtmlTag == 'style' and 'style' in tag.attrs:

                print (' * Tag = ' + tag.name + ' [parser_dataid='+tag.attrs['parser_dataid']+'] style: ' + tag.attrs['style'])
        return

    for tag in aSoupDiv.find_all( aHtmlTag ):    

        # open data 
        elem_data = ' * Tag = ' + tag.name + ' [parser_dataid='+tag.attrs['parser_dataid']+'] {'
    
        for attr in tag.attrs:

            # ignore ..
            if attr in ['class', 'parser_dataid']:
                continue

            try:
                elem_data += '' + attr +  ': ' + tag.attrs[ attr ] + ', '
            except:
                pass

            # close data
            elem_data += '} '

        # print ..
        print (elem_data)

def p_del( aTag, aId ):

    if not isinstance(aTag, Tag) or not aId:
        print( 'ERR p_del(): wrong input' )
        return COMMON.ERR

    for tag in aTag.descendants:

        #if isinstance(tag, Tag) and int(data_id) == idx: #'parser_dataid' 
        if isinstance(tag, Tag) and 'parser_dataid' in tag.attrs and tag.attrs['parser_dataid'] == aId:
            tag.decompose()
            return COMMON.OK   
            break 

    # tag not located into tree
    return COMMON.NA       

def p_clean( aTag, aReturnCopy=True ):

    if not isinstance(aTag, Tag):
        print( 'ERR p_clean(): wrong input' )
        return COMMON.ERR

    retVal = aTag
    
    if aReturnCopy:
         retVal = copy.copy( aTag )

    for tag in retVal.recursiveChildGenerator():
    
        try:
        
            if 'parser_dataid' in tag.attrs:
                #print (' *** tag = ' + tag.name + ' parser_id = ' + tag['parser_dataid'])
                del tag[ 'parser_dataid' ]
            else: 
                #print (' *** no parser id for tag = ' + tag.name)     
                pass
        
        except AttributeError:
            # 'NavigableString' object has no attribute 'attrs'
            pass
    
    return retVal 

'''
#
# Helper to inject decisions in code
#
#  if not _q( 'Continue? ' ):
#    print (' ** Exit **')
#  else:
#    print (' ** #cool **')
#
'''
def _q( aQuestion ):
    
    print (' ')
    _in = input( aQuestion + ' (default N) ' ).lower()

    if ( ( '1' == _in ) or ( 'y' == _in ) ):
        print (' ')
        return True

    print (' ')
    return False

def is_int( aVal ):
    try: 
        int( aVal )
        return True
    except ValueError:
        return False

def is_str( aVal ):
    try: 
        return isinstance(aVal, str)
    except:
        return False

def is_list( aVal ):
    try: 
        return isinstance(aVal, list)
    except:
        return False

def file_exists( path ):

    try:

        if open( path, 'r'):
            #print ( ' *** File exists = ' + path )
            return True

    except:
        #print ( ' *** File not found = ' + path )
        return False    

def file_load( path, as_list=False ):

    try:

        f = open( path, 'r')
        if f:

            if as_list:
                content = f.readlines()
            else:
                content = f.read()    
            
            f.close()
            return content

    except:

        #print (' *** Err loading file: ' + str(path) )
        return None

def print_html( content ):

    soup = bs(content,'html.parser')
    return soup.prettify(formatter="html")
    
def file_append( file_path, new_content):

    print ( 'append content to file ' + file_path )
    return file_write( file_path, new_content, True ) 

def file_write( file_path, new_content, f_append=False ): 

    try:

        f = None

        if file_exists( file_path ):
            if f_append:    
                f = open( file_path, 'a+')
            else:
                f = open( file_path, 'w+')    
        else:
            f = open( file_path, 'w+')

        if not f:
            #'Err open file'
            return False

        f.seek(0) 
        f.write( new_content )
        f.truncate()

        f.close()
        return True

    except IOError:
        print( 'ERR file_write(): File IOError: ' + file_path )

    except:

        #print ( ' *** Err processing file ' + str(file_path) )
        return False

def file_print( file_path ):

    try:

        f = open( file_path, 'r')
        if f:
            for line in f.readlines():
                print ( line.rstrip() )

    except:

        #print ( ' *** Err loading file ' + str(file_path) )
        return None

def cfg_build( file_path ):

    if not file_exists( file_path ):
        return None

    config = configparser.ConfigParser()
    config.read( file_path )

    return config

def cfg_sections( cfg ):

    if cfg:
        return cfg.sections()

    return None

def copy_dir(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def list_files(dir_to_scan, ext):

    matches = []

    for root, dirnames, filenames in os.walk( dir_to_scan ):
        for filename in fnmatch.filter(filenames, '*.'+ ext):

            item = os.path.join(root, filename)

            #print ' **** type(item) = ' + str( type ( item ) )
            matches.append( item )

    return matches

def get_files( aPath ):

    FILES_LIST = [] 
    for (root, dirs, files) in walk( aPath ):
        FILES_LIST.extend( files )
        break

    return FILES_LIST
