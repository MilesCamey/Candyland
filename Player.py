import pygame
from pygame.locals import *
from typing import Tuple

class Player(pygame.sprite.Sprite):
  def __init__(self, x, y, image_path):
      super().__init__()
      self.position: Tuple[int, int] = (0, 0)
      self.image = pygame.image.load(image_path)
      self.size = self.image.get_size()
      self.index = 0
      self.skip_next_turn = False
      # create a 2x bigger image than self.image
      self.resize = pygame.transform.scale(self.image, (int(self.size[0]*.1), int(self.size[1]*.1)))

  def update(self):
    self.position = (self.position[0], self.position[1])

  def draw(self, surface):
    surface.blit(self.resize, self.position)