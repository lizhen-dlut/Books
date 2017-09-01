from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
drawing = svg2rlg("./electronical_idiogram.svg")
renderPDF.drawToFile(drawing, "file.pdf")
