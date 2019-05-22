import yaml
from subprocess import call
import os
import subprocess
import requests
import sys
import time


input_filepath = '~/home/centos/CentOS_ec2_converter/modern.fbx'

print("convert_stl_fbx_to_obj:Calling blender to convert stl/fbx file:" + input_filepath)

cmdline = "/home/centos/blender-2.8/blender -b --python ObjGltf.py -- {0}" \
    .format(input_filepath)
print("convert_stl_fbx_to_obj: blender command: " + cmdline)

os.system(cmdline)
