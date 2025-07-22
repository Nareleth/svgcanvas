# svgcanvas
A simple to use python library to generate SVG images files.  
No dependencies are required.  

## Example
```
import svgcanvas

# Create a Canvas object for writing
myCanvas = svgCanvas(400, 600)

# Create a shape object with required dimensions
# Add style to your shape object

circle1 = myCanvas.circle(50, 50, 10)
circle1.style(stroke="black", strokeWidth=2, fill="red")

rect1 = myCanvas.rect(100, 200, 100, 200)
rect1.style(stroke="blue", strokeWidth=3, fill="orange")	

line1 = myCanvas.line(50, 0, 50, 600)
line1.style(fill="green")

ellipse1 = myCanvas.ellipse(300, 200, 100, 30)
ellipse1.style(stroke="blue", fill="orange")


# Write your canvas to a file
myCanvas.save("coconut.svg")
```

## Installation
From Source:  
```foobar```

