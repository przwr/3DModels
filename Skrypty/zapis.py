import bpy, os

from bpy import context

scene = context.scene

objList = scene.objects

cams = []
dir = bpy.data.scenes["Scene"].render.filepath

cams.append(objList["Clbok"])
cams.append(objList["Clewytyl"])
cams.append(objList["Ctyl"])
cams.append(objList["Cprawytyl"])
cams.append(objList["Cpbok"])
cams.append(objList["Cprawyprzod"])
cams.append(objList["Cprzod"])
cams.append(objList["Clewyprzod"])

for i in range(0,8):
    bpy.data.scenes["Scene"].render.filepath = dir + str(i)
    scene.camera  = cams[i]
    bpy.ops.render.render(animation=True)
    
bpy.data.scenes["Scene"].render.filepath = dir