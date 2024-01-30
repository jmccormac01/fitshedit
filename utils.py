"""
Utilities for IRAF header manipulation
"""
from glob import glob

def getImageList(filename_list):
    """
    Get the list of Images to edit
    """
    if '*' in filename_list:
        image_list = glob(filename_list)
    elif ',' in filename_list:
        image_list = filename_list.split(',')
    else:
        # assumed to not be a list by this point
        image_list = [filename_list]
    return image_list

def splitKeywordArgs(kwarg_list):
    """
    Split the keyword=argument pairs
    """
    kwargs = {}
    for kwarg in kwarg_list:
        if '=' in kwarg:
            key, arg = kwarg.split('=')
            kwargs[key] = arg
        else:
            print('No matching keyword=argument for {0:s}, skipping...'.format(kwarg))
    return kwargs
