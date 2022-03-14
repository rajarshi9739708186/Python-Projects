import pygame
import os
import random
from pygame import mixer
import tkinter.messagebox as tmsg

# It will initialize Pygame
# To access all of it's methods and features
pygame.init()

# Display Screen
# Width = 800
# Height = 600
game_screen = pygame.display.set_mode((800, 600))

# Title of the Game Window
pygame.display.set_caption("Space Invaders")

Supporting_Files_Missing = False

# Icon of the Game window
try:
    GameWindow_Icon = pygame.image.load(os.path.join(os.getcwd(), "Supporting_Images\\Game_Screen_Icon.png")) # Icon Object
except:
    Supporting_Files_Missing = True
pygame.display.set_icon(GameWindow_Icon) # Set Icon

# Space Background
try:
    SpaceBackground_Image = pygame.image.load(os.path.join(os.getcwd(), "Supporting_Images\\Space.jpg")) # Image Size 800 X 600
except:
    Supporting_Files_Missing = True

# Spaceship Image
try:
    SpaceShip_Image = pygame.image.load(os.path.join(os.getcwd(), "Supporting_Images\\SpaceShip.png")) # Image Size 64 x 64
except:
    Supporting_Files_Missing = True
# X and Y co-ordinate supposed to be the top left corner of the Image
# Trying to place the Spaceship Image at Exactly Middle at Bottom
# X supposed to be Middle
# Y supposed to be little up from bottom
SpaceShip_Pos_X = 368 # 800/2 => 400 - (64/2) => 368
SpaceShip_Pos_Y = 520 # 600 - 64 + 16 (little up from exact bottom) => 536

# Alien Image
Number_of_Aliens = 5
Aliens_Image = []
Aliens_Pos_X = []
Aliens_Pos_Y = []
Move_To_Right = []
Move_To_Left = []

for Alien in range(Number_of_Aliens):
    try:
        Aliens_Image.append(pygame.image.load(os.path.join(os.getcwd(), "Supporting_Images\\Alien.png"))) # Image Size 64 x 64
    except:
        Supporting_Files_Missing = True
    # Enemy will appear in different positions
    Aliens_Pos_X.append(random.randint(0,736))
    Aliens_Pos_Y.append(random.randint (10, 100))
    Move_To_Right.append(True)
    Move_To_Left.append(False)

# Bullet Image
try:
    Bullet_Image = pygame.image.load(os.path.join(os.getcwd(), "Supporting_Images\\Bullet.png")) # Image Size 32 x 32
except:
    Supporting_Files_Missing = True
Bullet_Pos_X = 0
Bullet_Pos_Y = 0

# Explosion Image
try:
    Explosion_Image = pygame.image.load(os.path.join(os.getcwd(), "Supporting_Images\\Explosion.png")) # Image Size 32 x 32
except:
    Supporting_Files_Missing = True

# Need to draw the space background over game screen
def drawSpaceBackground():
    game_screen.blit(SpaceBackground_Image, (0,0))

# Need to draw the spaceship over game screen
def drawSpaceShip(pos_X, pos_Y):
    game_screen.blit(SpaceShip_Image, (pos_X, pos_Y))

# Need to draw the Alien over game screen
def drawAlien(Alien_Image, pos_X, pos_Y):
    game_screen.blit(Alien_Image, (pos_X, pos_Y))

# Need to draw the Bullet over game screen
def drawBullet(pos_X, pos_Y):
    game_screen.blit(Bullet_Image, (pos_X, pos_Y))

# Check if collision happend in between current bullet and Enemy
def detectCollision(bullet_X, bullet_y, alien_x, alien_y):
    if (bullet_X >= alien_x+3 and bullet_X <= alien_x+64-3) and (bullet_y <= alien_y+64-3 and bullet_y >= alien_y+3):
        game_screen.blit(Explosion_Image, (alien_x, alien_y)) # Draw Explosion Image
        return True # Collision Happened
    else:
        return False

# Check If Alien enterd into Spaceship Zone
def AlienEnterdIntoSpaceshipArea(Aliens_Pos, SpaceShip_Pos):
    if Aliens_Pos >= SpaceShip_Pos:
        return True
    else:
        return False

# Variable to Detect if Game is running
Game_ON = True
Game_Over = False
Bullet_can_be_Fired = False
Bullet_is_on_Screen = False
Enemy_is_Killed = False

# Player Score
Player_Score = 0
# Player score Font
try:
    Player_Score_Font = pygame.font.Font(os.path.join(os.getcwd(), "Supporting_Images\\OpenSans-Regular.ttf"), 24)
except:
    Supporting_Files_Missing = True
# Game Over Message Font
try:
    GameOverMessage_Font = pygame.font.Font(os.path.join(os.getcwd(), "Supporting_Images\\OpenSans-Regular.ttf"), 64)
except:
    Supporting_Files_Missing = True

# Bullet Sound
try:
    Bullet_Sound = mixer.Sound("Supporting_Images\\Bullet_Sound.wav")
except:
    Supporting_Files_Missing = True
# Explosion Sound
try:
    Explosion_Sound = mixer.Sound("Supporting_Images\\Explosion.wav")
except:
    Supporting_Files_Missing = True

# Show Player score
def showPlayerScore(Score_value):
    # Render Message
    scoreMassage = Player_Score_Font.render(f"Score : {Score_value}", True, (255, 255, 255))
    game_screen.blit(scoreMassage, (10, 10))

# Show Game Over Message
def GameOverMessage():
    # Render Message
    GameOverMassage = GameOverMessage_Font.render(f"Game Over", True, (255, 255, 255))
    game_screen.blit(GameOverMassage, (200, 250))

# Show Supporting File Issue Message
def SupportingFileIssueMessage():
    pygame.font.init()
    SupportingFileIssue_Font = pygame.font.SysFont('Comic Sans MS', 64)
    # Render Message
    SupportingFileIssueMassage = SupportingFileIssue_Font.render(f"Supporting File Missing", True, (255, 0, 0))
    game_screen.blit(SupportingFileIssueMassage, (50, 250))

# Start Game
while Game_ON:
    # Set color for Window
    # We always to to fill color first. If needed
    # Rest of the Images which supposed to be drawn should come over the fill screen
    game_screen.fill((0, 0, 0))  # RGB value. Now set to Black

    # If Supporting Files are not missing
    if Supporting_Files_Missing == False:
        # Draw space background on each frame
        drawSpaceBackground()

        if Game_Over == False:
            # During game is active
            # Pygame will full of continuous Events
            # At each moment we should capture which all events are going on
            # Based on that we should control the Game
            for event in pygame.event.get(): # Capture all the events at every moment
                if event.type == pygame.QUIT: # Pressed close button of the screen window
                    Game_ON = False # Game screen is closed

                if event.type == pygame.KEYDOWN: # KEYDOWN means some key from keyboard is presses. It will true until we are not releasing finger from the key
                    # Check which particular key is pressed
                    if event.key == pygame.K_LEFT: # Left arrow key is pressed
                        if SpaceShip_Pos_X >= 10: # Ensure that Spaceship is not moved out from screen
                            SpaceShip_Pos_X -= 10
                    if event.key == pygame.K_RIGHT: # Right arrow pressed
                        if SpaceShip_Pos_X <= 790-64:  # Ensure that Spaceship is not moved out from screen
                            SpaceShip_Pos_X += 10
                    if event.key == pygame.K_SPACE:  # Fire Bullet if No Bullet is on Screen. At a time only 1 bullet can be fired
                        Bullet_can_be_Fired = True # Now Bullet can be fired
                        if Bullet_is_on_Screen == False: # Only if no bullet is on Screen, then only fire next one
                            Bullet_is_on_Screen = True
                            Bullet_Pos_X = SpaceShip_Pos_X + 16
                            Bullet_Pos_Y = SpaceShip_Pos_Y - 32 - 5
                if event.type == pygame.KEYUP: # KEYUP means Key is released
                    pass # Nothing to do with this Game

            # Draw Spaceship Continously over the screen
            drawSpaceShip(SpaceShip_Pos_X, SpaceShip_Pos_Y)

            for Alien_pos, Alien in enumerate(Aliens_Image):
                Bullet_coolided_with_ALien = detectCollision(Bullet_Pos_X, Bullet_Pos_Y, Aliens_Pos_X[Alien_pos],Aliens_Pos_Y[Alien_pos])

                # Display Current Bullet and Current enemy over the screen, until they are not collided
                if not Bullet_coolided_with_ALien:
                    # Enemy Movement
                    # While it will hit at left wall it will start moving to right
                    # While it will hit at right wall it will start moving at left
                    if Aliens_Pos_X[Alien_pos] <= 0:
                        Move_To_Right[Alien_pos] = True
                        Move_To_Left[Alien_pos] = False
                    if Aliens_Pos_X[Alien_pos] >= 800 - 64 - 0.1:
                        Move_To_Right[Alien_pos] = False
                        Move_To_Left[Alien_pos] = True
                    if Move_To_Right[Alien_pos]:
                        Aliens_Pos_X[Alien_pos] += 0.8
                    if Move_To_Left[Alien_pos]:
                        Aliens_Pos_X[Alien_pos] -= 0.8
                    Aliens_Pos_Y[Alien_pos] += 0.02

                    # Draw Alien Continously over the screen
                    drawAlien(Aliens_Image[Alien_pos], Aliens_Pos_X[Alien_pos], Aliens_Pos_Y[Alien_pos])

                    # Bullet Movement
                    if Bullet_can_be_Fired:
                        # If bullet is on screen keep on moving
                        if Bullet_is_on_Screen:
                            # If Bullet disappear from screen
                            # Next bullet is ready for Fire
                            # If we press Spacebar
                            if Bullet_Pos_Y <= 0:
                                Bullet_can_be_Fired = False  # Ready for next bullet
                                Bullet_is_on_Screen = False  # Current bullet got disappear from screen
                            drawBullet(Bullet_Pos_X, Bullet_Pos_Y)
                            Bullet_Pos_Y -= 1
                            # Bullet Sound
                            Bullet_Sound.play()
                else:
                    Player_Score += 1

                    # Explosion Sound
                    mixer.music.load("Supporting_Images\\Explosion.wav")
                    mixer.music.play()

                    # Reset Bullet Status
                    Bullet_Pos_X = 0
                    Bullet_Pos_Y = 0
                    Bullet_can_be_Fired = False
                    Bullet_is_on_Screen = False

                    # Regenerate Alien for that position
                    # Create a New Alien
                    Aliens_Pos_X[Alien_pos] = random.randint(0, 736)
                    Aliens_Pos_Y[Alien_pos] = random.randint(10, 100)
                    Move_To_Right[Alien_pos] = True
                    Move_To_Left[Alien_pos] = False

                # Check If Alien entered into spaceship zone
                if AlienEnterdIntoSpaceshipArea(Aliens_Pos_Y[Alien_pos]+64, SpaceShip_Pos_Y):
                    Game_Over = True
                    break
        else:
            GameOverMessage()
            for event in pygame.event.get(): # Capture all the events at every moment
                if event.type == pygame.QUIT: # Pressed close button of the screen window
                    Game_ON = False # Game screen is closed

        # Show Player Score
        showPlayerScore(Player_Score)
    else:
        SupportingFileIssueMessage()
        for event in pygame.event.get():  # Capture all the events at every moment
            if event.type == pygame.QUIT:  # Pressed close button of the screen window
                Game_ON = False  # Game screen is closed

    # Update Game Screen
    # We need to updae screen in a continuous manner
    # so that game screen always gets updated with setting u have done
    pygame.display.update()