import bpy

def switchLayer(i, show):
	bpy.data.scenes["Scene"].layers[i] = show

def showOnlyLayer(i):
	for index in range(len(bpy.data.scenes["Scene"].layers)):
		if index == i:
			bpy.data.scenes["Scene"].layers[index] = True
		else:
			bpy.data.scenes["Scene"].layers[index] = False
			bpy.data.scenes["Scene"].layers[index] = False

def changeAllLayers(change):
	for index in range(len(bpy.data.scenes["Scene"].layers)):
		bpy.data.scenes["Scene"].layers[index] = change
		bpy.data.scenes["Scene"].layers[index] = change

def showLayersOfObject(object, change):
	for index in range(len(bpy.data.scenes["Scene"].layers)):
		if bpy.data.objects[object].layers[index] == change:
			bpy.data.scenes["Scene"].layers[index] = change
			bpy.data.scenes["Scene"].layers[index] = change