from xml.etree.ElementTree import Element, ElementTree, dump

root = Element("nodes")

node1 = Element("node", {"id" : "bottom-left", "x" : "0", "y" : "0"})
root.append(node1)
node2 = Element("node", {"id" : "bottom-right", "x" : "1250", "y" : "0"})
root.append(node2)
node3 = Element("node", {"id" : "top-right", "x" : "1250", "y" : "1250"})
root.append(node3)
node4 = Element("node", {"id" : "top-left", "x" : "0", "y" : "1250"})
root.append(node4)

ElementTree(root).write("node.xml")
#################################################

types = Element("types")
type = Element("type", {"id" : "edgeType", "numLanes" : "2", "speed" : "36.1"})
types.append(type)

ElementTree(types).write("types.xml")
#####################################################
edges = Element("edges")
edge1 = Element("edge", {"from" : "bottom-left", "id" : "bottom", "to" : "bottom-right", "type" : "edgetype"})
edges.append(edge1)
edge2 = Element("edge", {"from" : "bottom-right", "id" : "right", "to" : "top-right", "type" : "edgetype"})
edges.append(edge2)
edge3 = Element("edge", {"from" : "top-right", "id" : "top", "to" : "top-left", "type": "edgetype"})
edges.append(edge3)
edge4 = Element("edge", {"from" : "top-left", "id" : "left", "to" : "bottom-left", "type": "edgetype"})
edges.append(edge4)

ElementTree(edges).write("edges.xml")
###################################################
# <?xml version="1.0" encoding="UTF-8"?>
# XMLV = Element("?xml", {"version" : "1.0", "encoding" : "UTF-8"})


Configuration = Element("configuration")
input  =Element("input")
Configuration.append(input)
node_files = Element("node-files", value = "node.xml")
edge_files = Element("edge-files", value = "edges.xml")
type_files = Element("type-files", value = "types.xml")
input.append(node_files)
input.append(edge_files)
input.append(type_files)

output = Element("output")
output_file = Element("ouput-file", value = "circular.net.xml")
output.append(output_file)
Configuration.append(output)

processing = Element("processing")
no_internal_links = Element("no-internal-links", value = "ture")
processing.append(no_internal_links)
no_turnarounds = Element("no-turnarounds", value = "true")
processing.append(no_internal_links)

Configuration.append(processing)
ElementTree(Configuration).write("circular.net.xml")




