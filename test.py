import config
import json
import pickle
import os

with open(config.DATA_PATH,'r') as f:
        boston_data = json.load(f)

print(boston_data)


with open(config.MODEL_PATH,'rb') as f:
        boston_model = pickle.load(f)

print(boston_model)