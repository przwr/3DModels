import bpy, os
import ctypes
import subprocess

from bpy import context

def renderDirection(dir, addon):
    bpy.data.scenes["Scene"].render.filepath = dir + addon
    bpy.ops.render.render(animation=True)

dir = bpy.data.scenes["Scene"].render.filepath
cam = context.scene.objects["Kamera"]
z = cam.location[2]	
l = -cam.location[1]	
r60 = 1.04719
r30 = 0.52359
x = l * 0.866
y = l * 0.5
	
renderDirection(dir, addon + "0")

cam.location[0] = -x
cam.location[1] = -y
cam.rotation_euler[2] -= r60

renderDirection(dir, addon + "1")

cam.location[0] = -l
cam.location[1] = 0
cam.rotation_euler[2] -= r30

renderDirection(dir, addon + "2")

cam.location[0] = -x
cam.location[1] = y
cam.rotation_euler[2] -= r30

renderDirection(dir, addon + "3")

cam.location[0] = 0
cam.location[1] = l
cam.rotation_euler[2] -= r60

renderDirection(dir, addon + "4")

cam.location[0] = x
cam.location[1] = y
cam.rotation_euler[2] -= r60

renderDirection(dir, addon + "5")

cam.location[0] = l
cam.location[1] = 0
cam.rotation_euler[2] -= r30

renderDirection(dir, addon + "6")

cam.location[0] = x
cam.location[1] = -y
cam.rotation_euler[2] -= r30

renderDirection(dir, addon + "7")

cam.location[0] = 0
cam.location[1] = -l
cam.location[2] = z
cam.rotation_euler[2] = 0
	
bpy.data.scenes["Scene"].render.filepath = dir

os.chdir(bpy.path.abspath("//Merger"))
subprocess.call(['java', '-jar', "Merger.jar"])

print("Koniec!")