#! /usr/bin/python3

import sys
import os.path
import numpy as np
np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)

print("\n----Python unconcealed computation start----\n")

datatype = int

# count players
player = 0
while os.path.isfile("Player-Data/Input-P" + str(player) +"-0"):
    player += 1

if player == 0:
    exit()

# count inputs
f = open("Player-Data/Input-P0-0", 'r')
size = len(f.readline().split())

inputs = np.zeros( (player, size), dtype=datatype)
# fill player inputs
player = 0
while os.path.isfile("Player-Data/Input-P" + str(player) +"-0"):
    f = open("Player-Data/Input-P" + str(player) +"-0", 'r')
    inputs[player] = np.array(f.readline().split())
    player += 1

result = inputs[0]
result = np.max(result, 0)

print([x for x in result])

print("\n----Python unconcealed computation stop----\n")