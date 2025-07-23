# svgcanvas
A simple to use python library to generate SVG images files.  

## Quick Start
```
from svgcanvas import svgCanvas

myCanvas = svgCanvas(400, 600)

# Add style to your shape object

circle = myCanvas.circle(50, 50, 10)
circle.style(stroke="black", strokeWidth=2, fill="red")

myCanvas.save("coconut.svg")
```

## Installation
From Source:  
1. Git Clone this repository:  
```$ git clone https://github.com/Nareleth/svgcanvas.git```
1. Change into this project directory:  
```$ cd svgcanvas```
1. Install package with pip:  
```$ pip install .```


## Usage
There are sample usage files in the *examples/* directory.  
The samples show files that use the api to generate svg images, showcasing the flexibility of its usage.
### Creating a Grid
```

```

## API Reference
### svgCanvas(height, width)  
Creates a canvas object with specified dimensions.  
#### Parameters:
- ```height```(int): Canvas height in int pixels.
- ```width```(int): Canvas width in int pixels.

### Shapes
#### canvas.line(x1, y1, x2, y2)
Creates a line from (x1,y1) to (x2,y2).
**Returns:** Line object with ```.style()``` method. Requires a **stroke** color to be displayed.

#### canvas.rect(x,y, width, height)
Creates a rectangle at position (x,y) with given width and height.  
**Returns:** Rectangle object with ```.style()``` method.

#### canvas.circle(cx,cy,r)
Creates a circle centered at (cx,cy) with radius r.
**Returns:** Circle object with ```.style()``` method.

#### canvas.ellipse(cx,cy,rx,ry)
Creates an ellipse centered at (cx,cy) with x-radius rx and r-radius ry.
**Returns:** Ellipse object with ```.style()``` method.

### Style
All shape objects have a ```.style()``` method that access CSS properties:
- ```fill```- Fill color(color name, hex, rgb)
- ```stroke```- Stroke color (color, name, hex, rgb)
- ```stroke_width```- Stroke thickness (pixels)
- ```opacity```- Transparency (0.0 to 1.0)
- ```stroke_dasharray```- Dash patterns for strokes
- ```fill_opacity```- Fill transparency
- ```stroke_opacity```- Stroke transparency

### Save
**canvas.save(filename)**  
Writes xml formatted lines to an svg file.
#### Parameters:
- ```filename```(str): Output file path(should end with .svg)

## Requirements
- Python3.6+
- There are no dependencies required to install or use this package..  

## License
No License.

## Contributing
Not accepting pull requests, but comments and feedback are welcome.
