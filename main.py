# Devan Mathis, Talan Knipp, Miles Camey
# 11/29/23
# Candyland

# from os import
import sys
import time
import pygame
from pygame.locals import *
from Card import Cards
from Board import Board
from Player import Player

players = []
indexList = []
res = (575, 575)

screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

card = Cards()
board = Board()
"""while True:
  play = input("\nHow many people would like to play? (2, 3, or 4): ")

  if play.isdigit():
    play = int(play)
    if play in range(2, 4):
      break
    else:
      print("\nPlease enter a number 2 through 4 ")
  else:
    print("\nPlease enter a number 2-4 ")
    continue"""

# var for screen size
screen_size = (575, 575)

width = screen.get_width()
height = screen.get_height()

text_color = (255, 255, 255)
color_light = (1, 181, 46)
color_dark = (254, 84, 97) 

showCard = False
displayStartTime = 0
displayTime = 2
cardImage = None
cards = None
currentPlayerIndex = 0

playing = True

# modify icon on pygame window
icon = pygame.image.load('fudgebar_icon-removebg-preview.png')

# modify pygame window name
pygame.display.set_caption(' Candyland')
pygame.display.set_icon(icon)

# screen var using screen size parameter and resizable parameter
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

# game board
image = pygame.image.load('candyland_board.jpg').convert_alpha()
bg = pygame.transform.scale(image, screen_size)
blue_boi = 'blue_boi.png'
green_boi = 'green_boi.png'
purple_boi = 'purple_boi.png'
red_boi = 'red_boi.png'

singleBlue = 'Blue.png'
singleGreen = 'Green.png'
singlePurple = 'Purple.png'
singleRed = 'Red.png'
singleYellow = 'Yellow.png'
singleOrange = 'Orange.png'
doubleBlue = 'Double Blue.png'
doubleGreen = 'Double Green.png'
doublePurple = '2_Purple.png'
doubleRed = 'Double Red.png'
doubleYellow = 'Double Yellow.png'
doubleOrange = 'Double Orange.png'
Icecream = 'Ice Cream.png'
Peppermint = 'Peppermint.png'
Peanut = 'Peanut.png'
Lollipop = 'Lollipop.png'

pygame.init()

players = []
while True:
  play = input("\nHow many people would like to play? (2, 3, or 4): ")
  if play.isdigit():
    play = int(play)
    if play in range(2, 4+1):
      break
    else:
      print('\nPlease enter a number 2-4')
  else:
    print('\nPlease enter a number 2-4')

if play == 2:
  blueBoi = Player(400, 390, blue_boi)
  greenBoi = Player(8, 500, green_boi)
  players.append(blueBoi)
  players.append(greenBoi)
 
elif play == 3:
  blueBoi = Player(400, 390, blue_boi)
  greenBoi = Player(8, 500, green_boi)
  
  players.append(blueBoi)
  players.append(greenBoi)
  
  purpleBoi = Player(8, 520, purple_boi)
  players.append(purpleBoi)

elif play == 4:
  blueBoi = Player(400, 390, blue_boi)
  greenBoi = Player(8, 500, green_boi)
  
  players.append(blueBoi)
  players.append(greenBoi)
  
  purpleBoi = Player(8, 520, purple_boi)
  players.append(purpleBoi)
  
  redBoi = Player(-12, 520, red_boi)
  players.append(redBoi)

def displayWinScreen():
  screen.fill((0, 0, 0))
  font = pygame.font.Font(None, 36)
  text = font.render(f'Congratulations Player {currentPlayerIndex+1}! You win!', 1, (255,255,255))
  textpos = text.get_rect(centerx = screen.get_width()/2, centery = screen.get_height()/2)
  screen.blit(text, textpos)
  pygame.display.flip()
  time.sleep(5)
  pygame.quit()
  sys.exit()


def displayPlayers():
  for player in players:
    player.draw(screen)
    player.update()

smallfont = pygame.font.SysFont('Comic Sans MS', 50)
text = smallfont.render('draw', True, text_color) 

card.makeDeck()
card.shuffle()

while playing:
  currentPlayer = players[currentPlayerIndex]
  
  mouse = pygame.mouse.get_pos()
  screen.blit(bg, (0, 0))

  if currentPlayer.position == (240, 120):
    if showCard:
      displayStartTime = time.time()
      while time.time() - displayStartTime < displayTime:
        pass
      showCard = False
      cardImage = None
    playing = False
    displayWinScreen()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing = False
      pygame.quit()
      quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
      if width/2 <= mouse[0] <= width/2+100 and height/2 <= mouse[1] <= height/2+40:
        showCard = True
        displayStartTime = time.time()
        cards = card.draw()
        if cards[0] == 'blue' and cards[1] == 2:
          cardImage = pygame.image.load(doubleBlue).convert_alpha()
          
        elif cards[0] == 'red' and cards[1] == 2:
          cardImage = pygame.image.load(doubleRed).convert_alpha()
          
        elif cards[0] == 'green' and cards[1] == 2:
          cardImage = pygame.image.load(doubleGreen).convert_alpha()
          
        elif cards[0] == 'orange' and cards[1] == 2:
          cardImage = pygame.image.load(doubleOrange).convert_alpha()
          
        elif cards[0] == 'yellow' and cards[1] == 2:
          cardImage = pygame.image.load(doubleYellow).convert_alpha()

        elif cards[0] == 'purple' and cards[1] == 2:
          cardImage = pygame.image.load(doublePurple).convert_alpha()
          
        elif cards[0] == 'red':
          cardImage = pygame.image.load(singleRed).convert_alpha()
          
        elif cards[0] == 'blue':
          cardImage = pygame.image.load(singleBlue).convert_alpha()
          
        elif cards[0] == 'green':
          cardImage = pygame.image.load(singleGreen).convert_alpha()
          
        elif cards[0] == 'yellow':
          cardImage = pygame.image.load(singleYellow).convert_alpha()
          
        elif cards[0] == 'orange':
          cardImage = pygame.image.load(singleOrange).convert_alpha()
        
        elif cards[0] == 'purple':
          cardImage = pygame.image.load(singlePurple).convert_alpha()
          
        elif cards[0] == 'peppermint':
          cardImage = pygame.image.load(Peppermint).convert_alpha()
          
        elif cards[0] == 'icecream':
          cardImage = pygame.image.load(Icecream).convert_alpha()
          
        elif cards[0] == 'peanut':
          cardImage = pygame.image.load(Peanut).convert_alpha()
          
        elif cards[0] == 'lollipop':
          cardImage = pygame.image.load(Lollipop).convert_alpha()

  if showCard and cardImage is not None:
    img = pygame.transform.scale(cardImage, (300,400))
    screen.blit(img, (155, 50))
    if time.time() - displayStartTime > displayTime:
      showCard = False
      cardImage = None

  else:
    if not showCard:
      displayPlayers()
      for player in players:
        player.draw(screen)
        player.update()
    

    if width/2 <= mouse[0] <= width/2+100 and height/2 <= mouse[1] <= height/2+40: 
      pygame.draw.rect(screen,color_light,[width/2,height/2,90,40], border_radius=15) 
  
    else: 
      pygame.draw.rect(screen,color_dark,[width/2,height/2,90,40], border_radius=15)
  
    text_rect = text.get_rect(center=(width/2+44, height/2+18))
    screen.blit(text, text_rect)

  if cards and cards[0] in board.spacesList:
    try:
      next_index = board.spacesList.index(cards[0], currentPlayer.index + 1)
    except ValueError:
      if cards[0] in board.specialSpot:
        next_index = board.spacesList.index(cards[0])
      else:
        next_index = currentPlayer.index
    steps = next_index - currentPlayer.index
    currentPlayer.index += steps
    
    if cards[0] in board.specialSpot:
      specialInd = board.specialSpot.index(cards[0])
      x, y = map(int, board.specialCords[specialInd].split(', '))
      currentPlayer.position = (x,y)
      
    elif currentPlayer.position == board.bridgeCord[0]:
      currentPlayer.position = (400, 390)
      currentPlayer.index = board.cordList.index('400, 390')
      
    elif currentPlayer.position == board.bridgeCord[1]:
      currentPlayer.position = (185, 440)
      currentPlayer.index = board.cordList.index('185, 440')
      
    elif cards[1] == 2:
      currentPlayer.index = board.spacesList.index(cards[0], currentPlayer.index + 1)
      x, y = map(int, board.cordList[currentPlayer.index].split(', '))
      currentPlayer.position = (x, y)
    
    next_index = board.spacesList.index(cards[0], currentPlayer.index)
    steps = next_index - currentPlayer.index
    currentPlayer.index += steps
    x, y = map(int, board.cordList[currentPlayer.index].split(', '))
    currentPlayer.position = (x, y)
    cards = None
    if currentPlayer.position in board.licorseCords:
      currentPlayer.skip_next_turn = True
    else:
      currentPlayerIndex = (currentPlayerIndex + 1) % len(players)
  displayPlayers()
  
  pygame.display.update()
  clock.tick(60)
