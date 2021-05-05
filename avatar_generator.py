# BUILT-IN
import re
import random
# PIP
from cairosvg import svg2png
from xml.sax.saxutils import escape as xml_escape
COLORS = [
    ['#512da9', '#DF7FD7', '#591854'],
    ['#aa47bc', '#DF8A82', '#5E3A37'],
    ['#689f39', '#E05118', '#61230B'],
    ['#f5511e', '#E6CB97', '#614C23'],
    ['#00579c', '#492661', '#C59BE0'],
    ['#034d3c', '#141961', '#9B9FE0'],
    ['#606bc4', '#104F61', '#9BD1E0'],
    ['#00a291', '#0A6129', '#9BE0B3'],
    ['#ec407a', '#6B5621', '#E0AD2B'],
    ['#008cd8', '#E6CB97', '#614C23'],
    ['#ff3a3a', '#492661', '#C59BE0'],
    ['#af0000', '#141961', '#9B9FE0'],
]
INITIALS_SVG_TEMPLATE = """
<svg xmlns="http://www.w3.org/2000/svg" 
	pointer-events="none" 
	width="600" height="800">
  <defs>
    <linearGradient id="grad">
    <stop offset="0%" stop-color="{color1}" />
    <stop offset="100%" stop-color="{color2}" />
    </linearGradient>
  </defs>
  <rect width="600" height="800" style="fill:rgb(32,32,36);"/>
  <circle r="165" cx="300" cy="400" fill="url(#grad)"></circle>
  <text text-anchor="middle" y="50%" x="50%" dy="0.35em"
        pointer-events="auto" fill="{text_color}" font-family="sans-serif"
        style="font-weight: 400; font-size: 160px">{text}</text>
</svg>
""".strip()
INITIALS_SVG_TEMPLATE = re.sub('(\\s+|\\n)', ' ', INITIALS_SVG_TEMPLATE)
def get_png_avatar(text, output_file):
    random_color = random.choice(COLORS)
    svg_avatar = INITIALS_SVG_TEMPLATE.format(**{
        'color1': random_color[0],
        'color2': random_color[0],
        'text_color': '#FFFFFF',
        'text': text,
    }).replace('\\n', '')
    
    svg2png(svg_avatar, write_to=output_file)