#!/usr/bin/env python
import pyglet
from pyglet.window import key

class sprites(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def update(self, dx, dy):
		self.x += dx
		self.y += dy

	def check_bounds(self, width, height):
		min_x = -self.width / 2
		min_y = -self.height / 2
		max_x = width + self.width / 2
		max_y = height + self.height / 2
		if self.x < min_x:
			self.x = max_x
		elif self.x > max_x:
			self.x = min_x
		if self.y < min_y:
			self.y = max_y
		elif self.y > max_y:
			self.y = min_y

class game(pyglet.window.Window):
	bin = pyglet.image.atlas.TextureBin()
	def __init__(self):
		super(game, self).__init__()
		# Make the background white
		pyglet.gl.glClearColor(1,1,1,1)

		self.set_visible(False)

		self.set_fullscreen(True)
		self.set_vsync(True)
		self.set_location(0, 0)

		self.set_visible()

		self.default_cursor = self.get_system_mouse_cursor(self.CURSOR_DEFAULT)
		self.crosshair_cursor = self.get_system_mouse_cursor(self.CURSOR_CROSSHAIR)

		self.main_batch = pyglet.graphics.Batch()
		self.batches = [pyglet.graphics.Batch() for i in range(5)]
		self.background = pyglet.graphics.OrderedGroup(0)
		self.foreground = pyglet.graphics.OrderedGroup(1)

		self.step = 0

		self.step1 = sprites(pyglet.image.load('Images/Step1.png'), batch=self.batches[0], group=self.background, x = 0, y = 0)
		self.step2 = sprites(pyglet.image.load('Images/step2.png'), batch=self.batches[1], group=self.background, x = 0, y = 0)
		self.step3 = sprites(pyglet.image.load('Images/step3.png'), batch=self.batches[2], group=self.background, x = 0, y = 0)
		self.step4 = sprites(pyglet.image.load('Images/step4.png'), batch=self.batches[3], group=self.background, x = 0, y = 0)
		self.step5 = sprites(pyglet.image.load('Images/step5.png'), batch=self.batches[4], group=self.background, x = 0, y = 0)

		self.arrow_clock_label = sprites(pyglet.image.load('Images/arrow.png'), batch=self.batches[0], group=self.foreground, x = int(835/3840 * self.width), y = (self.height//3) + 50)
		self.arrow_power_label = sprites(pyglet.image.load('Images/arrow.png'), batch=self.batches[1], group=self.foreground, x = int(450/3840 * self.width), y = (self.height//3))
		self.arrow_cpu_label = sprites(pyglet.image.load('Images/arrow.png'), batch=self.batches[2], group=self.foreground, x = int(1680/3840 * self.width), y = (self.height//3) + 50)
		self.arrow_memory_label = sprites(pyglet.image.load('Images/arrow.png'), batch=self.batches[3], group=self.foreground, x = int(2340/3840 * self.width), y = (self.height//3) + 50)

		self.next = sprites(pyglet.image.load('Images/next.png'), batch=self.main_batch, group=self.foreground, x = self.width - 400, y = 0)
		self.next.scale_y = 1.2
		self.back = sprites(pyglet.image.load('Images/back.png'), batch=self.main_batch, group=self.foreground, x = 0, y = 0)

		# Labels
		self.clock_label_1 = pyglet.text.Label(text="Hello, I'm a clock! I act as the 'heart' of your computer by pulsing high and low signals", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3), color=(0, 0, 0, 255), batch=self.batches[0], group=self.foreground)
		self.clock_label_2 = pyglet.text.Label(text="to the rest of my system like a heart beats in your body. Each time I pulse, I output a high pulse", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-50, color=(0, 0, 0, 255), batch=self.batches[0], group=self.foreground)
		self.clock_label_3 = pyglet.text.Label(text="that tells the computer to perform one instruction. The more times I pulse per second, the faster", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-100, color=(0, 0, 0, 255), batch=self.batches[0], group=self.foreground)

		self.power_label_1 = pyglet.text.Label(text="Watts up! I'm food that goes into the belly of the computer! The CPU, Clock, Memory, and", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3), color=(0, 0, 0, 255), batch=self.batches[1], group=self.foreground)
		self.power_label_2 = pyglet.text.Label(text="the Console all rely on me to keep them working in tip top shape! Just like you need food", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-50, color=(0, 0, 0, 255), batch=self.batches[1], group=self.foreground)
		self.power_label_3 = pyglet.text.Label(text="to fill your stomach, computer's need electricity to live!", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-100, color=(0, 0, 0, 255), batch=self.batches[1], group=self.foreground)

		self.cpu_label_1 = pyglet.text.Label(text="Greetings! I am the CPU of your computer, which stands for Central Processing Unit.", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3), color=(0, 0, 0, 255), batch=self.batches[2], group=self.foreground)
		self.cpu_label_2 = pyglet.text.Label(text="Think of me as the brain of your computer, figuring out what the computer should do", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-50, color=(0, 0, 0, 255), batch=self.batches[2], group=self.foreground)
		self.cpu_label_3 = pyglet.text.Label(text="every time I get a clock pulse. In order to figure out what to do, I read a 'program',", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-100, color=(0, 0, 0, 255), batch=self.batches[2], group=self.foreground)
		self.cpu_label_4 = pyglet.text.Label(text="which is kind of like a blueprint of how to do something like display an Instagram page", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-150, color=(0, 0, 0, 255), batch=self.batches[2], group=self.foreground)
		self.cpu_label_5 = pyglet.text.Label(text="or do your taxes. But how do I run each instruction? Every instruction in your program", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-200, color=(0, 0, 0, 255), batch=self.batches[2], group=self.foreground)
		self.cpu_label_6 = pyglet.text.Label(text="includes a piece of data and an address. The address tells the CPU where the instruction", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-250, color=(0, 0, 0, 255), batch=self.batches[2], group=self.foreground)
		self.cpu_label_7 = pyglet.text.Label(text="is stored so that the CPU can find it! It's like knowing the address of your friend's", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-300, color=(0, 0, 0, 255), batch=self.batches[2], group=self.foreground)
		self.cpu_label_8 = pyglet.text.Label(text="house so you can find it. The data is the actual action to perform, like adding two numbers.", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-350, color=(0, 0, 0, 255), batch=self.batches[2], group=self.foreground)
		self.cpu_label_9 = pyglet.text.Label(text="So if I know where my friends house is located, I can get directions from where I am to get there!", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-400, color=(0, 0, 0, 255), batch=self.batches[2], group=self.foreground)

		self.memory_label_1 = pyglet.text.Label(text="Hi there! I'm your computer's memory. Think of me as the library of your computer that holds", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3), color=(0, 0, 0, 255), batch=self.batches[3], group=self.foreground)
		self.memory_label_2 = pyglet.text.Label(text="your program and all the data that it needs to work. Remember how we talked about data and", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-50, color=(0, 0, 0, 255), batch=self.batches[3], group=self.foreground)
		self.memory_label_3 = pyglet.text.Label(text="addresses? I hold both of these pieces to create a program that I send to the CPU. Think of", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-100, color=(0, 0, 0, 255), batch=self.batches[3], group=self.foreground)
		self.memory_label_4 = pyglet.text.Label(text="a program like a very tall shelf with cubbies for each address that holds a piece of data.", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-150, color=(0, 0, 0, 255), batch=self.batches[3], group=self.foreground)
		self.memory_label_5 = pyglet.text.Label(text="Every time the CPU needs some data, it just goes to the cubby or address where that data is,", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-200, color=(0, 0, 0, 255), batch=self.batches[3], group=self.foreground)
		self.memory_label_6 = pyglet.text.Label(text="grabs it, and then does something with it!", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-250, color=(0, 0, 0, 255), batch=self.batches[3], group=self.foreground)

		self.build_label_1 = pyglet.text.Label(text="Okay, now that we know about each of the pieces, how do we put them together? In the box to the", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3) - 100, color=(0, 0, 0, 255), batch=self.batches[4], group=self.foreground)
		self.build_label_2 = pyglet.text.Label(text="left, you can click and drag the blocks to create connections. To start, let's plug in the power.", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-150, color=(0, 0, 0, 255), batch=self.batches[4], group=self.foreground)
		self.build_label_3 = pyglet.text.Label(text="Take the cable and drag it into the outlet and the power input of the clock. Good job! Now you", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-200, color=(0, 0, 0, 255), batch=self.batches[4], group=self.foreground)
		self.build_label_4 = pyglet.text.Label(text="need to connect the clock output to the CPU and the memory. Click and drag from the clock output", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-250, color=(0, 0, 0, 255), batch=self.batches[4], group=self.foreground)
		self.build_label_5 = pyglet.text.Label(text="to the clock inputs of both of these blocks. Now that you're done with that, click and drag from", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-300, color=(0, 0, 0, 255), batch=self.batches[4], group=self.foreground)
		self.build_label_6 = pyglet.text.Label(text="each of the data and address lines of the CPU to the memory. Make sure to match the numbers for each of the lines!", font_name="Comic Sans", font_size=30, x=self.width//2, anchor_x='center', y=(self.height//3)-350, color=(0, 0, 0, 255), batch=self.batches[4], group=self.foreground)

		# For animating the heart
		self.hearts = [pyglet.image.load(f'Images/heart{i}.png') for i in range(1, 5)]
		self.hearts = [self.hearts[0], self.hearts[1], self.hearts[2], self.hearts[1], self.hearts[2], self.hearts[3], self.hearts[2], self.hearts[1], self.hearts[0]]
		self.heart_animation = sprites(pyglet.image.Animation.from_image_sequence(self.hearts, duration=0.1, loop=True), batch=self.main_batch, group=self.foreground, x=(self.width/4.6), y=(self.height/1.9))
		self.heart_animation.scale = 0.5

	def on_draw(self):
		self.render()

	def render(self):
		## == Clear the frame
		self.clear()

		self.batches[self.step].draw()

		self.main_batch.draw()

		## == And flip the current buffer to become the active viewed buffer.
		self.flip()

	def on_key_press(self, symbol, modifiers):
		if symbol == key.ESCAPE:
			print('The escape key was pressed.')
			self.close()

	def next_step(self):
		self.step+= 1
		if self.step == 5:
			self.step = 0

	def back_step(self):
		self.step-= 1
		if self.step == -1:
			self.step = 0

	# Handles the X button
	def on_close(self):
		print('The window was closed.')
		self.set_visible(False)
		self.close()

	# Handles the mouse button presses
	def on_mouse_press(self, x, y, button, modifiers):
		if ((self.next.height > y) and ((self.width - self.next.x) < x) and (self.width - self.next.x + self.next.width < x)):
			self.next_step()
		elif ((self.back.height > y) and (self.back.x + self.back.width > x)):
			self.back_step()
		else:
			print(f"Pressed ({x}, {y}). Next: ({self.next.x}, {self.next.y}) height {self.next.height}, Back: ({self.back.x}, {self.back.y})")
		pass

	def on_mouse_release(self, x, y, button, modifiers):
		pass

	def on_mouse_motion(self, x, y, dx, dy):
		pass

	# Required to drag items across the screen
	def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
		# Checks if the mouse is over the heart animation while it was dragged, works
		# if (((self.height - self.heart_animation.x - self.heart_animation.height) > x) and (self.heart_animation.x < x) and ((self.width - self.heart_animation.y - self.heart_animation.width) > y) and (self.heart_animation.y < y)):
		# 	self.heart_animation.update(dx, dy)
		# 	self.heart_animation.check_bounds(self.width, self.height)
		pass

	def on_mouse_enter(self, x, y):
		pass

	def on_mouse_leave(self, x, y):
		pass

	def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
		pass

if __name__ == '__main__':
	window = game()
	pyglet.app.run()