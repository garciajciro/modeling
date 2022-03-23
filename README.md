# Emergency Facility Location Problem: Rio Rancho

## Why are this problem?
* In this model we are attempting to find the optimal location to place two emergency locations in order to minimize
travel time for emergency vehicles. We were given a map of the town that shows which streets can be driven on,
which areas are blocked by obstacles, and where incidents occurred most often in the past. This model is useful
for cities and towns to use if they need to place new emergency facilities in the future,

## Code:

* We decided to implement Dijkstra's algorithm (https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/) to find the distance from all of the sources in the map to all of the other nodes. From here we decided to see their average distance and the maximum distance.

## How to use code:

* Make sure to have a .txt file named "AdjList_emergency_Facilities (1).txt" that contains an adjacency list of the map. Make sure this is in the same folder as in the main.py code.
* When you have the adjacency list ready make sure that in line 66 where g = Graph(66) the 66 is changed to the number of rows in that .txt file.
* When you run the code, it will create an outputSources file containing all of the distances from every single source in the list.
* If you're going to re-run the code make sure to delete the "outputSources" file, if not the information would just be added on to the previous data.
