import yaml
from subprocess import call
import os
import subprocess
import requests
import sys
import time


cmd_fbx_gltf = "./home/centos/blender-2.8/blender -b --python ObjGltf.py"
os.system(cmd_fbx_gltf)

#cmd_gltf_usdz = "python /home/centos/gltf2usd/Source/gltf2usd.py -g /home/centos/CentOS_ec2_converter/Modern.gltf -o /home/centos/CentOS_ec2_converter/Modern.usdz"
#os.system(cmd_gltf_usdz)
