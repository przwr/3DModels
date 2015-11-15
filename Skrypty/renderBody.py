import bpy, sys
import renderer
import bodyMasks
import layers

cam = bpy.context.scene.objects["Kamera"]

def renderBodyPart(bodyPart):
    bodyMasks.setBodyPartMasked("Gracz", bodyPart, True)
    renderer.render(bodyPart)
    bodyMasks.setBodyPartMasked("Gracz", bodyPart, False)

def render():
	layers.showOnlyLayer(0)
	
	renderBodyPart("GlowaMask")
	renderer.merge("head")
	
	renderBodyPart("LnogaMask")
	renderer.merge("leg1")
	
	renderBodyPart("PnogaMask")
	renderer.merge("leg")
	
	renderBodyPart("TorsMask")
	renderer.merge("torso")
	
	renderBodyPart("LrekaMask")
	renderer.merge("torso2")
	
	renderBodyPart("PrekaMask")
	renderer.merge("torso1")
	
	layers.changeAllLayers(True)