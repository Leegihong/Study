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
edge1 = Element("edge", {"from" : "bottom-left", "id" : "bottom", "to" : "bottom-right", "type" : "edgeType"})
edges.append(edge1)
edge2 = Element("edge", {"from" : "bottom-right", "id" : "right", "to" : "top-right", "type" : "edgeType"})
edges.append(edge2)
edge3 = Element("edge", {"from" : "top-right", "id" : "top", "to" : "top-left", "type": "edgeType"})
edges.append(edge3)
edge4 = Element("edge", {"from" : "top-left", "id" : "left", "to" : "bottom-left", "type": "edgeType"})
edges.append(edge4)

ElementTree(edges).write("edges.xml")
###################################################
# <?xml version="1.0" encoding="UTF-8"?>
# XMLV = Element("?xml", {"version" : "1.0", "encoding" : "UTF-8"})


# Configuration = Element("configuration")
# input  =Element("input")
# Configuration.append(input)
# node_files = Element("node-files", value = "node.xml")
# edge_files = Element("edge-files", value = "edges.xml")
# type_files = Element("type-files", value = "types.xml")
# input.append(node_files)
# input.append(edge_files)
# input.append(type_files)

# output = Element("output")
# output_file = Element("ouput-file", value = "circular.net.xml")
# output.append(output_file)
# Configuration.append(output)

# processing = Element("processing")
# no_internal_links = Element("no-internal-links", value = "true")
# processing.append(no_internal_links)
# no_turnarounds = Element("no-turnarounds", value = "true")
# processing.append(no_turnarounds)

# Configuration.append(processing)
# ElementTree(Configuration).write("circular.net.xml")

#################################################
routes = Element("routes")
vtype1 = Element("vType", {"accel" : "1.5", "decel" :"4.5" ,"id" :"car", "length":"5" ,"maxSpeed":"36.1"})
routes.append(vtype1)
vtype2 = Element("vType", {"accel" : "0.4", "decel" :"4.5" ,"id" :"truck", "length":"12" ,"maxSpeed":"22.2"})
routes.append(vtype2)

route1 = Element("route", {"id" : "routeRight", "edges" : "bottom right top left"})
routes.append(route1)
route2 = Element("route", {"id" : "routeLeft", "edges" : "top left bottom right"})
routes.append(route2)
route3 = Element("route", {"id" : "routeTop", "edges" : "left bottom right top"})
routes.append(route3)
route4 = Element("route", {"id" : "routeBottom", "edges" : "bottom right top left"})
routes.append(route4)

flow1 = Element("flow", {"begin" :"0", "departPos" : "free", "id":"carRight", "period" : "1", "number":"70", "route" :"routeRight", "type":"car"})
routes.append(flow1)
flow2 = Element("flow", {"begin" :"0", "departPos" : "free", "id":"carTop", "period" : "1", "number":"70", "route" :"routeTop", "type":"car"})
routes.append(flow2)
flow3 = Element("flow", {"begin" :"0", "departPos" : "free", "id":"carLeft", "period" : "1", "number":"70", "route" :"routeLeft", "type":"car"})
routes.append(flow3)
flow4 = Element("flow", {"begin" :"0", "departPos" : "free", "id":"carBottom", "period" : "1", "number":"70", "route" :"routeBottom", "type":"car"})
routes.append(flow4)
flow5 = Element("flow", {"begin" :"0", "departPos" : "free", "id":"truckRight", "period" : "1", "number":"30", "route" :"routeRight", "type":"truck"})
routes.append(flow5)
flow6 = Element("flow", {"begin" :"0", "departPos" : "free", "id":"truckTop", "period" : "1", "number":"30", "route" :"routeTop", "type":"truck"})
routes.append(flow6)
flow7 = Element("flow", {"begin" :"0", "departPos" : "free", "id":"truckLeft", "period" : "1", "number":"30", "route" :"routeLeft", "type":"truck"})
routes.append(flow7)
flow8 = Element("flow", {"begin" :"0", "departPos" : "free", "id":"truckBottom", "period" : "1", "number":"30", "route" :"routeBottom", "type":"truck"})
routes.append(flow8)

ElementTree(routes).write("circular.rou.xml")

############################################################
rerouters = Element("additional")
route1 = Element("route", {"id" : "routeRight", "edges" : "bottom right top left"})
rerouters.append(route1)
route2 = Element("route", {"id" : "routeLeft", "edges" : "top left bottom right"})
rerouters.append(route2)
route3 = Element("route", {"id" : "routeTop", "edges" : "left bottom right top"})
rerouters.append(route3)
route4 = Element("route", {"id" : "routeBottom", "edges" : "bottom right top left"})
rerouters.append(route4)

rerouter1 = Element("rerouter", {"id" : "rerouterBottom", "edges": "bottom"})
interval1 = Element("interval", {"begin" : "0", "end": "100000"})
routeprobReroute1 = Element("routeProbReroute", {"id" : "routeRight"})
interval1.append(routeprobReroute1)
rerouter1.append(interval1)
rerouters.append(rerouter1)

rerouter2 = Element("rerouter", {"id" : "rerouterTop", "edges": "top"})
interval2 = Element("interval", {"begin" : "0", "end": "100000"})
routeprobReroute2 = Element("routeProbReroute", {"id" : "routeLeft"})
interval2.append(routeprobReroute2)
rerouter2.append(interval2)
rerouters.append(rerouter2)

ElementTree(rerouters).write("circular.add.xml")

########################################################
# configuration = Element("configuration")
# input = Element("input")
# net_file = Element("net-file", {"value" : "circular.net.xml"})
# input.append(net_file)
# route_file = Element("route-files", {"value" : "circular.rou.xml"})
# input.append(route_file)
# add_file = Element("additional-files", {"values" : "circular.add.xml"})
# input.append(add_file)
# configuration.append(input)

# output = Element("output")
# netstate = Element("netstate-dump", {"value" : "dump.xml"})
# output.append(netstate)
# configuration.append(output)

# time = Element("time")
# begin = Element("begin", {"value" : "0"})
# time.append(begin)
# end = Element("end", {"value": "10000"})
# time.append(end)
# configuration.append(time)

# ElementTree(configuration).write("dump.xml")

