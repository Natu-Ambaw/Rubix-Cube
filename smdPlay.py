from cmu_graphics import*
import random
import copy
import math
from smdFunc import *

###############
# Play Screen #
###############
def onAppStart(app):
    app.count=0
    app.moves={}
    app.flip = False
    app.width = 1000
    app.height = 800
    app.rows=3
    app.cols=3
    app.boardHeight=225
    app.boardWidth=225
    app.frontLayer = Face([(['pink']*app.cols) for row in range(app.rows)],265,288,'app.frontLayer')
    app.frontLayer1 = Face([[1,2,3],[4,5,6],[7,8,9]],265,288,'app.frontLayer1')
    app.topLayer = Face([(['white']*app.cols) for row in range(app.rows)],265,31,'app.topLayer')
    app.topLayer1 = Face([[1,2,3],[4,5,6],[7,8,9]],265,31,'app.topLayer1')
    app.rightLayer = Face([(['lightblue']*app.cols) for row in range(app.rows)],510,288,'app.rightLayer')
    app.rightLayer1 = Face([[1,2,3],[4,5,6],[7,8,9]],510,288,'app.rightLayer1')
    app.leftLayer = Face([(['lightgreen']*app.cols) for row in range(app.rows)],20,288,'app.leftLayer')
    app.leftLayer1 = Face([[1,2,3],[4,5,6],[7,8,9]],20,288,'app.leftLayer1')
    app.bottomLayer = Face([(['yellow']*app.cols) for row in range(app.rows)],265,545,'app.bottomLayer')
    app.bottomLayer1 = Face([[1,2,3],[4,5,6],[7,8,9]],265,545,'app.bottomLayer1')
    app.backLayer = Face([(['orange']*app.cols) for row in range(app.rows)],755,288,'app.backLayer')
    app.backLayer1 = Face([[1,2,3],[4,5,6],[7,8,9]],755,288,'app.backLayer1')
    app.cellBorderWidth = 2
    app.layers=[app.frontLayer,app.topLayer,app.leftLayer,app.rightLayer,app.bottomLayer,app.backLayer]
    app.layers1=[app.frontLayer1,app.topLayer1,app.leftLayer1,app.rightLayer1,app.bottomLayer1,app.backLayer1,[(['lightblue']*app.cols) for row in range(app.rows)],[(['lightgreen']*app.cols) for row in range(app.rows)],[(['yellow']*app.cols) for row in range(app.rows)],[(['orange']*app.cols) for row in range(app.rows)]]
    app.selectedCell=((0,0),app.leftLayer)
    app.buttonColor='grey'
    app.render=False
    app.layersRow = [app.frontLayer,app.leftLayer,app.backLayer, app.rightLayer]
    app.layersCol = [app.leftLayer, app.rightLayer, app.frontLayer]
    app.solved = [[(['pink']*app.cols) for row in range(app.rows)],[(['white']*app.cols) for row in range(app.rows)],[(['lightgreen']*app.cols) for row in range(app.rows)],[(['lightblue']*app.cols) for row in range(app.rows)],[(['yellow']*app.cols) for row in range(app.rows)],[(['orange']*app.cols) for row in range(app.rows)]]

def smdPlay_redrawAll(app):
    drawLabel('Rubix Almost Cube', 100, 30, size=16)
    drawRect(750,700,150,70,fill=app.buttonColor)
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

def smdPlay_onKeyPress(app,key):
    if key =='l':#change to rotate by face
        rotateCol(app,app.selectedCell)
    if key =='r':
        rotateRow(app,app.selectedCell)
    if key == 'j':
        rotateColReverse(app,app.selectedCell)
    if key == 'w':
        rotateRowReverse(app,app.selectedCell)
    if key == 'm':
        reset(app)

##########
# Boards #
##########
def drawFaceId(app):
    drawLabel('Left',133,273,size=16)
    drawLabel('Front',378,273,size=16)
    drawLabel('Right',623,273,size=16)
    drawLabel('Back',868,273,size=16)
    drawLabel('Top',378,16,size=16)
    drawLabel('Bottom',378,530,size=16)
def drawBoard(app,board,layer):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col, board.face[row][col],board,layer)
def drawBoardBorder(app,board):
  # draw the board outline (with double-thickness):
  drawRect(board.left, board.top, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)
def drawCell(app, row, col, color,board,layer):
    cellLeft, cellTop = getCellLeftTop(app, row, col,board)
    cellWidth, cellHeight = getCellSize(app)
    borderColor = 'cyan' if ((row, col),board) == app.selectedCell else 'black'
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color, border=borderColor,
             borderWidth=app.cellBorderWidth)
    # drawLabel(f'{app.layers1[layer].face[row][col]}',cellLeft+cellWidth/2,cellTop+cellHeight/2, fill = 'black')
def getCellLeftTop(app, row, col,board):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = board.left + col * cellWidth
    cellTop = board.top + row * cellHeight
    return (cellLeft, cellTop)
def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

#############
# Selection #
#############
def smdPlay_onMousePress(app, mouseX, mouseY):
    if 750<=mouseX<=900 and 600<=mouseY<=650:#solver button
        setActiveScreen('smdHelp')
    if 30<=mouseX<=180 and 50<=mouseY<=120:#solver button
        solver(app)
    if 30<=mouseX<=180 and 150<=mouseY<=220:#scramble buttom
        scramble(app)
    selCell = getCell(app, mouseX, mouseY)#cell selection
    if selCell != None:
        selectedCell,layer=getCell(app, mouseX, mouseY)
        app.selectedCell = selectedCell,layer
    if 750<=mouseX<=950 and 700<=mouseY<=770:
        app.render=not app.render
        if app.render:
            app.buttonColor='black'
        else:
            app.buttonColor='grey'
        setActiveScreen('smdRender')
def getCell(app, x, y):
    for layer in app.layers:
        dx = x - layer.left
        dy = y - layer.top
        cellWidth, cellHeight = getCellSize(app)
        row = math.floor(dy / cellHeight)
        col = math.floor(dx / cellWidth)
        if (0 <= row < app.rows) and (0 <= col < app.cols):
            return ((row, col),layer)
    else:
        return None
        

