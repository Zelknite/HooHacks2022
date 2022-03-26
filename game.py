#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, pygame
pygame.init()
Clock = pygame.time.Clock()
MAX_FRAME_RATE = 120

# The animating heart
class Heart(pygame.sprite.Sprite):
	def __init__(self, pos_x = 0, pos_y = 0):
		super().__init__()
		# Image and animation
		self.images = [pygame.image.load(f"Images/heart{i}.png") for i in range(1, 5)]
		self.image = self.images[0]
		self.animation_frames = [0, 1, 2, 1, 2, 3, 2, 1, 0]
		self.current_frame = 0
		self.rect = self.image.get_rect()
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.rect.topleft = [self.pos_x, self.pos_y]

	def update(self):
		if Clock.tick(MAX_FRAME_RATE/10):
			self.current_frame += 1
			if self.current_frame >= len(self.animation_frames):
				self.current_frame = 0
				self.is_animating = False
			self.image = self.images[self.animation_frames[self.current_frame]]
			self.rect = self.image.get_rect()
			self.rect.topleft = [self.pos_x, self.pos_y]
			return self.image

size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
speed = [2, 2]
background_color = 255, 255, 255

moving_sprites = pygame.sprite.Group()
heart = Heart(10, 10)
moving_sprites.add(heart)

while 1:
	# Handles the close button
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				heart.rect.x = event.pos[0]
				heart.rect.y = event.pos[1]

	screen.fill(background_color)
	moving_sprites.draw(screen)
	moving_sprites.update()
	pygame.display.flip()
	Clock.tick(MAX_FRAME_RATE)