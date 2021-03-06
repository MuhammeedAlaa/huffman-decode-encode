# -- coding: utf-8 --
import heapq
import bitarray
from Node import Node


# read the file to be encoded
file = open("input.txt", "r")
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

if len(nodes) == 1:
    left = heapq.heappop(nodes)
    parent = Node(None, left.prob)
    parent.left = left
    heapq.heappush(nodes, parent) 

while len(nodes) != 1:
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
encoded = open("encode.bin", "wb")
encodedBinary = ''
for char in input:
    encodedBinary += codes[char]
padding = 8 - (len(encodedBinary) % 8)
padding = f'{padding:08b}'
encodedBinary = padding + encodedBinary
binary = bitarray.bitarray(encodedBinary)
encoded.write(binary)
encoded.close()

# opening file for write and open the encode file a decode in the decode file
file = open("encode.bin", "rb")
encodedReader = bitarray.bitarray()
encodedReader.fromfile(file)
decoded = open("decoded.txt", "w+")
padding = encodedReader[:8]
padding = int(padding.to01(), 2)
encodedReader = encodedReader[8: -1*padding]
currentCode = ''
for char in encodedReader:
    if char:
        currentCode += '1'
    else:
        currentCode += '0'
    if currentCode in inverseCode:
        decoded.write(inverseCode[currentCode])
        currentCode = ''


