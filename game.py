#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, pygame
pygame.init()
Clock = pygame.time.Clock()
MAX_FRAME_RATE = 120

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
speed = [2, 2]
background_color = 255, 255, 255

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
		self.current_frame += 0.2
		if self.current_frame >= len(self.animation_frames):
			self.current_frame = 0
			self.is_animating = False
		self.image = self.images[self.animation_frames[int(self.current_frame)]]
		self.rect = self.image.get_rect()
		self.rect.center = [self.pos_x, self.pos_y]

# class CPU(pygame.sprite.Sprite):
# 	def __init__(self, pos_x = 0, pos_y = 0):
# 		super().__init__()
# 		# Image and animation
# 		self.images = [pygame.image.load(f"Images/CPU.png")]
# 		self.image = self.images[0]
# 		self.current_frame = 0
# 		self.rect = self.image.get_rect()
# 		self.pos_x = pos_x
# 		self.pos_y = pos_y
# 		self.rect.topleft = [self.pos_x, self.pos_y]
# 		self.dragging = False

# 	def update(self):
# 		pass

# class Memory(pygame.sprite.Sprite):
# 	def __init__(self, pos_x = 0, pos_y = 0):
# 		super().__init__()
# 		# Image and animation
# 		self.images = [pygame.image.load(f"Images/Memory.png")]
# 		self.image = self.images[0]
# 		self.current_frame = 0
# 		self.rect = self.image.get_rect()
# 		self.pos_x = pos_x
# 		self.pos_y = pos_y
# 		self.rect.topleft = [self.pos_x, self.pos_y]
# 		self.dragging = False

# 	def update(self):
# 		pass

# class Power(pygame.sprite.Sprite):
# 	def __init__(self, pos_x = 0, pos_y = 0):
# 		super().__init__()
# 		# Image and animation
# 		self.images = [pygame.image.load(f"Images/power.png")]
# 		self.image = self.images[0]
# 		self.current_frame = 0
# 		self.rect = self.image.get_rect()
# 		self.pos_x = pos_x
# 		self.pos_y = pos_y
# 		self.rect.topleft = [self.pos_x, self.pos_y]
# 		self.dragging = False

# 	def update(self):
# 		pass

animated_sprites = pygame.sprite.Group()
heart = Heart(10, 10)
animated_sprites.add(heart)

# Non-animating objects
power = pygame.image.load("Images/power.png")
power_pos = [10, 10]
power_rect = power.get_rect()
power_dragging = False
memory = pygame.image.load("Images/Memory.png")
memory_pos = [100, 100]
memory_rect = memory.get_rect()
memory_dragging = False
cpu = pygame.image.load("Images/CPU.png")
cpu_pos = [200, 200]
cpu_rect = cpu.get_rect()
cpu_dragging = False
clock_without_heart = pygame.image.load("Images/Clock_without_heart.png")
clock_without_heart_pos = [300, 300]
clock_without_heart_rect = clock_without_heart.get_rect()
clock_without_heart_dragging = False

while 1:
	# Handles the close button
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			sys.exit()
		# The following block will handle the dragging of the heart across the screen
		if event.type == pygame.MOUSEBUTTONDOWN:
			if heart.rect.collidepoint(event.pos):
				heart.dragging = True
				heart_mouse_x, heart_mouse_y = event.pos
				heart_offset_x = heart.pos_x - heart_mouse_x
				heart_offset_y = heart.pos_y - heart_mouse_y
			elif power_rect.collidepoint(event.pos):
				power_dragging = True
				power_mouse_x, power_mouse_y = event.pos
				power_offset_x = power_pos[0] - power_mouse_x
				power_offset_y = power_pos[1] - power_mouse_y
			elif memory_rect.collidepoint(event.pos):
				memory_dragging = True
				memory_mouse_x, memory_mouse_y = event.pos
				memory_offset_x = memory_pos[0] - memory_mouse_x
				memory_offset_y = memory_pos[1] - memory_mouse_y
			elif cpu_rect.collidepoint(event.pos):
				cpu_dragging = True
				cpu_mouse_x, cpu_mouse_y = event.pos
				cpu_offset_x = cpu_pos[0] - cpu_mouse_x
				cpu_offset_y = cpu_pos[1] - cpu_mouse_y
			elif clock_without_heart_rect.collidepoint(event.pos):
				clock_without_heart_dragging = True
				clock_without_heart_mouse_x, clock_without_heart_mouse_y = event.pos
				clock_without_heart_offset_x = clock_without_heart_pos[0] - clock_without_heart_mouse_x
				clock_without_heart_offset_y = clock_without_heart_pos[1] - clock_without_heart_mouse_y
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				heart.dragging = False
				power_dragging = False
				memory_dragging = False
				cpu_dragging = False
				clock_without_heart_dragging = False
		elif event.type == pygame.MOUSEMOTION:
			if heart.dragging:
				heart_mouse_x, heart_mouse_y = event.pos
				if ((heart_mouse_x + heart_offset_x + heart.image.get_width()) > 0 and (heart_mouse_x + heart_offset_x + heart.image.get_width()) <= width):
					heart.pos_x = heart_mouse_x + heart_offset_x
				if ((heart_mouse_y + heart_offset_y + heart.image.get_height()) > 0 and (heart_mouse_y + heart_offset_y + heart.image.get_height()) <= height):
					heart.pos_y = heart_mouse_y + heart_offset_y
			elif power_dragging:
				power_mouse_x, power_mouse_y = event.pos
				if ((power_mouse_x + power_offset_x + power.get_width()) > 0 and (power_mouse_x + power_offset_x + power.get_width()) <= width):
					power_pos[0] = power_mouse_x + power_offset_x
				if ((power_mouse_y + power_offset_y + power.get_height()) > 0 and (power_mouse_y + power_offset_y + power.get_height()) <= height):
					power_pos[1] = power_mouse_y + power_offset_y
			elif memory_dragging:
				memory_mouse_x, memory_mouse_y = event.pos
				if ((memory_mouse_x + memory_offset_x + memory.get_width()) > 0 and (memory_mouse_x + memory_offset_x + memory.get_width()) <= width):
					memory_pos[0] = memory_mouse_x + memory_offset_x
				if ((memory_mouse_y + memory_offset_y + memory.get_height()) > 0 and (memory_mouse_y + memory_offset_y + memory.get_height()) <= height):
					memory_pos[1] = memory_mouse_y + memory_offset_y
			elif cpu_dragging:
				cpu_mouse_x, cpu_mouse_y = event.pos
				if ((cpu_mouse_x + cpu_offset_x + cpu.get_width()) > 0 and (cpu_mouse_x + cpu_offset_x + cpu.get_width()) <= width):
					cpu_pos[0] = cpu_mouse_x + cpu_offset_x
				if ((cpu_mouse_y + cpu_offset_y + cpu.get_height()) > 0 and (cpu_mouse_y + cpu_offset_y + cpu.get_height()) <= height):
					cpu_pos[1] = cpu_mouse_y + cpu_offset_y

	screen.fill(background_color)
	# Add the animated widgets
	animated_sprites.draw(screen)
	animated_sprites.update()
	# Draw the non-animated widgets
	screen.blit(power, power_pos)
	screen.blit(memory, memory_pos)
	screen.blit(cpu, cpu_pos)
	pygame.display.flip()
	Clock.tick(MAX_FRAME_RATE)
