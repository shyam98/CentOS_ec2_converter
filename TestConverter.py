


dirpath = input("Folder where obj and mtl files are located: ")

def convert_stl_fbx_to_obj(input_filepath):
    print("convert_stl_fbx_to_obj:Calling blender to convert stl/fbx file:" + input_filepath)
    cmdline = "/home/centos/blender-2.8/blender -b --python ObjGltf.py -- {0}" \
        .format(input_filepath)
    print("convert_stl_fbx_to_obj: blender command: " + cmdline)
    p = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
    print("convert_stl_fbx_to_obj: blender subprocess starting")
    out, err = p.communicate()
    if p.returncode != 0:
        print("Blender failed: stl/fbx to obj conversion failed %d %s" % (p.returncode, out))
        raise Exception('Blender Failed')
