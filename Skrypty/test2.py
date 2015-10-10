import bpy, os
import ctypes
import subprocess

from bpy import context

sceneRender = bpy.data.scenes["Scene"].render
dir = sceneRender.filepath

def render(addon):
    sceneRender.filepath = dir + addon
    bpy.ops.render.render(animation=True)

cam = context.scene.objects["Kamera"]

z = cam.location[2]

l = -cam.location[1]

r60 = 1.04719
r30 = 0.52359
x = l * 0.866
y = l * 0.5

render("0")

cam.location[0] = -x
cam.location[1] = -y
cam.rotation_euler[2] -= r60

render("1")

cam.location[0] = -l
cam.location[1] = 0
cam.rotation_euler[2] -= r30

render("2")

cam.location[0] = -x
cam.location[1] = y
cam.rotation_euler[2] -= r30

render("3")

cam.location[0] = 0
cam.location[1] = l
cam.rotation_euler[2] -= r60

render("4")

cam.location[0] = x
cam.location[1] = y
cam.rotation_euler[2] -= r60

render("5")

cam.location[0] = l
cam.location[1] = 0
cam.rotation_euler[2] -= r30

render("6")

cam.location[0] = x
cam.location[1] = -y
cam.rotation_euler[2] -= r30

render("7")

cam.location[0] = 0
cam.location[1] = -l
cam.location[2] = z
cam.rotation_euler[2] = 0
    
bpy.data.scenes["Scene"].render.filepath = dir

os.chdir(bpy.path.abspath("//Merger"))
subprocess.call(['java', '-jar', "Merger.jar"])

print("\nSKONCZONE!")
ctypes.windll.user32.MessageBoxA(0, "Skończone!", "", 0)