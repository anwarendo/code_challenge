#!/usr/bin/python3

from typing import List

'''
A class of building with building number and distance to other buildings property.
The distances are listed from building 0 (the starting builing) to the last bilding
in ascending order. Starting from line 38 on wards, I included an example for how to use the
delivery route optimization function. In the example, the starting building (building 0)
has distances list [1000, 1200, 1700] that means the distance from building 0 to building 1
is 1000 units (meter or kilometer doesn't matter), the distance from building 0 to building 2
is 1200 units, and from building 0 to building 3 is 1700 units. The same goas for other buildings,
if the building of interest is building 1 the list would include [ 1 to 0, 1 to 2, 1 to 3], etc.
'''

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
        nearest_distance = float('inf') # start by making the nearest distance a very large number like infinity
        for building in buildings:
            if building not in visited and building.distances[current_building.bldg_num] < nearest_distance:
                nearest_neighbor = building
                nearest_distance = building.distances[current_building.bldg_num]
        visited.add(nearest_neighbor)
        route.append(nearest_neighbor)
        current_building = nearest_neighbor
    route.append(start)
    return route

# prepare example buildings
bldg0 = Building(0, [1000, 1200, 1700])
bldg1 = Building(1, [1000, 1400, 800])
bldg2 = Building(2, [1200, 1400, 900])
bldg3 = Building(3, [1700, 800, 900])

buildings = [bldg1, bldg2, bldg3]

optimized_route = delivery_route_optimization(buildings, bldg0)

# print the list of buildings to the console
for route in optimized_route:
    print(f'building number: {route.bldg_num}, distance to other buildings: {route.distances}')
    
# print the route in terms of building number only
print("\nRoute in terms of builing number:")
for route in optimized_route:
    print(route.bldg_num, end="   ")
    

