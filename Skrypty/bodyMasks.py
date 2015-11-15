import bpy

def setBodyPartMasked(playerName, bodyPart, masked):
    player = bpy.data.objects[playerName].modifiers
    player[bodyPart].show_viewport = masked
    player[bodyPart].show_render = masked

def makePlayerMasked(masked):
    bpy.data.materials['skora'].use_sky = masked
    bpy.data.materials['twarz'].use_sky = masked

def hideObject(object, hidden):
    bpy.data.objects[object].hide = hidden
    bpy.data.objects[object].hide_render = hidden   

def hideAllObjects(hidden):
    for index in range(len(bpy.data.objects)):
        bpy.data.objects[index].hide = hidden
        bpy.data.objects[index].hide_render = hidden   
