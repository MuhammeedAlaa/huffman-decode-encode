# -*- coding: utf-8 -*-
import heapq

from Node import Node

# read the file to be encoded
file = open("test.txt", "r")
input = file.read()

# making a dictionary to store the frequency  
freq = {}
nodes = []

# calculate the frequency of each symobol in the file
for ch in input:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1  

# calculate the propability of each symbol and make a heap
for key in freq:
    heapq.heappush(nodes, Node(key, freq[key] / len(input) ))

# apply the huffman algorithm to make the tree where symbols are the leaves
while(len(nodes) != 1):
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    parent = Node(None, left.prob + right.prob)
    parent.left = left
    parent.right = right
    heapq.heappush(nodes, parent)    
inverseCode = {}
codes = {}
nodes[0].inorderTraversal(nodes[0], '', codes, inverseCode)
# writing codes to encoded file
encoded = open("encode.txt","w+")
for char in input:
    encoded.write(codes[char])
encoded.close()    
# opeing file for write and open the encode file a decode in the decode file
encodedReader = open("encode.txt","r+")
encodedReader = file.read()
decoded = open("decoded.txt","w+")
currentCode = ''
print(encodedReader)
for char in encodedReader:
    currentCode += char
    print(currentCode)
    if currentCode in inverseCode:
        decoded.write(inverseCode[currentCode])
        currentCode = ''