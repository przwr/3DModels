import bpy
import bodyMasks, renderer, layers

def renderClothPart(cloth, bodyPart):
    bodyMasks.setBodyPartMasked(cloth, bodyPart, True)
    renderer.render(cloth + bodyPart)
    bodyMasks.setBodyPartMasked(cloth, bodyPart, False)

def renderParts(cloth, clothFile, parts):
	layers.showOnlyLayer(0)
	layers.showLayersOfObject(cloth, True)
	
	bodyMasks.hideAllObjects(True)
	bodyMasks.hideObject("Gracz", False)
	bodyMasks.hideObject(cloth, False)
			
	bodyMasks.makePlayerMasked(True)
	for part in parts:
		renderClothPart(cloth, part)
		renderer.merge(clothFile)
	bodyMasks.makePlayerMasked(False)
	
def render(cloth, clothFile):
	layers.showOnlyLayer(0)
	layers.showLayersOfObject(cloth, True)
	
	bodyMasks.hideAllObjects(True)
	bodyMasks.hideObject("Gracz", False)
	bodyMasks.hideObject(cloth, False)
			
	bodyMasks.makePlayerMasked(True)
	renderer.render(cloth)
	bodyMasks.makePlayerMasked(False)
	renderer.merge(clothFile)