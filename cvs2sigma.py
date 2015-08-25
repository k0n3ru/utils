#!/usr/bin/env python

"""

 { "node":[ { "id":** , "color":"red",.... },{ "id":yy , "color":"red",.... }],"edges":[{},{}...] }

"""


import sys
import json
import csv

def find_next_node_id(nodes,source):
  for node in nodes:
    #print node,' vs ',source
    if node['color'] == source['color'] and int(node["line_id"]) == int(source["line_id"])+1 :
      return node["id"]
  
  
  
def gen_edges(nodes):
  # for each node map its edge
  # { "id":XX,"source":id,"target":id }]
  edges = []
  edge_id = 1
  for node in nodes:
    next_node = find_next_node_id(nodes,node)
    if next_node:
      edges.append({'id':str(edge_id),'source':str(node['id']),'target':str(next_node) })
      edge_id = edge_id +1

  return edges

def sigma_jsonify(fname):
  csvfile = open(fname,'rb')
  fieldnames = ("color","line_id","x","y")
  creader = csv.DictReader( csvfile, fieldnames)
  # make a list of nodes.We will add id,size later
  nodes = []
  id_counter = 1
  for row in creader:
    # add id,size to the nodes
    # TODO find the intersecting nodes may be change the size
    # and move this code to appropriate place
    row["id"] = str(id_counter)
    row["size"] = 0.1 # default
    row["label"] = "lbl"+str(id_counter)
    row["x"] = float(row["x"])
    row["y"] = float(row["y"])
    row["line_id"] = int(row["line_id"])
    nodes.append(row)
    id_counter = id_counter+1
  
  edges = gen_edges(nodes)
  
  #print nodes
  #print edges
  
  print json.dumps({"nodes":nodes,"edges":edges},indent=2)

def main():
  fname = sys.argv[1]
  sigma_jsonify(fname)

if __name__ == '__main__':
  main()