#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

##################################
# @program        synda
# @description    climate models data transfer program
# @copyright      Copyright “(c)2009 Centre National de la Recherche Scientifique CNRS. 
# 						 All Rights Reserved”
# @license        CeCILL (https://raw.githubusercontent.com/Prodiguer/synda/master/sdt/doc/LICENSE)
##################################

"""This module compute local path for both file and dataset.

Note
    This module is only used in the file pipeline, not in the dataset pipeline.
"""

import os
import sys
import re
import argparse
import json
import sdapp
from sdexception import SDException
import sdlog
import sdconst
import sdprint
import sdpostpipelineutils

def run(files):
    files=add_dataset_local_path(files)

    files=transform_local_path_product(files)
    files=transform_local_path_project(files)

    files=local_path_custom_transform(files)
    files=local_path_homemade_transform(files)

    files=add_file_local_path(files)

    return files

def add_dataset_local_path(files):
    for f in files:
        f["dataset_local_path"]=get_dataset_local_path(f)

    return files

def add_file_local_path(files):
    for f in files:
        f["local_path"]=get_file_local_path(f)

    return files

def get_dataset_local_path(f):
    fmt=sdpostpipelineutils.get_attached_parameter(f,'local_path_format',sdconst.DEFAULT_LOCAL_PATH_FORMAT)

    if fmt=="treevar":
        path="%(dataset_path)s"%f # note that we don't add var folder here (we do ot only for the file local path)
    elif fmt=="tree":
        path="%(dataset_path)s"%f
    elif fmt=="notree":
        path=""
    else:
        raise SDException('SDLOCALP-010',"'local_path_format' is incorrect (%s)"%fmt)

    return path    

def get_file_local_path(f):
    fmt=sdpostpipelineutils.get_attached_parameter(f,'local_path_format',sdconst.DEFAULT_LOCAL_PATH_FORMAT)

    if fmt=="treevar":
        path="%(dataset_local_path)s/%(variable)s/%(filename)s" % f
    elif fmt=="tree":
        path="%(dataset_local_path)s/%(filename)s"%f
    elif fmt=="notree":
        path="%(filename)s"%f
    else:
        raise SDException('SDLOCALP-001',"'local_path_format' is incorrect (%s)"%fmt)

    return path

def transform_local_path_project(files):
    def extract_project(path):
        m=re.search('^([^/]+)/',path)
        if m!=None:
            project=m.group(1)

            return project
        else:
            raise SDException('SDLOCALP-006','Incorrect value (path=%s)'%path)

    for f in files:
        fmt=sdpostpipelineutils.get_attached_parameter(f,'local_path_project_format',sdconst.DEFAULT_LOCAL_PATH_PROJECT_FORMAT)
        if fmt=="uc":

            path=f["dataset_local_path"]
            project=extract_project(path)

            f["dataset_local_path"]=re.sub('^'+project,project.upper(),path)
    return files

def local_path_custom_transform(files):
    """
    Note
        'sdreducecol' filter must be disabled when using this func
    """

    # Example
    #
    #for f in files:
    #    if f['project']=='CORDEX':
    #        custom_dataset_template='cordex/%(product)s/%(domain)s/%(institute)s/%(driving_model)s/%(experiment)s/%(ensemble)s/%(institute)s-%(rcm_name)s/%(rcm_version)s/%(time_frequency)s/%(variable)s/%(dataset_version)s'
    #        f["dataset_local_path"]=custom_dataset_template%f

def local_path_homemade_transform(files):
    """
    This is to implement complex rules to build local_path (rules which cannot
    fit in local_path_custom_transform() func).

    Note
        'sdreducecol' filter must be disabled when using this func

    TODO
        Make a plugin of this func
    """

    # user code goes here

    return files

def transform_local_path_product(files):
    for f in files:
        fmt=sdpostpipelineutils.get_attached_parameter(f,'local_path_product_format',sdconst.DEFAULT_LOCAL_PATH_PRODUCT_FORMAT)

        if fmt=="normal":
            pass
        elif fmt=="merge":

            path=f["dataset_local_path"]

            # TODO: move to sdproduct

            for product in ['/output1/','/output2/']:
                path=path.replace(product,"/output/")

            f["dataset_local_path"]=path
        elif fmt=="remove":

            path=f["dataset_local_path"]

            # TODO: move to sdproduct

            for product in ['/output/','/output1/','/output2/']:
                path=path.replace(product,"/")

            f["dataset_local_path"]=path
        else:
            raise SDException('SDLOCALP-002',"'local_path_product_format' is incorrect (%s)"%fmt)

    return files

def keep_old_model_name(model):
    """This func is used when you have a lot of already transferred data and
    don't want to move on a new naming scheme.

    Not used for now.

    Deprecated, as we now use model and institute from dataset path, which are the same from the beginning (i.e. CCCma, inmcm4, etc...)
    """
    
    if model=="INM-CM4":
        return "inmcm4"
    elif model=="GFDL-CM2-1":
        return "GFDL-CM2p1"
    elif model=="BCC-CSM1-1":
        return "bcc-csm1-1"
    elif model=="BCC-CSM1-1-m":
        return "bcc-csm1-1-m"
    else:
        return model

def keep_old_institute_name(institute):
    """This func is used when you have a lot of already transferred data and
    don't want to move on a new naming scheme.

    Not used for now.

    Deprecated, as we now use model and institute from dataset path, which are the same from the beginning (i.e. CCCma, inmcm4, etc...)
    """

    if institute=="CCCMA":
        return "CCCma"
    else:
        return institute

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-1','--print_only_one_item',action='store_true')
    parser.add_argument('-F','--format',choices=sdprint.formats,default='raw')
    args = parser.parse_args()

    files=json.load( sys.stdin )

    files=run(files)

    sdprint.print_format(files,args.format,args.print_only_one_item)
