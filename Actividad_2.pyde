import random
sys.setrecursionlimit(999999)
sz=10
timed=50
time=50 
grid = [ [0]*sz for _ in range (sz) ]
w=600/sz
inf = 99
lim = 500
auxmin=0
auxlist=[]
def setup():
    size(820,600)
    grid[sz-1][0]=1
    grid[0][sz-1]=9
    global play,puttingOrigin,puttingDestination, played, showPath, terminar
    global waterImg,ravineImg,mountainImg,wallImg,lucasImg,momboImg,piroloImg,houseImg,backgImg,originImg
    global mombo, pirolo, lucas
    global posm, qm, posp, qp, posl, ql
    qm=[]
    qp=[]
    ql=[]
    #(self,backg,water,ravine,mountain):
    mombo = Avatar(1.0,0.3,1.5,2.5)
    pirolo = Avatar(1.5,2.5,1.0,0.3)
    lucas = Avatar(0.3,1.0,2.5,1.5)
    
    waterImg = loadImage("assets/water.png")
    ravineImg = loadImage("assets/ravine.png")
    mountainImg = loadImage("assets/mountain.png")
    houseImg = loadImage("assets/house.png")
    wallImg = loadImage("assets/wall.png")
    lucasImg = loadImage("assets/lucas.png")
    momboImg = loadImage("assets/mombo.png")
    piroloImg = loadImage("assets/pirolo.png")
    backgImg = loadImage("assets/backg.png")
    originImg = loadImage("assets/origin.png")
    
    puttingOrigin = False
    puttingDestination = False
    play=False
    played=True
    showPath=False
    terminar=False

def draw():
    interface()
    
def endWin():
    global played,play
    played=True
    play = False

def endLose():
    global played,play
    print "SE ACABOOOOO"
    play=False
    played=True

def interface():
    global posm, qm, posp, qp, posl, ql, lim, showPath,play,auxlist,lucasImg,momboImg,piroloImg
    background(255)
    fill(255)
    b1()
    fill(255)
    b2()
    fill(255)
    b3()
    levers()
    fill(255)
    b4()
    update()
    if play==True:
        if len(ql)> posl and posl < lim:
            aux=ql[posl]
            posl+=1
            image(lucasImg,aux[1]*w,aux[0]*w,w,w)
        if len(qm)> posm and posm < lim:
            aux=qm[posm]
            posm+=1
            image(momboImg,aux[1]*w,aux[0]*w,w,w)
        if len(qp)> posp and posp < lim:
            aux=qp[posp]
            posp+=1
            image(piroloImg,aux[1]*w,aux[0]*w,w,w)
        if (len(ql)<= posl or posl >= lim)and(len(qm)<= posm or posm >= lim)and(len(qp)<= posp or posp >= lim):
            endWin()
            print "SE PONE PLAY EN FALSE"
        delay(time)
    if showPath:
        if len(auxlist) > posl:
            aux=auxlist[posl]
            posl+=1
            image(lucasImg,aux[1]*w,aux[0]*w,w,w)
            delay(time)
        else: showPath=False

def levers():
    stroke(0)
    fill(0)
    bar()
    fill(255,0,0)
    lever()
    pLever()
    stroke(0)
    fill(0)
    bar1()
    fill(255,0,0)
    lever1()
    pLever1()
    stroke(0)
    fill(0)
    bar2()
    fill(255,0,0)
    lever2()
    pLever2()
    stroke(0)
    fill(0)
    bar3()
    fill(255,0,0)
    lever3()
    pLever3()

def update():
    global grid
    x,y=0,0;
    for row in grid:
        for col in row:
            image(backgImg,x,y,w,w)
            img = selectImg(col)
            image(img,x,y,w,w)
            x=x+w
        y=y+w
        x=0
    #image(houseImg,desy*w,desx*w,w,w)
    #image(originImg,oriy*w,orix*w,w,w)

def b1():
    stroke(0)
    rect(b1x,b1y,b1w,b1h)
    textSize(20);
    fill(0)
    text("Entrenar!", b1x+7, b1y+20-2);

def b2():
    rect(b2x,b2y,b2w,b2h)
    image(originImg,b2x,b2y,b2w,b2h)
    
def b3():
    rect(b3x,b3y,b3w,b3h)
    image(houseImg,b3x,b3y,b3w,b3h)
    
def bar():
    rect(barx,bary,barw,barh)
    rect(barx-levw,bary,levw,barh)
def lever():
    global overLever
    if mouseX > levx and mouseY > levy and  mouseX < levx+levw and mouseY < levy+levh:
        overLever = True
        if not locked:
            stroke(120)
            fill(255,0,0)
    else:
        stroke(255)
        fill(255,0,0)
        overLever = False
    rect(levx,levy,levw,levh)
def pLever():
    text(str(round(percent,1)) + "%", perx-8, pery);

def bar1():
    rect(bar1x,bar1y,bar1w,bar1h)
    rect(bar1x-lev1w,bar1y,lev1w,bar1h)
def lever1():
    global overLever1
    if mouseX > lev1x and mouseY > lev1y and  mouseX < lev1x+lev1w and mouseY < lev1y+lev1h:
        overLever1 = True
        if not locked1:
            stroke(120)
            fill(255,0,0)
    else:
        stroke(255)
        fill(255,0,0)
        overLever1 = False
    rect(lev1x,lev1y,lev1w,lev1h)
def pLever1():
    text(str(round(percent1,1)) + "%", per1x-8, per1y);

def bar2():
    rect(bar2x,bar2y,bar2w,bar2h)
    rect(bar2x-lev2w,bar2y,lev2w,bar2h)
def lever2():
    global overLever2
    if mouseX > lev2x and mouseY > lev2y and  mouseX < lev2x+lev2w and mouseY < lev2y+lev2h:
        overLever2 = True
        if not locked2:
            stroke(120)
            fill(255,0,0)
    else:
        stroke(255)
        fill(255,0,0)
        overLever2 = False
    rect(lev2x,lev2y,lev2w,lev2h)
def pLever2():
    text(str(round(percent2,1)) + "%", per2x-8, per2y);
    
def bar3():
    rect(bar3x,bar3y,bar3w,bar3h)
    rect(bar3x-lev3w,bar3y,lev3w,bar3h)
def lever3():
    global overLever3
    if mouseX > lev3x and mouseY > lev3y and  mouseX < lev3x+lev3w and mouseY < lev3y+lev3h:
        overLever3 = True
        if not locked3:
            stroke(120)
            fill(255,0,0)
    else:
        stroke(255)
        fill(255,0,0)
        overLever3 = False
    rect(lev3x,lev3y,lev3w,lev3h)
def pLever3():
    text(str(round(percent3,1)) + "%", per3x-8, per3y);

def b4():
    global play,orix,oriy,desx,desy,played
    fill(255)
    noStroke()
    rect(b4x,b4y,b4w,b4h)
    textSize(20);
    fill(0)
    if not play and played:
        text("LISTO", b4x+7, b4y+20-2);
        #if orix==desx and oriy==desy:
        #    text("ENCONTRADO", b4x+7, b4y+20-2);
        #else:
        #    text("NO ENCONTRADO", b4x+7, b4y+20-2);

def training():
    global posm, qm, posp, qp, posl, ql,played,time
    inix=0
    iniy=0
    endx=0
    endy=0
    for i in range(sz):
        for j in range(sz):
            if grid[i][j]==1:
                inix=i
                iniy=j
            if grid[i][j]==9:
                endx=i
                endy=j

    lucas.restart()
    ql=[]
    for i in range(100):
        lucas.active=True
        ql+=lucas.train(inix,iniy,0,i)
        lucas.vis=[ [False]*sz for _ in range (sz) ]
    print "LUCAS"
    print ' '
    for i in lucas.pon:
        print i
    posl=0
    
    mombo.restart()
    qm=[]
    for i in range(100):
        mombo.active=True
        qm+=mombo.train(inix,iniy,0,i)
        mombo.vis=[ [False]*sz for _ in range (sz) ]
    print "MOMBO"
    print ' '
    for i in mombo.pon:
        print i
    posm=0
    
    pirolo.restart()
    qp=[]
    for i in range(100):
        pirolo.active=True
        qp+=pirolo.train(inix,iniy,0,i)
        pirolo.vis=[ [False]*sz for _ in range (sz) ]
    print "PIROLO"
    print ' '
    for i in pirolo.pon:
        print i
    posp=0
    played=True
    time=0
    
def clearGridOrigin():
    global grid
    for i in range(sz):
        for j in range(sz):
            if grid[i][j]==1:
                grid[i][j]=0
                return

def clearGridDestination():
    global grid
    for i in range(sz):
        for j in range(sz):
            if grid[i][j]==9:
                grid[i][j]=0
                return

def clearGrid(type):
    global grid
    v = [[(j,i) for i in range(0,sz)] for j in range(0,sz)]
    for i in range(sz):
        for j in range(sz):
            if grid[i][j]==type:
                grid[i][j]=0
            elif grid[i][j]!=0:
                v[i].remove((i,j))
    return v;

def putObstacles(type,p):
    global grid,total
    #v = [[(j,i) for i in range(0,sz)] for j in range(0,sz)]
    v = clearGrid(type)
    cont = 0
    for i in range(sz):
        for j in range(sz):
            if grid[i][j]==0:
                cont+=1
    objectsP=int(cont*p)/100
    #if objectsP>total-2: objectsP = total-2
    raux=int(objectsP*(sz*sz))/100
    #print ("Objects: ",objectsP)
    #print v
    while objectsP>0:
        aux=random.choice(v)
        while len(aux)==0:
            aux=random.choice(v)
        pos=random.choice(aux)
        grid[pos[0]][pos[1]]=type
        objectsP-=1
        aux.remove(pos)
    return raux


def mousePressed():
    global puttingDestination, puttingOrigin,overLever,locked, xOffset,play,grid,auxmin,auxlist,terminar,posl,showPath,played,visitados,qm,qp,ql,posm,posp,time,timed
    global overLever1,locked1,xOffset1
    global overLever2,locked2,xOffset2
    global overLever3,locked3,xOffset3
    if mouseX > b1x and mouseY > b1y and  mouseX < b1x+b1w and mouseY < b1y+b1h:
        #played=False
        play=True
        training()
        fill(0)
        b1()
    if mouseX > b2x and mouseY > b2y and  mouseX < b2x+b2w and mouseY < b2y+b2h:
        #played=False
        fill(0)
        b2()
        clearGridOrigin()
        puttingOrigin=True
    if mouseX > b3x and mouseY > b3y and  mouseX < b3x+b3w and mouseY < b3y+b3h:
        #played=False
        fill(0)
        b3()
        clearGridDestination()
        puttingDestination=True
    
    if overLever:
        locked = True
        fill(255,0,0)
    else:
        locked = False
    xOffset = mouseX - levx
    
    if overLever1:
        locked1 = True
        fill(255,0,0)
    else:
        locked1 = False
    xOffset1 = mouseX - lev1x
    
    if overLever2:
        locked2 = True
        fill(255,0,0)
    else:
        locked2 = False
    xOffset2 = mouseX - lev2x
    
    if overLever3:
        locked3 = True
        fill(255,0,0)
    else:
        locked3 = False
    xOffset3 = mouseX - lev3x
        
    if (mouseX/w)<sz and (mouseY/w)<sz :
        inix=mouseY/w
        iniy=mouseX/w
        print (inix,iniy)
        if played:
            print "POS aqui estoy krnal"
            terminar=False
            auxmin=inf*100
            visitados = [ [False]*sz for _ in range (sz) ]
            recur(inix,iniy,0,lucas,[])
            ql=[(inix,iniy)]+auxlist
            
            terminar=False
            auxmin=inf*100
            visitados = [ [False]*sz for _ in range (sz) ]
            recur(inix,iniy,0,pirolo,[])
            qp=[(inix,iniy)]+auxlist
            
            terminar=False
            auxmin=inf*100
            visitados = [ [False]*sz for _ in range (sz) ]
            recur(inix,iniy,0,mombo,[])
            qm=[(inix,iniy)]+auxlist
            
            time=timed
            print ql
            print qp
            print qm
            posl=0
            posm=0
            posp=0
            play=True
            
        if puttingOrigin:
            grid[mouseY/w][mouseX/w]=1
            print "AVATAR: "+str(mouseY/w) + ' ' + str(mouseX/w)
            puttingOrigin=False
        elif puttingDestination:
            grid[mouseY/w][mouseX/w] = 9
            print "TREASURE: "+str(mouseY/w) + ' ' + str(mouseX/w)
            puttingDestination=False
            
            
            
            
def recur(inix,iniy,sum,ava,lista):
    print sz
    print (inix,iniy)
    global auxmin, auxlist,terminar,visitados
    if terminar: return
    bx=0
    by=0
    minl=inf
    visitados[inix][iniy]=True
    if(grid[inix][iniy]==9):
        # if sum<auxmin:
        auxmin=sum
        auxlist=lista
        terminar=True
        return

    for i in range(-1,2):
        for j in range(-1,2):
            if not(i==0 and j==0) and inix+i>=0 and inix+i<sz and iniy+j>=0 and iniy+j<sz and grid[inix+i][iniy+j]!=2 and visitados[inix+i][iniy+j]==False:
                if grid[inix+i][iniy+j]==9:
                    recur(inix+i,iniy+j, sum+ava.pon[inix][iniy] ,ava,lista+[(inix+i,iniy+j)])
                    return
                elif minl>ava.pon[inix+i][iniy+j]:
                    minl=ava.pon[inix+i][iniy+j]
                    bx=inix+i
                    by=iniy+j
    print(bx,by)
    if not(bx==0 and by==0) and not(bx==inix and by==iniy):recur(bx,by, sum+ava.pon[inix][iniy] ,ava,lista+[(bx,by)])
    else: return

            

def ruta(inix,iniy):
    dp = [ [inf]*sz for _ in range (sz) ]
    ant = [ [(-1,-1)]*sz for _ in range (sz) ]
    
    cola = []
    cola.append((inix,iniy))
    
    
    
    
    

def mouseDragged():
    global levx,percent,played
    global lev1x,percent1
    global lev2x,percent2
    global lev3x,percent3
    if locked:
        #played=False
        levx = mouseX - xOffset
        if levx +levw < barx:
            levx = barx -levw
        if levx + levw > barx + barw:
            levx = barx + barw -levw
        percent = (float( barw-(barx+barw-(levx+levw)) )*100.0) / float(barw)
        #print percent
        percent=putObstacles(2,percent)
    elif locked1:
        #played=False
        lev1x = mouseX - xOffset1
        if lev1x +lev1w < bar1x:
            lev1x = bar1x -lev1w
        if lev1x + lev1w > bar1x + bar1w:
            lev1x = bar1x + bar1w -lev1w
        percent1 = (float( bar1w-(bar1x+bar1w-(lev1x+lev1w)) )*100.0) / float(bar1w)
        #print percent1
        percent1=putObstacles(3,percent1)
    elif locked2:
        #played=False
        lev2x = mouseX - xOffset2
        if lev2x +lev2w < bar2x:
            lev2x = bar2x -lev2w
        if lev2x + lev2w > bar2x + bar2w:
            lev2x = bar2x + bar2w -lev2w
        percent2 = (float( bar2w-(bar2x+bar2w-(lev2x+lev2w)) )*100.0) / float(bar2w)
        #print percent2
        percent2=putObstacles(4,percent2)
    elif locked3:
        #played=False
        lev3x = mouseX - xOffset3
        if lev3x +lev3w < bar3x:
            lev3x = bar3x -lev3w
        if lev3x + lev3w > bar3x + bar3w:
            lev3x = bar3x + bar3w -lev3w
        percent3 = (float( bar3w-(bar3x+bar3w-(lev3x+lev3w)) )*100.0) / float(bar3w)
        #print percent3
        percent3=putObstacles(5,percent3)

def mouseReleased():
    locked = False
    locked1 = False
    locked2 = False
    locked3 = False

def selectImg(x):
    return {
        0: backgImg,
        1: originImg,
        2: wallImg,
        3: waterImg,
        4: ravineImg,
        5: mountainImg,
        6: lucasImg,
        7: momboImg,
        8: piroloImg,
        9: houseImg
    }.get(x, backgImg)
    


class Avatar:
    def __init__(self,backg,water,ravine,mountain):
        self.pon = [ [0]*sz for _ in range (sz) ]
        self.M = -inf
        self.m = inf
        self.vis = [ [False]*sz for _ in range (sz) ]
        self.dbackg = backg
        self.dwater = water
        self.dravine = ravine
        self.dmountain = mountain
        self.active = False
        self.adjust = 0
    
    def train(self,inix,iniy,eff,ind):
        aux=[]
        q=[]
        self.vis[inix][iniy]=True
        if grid[inix][iniy]==9:
            self.active=False
            self.adjust=eff - ((float(self.M+self.m))/2.0)
            if eff > self.M: self.M = eff
            if eff < self.m: self.m = eff
            if ind==0: self.adjust=0
        if not self.active: return [(inix,iniy)]
        else: q.append((inix,iniy))
        for i in range(-1,2):
            for j in range(-1,2):
                if not(i==0 and j==0) and inix+i>=0 and inix+i<sz and iniy+j<sz and iniy+j>=0 and grid[inix+i][iniy+j]!=2 and not self.vis[inix+i][iniy+j]:
                    aux.append((i,j))
        while len(aux)!=0 and self.active:
            op = random.choice(aux)
            aux.remove(op)
            i = op[0]
            j = op[1]
            if self.vis[inix+i][iniy+j]: continue
            if grid[i][j]!=9: q += self.train(inix+i,iniy+j, eff + self.effort( grid[inix+i][iniy+j] ),ind )
            if self.active: q.append((inix,iniy))
            else: self.pon[inix][iniy]=round(self.adjust,2)
        #q.append((inix,iniy))    
        return q
    
    def restart(self):
        self.M = -inf
        self.m = inf
        self.pon = [ [0]*sz for _ in range (sz) ]
        self.vis = [ [False]*sz for _ in range (sz) ]
        
    def effort(self,val):
        return{
           0: self.dbackg,
           3: self.dwater,
           4: self.dravine,
           5: self.dmountain
        }.get(val, 0)

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    

#0: backgImg,
#1: originImg,
#2: wallImg,
#3: waterImg,
#4: ravineImg,
#5: mountainImg,
#6: lucasImg,
#7: momboImg,
#8: piroloImg,
#9: houseImg

# Button one
b1x=650
b1y=55
b1w=100
b1h=20

# Button two
b2x=620
b2y=100
b2w=70
b2h=70

# Button three
b3x=700
b3y=100
b3w=70
b3h=70

# Bar 
barx=630
bary=225
barw=180
barh=20

# Lever
levx=barx - barh 
levy= bary - 5
levw=20
levh=barh +10
overLever = False
locked = False
xOffset = 0.0 

# Percent Lever
perx=barx + barw/2 -10
pery=bary-5
percent=0.0

# B1
bar1x=630
bar1y=275
bar1w=180
bar1h=20

# L1
lev1x=bar1x - bar1h 
lev1y= bar1y - 5
lev1w=20
lev1h=bar1h +10
overLever1 = False
locked1 = False
xOffset1 = 0.0 

# PL1
per1x=bar1x + bar1w/2 -10
per1y=bar1y-5
percent1=0.0

# B2
bar2x=630
bar2y=325
bar2w=180
bar2h=20

# L2
lev2x=bar2x - bar2h 
lev2y= bar2y - 5
lev2w=20
lev2h=bar2h +10
overLever2 = False
locked2 = False
xOffset2 = 0.0 

# PL2
per2x=bar2x + bar2w/2 -10
per2y=bar2y-5
percent2=0.0

# B3
bar3x=630
bar3y=375
bar3w=180
bar3h=20

# L3
lev3x=bar3x - bar3h 
lev3y= bar3y - 5
lev3w=20
lev3h=bar3h +10
overLever3 = False
locked3 = False
xOffset3 = 0.0 

# PL3
per3x=bar3x + bar3w/2 -10
per3y=bar3y-5
percent3=0.0

# Button obstacles
b4x=610
b4y=555
b4w=200
b4h=20
    
