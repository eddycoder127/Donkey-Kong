import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 10
fpsClock = pygame.time.Clock()
g=0

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255,0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
BLACK = (0,0,0)
random = 0
sanket = 0
score = 0

DISPLAYSURF = pygame.display.set_mode((1500, 1500),0,32)
DISPLAYSURF.fill(WHITE)
don = pygame.image.load('donkey.png')
don = pygame.transform.scale(don,(80,80))
mario = pygame.image.load('mario.png')
f = pygame.image.load('coin.png')
f = pygame.transform.scale(f,(30,30))
mario = pygame.transform.scale(mario,(60,60))
lad1 = pygame.image.load('ladd.png')
lad1 = pygame.transform.scale(lad1,(100,110))
sc = pygame.image.load('scene.jpg')
sc = pygame.transform.scale(sc,(1080,700))
gm1 = pygame.image.load('youwin.png')
gm = pygame.image.load('gameover.png')
fireball = pygame.image.load('ball.png')
fireball = pygame.transform.scale(fireball,(30,30))
fireball = pygame.transform.rotate(fireball,91)
prince = pygame.image.load('princ.png')
prince = pygame.transform.scale(prince,(60,70))

ladderup = [[700,750,0,130],[300,350,120,250],[900,960,240,365],[640,700,355,485],[400,453,475,610]]	

def checkup(xa,ya):
	i=0
	for i in range(len(ladderup)):
		if (ladderup[i][0] < xa and ladderup[i][1] > xa) and (ya > ladderup[i][2] and ya < ladderup[i][3]):
			return 1
	return 0
def checkl(xa,ya):
	i=0;
	for i in range(len(ladderup)):
		if (xa < ladderup[i][0]-15 or xa > ladderup[i][1]+15) and (ya > ladderup[i][2]+10 and ya < ladderup[i][3]-10):
			return i
	return -1

end = [[1450,600],[1220,480],[60,360],[1220,240],[70,120],[1220,0]]
coin = [[160,620,1],[1200,620,1],[700,620,1],[400,500,1],[800,500,1],[1000,380,1],[400,380,1],[190,380,1],[800,260,1],[120,260,1]]
i = 0
j = 180
dist = 80
#for i in range(4):

i=0
fire = []
for i in range(50):
	fire.append([0,30,0,1])
	fire.append([150,150,0,1])
def modi(xa,xb):
	if xa>xb:
		return xa-xb
	else:
		return xb-xa
def checklr(xa,xb):
	i = 0
	for i in range(len(end)):
		if modi(xa,end[i][0])<30 and (modi(xb,end[i][1]))<30:
			return i;
	return -1;
def checkrl(xa):
	i = 0
	for i in range(len(end)):
		if modi(end[i][1],xa)<=8:
			return 1
	return -1

forfire = [[758,60],[340,180],[955,305],[685,435],[400,555]]
def checkf(xa,xb):
	i = 0
	for i in range(len(forfire)):
		if modi(xa,forfire[i][0])<2 and modi(xb,forfire[i][1])<60:
			if random%2==1:
				return 1
			else:
				return -1
	return -1

cnt = 0
dx = 110
dy = 100
mx = 0
my = 600
flag = 1
ch = 0
ar = [[1,1220],[110,1370],[1,1220],[110,1370],[1,1220],[1,1370]]
jumpar = [-60,60,180,300,420,540,660]
jump = 0
dirj = 0
e = 1
allg = 1
life = 3

while True:
	if allg==1:
		keys=pygame.key.get_pressed()
		if keys[K_SPACE]:
			jump = 1
			dirj = 1
		if keys[K_LEFT]:
			e = 0
		elif keys[K_RIGHT]:
			e = 1
		DISPLAYSURF.fill((GREEN))
		i=0
		j=60
		fire[g][2] = 1;
		cnt+=1
		random+=1
		if cnt%200==0:
			g += 1
		h = g
		i = 0
		for i in range(g+1):
			j = 0
			for j in range(len(end)):
				if modi(end[j][0],fire[i][0])<20 and modi(end[j][1],fire[i][1])<60:
					fire[i][1] += 120
					if random%5==1:
						fire[i][3] = (fire[i][3]+1)%2
			if fire[i][2]==1:
			 	j = 0
			 	for j in range(h):
					if (modi(mx,fire[j][0])<2) and (modi(my,fire[j][1])<40):
						life-=1
						mx = 0
						my = 600
				if fire[i][1] > 700:
					fire[i][2] = 0
				DISPLAYSURF.blit(fireball,(fire[i][0],fire[i][1]))
				if checkf(fire[i][0],fire[i][1])==1:
					fire[i][1] += 120
					if random%3==1:
						fire[i][3] = (fire[i][3]+1)%2
				if fire[i][3] == 1:
					if fire[i][0] < 1300:
						fire[i][0]+=2
					else:
						fire[i][0]-=2
						fire[i][3] = 0
				else:
					if fire[i][0] > 2:
						fire[i][0]-=2
					else:
						fire[i][0] += 2
						fire[i][3] = 1
			j=60
			for i in range(len(ar)):
				pygame.draw.line(DISPLAYSURF,BLACK,(ar[i][0],j),(ar[i][1],j),8)
				j += 120
		i = 0
		for i in range(len(coin)):
			if modi(coin[i][0],mx)<15 and modi(coin[i][1],my)<60 and coin[i][2]==1:
				score += 50
			if modi(coin[i][0],mx)<15 and modi(coin[i][1],my)<60:
				coin[i][2] = 0
			if coin[i][2]==1:
				DISPLAYSURF.blit(f,(coin[i][0],coin[i][1]))
		if jump==0:
			if ch==0:
				if checklr(mx,my) != -1:
					ch = 1
					my = my+2
			else:
				my+=2
				if checkrl(my) != -1:
					ch = 0
			if keys[K_LEFT] and mx>=4:
			 	if checkl(mx,my)==-1:
					mx = mx-4
				else:
				 	mx = mx-4
				 	my = ladderup[checkl(mx,my)][3]-4
			elif keys[K_RIGHT] and mx<=1300:
				if checkl(mx,my)==-1:
					mx = mx+4
				else:
				 	mx = mx+4
				 	my = ladderup[checkl(mx,my)][3]-4
			elif keys[K_UP] and checkup(mx,my)==1:
				my = my-2
			elif keys[K_DOWN] and checkup(mx,my+4)==1:
				my = my+2
		else:
			if dirj==1:
				my-=2
				for i in range(len(jumpar)):
					if modi(my,jumpar[i])<10:
						dirj = 0
			else:
				my+=2
				i=0
				for i in range(len(jumpar)):
					if modi(my,jumpar[i]-60)<10:
						jump = 0
						my = jumpar[i]-60
			if e==1:
				mx+=2
			else:
				mx-=2
		if flag==1:
			if dx<=1250:
				dx = dx+1
			else:
				dx = dx-1
				flag = 0
		else:
			if dx>=110:
				dx = dx-1
			else:
				dx = dx+1
				flag = 1
		i = 0
		o = [[705,65],[305,185],[905,305],[645,425],[405,545]]
		for i in range(len(o)):
			DISPLAYSURF.blit(lad1,(o[i][0],o[i][1]))
 		DISPLAYSURF.blit(don,(dx,dy))
		DISPLAYSURF.blit(mario,(mx,my))
		DISPLAYSURF.blit(prince,(1220,0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		if (mx>1200 and my<40):
			allg = 2
		if life<1:
			allg = 0
		myfont = pygame.font.SysFont("monospace", 35)
		label = myfont.render("Score = "+str(score), 1, (255,0,0))
		DISPLAYSURF.blit(label, (10, 10))
		myfont = pygame.font.SysFont("monospace", 35)
		label = myfont.render("Lives = "+str(life), 1, (255,0,0))
		DISPLAYSURF.blit(label, (10, 35))
		pygame.display.update()
	elif allg==0:
	 	sanket+=1 
	  	if sanket%400==0:
	  		mx = 0
	  		my = 600
	  		allg = 1
	  		life = 3
			score = 0
			g=0
		DISPLAYSURF.blit(gm,(500,300))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()
	else:
		sanket+=1
	  	if sanket%400==0:
	  		mx = 0
	  		my = 600
			allg = 1
			life = 3
			score = 0
			g=0
		DISPLAYSURF.blit(gm1,(200,300))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		pygame.display.update()

