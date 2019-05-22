import bpy
import sys
import pathlib
import math

bpy.ops.wm.addon_enable(module="io_scene_gltf2")
# Adjust this for where you have the OBJ files.
dirpath = input("Folder where obj and mtl files are located: ")



obj_root = pathlib.Path(dirpath)
print(obj_root)

export_name = str(obj_root)[:-4] + '.obj'
# Before we start, make sure nothing is selected. The importer will select
# imported objects, which allows us to delete them after rendering.
#render = bpy.context.scene.renders


bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Cube'].select = True
bpy.data.objects["Lamp"].select = True
bpy.ops.object.delete() 

if dirpath.lower().endswith('.obj'):
    bpy.ops.import_scene.obj(filepath=str(obj_root))
bpy.ops.export_scene.gltf(filepath=str(export_name))



