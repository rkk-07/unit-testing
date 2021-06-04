#!/usr/bin/env python

import argparse
import shortuuid
from os import path
from datetime import datetime

now = datetime.now()
date = now.strftime("%d-%m-%Y")
year = now.strftime("%Y")
copyright_tmpl = \
"""/**
  ******************************************************************************
  * @file    %(fullfilename)s
  * @author  Lucas-TVS software team.
  * @date    """+date + """
  * @version 0.1.0
  * @brief   %(description)s
  ******************************************************************************
  * @copyright 
  * @verbatim
    _                                            _______  __      __   _____ 
   | |                                          |__   __| \ \    / /  / ____|
   | |       _   _    ___    __ _   ___   ____     | |     \ \  / /  | (___  
   | |      | | | |  / __|  / _` | / __| |____|    | |      \ \/ /    \___ \ 
   | |____  | |_| | | (__  | (_| | \__ \           | |       \  /     ____) |
   |______|  \__,_|  \___|  \__,_| |___/           |_|        \/     |_____/ 

  * @endverbatim
  *
  * Copyright (C) """ + year + """ Lucas-TVS - All Rights Reserved.
  *
  * This program and the accompanying materials are made available
  * under the terms described in the LICENSE file which accompanies
  * this distribution.
  ******************************************************************************
  */
"""

header_incl_tmpl = \
"""
#ifndef GUARD_%(FILENAME)s_H_%(uuid)s
#define GUARD_%(FILENAME)s_H_%(uuid)s

#ifdef __cplusplus
extern "C"
{
#endif /* __cplusplus */

/**
 * @brief Source file version tag
 */
#define VER_%(FILENAME)s_MAJ    (0x000u) /**< [31:20] Major version */
#define VER_%(FILENAME)s_MIN    (0x001u) /**< [19:8] Minor version */
#define VER_%(FILENAME)s_PATCH  (0x00u)  /**< [7:0] Patch version */
#define VER_%(FILENAME)s    ((VER_%(FILENAME)s_MAJ << 20u) \\
                            |(VER_%(FILENAME)s_MIN << 8u) \\
                            |(VER_%(FILENAME)s_PATCH))

/* Includes ------------------------------------------------------------------*/
/* Exported types ------------------------------------------------------------*/
/* Exported constants --------------------------------------------------------*/
/* Exported macro ------------------------------------------------------------*/
/* Exported functions --------------------------------------------------------*/

#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif /* GUARD_%(FILENAME)s_H_%(uuid)s */

/*                        (C) COPYRIGHT LUCAS-TVS                             */
/******************************* END OF FILE **********************************/
"""

source_tmpl = \
"""
/* Includes ------------------------------------------------------------------*/
#include "%(ownheader)s"
/* Private typedef -----------------------------------------------------------*/
/* Private define ------------------------------------------------------------*/
/* Private macro -------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/
/* Private function prototypes -----------------------------------------------*/
/* Private functions ---------------------------------------------------------*/

/*                        (C) COPYRIGHT LUCAS-TVS                             */
/******************************* END OF FILE **********************************/
"""

config_incl_tmpl = \
"""
#ifndef GUARD_%(FILENAME)s_CFG_%(uuid)s
#define GUARD_%(FILENAME)s_CFG_%(uuid)s

#ifdef __cplusplus
extern "C"
{
#endif /* __cplusplus */

/**
 * @brief Configuration file version tag
 */
#define VER_%(FILENAME)s_CFG_MAJ    (0x000u) /**< [31:20] Major version */
#define VER_%(FILENAME)s_CFG_MIN    (0x001u) /**< [19:8] Minor version */
#define VER_%(FILENAME)s_CFG_PATCH  (0x00u)  /**< [7:0] Patch version */
#define VER_%(FILENAME)s_CFG    ((VER_%(FILENAME)s_CFG_MAJ << 20u) \\
                                |(VER_%(FILENAME)s_CFG_MIN << 8u) \\
                                |(VER_%(FILENAME)s_CFG_PATCH))

#if (VER_%(FILENAME)s_CFG != VER_%(FILENAME)s)
#warning(Module configuration version mismatch)
#endif

/* Includes ------------------------------------------------------------------*/
/* Exported types ------------------------------------------------------------*/
/* Exported constants --------------------------------------------------------*/
/* Exported macro ------------------------------------------------------------*/
/* Exported functions --------------------------------------------------------*/

#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif /* GUARD_%(FILENAME)s_CFG_%(uuid)s */

/*                        (C) COPYRIGHT LUCAS-TVS                             */
/******************************* END OF FILE **********************************/
"""

def h_create (file_handle, fname):
    file_handle.write (copyright_tmpl %
                       ({'description': "Header file of " + str(fname) + " module.",
                        'fullfilename': str(fname)+'.h'}),)
    file_handle.write (header_incl_tmpl %
                       ({'uuid': str(shortuuid.ShortUUID().random(length=6)).upper(),
                         'FILENAME': str(fname).upper().replace('-','_')}),)
    file_handle.close ()

def cfg_create (file_handle, fname):
    file_handle.write (copyright_tmpl %
                       ({'description': "Configuration file of " + str(fname) + " module.",
                        'fullfilename': str(fname)+"-cfg.h"}),)
    file_handle.write (config_incl_tmpl %
                       ({'uuid': str(shortuuid.ShortUUID().random(length=6)).upper(),
                         'FILENAME': str(fname).upper().replace('-','_')}),)
    file_handle.close ()

def src_create (file_handle, fname):
    file_handle.write (copyright_tmpl %
                       ({'description': str(fname) + " module driver.",
                        'fullfilename': str(fname)+'.c'}),)
    file_handle.write (source_tmpl %
                       ({'ownheader': str(fname)+'.h'}),)
    file_handle.close ()

def main():
    parser = argparse.ArgumentParser (
        prog="stool", description="C/C++ source and header file generation tool.\
                                   For support <gokul.a@lucastvs.co.in>")
    parser.add_argument ("-f", "--file-name",
                         help="C/C++ header/source file name",
                         type=str, required=True)

    parser.add_argument ("-d", "--directory",
                         help="C/C++ header/source create directory",
                         type=str, required=False)

    parser.add_argument ("-s", "--smart",
                         help="C/C++ header/source create in source and config",
                         type=str, required=False)

    args = vars(parser.parse_args ())

    if args['directory'] is not None:
        path_src = args['directory'] + '/' + args['file_name']
        path_cfg = path_src
    elif args['smart'] is not None:
        path_src = args['smart'] + '/' + 'source' + '/' + args['file_name']
        path_cfg = args['smart'] + '/' + 'config' + '/' + args['file_name']
    else:
        path_src = args['file_name']
        path_cfg = path_src

    src_path = (path_src+'.c')
    
    if(path.exists(src_path)):
        print("file exists", src_path)
    else:
        c_file = open(src_path,'w')
        src_create(c_file, args['file_name'])
        print("file create", src_path)

    src_path = (path_src+'.h')

    if(path.exists(src_path)):
        print("file exists", src_path)
    else:
        h_file = open(src_path,'w')
        h_create(h_file, args['file_name'])
        print("file create", src_path)

    src_path = (path_cfg + '-cfg.h')

    if(path.exists(src_path)):
        print("file exists", src_path)
    else:
        cfg_file = open(src_path,'w')
        cfg_create(cfg_file, args['file_name'])
        print("file create", src_path)

    src_path = (path_cfg + '-cfg.c')

#    if(path.exists(src_path)):
#        print("file exists", src_path)
#    else:
#        cfg_src_file = open(src_path,'w')
#        src_create(cfg_src_file, args['file_name'])
#        print("file create", src_path)
    

if __name__ == "__main__":
    main ()