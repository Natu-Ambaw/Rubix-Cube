from cmu_graphics import*
import random
import copy
import math
from smdFunc import *


#################
# Render Screen #
#################

def smdRender_onScreenActivate(app):
    app.rowbutton1 = Region('row1',180,265)
    app.rowbutton2 = Region('row2',180,390)
    app.rowbutton3 = Region('row3',180,530)
    app.colbutton1 = Region('col1',256,630)
    app.colbutton2 = Region('col2',355,650)
    app.colbutton3 = Region('col3',450,672)
    app.sidebutton1 = Region('side1',565,670)
    app.sidebutton2 = Region('side2',655,650)
    app.sidebutton3 = Region('side3',750,630)
    app.buttons = [app.rowbutton1,app.rowbutton2,app.rowbutton3,app.colbutton1,app.colbutton2,app.colbutton3,app.sidebutton1,app.sidebutton2,app.sidebutton3]
    app.selectedbutton=None
    app.pointsRot3 = []
    app.transform = [[1,0,0],[0,1,0],[0,0,0]]
    app.rotateX =[]
    app.rotateY=[]
    app.rotateZ = []
    app.angleX = 13
    app.angleY = 45
    app.angleZ = 0
    app.points3= [[[-1],[-1],[1]],#back top -0
                [[1],[-1],[1]],#right top -1
                [[1],[1],[1]],#right bottom -2
                [[-1],[1],[1]],#back bottom -3
                [[-1],[-1],[-1]],#left top -4
                [[1],[-1],[-1]],#front top -5
                [[1],[1],[-1]],#front bottom -6
                [[-1],[1],[-1]],#left bottom -7
                [[-1/3],[-1],[-1]],#2nd from left top -8
                [[1/3],[-1],[-1]],#3rd from left top -9
                [[-1/3],[-1/3],[-1]],#end of piece 1 --front Face -10
                [[-1],[-1/3],[-1]],#end of piece 1 --front Face edge -11
                [[1/3],[-1/3],[-1]],#end of peice 2 and 3 --front Face -12
                [[1],[-1/3],[-1]],#end of peice 3 --front Face edge -13
                [[-1/3],[1/3],[-1]],#end of piece 4 --front Face -14
                [[-1],[1/3],[-1]],#end of piece 4 --front Face edge -15
                [[1/3],[1/3],[-1]],#end of piece 5 and 6 --front Face -16
                [[1],[1/3],[-1]],#end of piece 6 --front Face edge -17
                [[-1/3],[1],[-1]],#end of piece 7 --front Face -18
                [[1/3],[1],[-1]],#end of piece 8 and 9 --front Face -19
                [[1],[-1],[-1/3]],#2nd from front top -- right face -20
                [[1],[-1],[1/3]],#3rd from front top -- right face -21
                [[1],[-1/3],[-1/3]],#end of piece 1 -- right face -22
                [[1],[-1/3],[1/3]],#end of piece 2 and 3 -- right face -23
                [[1],[-1/3],[1]],#end of piece 3 -- right face edge -24
                [[1],[1/3],[-1/3]],#end of piece 4 -- right face -25
                [[1],[1/3],[1/3]],#end of piece 5 and 6 -- right face -26
                [[1],[1/3],[1]],#end of piece 6 -- right face edge -27
                [[1],[1],[-1/3]],#2nd from right bottom -28
                [[1],[1],[1/3]],#3rd from right bottom -29
                [[-1],[-1],[-1/3]],#2nd from left top -- back -30
                [[-1],[-1],[1/3]],#3rd from left top -- back -31
                [[-1/3],[-1],[-1/3]],#end of piece 1 -- back -32
                [[-1/3],[-1],[1/3]],#end of piece 2 and 3 -- back -33
                [[-1/3],[-1],[1]],#end of piece  3 -- back edge -34
                [[1/3],[-1],[-1/3]],#end of piece 4 -- back -35
                [[1/3],[-1],[1/3]],#end of piece 5 and 6 -- back -36
                [[1/3],[-1],[1]],]#end of piece  6 -- back edge -37

def smdRender_onStep(app):
    getNewRotationMatrixZ(app)
    getNewRotationMatrixX(app)
    getNewRotationMatrixY(app)
    app.pointsRot1 = []
    rotate(app, app.points3,200,app.pointsRot3)

def smdRender_redrawAll(app):
    drawRect(750,700,150,70,fill=app.buttonColor)
    drawLabel('3D Render',825,735,fill='white',size=28)
    drawRect(840,150,150,70,fill='grey')
    drawLabel('Flip',915,185,fill='white',size=16)
    k=0
    pointsLocs3=[[z,z] for z in range(len(app.pointsRot3))]
    for cx3,cy3 in app.pointsRot3:
        pointsLocs3[k]=[cx3,cy3]
        k+=1
    drawRender(app, pointsLocs3)

def smdRender_onMousePress(app,mouseX,mouseY):
    #3d selection
    if 217<=mouseX<=783 and 529<=mouseY<=658:
        row = 2
    if 217<=mouseX<=783 and 399<=mouseY<=529:
        row = 1
    if 217<=mouseX<=783 and 142<=mouseY<=399:
        row = 0
    if 217<=mouseX<=311:
        col = 0
    if 311<=mouseX<=406:
        col = 1
    if 406<=mouseX:
        col = 2
    if not app.flip:
        if 217<=mouseX<=500 and 269<=mouseY<=595:#front
            app.selectedCell = ((row,col),app.frontLayer)
        if 500<=mouseX<=783 and 269<=mouseY<=658:#right
            app.selectedCell = ((row,col),app.rightLayer)
        if 311<=mouseX<=689 and 142<=mouseY<=248:#top
            app.selectedCell = ((row,col),app.topLayer)
    if app.flip:
        if 217<=mouseX<=500 and 269<=mouseY<=595:#left
            app.selectedCell = ((row,2-col),app.leftLayer)
        if 500<=mouseX<=783 and 269<=mouseY<=658:#back
            app.selectedCell = ((row,col),app.backLayer)
        if 311<=mouseX<=689 and 142<=mouseY<=248:#bottom
            app.selectedCell = ((row,col),app.bottomLayer)
    #buttons
    if 840<=mouseX<=990 and 150<=mouseY<=220:
        app.flip= not app.flip
    if 750<=mouseX<=950 and 700<=mouseY<=770:
        app.render=not app.render
        if app.render:
            app.buttonColor='black'
        else:
            app.buttonColor='grey'
        setActiveScreen('smdPlay')

def smdRender_onKeyPress(app, key):
    if key =='l':#change to rotate by face
        rowCol,layer = app.selectedCell
        row,col = rowCol
        if col == 0 and layer == app.frontLayer:
            app.selectedCell = (rowCol,app.leftLayer)
        rotateCol(app,app.selectedCell)
    if key =='r':
        rotateRow(app,app.selectedCell)
    if key == 'j':
        rotateColReverse(app,app.selectedCell)
    if key == 'w':
        rotateRowReverse(app,app.selectedCell)
    if key == 'm':
        reset(app)
    
def rotateLayer(app, layer):
    if layer!=None:
        if layer == app.rowbutton1:
            rotateRow(app, ((0,0),app.leftLayer))
        if layer == app.rowbutton2:
            rotateRow(app, ((1,0),app.leftLayer))
        if layer == app.rowbutton3:
            rotateRow(app, ((2,0),app.leftLayer))
        if layer == app.colbutton1:
            rotateCol(app, ((0,0),app.leftLayer))
        if layer == app.colbutton3:
            rotateCol(app, ((0,0),app.rightLayer))
        if layer == app.colbutton2:
            rotateCol(app, ((0,0),app.frontLayer))

def drawRender(app,pointsLocs3):
    if not app.flip:
    #front Face
        drawFace(4,8,10,11,pointsLocs3,app.frontLayer.face[0][0])
        drawFace(8,10,12,9,pointsLocs3,app.frontLayer.face[0][1])
        drawFace(9,12,13,5,pointsLocs3,app.frontLayer.face[0][2])
        drawFace(11,10,14,15,pointsLocs3,app.frontLayer.face[1][0])
        drawFace(10,14,16,12,pointsLocs3,app.frontLayer.face[1][1])
        drawFace(16,12,13,17,pointsLocs3,app.frontLayer.face[1][2])
        drawFace(15,7,18,14,pointsLocs3,app.frontLayer.face[2][0])
        drawFace(18,14,16,19,pointsLocs3,app.frontLayer.face[2][1])
        drawFace(19,16,17,6,pointsLocs3,app.frontLayer.face[2][2])
        #right Face
        drawFace(5,20,22,13,pointsLocs3,app.rightLayer.face[0][0])
        drawFace(20,22,23,21,pointsLocs3,app.rightLayer.face[0][1])
        drawFace(23,21,1,24,pointsLocs3,app.rightLayer.face[0][2])
        drawFace(13,22,25,17,pointsLocs3,app.rightLayer.face[1][0])
        drawFace(25,22,23,26,pointsLocs3,app.rightLayer.face[1][1])
        drawFace(23,26,27,24,pointsLocs3,app.rightLayer.face[1][2])
        drawFace(17,25,28,6,pointsLocs3,app.rightLayer.face[2][0])
        drawFace(28,25,26,29,pointsLocs3,app.rightLayer.face[2][1])
        drawFace(29,26,27,2,pointsLocs3,app.rightLayer.face[2][2])
        #top face
        drawFace(4,30,32,8,pointsLocs3,app.topLayer.face[2][0])
        drawFace(30,32,33,31,pointsLocs3,app.topLayer.face[1][0])
        drawFace(33,31,0,34,pointsLocs3,app.topLayer.face[0][0])
        drawFace(8,32,35,9,pointsLocs3,app.topLayer.face[2][1])
        drawFace(32,35,36,33,pointsLocs3,app.topLayer.face[1][1])
        drawFace(36,33,34,37,pointsLocs3,app.topLayer.face[0][1])
        drawFace(9,35,20,5,pointsLocs3,app.topLayer.face[2][2])
        drawFace(20,35,36,21,pointsLocs3,app.topLayer.face[1][2])
        drawFace(21,36,37,1,pointsLocs3,app.topLayer.face[0][2])
        #edges
        # face1
        connectLine(0,1,pointsLocs3,pointsLocs3)
        connectLine(1,2,pointsLocs3,pointsLocs3)
        # face2
        connectLine(4,5,pointsLocs3,pointsLocs3)
        connectLine(5,6,pointsLocs3,pointsLocs3)
        connectLine(6,7,pointsLocs3,pointsLocs3)
        connectLine(7,4,pointsLocs3,pointsLocs3)
        # sides
        connectLine(0,4,pointsLocs3,pointsLocs3)
        connectLine(1,5,pointsLocs3,pointsLocs3)
        connectLine(2,6,pointsLocs3,pointsLocs3)
        # face front
        connectLine(8,18,pointsLocs3,pointsLocs3)
        connectLine(9,19,pointsLocs3,pointsLocs3)
        connectLine(11,13,pointsLocs3,pointsLocs3)
        connectLine(15,17,pointsLocs3,pointsLocs3)#no more 3
        # face right
        connectLine(20,28,pointsLocs3,pointsLocs3)
        connectLine(21,29,pointsLocs3,pointsLocs3)
        connectLine(13,24,pointsLocs3,pointsLocs3)
        connectLine(17,27,pointsLocs3,pointsLocs3)
        # face top
        connectLine(8,34,pointsLocs3,pointsLocs3)
        connectLine(9,37,pointsLocs3,pointsLocs3)
        connectLine(30,20,pointsLocs3,pointsLocs3)
        connectLine(31,21,pointsLocs3,pointsLocs3)
    else:
        drawFace(4,8,10,11,pointsLocs3,app.leftLayer.face[2][2])
        drawFace(8,10,12,9,pointsLocs3,app.leftLayer.face[2][1])
        drawFace(9,12,13,5,pointsLocs3,app.leftLayer.face[2][0])
        drawFace(11,10,14,15,pointsLocs3,app.leftLayer.face[1][2])
        drawFace(10,14,16,12,pointsLocs3,app.leftLayer.face[1][1])
        drawFace(16,12,13,17,pointsLocs3,app.leftLayer.face[1][0])
        drawFace(15,7,18,14,pointsLocs3,app.leftLayer.face[0][2])
        drawFace(18,14,16,19,pointsLocs3,app.leftLayer.face[0][1])
        drawFace(19,16,17,6,pointsLocs3,app.leftLayer.face[0][0])
        #right Face
        drawFace(5,20,22,13,pointsLocs3,app.backLayer.face[2][2])
        drawFace(20,22,23,21,pointsLocs3,app.backLayer.face[2][1])
        drawFace(23,21,1,24,pointsLocs3,app.backLayer.face[2][0])
        drawFace(13,22,25,17,pointsLocs3,app.backLayer.face[1][2])
        drawFace(25,22,23,26,pointsLocs3,app.backLayer.face[1][1])
        drawFace(23,26,27,24,pointsLocs3,app.backLayer.face[1][0])
        drawFace(17,25,28,6,pointsLocs3,app.backLayer.face[0][2])
        drawFace(28,25,26,29,pointsLocs3,app.backLayer.face[0][1])
        drawFace(29,26,27,2,pointsLocs3,app.backLayer.face[0][0])
        #top face
        drawFace(4,30,32,8,pointsLocs3,app.bottomLayer.face[0][0])
        drawFace(30,32,33,31,pointsLocs3,app.bottomLayer.face[0][1])
        drawFace(33,31,0,34,pointsLocs3,app.bottomLayer.face[0][2])
        drawFace(8,32,35,9,pointsLocs3,app.bottomLayer.face[1][0])
        drawFace(32,35,36,33,pointsLocs3,app.bottomLayer.face[1][1])
        drawFace(36,33,34,37,pointsLocs3,app.bottomLayer.face[1][2])
        drawFace(9,35,20,5,pointsLocs3,app.bottomLayer.face[2][0])
        drawFace(20,35,36,21,pointsLocs3,app.bottomLayer.face[2][1])
        drawFace(21,36,37,1,pointsLocs3,app.bottomLayer.face[2][2])
        #edges
        # face1
        connectLine(0,1,pointsLocs3,pointsLocs3)
        connectLine(1,2,pointsLocs3,pointsLocs3)
        # face2
        connectLine(4,5,pointsLocs3,pointsLocs3)
        connectLine(5,6,pointsLocs3,pointsLocs3)
        connectLine(6,7,pointsLocs3,pointsLocs3)
        connectLine(7,4,pointsLocs3,pointsLocs3)
        # sides
        connectLine(0,4,pointsLocs3,pointsLocs3)
        connectLine(1,5,pointsLocs3,pointsLocs3)
        connectLine(2,6,pointsLocs3,pointsLocs3)
        # face front
        connectLine(8,18,pointsLocs3,pointsLocs3)
        connectLine(9,19,pointsLocs3,pointsLocs3)
        connectLine(11,13,pointsLocs3,pointsLocs3)
        connectLine(15,17,pointsLocs3,pointsLocs3)#no more 3
        # face right
        connectLine(20,28,pointsLocs3,pointsLocs3)
        connectLine(21,29,pointsLocs3,pointsLocs3)
        connectLine(13,24,pointsLocs3,pointsLocs3)
        connectLine(17,27,pointsLocs3,pointsLocs3)
        # face top
        connectLine(8,34,pointsLocs3,pointsLocs3)
        connectLine(9,37,pointsLocs3,pointsLocs3)
        connectLine(30,20,pointsLocs3,pointsLocs3)
        connectLine(31,21,pointsLocs3,pointsLocs3)


