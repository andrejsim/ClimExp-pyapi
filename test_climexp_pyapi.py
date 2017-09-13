# Climate Explorer KNMI Python Binding
# author: Andrej
# python api
import json


inputfile = 'inputs_local.json'
with open(inputfile, 'r') as fp:
  inputs = json.load(fp)


# api call...
  
climexp_pyapi.correlfield(inputs)