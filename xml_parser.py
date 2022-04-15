from xml.etree import ElementTree

colors = {
    'red': 0,
    'green': 0,
    'blue': 0}

xml_data = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube>' \
           '<cube color="red"></cube></cube>'
root = ElementTree.fromstring(xml_data)

if root.attrib['color'] in colors.keys():
    colors[root.attrib['color']] = 1


def getChildren(parent, level):
    level += 1
    for child in parent:
        child_color = child.attrib['color']
        if child_color in colors:
            colors[child_color] += level
        getChildren(child, level)


getChildren(root, 1)

for color in colors.values():
    print(color, end=' ')
