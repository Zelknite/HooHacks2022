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
		self.images = [pygame.transform.scale(pygame.image.load(f"Images/heart{i}.png"), (200, 200)) for i in range(1, 5)]
		self.image = self.images[0]
		self.animation_frames = [0, 1, 2, 1, 2, 3, 2, 1, 0, 0]
		self.current_frame = 0
		self.rect = self.image.get_rect()
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.rect.center = [self.pos_x, self.pos_y]
		self.dragging = False

	def update(self):
		self.current_frame += 0.1
		if self.current_frame >= len(self.animation_frames):
			self.current_frame = 0
			self.is_animating = False
		self.image = self.images[self.animation_frames[int(self.current_frame)]]
		self.rect = self.image.get_rect()
		self.rect.center = [self.pos_x, self.pos_y]


class CPU(pygame.sprite.Sprite):
	def __init__(self, pos_x = 0, pos_y = 0):
		super().__init__()
		# Image and animation
		self.images = [pygame.image.load(f"Images/CPU.png")]
		self.image = self.images[0]
		self.current_frame = 0
		self.rect = self.image.get_rect()
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.rect.topleft = [self.pos_x, self.pos_y]

class Memory(pygame.sprite.Sprite):
	def __init__(self, pos_x = 0, pos_y = 0):
		super().__init__()
		# Image and animation
		self.images = [pygame.image.load(f"Images/Memory.png")]
		self.image = self.images[0]
		self.current_frame = 0
		self.rect = self.image.get_rect()
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.rect.topleft = [self.pos_x, self.pos_y]

class Power(pygame.sprite.Sprite):
	def __init__(self, pos_x = 0, pos_y = 0):
		super().__init__()
		# Image and animation
		self.images = [pygame.image.load(f"Images/BetterPower.gif")]
		self.image = self.images[0]
		self.current_frame = 0
		self.rect = self.image.get_rect()
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.rect.topleft = [self.pos_x, self.pos_y]



size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
speed = [2, 2]
background_color = 255, 255, 255

moving_sprites = pygame.sprite.Group()
heart = Heart(10, 10)
power = Power(10, 10)
memory = Memory(10, 10)
cpu = CPU(10,10)
moving_sprites.add(heart)
moving_sprites.add(power)
moving_sprites.add(memory)
moving_sprites.add(cpu)

while 1:
	# Handles the close button
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			sys.exit()
		# The following block will handle the dragging of the heart across the screen
		if event.type == pygame.MOUSEBUTTONDOWN:
			if heart.rect.collidepoint(event.pos):
				heart.dragging = True
				mouse_x, mouse_y = event.pos
				offset_x = heart.pos_x - mouse_x
				offset_y = heart.pos_y - mouse_y
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				heart.dragging = False
		elif event.type == pygame.MOUSEMOTION:
			if heart.dragging:
				mouse_x, mouse_y = event.pos
				if ((mouse_x + offset_x + heart.image.get_width()) > 0 and (mouse_x + offset_x + heart.image.get_width()) < width):
					heart.pos_x = mouse_x + offset_x
				if ((mouse_y + offset_y + heart.image.get_height()) > 0 and (mouse_y + offset_y + heart.image.get_height()) < height):
					heart.pos_y = mouse_y + offset_y

	screen.fill(background_color)
	animated_sprites.draw(screen)
	animated_sprites.update()
	pygame.display.flip()
	Clock.tick(MAX_FRAME_RATE)
