#!/usr/bin/python3

from typing import List

class Building:
    def __init__(self, name: str, distances: List[int]):
        self.name = name
        self.distances = distances

def delivery_route_optimization(buildings: List[Building], start: Building) -> List[Building]:
    visited = set([start])
    route = [start]
    current_building = start
    while len(visited) < len(buildings):
        nearest_neighbor = None
        nearest_distance = float('inf')
        for building in buildings:
            if building not in visited and building.distances[current_building.name] < nearest_distance:
                nearest_neighbor = building
                nearest_distance = building.distances[current_building.name]
        visited.add(nearest_neighbor)
        route.append(nearest_neighbor)
        current_building = nearest_neighbor
    route.append(start)
    return route
