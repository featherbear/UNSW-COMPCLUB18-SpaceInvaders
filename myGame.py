multiFire = True  # Can multiple missiles be deployed at once
holdFire  = True  # Can the space bar be held down to continually fire
sprayFire = False # Does the missiles deviate

score = 0




fireReady = True

# Import the libraries
import pygame

# Initialise PyGame
pygame.display.init()

# Setting up the window              
win_w = 800
win_h = 600

# Create a screen
screen = pygame.display.set_mode((win_w, win_h))
clock = pygame.time.Clock()

# Global Variables
temp = 0

sprites = []
missile = []    
invader_flip = False

# Assigning images to characters
image_player = pygame.image.load("player.png").convert()
image_invader = pygame.image.load("invader.png").convert()
image_missile = pygame.image.load("missile.png").convert()

# Enabling transparency on the images
image_player.set_colorkey((255,255,255))
image_invader.set_colorkey((255,255,255))
image_missile.set_colorkey((255,255,255))

# For keyboard input
pygame.key.set_repeat(1,1)

class Sprite:
    active = None   # whether the sprite is active or off
    xp = None       # x coordinate
    yp = None       # y coordinate
    xv = None       # velocity
    image = None    # image for sprite
    type = None     # type of sprite
    fn_move = None  # to move (later)

    # Initialising sprite
    def __init__(self):
        self.active = False

    # For movement
    def move(self):
        if(self.fn_move is not None):
            self.fn_move(self)
            return

    # Drawing the sprite
    def draw(self):
            screen.blit(self.image,(self.xp, self.yp))

# List of Sprites
max_sprites = 200
sprites = [Sprite() for i in range(max_sprites)]


# Function for movement
def move_player(self):
    global fireReady
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and self.xp-4>0:
    	self.xp-=4
    elif keys[pygame.K_RIGHT] and self.xp+4<win_w-38:
	    self.xp+=4
    if keys[pygame.K_SPACE]:
        if (not len(missile) or multiFire) and (fireReady or holdFire):
            fireReady = False
            obj = Sprite()

            obj.type = "player missile"
            obj.image = image_missile
            obj.fn_move = move_player_missile
        
            obj.xp = self.xp + 15
            obj.yp = self.yp + 12
            obj.active = True
            missile.append(obj)

import random
# Function for player missile
def move_player_missile(self):
    self.yp -= 12
    if self.yp < 0:
        self.active = False
        del missile[missile.index(self)]
    if sprayFire:
        self.xp += random.randint(-15,15)

# Function for dementor movement
def move_invader(self):
    global score
    global done
    global win_w
    global invader_flip
 
    # Speed multiplier
    speed = 2   
 
    # For horizontal movement
    self.xp += self.xv * speed
    
    # For checking the edge of the screen

    if self.xp + self.xv*speed <=0 or self.xp + self.xv*speed >=800-38:
        invader_flip = True
    

    # For checking to see if the dementor has been hit
    for obj in missile:      
        if obj.active:
            if obj.xp > self.xp and obj.xp < self.xp + 35 and obj.yp > self.yp and obj.yp < self.yp + 35:
                self.active = False
                obj.active = False
                score += 1
                del missile[missile.index(obj)]               

    # Check if the game is over


# For making the dementors go the other way
def check_invader_flip():
    global invader_flip
    global max_sprites
    if invader_flip:
        invader_flip = False
        for i in range(0, max_sprites):
            if sprites[i].active and sprites[i].type == "invader":
                sprites[i].xv = -sprites[i].xv
                sprites[i].yp += 12

def show_start_screen():
    return;
     
def show_end_screen():
    return;
   
# Initialise sprites
sprites[0].sprite_type = "player"  
sprites[0].active = True            
sprites[0].xp = win_w//2            
sprites[0].yp = win_h - 40          
sprites[0].image = image_player 
sprites[0].fn_move = move_player   

# Game loop
while True:

    # Decide whether to show start screen or not


    # Load the invaders
    i = 1
    for row in range(0, 6):
        for col in range(0, max(1,14)):
            sprites[i].type = "invader"
            sprites[i].active = True
            sprites[i].xp = col * 50
            sprites[i].yp = row * 50
            sprites[i].xv = 1
            sprites[i].image = image_invader
            sprites[i].fn_move = move_invader
            i += 1

    done = 0
    while done == 0:

        # Colour the screen
        screen.fill((255,255,255))

        # Check for closing of window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                fireReady = True

        # For movement of character
        for i in range(0, max_sprites):
            if sprites[i].active:
                sprites[i].move()

        # Check if invaders require flipping
        check_invader_flip()

        # Set game background
        
 
        # Draw the Sprites by calling their draw function
        for i in range(0, max_sprites):
		    if sprites[i].active:
			    sprites[i].draw()
        [(m.move(), m.draw()) if m.active else None for m in missile]
        
        # Set the frame refresh rate
	pygame.display.flip()
	clock.tick(60)
    # Check if dementors are all killed
    if done != 1:
        break
