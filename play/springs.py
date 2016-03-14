'''
Created on Jan 29, 2015

@author: oovadia
'''

from math import pi
import math
import random
import pygame
import PyParticles4

(width, height) = (1000, 1000)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Springs')

universe = PyParticles4.Environment((width, height))
universe.colour = (255,255,255)
universe.addFunctions(['move',  'accelerate','combine','attrac'])#'drag',
universe.acceleration = (pi,0)
universe.mass_of_air = 0.02
num_of_particles = 7
particle_height = height/2
prevRow=None
a= width/(num_of_particles+4)
cornerX,cornerY = (width/num_of_particles, height/num_of_particles)
for row in range(num_of_particles):
    row_height = height/(num_of_particles+1)*(row+1)
    for col in range(num_of_particles):
        p=row*num_of_particles+col
        speed = random.random()*0
        x = cornerX+a*col#width/(num_of_particles+1)*(p+1)#random.randint(size, width-size)
        y = cornerY+a*row#row_height#random.randint(size, height-size)
        mass = 5
        if (col==0) or (col==(num_of_particles-1)) or (row==0) or (row==(num_of_particles-1)):
            mass=100000000
            speed = 0
        universe.addParticles(x=x,y=y,mass=mass, size=9, speed=speed, elasticity=1, colour=(20,40,200))
        if col>0:
            #universe.addSpring(p-1,p, length=10, strength=0.7)
            pass
        if row>0:
            #universe.addSpring(p,(row-1)*num_of_particles+col, length=10, strength=0.5)
            pass
    prevRow = row
selected_particle = None
paused = False
running = True
cl = pygame.time.Clock()

while running:
    cl.tick(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected_particle = universe.findParticle(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        selected_particle.mouseMove(pygame.mouse.get_pos())
    if not paused:
        universe.update()
        
    screen.fill(universe.colour)
    
    for p in universe.particles:
        pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, 0)
        
    for s in universe.springs:
        pygame.draw.aaline(screen, (0,0,0), (int(s.p1.x), int(s.p1.y)), (int(s.p2.x), int(s.p2.y)))

    pygame.display.flip()