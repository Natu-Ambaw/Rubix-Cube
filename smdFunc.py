from cmu_graphics import *
import os, pathlib
import math
import random
import copy

###########
# Classes #
###########

class Button:
    def __init__(self,cx,cy):
        pass

class Face:
    def __init__(self,face,left,top,name):
        self.face=face
        self.left=left
        self.top=top
        self.name = name
    
    def __repr__(self):
        return self.name

class Region:
    def __init__(self,name, x,y):
        self.x = x
        self.y = y
        self.name = name
        self.color = 'plum'

    def __repr__(self):
        return self.name


############
# Rotation #
############
    
def rotateRow(app,selected):
    rowCol, layer = selected
    row,col = rowCol
    app.count+=1
    app.frontLayer.face[row], app.rightLayer.face[row], app.backLayer.face[row], app.leftLayer.face[row] = app.leftLayer.face[row], app.frontLayer.face[row], app.rightLayer.face[row], app.backLayer.face[row]
    app.frontLayer1.face[row], app.rightLayer1.face[row], app.backLayer1.face[row], app.leftLayer1.face[row] = app.leftLayer1.face[row], app.frontLayer1.face[row], app.rightLayer1.face[row], app.backLayer1.face[row]
    if row==0:
        newLayer = rotateRightBot(app,app.topLayer)
        app.topLayer.face = newLayer
        newLayer1 = rotateRightBot(app,app.topLayer1)
        app.topLayer1.face = newLayer1
    elif row==2:
        newLayer = rotateRightBot(app,app.bottomLayer)
        app.bottomLayer.face = newLayer
        newLayer1 = rotateRightBot(app,app.bottomLayer1)
        app.bottomLayer1.face = newLayer1
    boardPos = copy.deepcopy([app.frontLayer.face,app.topLayer.face,app.leftLayer.face,app.rightLayer.face,app.bottomLayer.face,app.backLayer.face])
    app.moves[app.count]=['r',rowCol,layer,boardPos]
def rotateRowReverse(app,selected):
    rowCol, layer = selected
    row,col = rowCol
    app.count+=1
    # app.frontLayer.face[row], app.rightLayer.face[row], app.backLayer.face[row], app.leftLayer.face[row] = app.leftLayer.face[row], app.frontLayer.face[row], app.rightLayer.face[row], app.backLayer.face[row]
    app.leftLayer.face[row], app.frontLayer.face[row], app.rightLayer.face[row], app.backLayer.face[row] = app.frontLayer.face[row], app.rightLayer.face[row], app.backLayer.face[row], app.leftLayer.face[row]
    # app.frontLayer1.face[row], app.rightLayer1.face[row], app.backLayer1.face[row], app.leftLayer1.face[row] = app.leftLayer1.face[row], app.frontLayer1.face[row], app.rightLayer1.face[row], app.backLayer1.face[row]
    if row==0:
        newLayer = rotateLeftTop(app,app.topLayer)
        app.topLayer.face = newLayer
        # newLayer1 = rotateRightBot(app,app.topLayer1)
        # app.topLayer1.face = newLayer1
    elif row==2:
        newLayer = rotateLeftTop(app,app.bottomLayer)
        app.bottomLayer.face = newLayer
        # newLayer1 = rotateRightBot(app,app.bottomLayer1)
        # app.bottomLayer1.face = newLayer1
    boardPos = copy.deepcopy([app.frontLayer.face,app.topLayer.face,app.leftLayer.face,app.rightLayer.face,app.bottomLayer.face,app.backLayer.face])
    app.moves[app.count]=['w',rowCol,layer,boardPos]

def rotateRightBot(app, layer):
    result = [([None]*app.cols) for row in range(app.rows)]
    result[0][0]=layer.face[2][0]
    result[0][1]=layer.face[1][0]
    result[0][2]=layer.face[0][0]
    result[1][0]=layer.face[2][1]
    result[1][1]=layer.face[1][1]
    result[1][2]=layer.face[0][1]
    result[2][0]=layer.face[2][2]
    result[2][1]=layer.face[1][2]
    result[2][2]=layer.face[0][2]
    return result
def rotateLeftTop(app, layer):
    result = [([None]*app.cols) for row in range(app.rows)]
    result[0][0]=layer.face[0][2]
    result[0][1]=layer.face[1][2]
    result[0][2]=layer.face[2][2]
    result[1][0]=layer.face[0][1]
    result[1][1]=layer.face[1][1]
    result[1][2]=layer.face[2][1]
    result[2][0]=layer.face[0][0]
    result[2][1]=layer.face[1][0]
    result[2][2]=layer.face[2][0]
    return result

def rotateCol(app,selected):
    rowCol, layer = selected
    front = copy.deepcopy(app.frontLayer.face)
    back = copy.deepcopy(app.backLayer.face)
    top = copy.deepcopy(app.topLayer.face)
    bottom = copy.deepcopy(app.bottomLayer.face)
    left = copy.deepcopy(app.leftLayer.face)
    right = copy.deepcopy(app.rightLayer.face)
    front1 = copy.deepcopy(app.frontLayer1.face)
    back1 = copy.deepcopy(app.backLayer1.face)
    top1 = copy.deepcopy(app.topLayer1.face)
    bottom1 = copy.deepcopy(app.bottomLayer1.face)
    left1 = copy.deepcopy(app.leftLayer1.face)
    right1 = copy.deepcopy(app.rightLayer1.face)
    app.count+=1
    if layer == app.leftLayer:
        for row in range(app.rows):
            app.frontLayer.face[row][0], app.topLayer.face[row][0], app.backLayer.face[row][2], app.bottomLayer.face[row][0]=top[row][0], back[2-row][2], bottom[2-row][0], front[row][0]
            app.frontLayer1.face[row][0], app.topLayer1.face[row][0], app.backLayer1.face[row][2], app.bottomLayer1.face[row][0]=top1[2-row][0], back1[2-row][2], bottom1[row][0], front1[row][0]
            app.leftLayer.face=rotateLeftTop(app,app.leftLayer)
            app.leftLayer1.face=rotateLeftTop(app,app.leftLayer1)
    if layer == app.rightLayer:
        for row in range(app.rows):
            app.frontLayer.face[row][2], app.topLayer.face[row][2], app.backLayer.face[row][0], app.bottomLayer.face[row][2]=top[row][2], back[2-row][0], bottom[2-row][2], front[row][2]
            app.frontLayer1.face[row][2], app.topLayer1.face[row][2], app.backLayer1.face[row][0], app.bottomLayer1.face[row][2]=top1[row][0], back1[2-row][0], bottom1[2-row][2], front1[row][2]
            app.rightLayer.face=rotateRightBot(app,app.rightLayer)
            app.rightLayer1.face=rotateRightBot(app,app.rightLayer1)
    if layer == app.frontLayer:
        for row in range(app.rows):
            app.frontLayer.face[row][1], app.topLayer.face[row][1], app.backLayer.face[row][1], app.bottomLayer.face[row][1]=top[row][1], back[2-row][1], bottom[2-row][1], front[row][1]
            app.frontLayer1.face[row][1], app.topLayer1.face[row][1], app.backLayer1.face[row][1], app.bottomLayer1.face[row][1]=top1[row][1], back1[2-row][1], bottom1[2-row][1], front1[row][1]
    boardPos = copy.deepcopy([app.frontLayer.face,app.topLayer.face,app.leftLayer.face,app.rightLayer.face,app.bottomLayer.face,app.backLayer.face])
    app.moves[app.count]=['l',rowCol,layer,boardPos]
def rotateColReverse(app,selected):
    rowCol, layer = selected
    front = copy.deepcopy(app.frontLayer.face)
    back = copy.deepcopy(app.backLayer.face)
    top = copy.deepcopy(app.topLayer.face)
    bottom = copy.deepcopy(app.bottomLayer.face)
    left = copy.deepcopy(app.leftLayer.face)
    right = copy.deepcopy(app.rightLayer.face)
    front1 = copy.deepcopy(app.frontLayer1.face)
    back1 = copy.deepcopy(app.backLayer1.face)
    top1 = copy.deepcopy(app.topLayer1.face)
    bottom1 = copy.deepcopy(app.bottomLayer1.face)
    left1 = copy.deepcopy(app.leftLayer1.face)
    right1 = copy.deepcopy(app.rightLayer1.face)
    app.count+=1
    
    if layer == app.leftLayer:
        for row in range(app.rows):
            # app.frontLayer.face[row][0], app.topLayer.face[row][0], app.backLayer.face[row][2], app.bottomLayer.face[row][0]=top[row][0], back[2-row][2], bottom[2-row][0], front[row][0]
            app.topLayer.face[row][0], app.backLayer.face[2-row][2], app.bottomLayer.face[2-row][0], app.frontLayer.face[row][0] = front[row][0], top[row][0], back[row][2], bottom[row][0]
            # app.frontLayer1.face[row][0], app.topLayer1.face[row][0], app.backLayer1.face[row][2], app.bottomLayer1.face[row][0]=top1[2-row][0], back1[2-row][2], bottom1[row][0], front1[row][0]
            app.leftLayer.face=rotateRightBot(app,app.leftLayer)
            # app.leftLayer1.face=rotateLeftTop(app,app.leftLayer1)
    if layer == app.rightLayer:
        for row in range(app.rows):
            # app.frontLayer.face[row][2], app.topLayer.face[row][2], app.backLayer.face[row][0], app.bottomLayer.face[row][2]=top[row][2], back[2-row][0], bottom[2-row][2], front[row][2]
            app.topLayer.face[row][2], app.backLayer.face[2-row][0], app.bottomLayer.face[2-row][2], app.frontLayer.Piece[row][2] = front[row][2], top[row][2], back[row][0], bottom[row][2]
            # app.frontLayer1.face[row][2], app.topLayer1.face[row][2], app.backLayer1.face[row][0], app.bottomLayer1.face[row][2]=top1[row][0], back1[2-row][0], bottom1[2-row][2], front1[row][2]
            app.rightLayer.face=rotateLeftTop(app,app.rightLayer)
            # app.rightLayer1.face=rotateRightBot(app,app.rightLayer1)
    if layer == app.frontLayer:
        for row in range(app.rows):
            # app.frontLayer.face[row][1], app.topLayer.face[row][1], app.backLayer.face[row][1], app.bottomLayer.face[row][1]=top[row][1], back[2-row][1], bottom[2-row][1], front[row][1]
            app.topLayer.face[row][1], app.backLayer.face[2-row][1], app.bottomLayer.face[2-row][1], app.frontLayer.face[row][1] = front[row][1], top[row][1], back[row][1], bottom[row][1]
            # app.frontLayer1.face[row][1], app.topLayer1.face[row][1], app.backLayer1.face[row][1], app.bottomLayer1.face[row][1]=top1[row][1], back1[2-row][1], bottom1[2-row][1], front1[row][1]
    boardPos = copy.deepcopy([app.frontLayer.face,app.topLayer.face,app.leftLayer.face,app.rightLayer.face,app.bottomLayer.face,app.backLayer.face])
    app.moves[app.count]=['j',rowCol,layer,boardPos]

def reset(app):
    app.frontLayer.face = [(['pink']*app.cols) for row in range(app.rows)]
    app.frontLayer1.face = [[1,2,3],[4,5,6],[7,8,9]]
    app.topLayer.face = [(['white']*app.cols) for row in range(app.rows)]
    app.topLayer1.face = [[1,2,3],[4,5,6],[7,8,9]]
    app.rightLayer.face = [(['lightblue']*app.cols) for row in range(app.rows)]
    app.rightLayer1.face = [[1,2,3],[4,5,6],[7,8,9]]
    app.leftLayer.face = [(['lightgreen']*app.cols) for row in range(app.rows)]
    app.leftLayer1.face = [[1,2,3],[4,5,6],[7,8,9]]
    app.bottomLayer.face = [(['yellow']*app.cols) for row in range(app.rows)]
    app.bottomLayer1.face = [[1,2,3],[4,5,6],[7,8,9]]
    app.backLayer.face = [(['orange']*app.cols) for row in range(app.rows)]
    app.backLayer1.face = [[1,2,3],[4,5,6],[7,8,9]]
    app.count=0
    app.moves={}

####################
# Solve & Scramble #
####################
def solver(app):#optimize by trying to find if previous cube states are repeated
    if app.moves == {}:
        print('Your Rubix Cube is Solved')
        print('-------------------------')
    currentState = [app.frontLayer.face,app.topLayer.face,app.leftLayer.face,app.rightLayer.face,app.bottomLayer.face,app.backLayer.face]
    startPoint = seenBefore(app,currentState)
    solverOrder={}
    moveOrder = list(app.moves.keys())[::-1]
    count=0
    for key in range(startPoint,0,-1):
        count+=1
        if app.moves[key][0]=='r':
            if app.moves[key][-1]== app.solved:
                break
            solverOrder[count]=['w',app.moves[key][1], app.moves[key][2]]
            print('-------------------------')
            print(f'{count}: {solverOrder[count]}')
            print('-------------------------')
            
            # print(f'current: {app.moves[key][-1]}')
            # print(f'Solved:  {app.solved}')
            
        if app.moves[key][0]=='l':
            if app.moves[key][-1]== app.solved:
                break
            solverOrder[count]=['j',app.moves[key][1], app.moves[key][2]]
            print('-------------------------')
            print(f'{count}: {solverOrder[count]}')
            print('-------------------------')
            # print(f'current: {app.moves[key][-1]}')
            # print(f'Solved:  {app.solved}')
            
    print('-------------------------')
    print('Your Rubix Cube is Solved')
    print('-------------------------')
    print(startPoint)

def seenBefore(app,state):
    for key in list(app.moves.keys())[::-1]:
        if app.moves[key][-1] == state:
            return key
    return (list(app.moves.keys())[::-1])[0]
        
def scramble(app):#record all scramble moves then reverse the order to make a back tracker
    movesR = random.randrange(30,100)
    movesL = random.randrange(30,100)
    for i in range(movesR):
        row = random.randrange(0,3)
        col = random.randrange(0,3)
        board = random.choice(app.layersRow)
        select = ((row,col),board)
        rotateRow(app, select)
        boardPos = copy.deepcopy([app.frontLayer.face,app.topLayer.face,app.leftLayer.face,app.rightLayer.face,app.bottomLayer.face,app.backLayer.face])
        app.moves[app.count]=['r',(row,col),board, boardPos]
    for j in range(movesL):
        row = random.randrange(0,3)
        col = random.randrange(0,3)
        board = random.choice(app.layersCol)
        select = ((row,col),board)
        rotateCol(app, select)
        boardPos = copy.deepcopy([app.frontLayer.face,app.topLayer.face,app.leftLayer.face,app.rightLayer.face,app.bottomLayer.face,app.backLayer.face])
        app.moves[app.count]=['l',(row,col),board,boardPos]


##########
#  Math  #
##########
def matrixMultiply(m1, m2):
    m1rows, m1cols = len(m1), len(m1[0])
    m2rows, m2cols = len(m2), len(m2[0])
    if m1cols != m2rows:
        return None
    result = [[0]*m2cols for i in range(m1rows)]
    m2mult = []
    for col in range(m2cols):
        m2col = []
        for row in range(m2rows):
            m2col.append(m2[row][col])
        m2mult.append(m2col)
    for row1 in range(m1rows):
        for row2 in range(len(m2mult)):
            result[row1][row2] = dotproduct(m1[row1],m2mult[row2])
    return result
def dotproduct(row, col):
    result=0
    for i in range(len(row)):
        result += row[i]*col[i]
    return result
def getNewRotationMatrixZ(app):
    a=math.cos(math.radians(app.angleZ))
    b=-math.sin(math.radians(app.angleZ))
    c=0
    d=math.sin(math.radians(app.angleZ))
    e=math.cos(math.radians(app.angleZ))
    f=0
    g=0
    h=0
    i=1
    app.rotateZ=[[a,b,c],
                [d,e,f],
                [g,h,i]]
def getNewRotationMatrixX(app):
    a=1
    b=0
    c=0
    d=0
    e=math.cos(math.radians(app.angleX))
    f=-math.sin(math.radians(app.angleX))
    g=0
    h=math.sin(math.radians(app.angleX))
    i=math.cos(math.radians(app.angleX))
    app.rotateX=[[a,b,c],
                [d,e,f],
                [g,h,i]]
def getNewRotationMatrixY(app):
    a=math.cos(math.radians(app.angleY))
    b=0
    c=math.sin(math.radians(app.angleY))
    d=0
    e=1
    f=0
    g=-math.sin(math.radians(app.angleY))
    h=0
    i=math.cos(math.radians(app.angleY))
    app.rotateY=[[a,b,c],
                [d,e,f],
                [g,h,i]]
def rotate(app, points, sf, rotated):
    for point in points:
        rotation = matrixMultiply(app.rotateZ,point)
        rotation = matrixMultiply(app.rotateY,rotation)
        rotation = matrixMultiply(app.rotateX,rotation)
        projection = matrixMultiply(app.transform,rotation)
        if projection[0][0] <0:
            cx = app.width/2+(projection[0][0])*sf
        if projection[1][0] <0:
            cy = app.height/2-(projection[1][0])*sf
        cx = (projection[0][0])*sf+app.width/2
        cy = (projection[1][0])*sf+app.height/2
        rotated.append((cx,cy))
        
##################
#  Drawing Cube  #
##################
def connectLine(i,j,points1, points2):
    if points1==[] or points2 == []:
        return
    cx1=points1[i][0]
    cy1=points1[i][1]
    cx2=points2[j][0]
    cy2=points2[j][1]
    drawLine(cx1,cy1,cx2,cy2, fill='black')  
def makeRubix(pointsLocs1):
    drawFace(4,5,6,7,pointsLocs1,'red')#front
    drawFace(4,0,1,5,pointsLocs1,'white')#top
    drawFace(5,6,2,1,pointsLocs1,'blue')#right

    connectLine(0,1,pointsLocs1,pointsLocs1)
    connectLine(1,2,pointsLocs1,pointsLocs1)
    # face2
    connectLine(4,5,pointsLocs1,pointsLocs1)
    connectLine(5,6,pointsLocs1,pointsLocs1)
    connectLine(6,7,pointsLocs1,pointsLocs1)
    connectLine(7,4,pointsLocs1,pointsLocs1)
    # sides
    connectLine(0,4,pointsLocs1,pointsLocs1)
    connectLine(1,5,pointsLocs1,pointsLocs1)
    connectLine(2,6,pointsLocs1,pointsLocs1)
        # row1
    connectLine(12,13,pointsLocs1,pointsLocs1)
    connectLine(15,12,pointsLocs1,pointsLocs1)
    #row 2
    connectLine(8,9,pointsLocs1,pointsLocs1)
    connectLine(11,8,pointsLocs1,pointsLocs1)
    #row3
    connectLine(18,19,pointsLocs1,pointsLocs1)
    connectLine(19,16,pointsLocs1,pointsLocs1)
    #row4
    connectLine(22,23,pointsLocs1,pointsLocs1)
    connectLine(23,20,pointsLocs1,pointsLocs1)
    #row5
    connectLine(26,27,pointsLocs1,pointsLocs1)
    connectLine(27,24,pointsLocs1,pointsLocs1)
    #row6
    connectLine(30,31,pointsLocs1,pointsLocs1)
    connectLine(31,28,pointsLocs1,pointsLocs1)
def drawFace(i,j,k,l,points,color):
    if points==[]:
        return
    cx1=points[i][0]
    cy1=points[i][1]
    cx2=points[j][0]
    cy2=points[j][1]
    cx3=points[k][0]
    cy3=points[k][1]
    cx4=points[l][0]
    cy4=points[l][1]
    drawPolygon(cx1,cy1,cx2,cy2,cx3,cy3,cx4,cy4, fill=color,opacity=100)#change back to color


################
# Sound Loader #
################

def loadSound(relativePath):#gotten from help page
    # Convert to absolute path (because pathlib.Path only takes absolute paths)
    absolutePath = os.path.abspath(relativePath)
    # Get local file URL
    url = pathlib.Path(absolutePath).as_uri()
    # Load Sound file from local URL
    return Sound(url)