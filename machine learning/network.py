from xml.etree.ElementTree import Element, ElementTree, dump


def specify_nodes(length):
        # one of the elements net_params will need is a "radius" value
        r = length

        # specify the name and position (x,y) of each node
        nodes = [{"id": "LU", "x": -r,  "y": +r},  # 1
                 {"id": "RU",  "x": +r,  "y": +r},  # 2
                 {"id": "LD",    "x": -r,  "y": -r},  # 3
                 {"id": "RD",   "x": +r, "y": -r},  # 4
                 {"id": "CL",   "x": -r, "y": 0},  # 5
                 {"id": "CR",   "x": +r, "y": 0},  # 6
                 {"id": "CU",   "x": 0, "y": r},  # 7
                 {"id": "CD",   "x": 0, "y": -r},  # 8
                 {"id": "IT",   "x": 0, "y": 0}]  # 9
        return nodes

Nodes = specify_nodes(100)
root = Element("nodes")

for i in Nodes:
    Node1 = Element("node")
    for j in i.items():
        Node1.attrib[j[0]] = str(j[1])
    root.append(Node1)

ElementTree(root).write("node1.xml")

def specify_edges(length, lanes, speed_limit):
        
        edgelen = length
        # this will let us control the number of lanes in the network
        lanes = lanes
        # speed limit of vehicles in the network
        speed_limit = speed_limit
        # L: left, R: right, U: Up D:Down
        edges = [
            {
                "id": "edge0",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "LU",
                "to": "CL",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(-pi/2, 0, 40)]
            },
            {
                "id": "edge1",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CL",
                "to": "LD",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(0, pi/2, 40)]
            },
            {
                "id": "edge2",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "LD",
                "to": "CD",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi/2, pi, 40)]
            },
            {
                "id": "edge3",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CD",
                "to": "RD",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge4",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "RD",
                "to": "CR",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(-pi/2, 0, 40)]
            },
            {
                "id": "edge5",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CR",
                "to": "RU",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(0, pi/2, 40)]
            },
            {
                "id": "edge6",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "RU",
                "to": "CU",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi/2, pi, 40)]
            },
            {
                "id": "edge7",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CU",
                "to": "LU",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge8",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "LU",
                "to": "CU",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge9",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CU",
                "to": "RU",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge10",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "RU",
                "to": "CR",
                "length": 2*edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge11",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CR",
                "to": "RD",
                "length": 2*edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge12",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "RD",
                "to": "CD",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge13",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CD",
                "to": "LD",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge14",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "LD",
                "to": "CL",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge15",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CL",
                "to": "LU",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge16",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CL",
                "to": "IT",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge17",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CR",
                "to": "IT",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge18",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CD",
                "to": "IT",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge19",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "CU",
                "to": "IT",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge20",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "IT",
                "to": "CR",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge21",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "IT",
                "to": "CL",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge22",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "IT",
                "to": "CU",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            },
            {
                "id": "edge23",
                "numLanes": lanes,
                "speed": speed_limit,
                "from": "IT",
                "to": "CD",
                "length": edgelen,
                # "shape": [(r*cos(t), r*sin(t)) for t in linspace(pi, 3*pi/2, 40)]
            }

        ]
        return edges

import numpy as np
root = Element("edges")
edges = specify_edges(50,2,20)
for i in edges:
    edge1 = Element("edge")
    for j in i.items():
        edge1.attrib[j[0]] = str(j[1])
    root.append(edge1)


ElementTree(root).write("edge1.xml")


types = Element("types")
type = Element("type", {"id" : "edgeType", "numLanes" : "2", "speed" : "36.1"})
types.append(type)

ElementTree(types).write("types.xml")

def specify_type(numlanes, speed):
    numlane = numlanes
    speed = speed
    type = [
        {
        "id" : "edgyType",
        "numLanes" : numlane,
        "speed" : speed
        }
    ]
    return type

root  = Element("types")
types = specify_type(2, 20)
for i in types:
    type1 = Element("type")
    for j in i.items():
        type1.attrib[j[0]] = str(j[1])
    root.append(type1)


ElementTree(root).write("type1.xml")

# netconvert -n node1.xml -e edge1.xml -t type1.xml -o circular.net.xml
# sumo-gui -n circular.net.xml



