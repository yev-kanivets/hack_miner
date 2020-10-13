import random

gamefield = []
visGF = []

H = 10#int(input("Введите высоту поля:"))
W = 10#int(input("Введите ширину поля:"))

N = 5#int(input(f"Введите количество мин(Не больше %s):" % (str(H*W))))

BombC = []

for i in range(H):
	gamefield.append([])
	visGF.append([])
	for k in range(W):
		gamefield[i].append(0)
		visGF[i].append(" ")



def GameIni():
	TempC = []								# Временная рандомная координата для мины

	for i in range(N):
		TempC = [random.randint(0, W-1), random.randint(0, H-1)]
		if gamefield[TempC[0]][TempC[1]] != 1:
			gamefield[TempC[0]][TempC[1]] = "B"
			BombC.append([TempC[0], TempC[1]])
		else:
			i -= 1

	for bomb in BombC:
		if bomb[0]-1 >=0 and bomb[1]-1 >=0 and gamefield[bomb[0]-1][bomb[1]-1] != "B":
			gamefield[bomb[0]-1][bomb[1]-1] += 1
		
		if bomb[1]-1 >=0 and gamefield[bomb[0]][bomb[1]-1] != "B":
			gamefield[bomb[0]][bomb[1]-1] += 1
		
		if bomb[0]+1 <=H-1 and bomb[1]-1 >= 0 and gamefield[bomb[0]+1][bomb[1]-1] != "B":
			gamefield[bomb[0]+1][bomb[1]-1] += 1
		
		if bomb[0]+1 <= W-1 and gamefield[bomb[0]+1][bomb[1]] != "B":
			gamefield[bomb[0]+1][bomb[1]] += 1
		
		if bomb[0]+1 <=W-1 and bomb[1]+1 <=H-1 and gamefield[bomb[0]+1][bomb[1]+1] != "B":
			gamefield[bomb[0]+1][bomb[1]+1] += 1
		
		if bomb[1]+1 <=H-1 and gamefield[bomb[0]][bomb[1]+1] != "B":
			gamefield[bomb[0]][bomb[1]+1] += 1
		
		if bomb[0]-1 >=0 and bomb[1]+1 <=H-1 and gamefield[bomb[0]-1][bomb[1]+1] != "B":
			gamefield[bomb[0]-1][bomb[1]+1] += 1
		
		if bomb[0]-1 >=0 and gamefield[bomb[0]-1][bomb[1]] != "B":
			gamefield[bomb[0]-1][bomb[1]] += 1

	for i in range(H):
		for k in range(W):
			if gamefield[i][k] == 0:
				gamefield[i][k] = " "
			else:
				gamefield[i][k] = str(gamefield[i][k])



			

"""def PrintField():
	for i in range(H):
		print(" ")
		for k in range(W):
			print(str(visGF[i][k]) + " ", end=" ")"""

def HandleClick(x, y):
	if gamefield[x][y] == "B":
		return "GO"
		print("Game Over!!!")
		break
	elif gamefield[x][y] == " ":
		return "OS"
	else:
		return "OC"



def Main():
	GameIni()
	
	HCret = " "

	#while True:
	#	PrintField()
	#	CheckC = input("Введите координату проверки: ").split()
	#	CheckC = [int(CheckC[0]), int(CheckC[1])]

	#	HCret = HandleClick(CheckC[0], CheckC[1])

	#	if HCret == "GO":
	#		print("Game Over!!!")
	#		break
	#	elif HCret == "OC":
	#		visGF[CheckC[0]][CheckC[1]] = gamefield[CheckC[0]][CheckC[1]]
	#	else:
	#		print("Open Space")


Main()

import pygame
pygame.init()

SIDE = 50
SCREEN_H = H * SIDE;
SCREEN_W = W * SIDE;

screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
bombImg = pygame.image.load(r'./bomb.png') 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
        	pos = pygame.mouse.get_pos()
        	x = int(pos[0] / SIDE) + 1
        	y = int(pos[1] / SIDE) + 1
        	HandleClick(x, y)

    screen.fill((255, 255, 255))

    for i in range(H):
    	for j in range(W):
    		if gamefield[i][j] == "B":
    			screen.blit(bombImg, (i * SIDE, j * SIDE))
    		else:
    			pygame.draw.rect(screen, (0, 0, 255), (i * SIDE, j * SIDE, (i + 1) * SIDE, (j + 1) * SIDE))

    		

    pygame.display.flip()

pygame.quit()