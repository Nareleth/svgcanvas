from svgcanvas import svgCanvas

# Declare the outfile for saving
outfile = "coconut.svg"

# Declare the canvas height and width (useful for the grid)
cHeight = 400
cWidth = 600

# Create a canvas object with declared height and width
canvas = svgCanvas(cHeight, cWidth)

# Grid

# Set a cell size for the grid
cellSize = 100


# Create initial rows of the Grid using the cell size and length of the canvas
for x in range(0, cWidth, cellSize):
	# Iterate through the rows and create columns for the grid using the height of the canvas
    for y in range(0, cHeight, cellSize):

		# Create dynamic objects for the Column lines 
        gridYIndex = canvas.line(0, f"{y}", cHeight, f"{y}")
        gridYIndex.style(stroke="grey")

	# Create dynamic objects for the Row lines
    gridXIndex = canvas.line(f"{x}", 0, f"{x}", cWidth)
    gridXIndex.style(stroke="grey")

# Write a file "coconut.svg" This is our svg file that is browser ready for rendering
canvas.save(outfile)
print(f"Wrote file: ", outfile)

