'''
Created on Jan 29, 2015

@author: oovadia
'''
import random
import pygame,math
import PyParticles4 as  PyParticles

(width, height) = (600, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Star formation')
(midX,midY) = (width/2, height/2)
universe = PyParticles.Environment((width, height))
universe.colour = (0,0,0)
universe.addFunctions(['move', 'attract', 'combine'])

def calculateRadius(mass):
    return 0.5 * mass ** (0.5)

for p in range(100):
    
    
    (x,y) = (random.randint(1,width),random.randint(1,height)) 
    (dx,dy) = (x-midX,y-midY)
    speed = math.hypot(dx, dy)/100
    particle_mass = random.random()/math.hypot(dx, dy)*100
    print particle_mass, math.hypot(dx, dy)
    particle_size = calculateRadius(particle_mass)
    angle = math.atan2(dy, dx) + (0.5+0.6) * math.pi 
    universe.addParticles(mass=particle_mass,x=x,y=y,angle=angle, size=particle_size, speed=speed, colour=(255,255,255))
    
particle_mass = 1000
particle_size = calculateRadius(particle_mass)
universe.addParticles(mass=particle_mass, size=particle_size, speed=0, colour=(255,255,255),x=midX,y=midY)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(universe.colour)
    universe.update()
    
    particles_to_remove = []
    for p in universe.particles:
        if 'collide_with' in p.__dict__:
            particles_to_remove.append(p.collide_with)
            p.size = calculateRadius(p.mass)
            del p.__dict__['collide_with']

        if p.size < 2:
            pygame.draw.rect(screen, p.colour, (int(p.x), int(p.y), 2, 2))
        else:
            pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), int(p.size), 0)
    
    for p in particles_to_remove:
        if p in universe.particles:
            universe.particles.remove(p)

    pygame.display.flip()