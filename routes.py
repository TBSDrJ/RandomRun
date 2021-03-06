import networkx as nx
import random

map = nx.Graph()
map.add_nodes_from(range(1,36))
map.add_weighted_edges_from([
    (1,2,0.07),
    (2,2,0.15),
    (2,3,0.04),
    (2,4,0.06),
    (4,4,0.15),
    (3,6,0.03),
    (3,12,0.16),
    (11,11,0.06),
    (12,12,0.06),
    (6,11,0.05),
    (6,9,0.07),
    (9,14,0.05),
    (9,13,0.10),
    (14,20,0.05),
    (14,14,0.10),
    (13,10,0.06),
    (20,20,0.06),
    (19,19,0.06),
    (18,18,0.06),
    (20,19,0.06),
    (18,19,0.06),
    (17,18,0.04),
    (4,5,0.05),
    (5,7,0.05),
    (7,8,0.05),
    (8,10,0.05),
    (10,16,0.08),
    (10,15,0.05),
    (15,16,0.12),
    (15,17,0.05),
    (20,21,0.05),
    (21,22,0.05),
    (22,23,0.05),
    (23,24,0.13),
    (24,32,0.05),
    (32,33,0.13),
    (33,34,0.05),
    (5,30,0.22),
    (7,29,0.22),
    (8,28,0.22),
    (16,25,0.06),
    (25,25,0.04),
    (26,26,0.04),
    (26,27,0.05),
    (27,31,0.08),
    (17,31,0.23),
    (32,35,0.05),
    (35,33,0.18),
])

currentNode = 2
history = [1,2]
historyIndex = 0
stepNum = 0
totalDistance = 0
# targetDistance = int(input("Roughly how many miles do you want to go? "))
targetDistance = 4
minDistance = targetDistance * 0.75
while totalDistance < minDistance:
    possibleNodes = map[currentNode]
    choices = list(possibleNodes.keys())
    choices.remove(history[historyIndex])
    historyIndex += 1
    print(history[historyIndex], choices)
    currentNode = random.choice(choices)
    history.append(currentNode)
    # print(currentNode, possibleNodes[currentNode]['weight'])
    if currentNode == 1:
        break
