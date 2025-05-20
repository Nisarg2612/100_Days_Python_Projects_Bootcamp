import colorgram

colors = colorgram.extract("painting.png", 10)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)

# extracted list of colors from the image
color_list = [(233, 233, 232), (231, 233, 236), (234, 230, 232), (224, 232, 226), (208, 160, 81), (55, 88, 130),
              (145, 91, 40), (140, 27, 48), (221, 207, 106), (133, 177, 203)]
