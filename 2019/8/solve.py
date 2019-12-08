data, = [line for line in open('input.txt')]
data = [int(x) for x in data]

width = 25
height = 6

def fetch_layers(data):
    pixels = width * height

    rest = data
    layers = []
    while True:
        layer, rest = rest[:pixels], rest[pixels:]
        layers.append(layer)
        if len(rest) == 0:
            return layers
    return layers

layers = fetch_layers(data) 

# part 1
# results = {}
# lowest = 999999
# for layer in layers:
#     lowest = min(lowest, layer.count(0))
#     if layer.count(0) < lowest:
#         lowest = layer.count(0)

#     results[layer.count(0)] = layer.count(1) * layer.count(2)
# from pprint import pprint
# pprint(results)

# part 2
image = []
for x in range(width*height):
    image.append(2)

# Color layer by layer. 2 transparent, 1 white, 0 black
for pos in range(width*height):
    for layer in layers:
        new = layer[pos]
        # ignore transparent
        if new == 2:
            continue

        current = image[pos]
        # if current already has color then ignore it!
        if current != 2:
            continue
        
        image[pos] = new

# Print the image
for y in range(height):
    for x in range(width):
        pixel = image[(y*width) + x]
        if pixel == 1:
            pixel = "X"
        else:
            pixel = ' '
        print(pixel, end="")
    print()