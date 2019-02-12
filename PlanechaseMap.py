import os
from PIL import Image
import random

class Map():

	def __init__(self):

		self.image_height = 210
		self.image_width = 300

		self.image_paths = ["static/images/" + filename for filename in os.listdir(os.path.join(os.getcwd(), 'static/images')) if filename.endswith('.png')]
		self.image_paths.remove("static/images/empty.png")
		self.image_paths.remove("static/images/x_spot.png")
		self.image_paths.remove("static/images/map.png")
		self.unused_planes = self.image_paths

		self.height = 20
		self.width = 20
		self.plane_matrix = [["static/images/empty.png" for i in range(self.width)] for j in range(self.height)]

		self.x = self.height//2
		self.y = self.width//2

		# populate current plane
		self.populate(self.x, self.y)

		# populate adjacent planes
		self.populate(self.x+1, self.y)
		self.populate(self.x-1, self.y)
		self.populate(self.x, self.y+1)
		self.populate(self.x, self.y-1)

	def populate(self,x,y):
		if x < self.height and y < self.width:
			if self.plane_matrix[x][y] == "static/images/empty.png":
				self.plane_matrix[x][y] = self.get_random_plane()
		else:
			raise Exception

	def get_random_plane(self):

		if len(self.unused_planes) > 0:

			random_index = random.randint(0,len(self.unused_planes) - 1)
			random_plane = self.unused_planes.pop(random_index)

			return random_plane

		else:
			raise Exception

	def moveup(self):

		if self.x - 2 < 0:
			raise Exception

		else:
			self.x -= 1
			self.populate(self.x-1, self.y)
			self.populate(self.x, self.y-1)
			self.populate(self.x, self.y+1)

	def movedown(self):

		if self.x + 2 > self.height:
			raise Exception

		else:
			self.x += 1
			self.populate(self.x+1, self.y)
			self.populate(self.x, self.y-1)
			self.populate(self.x, self.y+1)

	def moveleft(self):

		if self.y - 2 < 0:
			raise Exception

		else:
			self.y -= 1
			self.populate(self.x, self.y-1)
			self.populate(self.x-1, self.y)
			self.populate(self.x+1, self.y)

	def moveright(self):

		if self.y + 2 > self.width:
			raise Exception

		else:
			self.y += 1
			self.populate(self.x, self.y+1)
			self.populate(self.x-1, self.y)
			self.populate(self.x+1, self.y)

	def generate_map_image(self):

		new_im = Image.new('RGB', (5 * self.image_width, 5 * self.image_height))

		for row in range(self.x - 2, self.x + 3):
			for col in range(self.y - 2, self.y + 3):
				sub_image = Image.open(self.plane_matrix[row][col])
				new_im.paste(sub_image, ((col - self.y + 2) * self.image_width, (row - self.x + 2) * self.image_height))

		x_spot = Image.open("static/images/x_spot.png")
		new_im.paste(x_spot, (2 * self.image_width, 2 * self.image_height), x_spot)

		new_im.save("static/images/map.png")






if __name__ == "__main__":

	myMap = Map()

	myMap.generate_map_image()


