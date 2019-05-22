import bpy
import sys
import pathlib
import math


# Adjust this for where you have the OBJ files.
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"
print('arguments=',argv)
dirpath = argv[0]
obj_root = pathlib.Path(dirpath)
print(obj_root)

export_name = str(obj_root)[:-4] + '.obj'
# Before we start, make sure nothing is selected. The importer will select
# imported objects, which allows us to delete them after rendering.
#render = bpy.context.scene.renders


bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['Cube'].select_set(state=True)
bpy.data.objects['Light'].select_set(state=True)
bpy.ops.object.delete() 

if dirpath.lower().endswith('.fbx'):
    bpy.ops.import_scene.fbx(filepath=str(obj_root))
if dirpath.lower().endswith('.stl'):
    bpy.ops.import_mesh.stl(filepath=str(obj_root), axis_forward='-Z', axis_up='Y')
    bpy.ops.export_scene.obj(filepath=str(export_name))
    mat = bpy.data.materials.new("VusarDefault")
    mat.diffuse_color = (float(.69), float(.769), 1)
    o = bpy.context.selected_objects[0]
    o.active_material = mat

bpy.ops.export_scene.obj(filepath=str(export_name), group_by_material=True)
bpy.ops.export_scene.gltf(export_format='GLTF_SEPARATE', filepath=str(export_name), group_by_material=True)
