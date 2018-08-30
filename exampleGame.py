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
invader_flip = False
invader_count = 0

# Assigning images to characters
image_player = pygame.image.load("player.png").convert()
image_invader = pygame.image.load("invader.png").convert()
image_missile = pygame.image.load("missile.png").convert()
image_title = pygame.image.load("title.png").convert()
image_end = pygame.image.load("end.png").convert()
image_finish = pygame.image.load("finish.png").convert()

# Enabling transparency on the images
image_player.set_colorkey((255, 255, 255))
image_invader.set_colorkey((255, 255, 255))
image_missile.set_colorkey((255, 255, 255))

# For keyboard input
pygame.key.set_repeat(1,1)

class Sprite:
    active = None   # whether the sprite is active or off
    xp = None       # x coordinate
    yp = None       # y coordinate
    xv = None
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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        self.xp -= 4
    if keys[pygame.K_RIGHT]:
        self.xp += 4
    if keys[pygame.K_SPACE]:
        if sprites[1].active == False:
            sprites[1].active = True
            sprites[1].xp = self.xp + 14
            sprites[1].yp = self.yp

# Function for player missile
def move_player_missile(self):
    self.yp -= 12
    if self.yp < 0:
        self.active = False

# Function for dementor movement
def move_invader(self):
    global done
    global win_w
    global invader_flip
    global invader_count
 
    # Speed multiplier
    speed = 2   
 
    # For horizontal movement
    self.xp += self.xv * speed 

    # For checking the edge of the screen
    if (self.xp <= 0 or self.xp >= win_w-35):
        invader_flip = True

    # For checking to see if the dementor has been hit
    if sprites[1].active:
        if sprites[1].xp > self.xp and sprites[1].xp < self.xp + 35 and sprites[1].yp > self.yp and sprites[1].yp < self.yp + 35:
            self.active = False
            sprites[1].active = False
            invader_count -= 1

    # Check if the game is over
    if invader_count == 0:
        print("Dementors defeated!")
        done = 2
    if self.yp > sprites[0].yp or (self.yp == sprites[0].yp and self.xp == sprites[0].xp):
        print("The dementors have won!")
        done = 3

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
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        screen.fill([255,255,255])
        screen.blit(image_title, [0,0])
        
        pygame.display.update()
        clock.tick(15) 
     
def show_end_screen():
    global invader_count
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        screen.fill([255,255,255])
        if invader_count == 0:
            screen.blit(image_finish, [0,0])
        else :
            screen.blit(image_end, [0,0])
        
        pygame.display.update()
        clock.tick(15) 
   
# Initialise sprites
sprites[0].sprite_type = "player"  
sprites[0].active = True            
sprites[0].xp = win_w//2            
sprites[0].yp = win_h - 40          
sprites[0].image = image_player 
sprites[0].fn_move = move_player   

sprites[1].type = "player missile"
sprites[1].image = image_missile
sprites[1].fn_move = move_player_missile



# Game loop
while True:

    # Decide whether to show start screen or not
    show_start_screen()

    # Load the invaders
    i = 2
    for row in range(0, 1):
        for col in range(0, 1):
            sprites[i].type = "invader"
            sprites[i].active = True
            sprites[i].xp = col * 50
            sprites[i].yp = row * 50
            sprites[i].xv = 20
            sprites[i].image = image_invader
            sprites[i].fn_move = move_invader
            invader_count += 1
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

        # Set the frame refresh rate
        pygame.display.flip()
        clock.tick(60)
            

    # Check if dementors are all killed
    if done != 1:
        show_end_screen()
        break
