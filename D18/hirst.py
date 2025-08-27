import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('colors.jpg', 40)

collection=[]
count=0
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    collection.append((r,g,b))
    count+=1

print(collection)
print(count)

