from smdFunc import *
from smdPlay import *


def smdHelp_onScreenActivate(app):
    app.background = 'black'

def smdHelp_redrawAll(app):
    drawLabel('3D Render',825,735,fill='white',size=28)
    drawRect(750,600,150,50,fill=app.buttonColor)
    drawLabel('Help',825,625,fill='white',size=24)
    drawRect(30,150,150,70, fill='grey')
    drawLabel('Scramble',105,185,fill='white',size=16)
    drawRect(30,50,150,70, fill='grey')
    drawLabel('Solve',105,85,fill='white',size=16)
    drawFaceId(app)
    for layer in range(len(app.layers)):
        drawBoard(app,app.layers[layer],layer)
        drawBoardBorder(app,app.layers[layer])
    if app.render:
        drawRect(510,545,225,225,fill='white')
        drawRect(510,545,225,15,fill='grey')
        drawRect(510,545,225,225,fill=None,border='black',borderWidth=2)
    drawRect(0,0,app.width,app.height, fill='black', opacity =50)
    drawRect(app.width/2,app.height/2, 400,600, align = 'center', fill = 'black')
    drawRect(300,100, 400,20, fill = 'grey')
    drawLabel('Instructions:', 500, 150, size=24, fill = 'white')
    drawLabel("Click a piece to Select" , 500, 190, size=18, fill = 'white')
    drawLabel("Press 'r' to rotate a row counterClockwise" , 500, 230, size=18, fill = 'white')
    drawLabel("Press 'w' to rotate a row Clockwise" , 500, 270, size=18, fill = 'white')
    drawLabel("Press 'l' to rotate a column counterClockwise" , 500, 310, size=18, fill = 'white')
    drawLabel("Press 'j' to rotate a column Clockwise" , 500, 350, size=18, fill = 'white')
    drawLabel("Press 'm' to reset your cube" , 500, 390, size=18, fill = 'white')
    drawLabel("And Most Importantly:" , 500, 570, size=18, fill = 'white')
    drawLabel("Have Fun!" , 500, 600, size=24, fill = 'white')
    drawLabel("Click off the screen to close the window" , 500, 650, size=18, fill = 'white')

def smdHelp_onMousePress(app, mouseX, mouseY):
    if not (300<=mouseX<=700 and 100<=mouseY<=700):
        setActiveScreen('smdPlay')