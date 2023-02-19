#!/usr/bin/python3

from typing import List

class Building:
    def __init__(self, bldg_num: int, distances: List[int]):
        self.bldg_num = bldg_num
        self.distances = distances

def delivery_route_optimization(buildings: List[Building], start: Building) -> List[Building]:
    visited = set([start])
    route = [start]
    current_building = start
    while len(visited) < len(buildings):
        nearest_neighbor = None
        nearest_distance = float('inf')
        for building in buildings:
            if building not in visited and building.distances[current_building.bldg_num] < nearest_distance:
                nearest_neighbor = building
                nearest_distance = building.distances[current_building.bldg_num]
        visited.add(nearest_neighbor)
        route.append(nearest_neighbor)
        current_building = nearest_neighbor
    route.append(start)
    return route

bldA = Building(1, [1000, 1400, 800])
bldB = Building(2, [1200, 1400, 900])
bldC = Building(3, [1700, 800, 900])
bldStart = Building(0, [1000, 1200, 1700] )

buildings = [bldA, bldB, bldC]

optimized_route = delivery_route_optimization(buildings, bldStart)


for route in optimized_route:
    print(f'building number: {route.bldg_num}, distance to other buildings: {route.distances}')
    


