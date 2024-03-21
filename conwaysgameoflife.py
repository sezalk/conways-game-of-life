import pygame
import random

pygame.init()

BLACK =(0,0,0)
GREY=(128, 128, 128)
YELLOW=(255,255,0)

WIDTH, HEIGHT =800, 800
TILESIZE=20

GRIDWIDTH=WIDTH//TILESIZE
GRIDHEIGHT=HEIGHT//TILESIZE
FPS=60

screen=pygame.display.set_mode((WIDTH, HEIGHT))

clock=pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0,GRIDHEIGHT), random.randrange(0, GRIDWIDTH)) for _ in range(num)])

def draw_grid(positions):
    for position in positions:#translate col and row to pixel position
        col, row=position
        top_left=(col*TILESIZE, row*TILESIZE)
        pygame.draw.rect(screen, YELLOW, (*top_left, TILESIZE, TILESIZE))

    for row in range(GRIDHEIGHT):
        pygame.draw.line(screen, BLACK, (0, row*TILESIZE),(WIDTH, row*TILESIZE))
    for col in range(GRIDWIDTH):
        pygame.draw.line(screen, BLACK, (col*TILESIZE,0),(col*TILESIZE, HEIGHT))

def adjust_grid(positions):
    all_neighbours=set()
    new_positions=set()

    for position in positions:
        neighbours=get_neighbours(position)
        all_neighbours.update(neighbours)

        neighbours=list(filter(lambda x: x in positions, neighbours))
        if len(neighbours) in [2,3]:
            new_positions.add(position)

    for position in all_neighbours:
        neighbours=get_neighbours(position)
        neighbours=list(filter(lambda x: x in position, neighbours))
        if len(neighbours)==3:
            new_positions.add(position)

    return new_positions

def get_neighbours(pos):
    x,y=pos
    neighbours=[]
    for dx in [-1, 0, 1]:
        if x+dx<0 or x+dx>GRIDWIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y+dy<0 or y+dy>GRIDHEIGHT:
                continue
            if dx==0 and dy==0:
                continue

            neighbours.append((x+dy, y+dy))
    return neighbours

def main():
    running=True
    playing=False
    update_freq=120
    count=0

    positions=set()
    
    while running:
        clock.tick(FPS) #loop runs at max fps times per second

        if playing:
            count+=1

        if count>=update_freq:
            count=0
            positions=adjust_grid(positions)
        
        pygame.display.set_caption("PLAYING" if playing else "PAUSED")

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                col=x//TILESIZE
                row=y//TILESIZE
                pos=(col,row)

                if pos in positions:
                    positions.remove(pos)

                else:
                    positions.add(pos)

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    playing=not playing
                
                if event.key==pygame.K_c:
                    positions=set()
                    playing=False
                    count=0
                
                if event.key==pygame.K_g:
                    positions=gen(random.randrange(4,10)*GRIDWIDTH)

        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()
    
    pygame.quit()
#only want to run the code when we directly access this file and not when this file is imported by another file

if __name__=="__main__":  
    main()






