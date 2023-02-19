# Code Challenge

## Question:

### Implement a route planning algorithm for a delivery company.

A delivery company has to deliver packages to several buildings in a city. Given the set of buildings and the distance between every pair of buildings, the problem is to find the shortest possible route that visits every building exactly once and returns to the starting building.

Implement a function that takes a list of buildings and a starting building and returns the shortest possible route to travel from the starting building to all the other buildings, visiting all the buildings exactly once and returning to the starting building.

```python
def delivery_route_optimization(buildings: List[Building], start: Building) -> List[Building]:
```


where:
- buildings is a list of buildings with the name and distance attributes.
- start is the starting building.

The function should return a list of buildings representing the optimized delivery route, starting and ending with the start building.

> Note: Assume that the distance between any two buildings is given and it is symmetrical (i.e., if there is a path from building A to building B with a distance of d, then there is a path from building B to building A with a distance of d).

### Submission Instructions
~~~
1  Code: you can write your solution in a preferred programming language and provide the full code.
2. Comments: The code should be well-commented and should explain the thought process and logic behind the solution.
3. Test Cases: provide test cases that demonstrate the correctness of their solution, including edge cases.
4  Time & Space Complexity Analysis: provide an analysis of the time and space complexity of their solution.
5. Document: Provide a document explaining the solution, how you approached the problem, and how you tested it.
6. Submission: You can upload the code to a code hosting platform (e.g., GitHub, GitLab, Bitbucket) and share the link.
~~~

## Answer:

This problem is a classic example of the Traveling Salesman Prblem (TSP), which is known to be NP-hard. There are several algorithms to solve the TSP, but for small problem sizes, it's possible to use brute force to find the optimal solution. However,as the number of buildings increases, the brute-force algorithm becomes impractical.

One heuristic approach that works well for medium-sized TSPs is the nearest neighbor algorithm. The algorithm starts at the starting building, selects the nearest unvisited building, and continues until all buildings have been visited. The route is then completed by returning to the starting building. This algorithm does not guarantee the optimal solution but can provide a good approximation.

Here's an implementation of the nearest neighbor algorithm for the delivery route optimization problem: [delivery_route_optimization.py](delivery_route_optimization.py)

The function takes a list of Building objects, each with a name and a distances list, which contains the distance to all other buildings in the list. The start parameter is a Building object representing the starting building.The function initializes an empty set called visited to keep track of the buildings that have been visited, an empty list called route to store the optimized delivery route, and a variable called current_building to keep track of the current building in the route.

The while loop continues until all buildings have been visited. At each iteration, the algorithm selects the nearest unvisited building to the current building and adds it to the route. The nearest neighbor is selected by iterating over all buildings, excluding the visited ones, and selecting the one with the smallest distance to the current building.

Finally, the starting building is added to the end of the route to complete the cycle.

The function returns the optimized delivery route as a list of Building objects.