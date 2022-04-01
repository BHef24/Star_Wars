# imports 
import pygame, os, sys

# center pygame window on display
# technique found at https://stackoverflow.com/questions/5814125/how-to-designate-where-pygame-creates-the-game-window
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# initialize pygame
pygame.init()

# constants
WIDTH = 1440
HEIGHT = 900
FPS = 3

# RGB colors
yellow = (255, 255, 0)
black = (0, 0, 0)

# variables
image_count = 3 # counter for images
clock = pygame.time.Clock() # clock object
running = True
timer = 0

# load images into pygame
my_images = [
  pygame.image.load('./assets/abada_v3_1.png'),
  pygame.image.load('./assets/abada_v3_2.png'),
  pygame.image.load('./assets/abada_v3_3.png')
]

# changes size of all images to fit screen
for i in range(len(my_images)):
  my_images[i] = pygame.transform.scale(my_images[i], (500, 500))

# set Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A LONG TIME AGO IN A GALAXY FAR FAR AWAY!")
WINDOW.fill(black)

# set up your font
font = pygame.font.Font('./fonts/Dosis-Bold.ttf', 20)

# create your text
text = font.render('A LONG TIME AGO, IN A GALAXY FAR FAR AWAY', True, yellow, black)
textRect = text.get_rect()

# position the text
textRect.center = (WIDTH // 2, HEIGHT // 20)

# display text
WINDOW.blit(text, textRect)
pygame.display.flip()

pygame.display.set_caption("Graphic Artist: Zayn ")
text = font.render("Graphic Artist: Zayn", True, yellow, black)
textRect = text.get_rect()
textRect.center = (WIDTH // 2, HEIGHT // 6)
WINDOW.blit(text, textRect)
pygame.display.flip()


pygame.display.set_caption("Programmers: Sarah, Ben, Hope  ")
text = font.render("Programmers: Sarah, Ben, Hope", True, yellow, black)
textRect = text.get_rect()
textRect.center = (WIDTH // 2, HEIGHT // 8)
WINDOW.blit(text, textRect)
pygame.display.flip()
# draw shape function
def drawShape():
  global my_images
  global image_count
  if (image_count == 3):
     image_count = 0
  WINDOW.blit(my_images[image_count], (470, 200))
  pygame.display.flip()
  image_count += 1
  
# main animation Loop that will run for 10 seconds
while running and timer < 50:

  # upadate screen according to FPS value
  clock.tick(FPS)

  # update timer
  timer += 1

  # check if "X" is clicked by user 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      sys.exit()

  # call to drawShape function
  drawShape()
