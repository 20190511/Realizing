#1523 #1609 combination 구현 전
#https://www.acmicpc.net/problem/15686
from itertools import combinations
def findChicken(maps):
  size = len(maps)
  chicken = []
  house = []
  for i in range(size):
    for j in range(size):
      if maps[i][j] == 2:
        chicken.append([i+1, j+1])
      if maps[i][j] == 1:
        house.append([i+1, j+1])
  return house, chicken

def countPath(house, chicken):
  xpath = house[0] - chicken[0]
  ypath = house[1] - chicken[1]
  if xpath < 0:
    xpath = -xpath
  if ypath <0 :
    ypath = -ypath
  sums = xpath + ypath
  return sums

def sumS(l):
  sums = 0
  for i in l:
    sums += i
  return sums

"""
def comb (chicken, maxs):
  pivot = [i for i in range(1, maxs+1)]
  while True:
    if pivot[len(pivot)-1] == len(chicken) and 
"""
  
size, maxs = map(int, input().split())
maps = [[0]*size for _ in range(size)]
for i in range(size):
  maps[i] = list(map(int, input().split()))

house = []
chicken = []
house, chicken = findChicken(maps)

resultL = []
comb = list(combinations(chicken,maxs))
for i in range (len(comb)):
  ls = []
  for c in range(len(house)):
    small = []
    for h in range(maxs):
      small.append(countPath(house[c],comb[i][h]))
    val = min(small)
    ls.append(val)
  resultL.append(sumS(ls))

result = min(resultL)
print(result)

