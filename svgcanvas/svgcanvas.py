# Create shape objects to style and format
class Shape:
	def __init__(self, shape, **attributes):
		self.shape = shape
		self.attributes = attributes
		self.styles = {}

	# Create a keyword dictionary
	def style(self, **args):
		self.styles.update(args)
		return self

	
	# Create SVG format from shape
	def conv_svg(self):
		# Array for holding attributes and styles
		attrs = []

		# Append attributes (x, y, cx, cy) to attrs
		for key, value in self.attributes.items():
			attrs.append(f'{key}="{value}"')

		# Append styles to attrs
		for key, value in self.styles.items():
			attrs.append(f'{key}="{value}"')

		# Join attributes and styles into string
		attr_str = " ".join(attrs)

		# Return SVG format
		return f'<{self.shape} {attr_str}/>'



# Create an object for storing svg content
class svgCanvas():
	def __init__(self, height, width):
		# Create an object for drawing svg shapes
		self.height = height
		self.width = width
		# Array for storing svg items
		self.shapes = []

	# !!!!
	# Shape Template
	# def circle(self, cx, cy, r)
	#     circle = Shape("circle", cx=50, cy=50, r=10)
    #     self.shapes.append(circle)
	#     return circle


	# Line := x1, y1, x2, y2
	def line(self, x1, y1, x2, y2):
		line = Shape("line", x1=x1, y1=y1, x2=x2, y2=y2)
		self.shapes.append(line)
		return line


	# Rectangle := x, y, width, height
	def rect(self, x, y, width, height):
		rect = Shape("rect", x=x, y=y, width=width, height=height)
		self.shapes.append(rect)
		return rect


	# Circle := x, y, radius
	def circle(self, cx, cy, r):
		circle = Shape("circle", cx=cx, cy=cy, r=r)
		self.shapes.append(circle)
		return circle


	# Ellipse := x, y, radiusx, radiusy
	def ellipse(self, cx, cy, rx, ry):
		ellipse = Shape("ellipse", cx=cx, cy=cy, rx=rx, ry=ry)
		self.shapes.append(ellipse)
		return ellipse


    # Path := "M L C Z"
    def path(self, d):
        path = Shape("path", d=d)
        self.shapes.append(path)
        return path


	# Create XML content and write out file
	def save(self, filepath):
		# In order for most browsers to render, the SVG needs a header with w3 reference
		# SVG files are xml formatted, this is the first line
		xmlContent = f'<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">\n'

		# Add every shape from the shapes array to the xml file
		for shape in self.shapes:
			xmlContent += f'  {shape.conv_svg()}\n'
		xmlContent += '</svg>\n'

		# Save file out
		with open(filepath, 'w') as file:
			file.write(xmlContent)
