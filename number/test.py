import asyncio, random, sys, time

import cozmo

from cozmo.lights import blue_light, Color, green_light, Light, red_light, white_light, off_light
from cozmo.util import degrees, distance_mm, radians, speed_mmps

ones = [off_light] * 3 + [white_light]
two = [white_light] + [off_light] + [white_light] * 2
twos = [white_light] * 3 + [off_light]
threes = [white_light] + [off_light] + [white_light] * 2
four = [off_light] + [white_light] * 3
fours = [white_light] + [off_light] * 2 + [white_light]
five = [white_light] * 3 + [off_light]
fives = [white_light] + [off_light] + [white_light] * 2
six = [white_light] * 3 + [off_light]
sixs = [white_light] * 4
seven = [white_light] * 2 + [off_light] + [white_light]
sevens = [off_light] * 3 + [white_light]
eights = [white_light] * 4
nine = [white_light] * 4
nines = [white_light] + [off_light] + [white_light] * 2
zero = [white_light] * 2 + [off_light] + [white_light]
zeros = [off_light] + [white_light] * 3

class RUN:
	def __init__(self, robot: cozmo.robot.Robot):
		self.robot = robot
		self.cubes = None
		self.waittime = 1

	def run(self):
		if not self.cubes_connected():
			print('Cubes did not connect successfully - check that they are nearby. You may need to replace the batteries.')
			return
		self.show1()
		self.show2()
		self.show3()
		self.show4()
		self.show5()
		self.show6()
		self.show7()
		self.show8()
		self.show9()
		self.show0()

	def show1(self):
		self.cubes[0].set_light_corners(*ones)
		self.cubes[1].set_light_corners(*ones)
		time.sleep(self.waittime)

	def show2(self):
		self.cubes[0].set_light_corners(*two)
		self.cubes[1].set_light_corners(*twos)
		time.sleep(self.waittime)

	def show3(self):
		self.cubes[0].set_light_corners(*threes)
		self.cubes[1].set_light_corners(*threes)
		time.sleep(self.waittime)

	def show4(self):
		self.cubes[0].set_light_corners(*four)
		self.cubes[1].set_light_corners(*fours)
		time.sleep(self.waittime)

	def show5(self):
		self.cubes[0].set_light_corners(*five)
		self.cubes[1].set_light_corners(*fives)
		time.sleep(self.waittime)

	def show6(self):
		self.cubes[0].set_light_corners(*six)
		self.cubes[1].set_light_corners(*sixs)
		time.sleep(self.waittime)

	def show7(self):
		self.cubes[0].set_light_corners(*seven)
		self.cubes[1].set_light_corners(*sevens)
		time.sleep(self.waittime)

	def show8(self):
		self.cubes[0].set_light_corners(*eights)
		self.cubes[1].set_light_corners(*eights)
		time.sleep(self.waittime)

	def show9(self):
		self.cubes[0].set_light_corners(*nine)
		self.cubes[1].set_light_corners(*nines)
		time.sleep(self.waittime)

	def show0(self):
		self.cubes[0].set_light_corners(*zero)
		self.cubes[1].set_light_corners(*zeros)
		time.sleep(self.waittime)

	def cubes_connected(self):
		cube1 = self.robot.world.get_light_cube(cozmo.objects.LightCube1Id)
		cube2 = self.robot.world.get_light_cube(cozmo.objects.LightCube2Id)
		cube3 = self.robot.world.get_light_cube(cozmo.objects.LightCube3Id)
		self.cubes = [cube1, cube2, cube3]
		return not (cube1 == None or cube2 == None or cube3 == None)

async def cozmo_program(robot: cozmo.robot.Robot):
	game = RUN(robot)
	game.run()

cozmo.run_program(cozmo_program)