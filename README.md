# Code Challenge

## Implement a route planning algorithm for a delivery company.

A delivery company has to deliver packages to several buildings in a city. Given the set of buildings and the distance between every pair of buildings, the problem is to find the shortest possible route that visits every building exactly once and returns to the starting building.

Implement a function that takes a list of buildings and a starting building and returns the shortest possible route to travel from the starting building to all the other buildings, visiting all the buildings exactly once and returning to the starting building.

``` def delivery_route_optimization(buildings: List[Building], start: Building) -> List[Building]: ```


where:
- buildings is a list of buildings with the name and distance attributes.
- start is the starting building.

The function should return a list of buildings representing the optimized delivery route, starting and ending with the start building.

> Note: Assume that the distance between any two buildings is given and it is symmetrical (i.e., if there is a path from building A to building B with a distance of d, then there is a path from building B to building A with a distance of d).

## Submission Instructions

1  Code: you can write your solution in a preferred programming language and provide the full code.
2. Comments: The code should be well-commented and should explain the thought process and logic behind the solution.
3. Test Cases: provide test cases that demonstrate the correctness of their solution, including edge cases.
4  Time & Space Complexity Analysis: provide an analysis of the time and space complexity of their solution.
5. Document: Provide a document explaining the solution, how you approached the problem, and how you tested it.
6. Submission: You can upload the code to a code hosting platform (e.g., GitHub, GitLab, Bitbucket) and share the link.
