#--------------------------------------------------
# mau_blendTransform.py
# version: 0.0.1
# last updated: 15.05.22 (DD.MM.YY)
#--------------------------------------------------

import nuke

def mol_blendTransform():
    #empty list for selected nodes
    selnodes = []

    #adding selected nodes into list
    for i in nuke.selectedNodes():
        selnodes.append(i.name())

    #defining ORIGIN and DESTINATION based or order of selection 
    orig = selnodes[-1]
    dest = selnodes[0]

    #creating new Camera
    blendTransf = nuke.nodes.Transform()

    #defining node colour
    blendTransf_r = 0.055
    blendTransf_g = 0.169
    blendTransf_b = 0.243
    hexColour = int('%02x%02x%02x%02x' % (blendTransf_r*255,blendTransf_g*255,blendTransf_b*255,1),16)
    blendTransf.knob('tile_color').setValue(hexColour)

    #creating new slider knob and adding into Camera
    weight = nuke.Double_Knob('weight','weight')
    blendTransf.addKnob(weight)

    #adding expression into Transform's translation
    blendTransf.knob('translate').setExpression('((1-weight)*'+orig+'.translate)-('+dest+'.translate*-1*weight)')
    blendTransf.knob('scale').setExpression('((1-weight)*'+orig+'.scale)-('+dest+'.scale*-1*weight)')
    blendTransf.knob('rotate').setExpression('((1-weight)*'+orig+'.rotate)-('+dest+'.rotate*-1*weight)')
    blendTransf.knob('center').setExpression('((1-weight)*'+orig+'.center)-('+dest+'.center*-1*weight)')


    #adding new label into Camera
    blendTransf.knob('label').setValue('\n'+'BlendTransform'+'\n'+'\n'+orig+' <---> '+dest)


# add the following to menu.py
#===================================================================================================================
# MAU BLEND TRANSFORM
#===================================================================================================================
#import mau_blendTransform
#mauMenu.addCommand('comp/mo_blendTransform','mau_blendCam.mol_blendTransform()')
