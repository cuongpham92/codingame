import sys
import math

recursive_mode = False

class Person:
    def __init__(self, data):
        self.name = data[0]
        self.parent = data[1]
        self.birth = data[2]
        self.alive = (data[3] == "-")
        self.religion = data[4]
        self.gender = not (data[5] == "M")
        self.children = []
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
        
    def get_children(self, royal_family):
        for p in royal_family:
            if p.parent == self.name:
                self.children.append(p)
        if recursive_mode:
            self.children.sort(key = lambda p : (p.gender, p.birth))
        else:
            self.children.sort(key = lambda p : p.birth, reverse=True)
            self.children.sort(key = lambda p : p.gender, reverse=True)
        
    def make_succession(self):
        succession = [self]
        for c in self.children:
            succession.extend(c.make_succession())
        return succession
        
n = int(input())
family = []
for i in range(n):
    person = Person(input().split())
    family.append(person)

for p in family:
    p.get_children(family)
    if p.parent == "-":
        queen = p

def dfs(start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            for c in vertex.children:
                if c not in visited:
                    stack.append(c)
    return visited

if recursive_mode:
    for p in queen.make_succession():
        if p.alive and p.religion == "Anglican":
            print(p.name)
else:
    for p in dfs(queen):
        if p.alive and p.religion == "Anglican":
            print(p.name)


