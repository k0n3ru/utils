#!/usr/bin/env python

"""

 { "node":[ { "id":** , "color":"red",.... },{ "id":yy , "color":"red",.... }],"edges":[{},{}...] }

"""


import sys
import json
import csv

def sigma_jsonify(fname):
  csvfile = open(fname,'rb')
  fieldnames = ("color","x","y")
  creader = csv.DictReader( csvfile, fieldnames)
  # make a list of nodes.We will add id,size later
  nodes = []
  id_counter = 1
  for row in creader:
    # add id,size to the nodes
    # TODO find the intersecting nodes may be change the size
    # and move this code to appropriate place
    row["id"] = ++id_counter
    row["size"] = 3 # default
    nodes.append(row)
  
  print nodes

def main():
  fname = sys.argv[1]
  sigma_jsonify(fname)

if __name__ == '__main__':
  main()