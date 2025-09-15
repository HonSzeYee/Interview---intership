from math import inf

class MinHeap:
    def __init__(self, size):
        """
            Function description: Initialize a MinHeap.
            Approach description: Used for the Dijkstra algorithm.

            :Input: The size of the MinHeap.

            :Output, return or postcondition: No return value, construct an instance of MinHeap.

            :Time complexity:
                Best case: O(1)
                Worst case: O(1)
            :Time complexity analysis:
                Both best and worst case involve only attribute assignments.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(size)
            :Space complexity analysis: The array occupies the space of size+1 element.
        """
        self.length = 0
        self.size = size + 1
        self.the_array = [None] * self.size

    def __len__(self):
        """
            Function description: Return the current number of elements of the MinHeap.
            Approach description: Directly return self.length.

            :Output, return or postcondition: the number of elements of the MinHeap.

            :Time complexity:
                Best case: O(1)
                Worst case: O(1)
            :Time complexity analysis:
                Accessing a single attribute is constant time in all cases.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(1)
            :Space complexity analysis: No additional space used.
        """
        return self.length

    def is_full(self):
        """
            Function description: Check if the MinHeap is full.
            Approach description: Compare the length with the size of the MinHeap.

            :Output, return or postcondition: True if the MinHeap is full, False otherwise.

            :Time complexity:
                Best case: O(1)
                Worst case: O(1)
            :Time complexity analysis:
                Comparison of integer attributes only.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(1)
            :Space complexity analysis: No additional space used.
        """
        return self.length + 1 == len(self.the_array)

    def rise(self, k):
        """
            Function description: Rise the element at position k to its correct position.
            Approach description: Compare and swap the element at position k and its parent.

            :Input: k: the position of the element to be risen.

            :Time complexity:
                Best case: O(1)
                Worst case: O(log N)
            :Time complexity analysis:
                Best case when the element is already in heap order at position k so no swaps;
                worst case when it travels from a leaf up to the root, performing up to O(log N) swaps.
            :Space complexity:
            Input: O(1)
            Auxiliary: O(1)
            :Space complexity analysis: No additional space used.
        """
        while k > 1 and (self.the_array[k][2] < self.the_array[k // 2][2] or
                (self.the_array[k][2] == self.the_array[k // 2][2] and self.the_array[k][1] < self.the_array[k // 2][1])):
            self.swap(k, k // 2)
            k = k // 2

    def add(self, element):
        """
            Function description: Add new elements to the heap and maintain the heap properties.
            Approach description: Place the element at the end of the array and then perform rise to float up.

            :Input: element: (node, time, cost)

            :Output, return or postcondition: has_space_left: True if there is still space left in the heap, False otherwise.

            :Time complexity:
                Best case: O(1)
                Worst case: O(log N)
            :Time complexity analysis:
                Best case when heap is full or new element does not need to rise;
                worst case when rise must travel up O(log N) levels.
            :Space complexity:
            Input: O(1)
            Auxiliary: O(1)
            :Space complexity analysis: No additional space used beyond the heap array.
        """
        has_space_left = not self.is_full()
        if has_space_left:
            self.length += 1
            self.the_array[self.length] = element
            element[0].position = self.length
            self.rise(self.length)
        return has_space_left

    def smallest_child(self, k):
        """
            Function description: Return the index of the child node with the smaller value among the two child nodes of index k.
            Approach description: Compare the (cost, time) sequence of the left and right child nodes.

            :Input: k: index of the parent node.

            :Output, return or postcondition: index of the child node with the smaller value.

            :Time complexity:
                Best case: O(1)
                Worst case: O(1)
            :Time complexity analysis:
                Only constant number of comparisons are performed.
            :Space complexity:
            Input: O(1)
            Auxiliary: O(1)
            :Space complexity analysis: No additional space used.
        """
        if 2 * k == self.length:
            return 2 * k

        if (self.the_array[2 * k][2] < self.the_array[2 * k + 1][2]) or \
                (self.the_array[2 * k][2] == self.the_array[2 * k + 1][2] and self.the_array[2 * k][1] < self.the_array[2 * k + 1][1]):
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k):
        """
            Function description: Perform a sinking operation on the element at index k to maintain the minimum heap property.
            Approach description: Swap the current node with the smallest child node until the heap order is restored.

            :Input: k: index of element k.

            :Time complexity:
                Best case: O(1)
                Worst case: O(log N)
            :Time complexity analysis:
                Best case when element is already smaller than both children;
                worst case when it travels down O(log N) levels.
            :Space complexity:
            Input: O(1)
            Auxiliary: O(1)
            :Space complexity analysis: No additional space used.
        """
        while 2 * k <= self.length:
            child = self.smallest_child(k)
            if (self.the_array[k][2] < self.the_array[child][2]) or \
                    (self.the_array[k][2] == self.the_array[child][2] and self.the_array[k][1] < self.the_array[child][1]):
                break
            self.swap(k, child)
            k = child

    def swap(self, node_i, node_j):
        """
            Function description: Swap two elements at indices i and j, and update their position attributes.
            Approach description: After swapping the positions in the array, correct the node.position of both elements.

            :Input: node_i: index of the first element; node_j: index of the second element.

            :Time complexity:
                Best case: O(1)
                Worst case: O(1)
            :Time complexity analysis:
                A fixed number of assignments.
            :Space complexity: O(1).
            :Space complexity analysis: No additional space used.
        """
        self.the_array[node_i], self.the_array[node_j] = self.the_array[node_j], self.the_array[node_i]
        self.the_array[node_i][0].position = node_i
        self.the_array[node_j][0].position = node_j

    def get_min(self):
        """
            Function description: Return and remove the minimum element of the heap.
            Approach description: Replace root with last element and perform sink.

            :Output, return or postcondition: The minimum element (vertex, time, cost).

            :Time complexity:
                Best case: O(1)
                Worst case: O(log N)
            :Time complexity analysis:
                Best case when heap has size 1 or replaced element already satisfies heap property;
                worst case requires sinking down O(log N) levels.
            :Space complexity:
            Input: O(1)
            Auxiliary: O(1)
            :Space complexity analysis: No additional space used.
        """
        minimum = self.the_array[1]
        self.the_array[1] = self.the_array[self.length]
        if self.length > 1:
            self.the_array[1][0].position = 1
        self.length -= 1
        self.sink(1)
        return minimum

    def update(self, vertex, new_time, new_cost):
        """
            Function description: Decrease the key of an existing node to (new_time, new_cost) and adjust heap.
            Approach description: Compare new and old values to determine whether to rise or sink.

            :Input: vertex: the node to be updated; new_time: the new time; new_cost: the new cost.

            :Time complexity:
                Best case: O(1)
                Worst case: O(log N)
            :Time complexity analysis:
                Best case when no movement needed; worst case when rise or sink travels O(log N).
            :Space complexity:
            Input: O(1)
            Auxiliary: O(1)
            :Space complexity analysis: No additional space used.
        """
        k = vertex.position
        pre_time, pre_cost = self.the_array[k][1], self.the_array[k][2]
        self.the_array[k] = (vertex, new_time, new_cost)
        if new_cost < pre_cost or (new_cost == pre_cost and new_time < pre_time):
            self.rise(k)
        else:
            self.sink(k)

class Edge:
    def __init__(self, target_vertex, weight):
        """
            Function description: Represent a directed edge with cost and time weight.
            Approach description: Store target vertex and weight.

            :Input: target_vertex: Node or Vertex; weight: cost, time.

            :Time complexity:
                Best case: O(1)
                Worst case: O(1)
            :Time complexity analysis:
                Attribute assignments only.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(1)
            :Space complexity analysis: References to existing objects.
        """
        self.target_vertex = target_vertex
        self.weight = weight  # (cost, time)

class Vertex:
    def __init__(self, ori_vertex_id):
        """
            Function description: Represent a static location node in the original graph.
            Approach description: Store ID and initialize station flag and edge list.

            :Input: ori_vertex_id, original graph vertex id.

            :Time complexity:
                Best case: O(1)
                Worst case: O(1)
            :Time complexity analysis:
                Attribute assignments only.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(1)
            :Space complexity analysis: Empty edge list.
        """
        self.id = ori_vertex_id
        self.is_station = False
        self.visited = False
        self.edges = []

class Node:
    def __init__(self, ori_vertex_id, time, global_id):
        """
            Function description: Represent a time-expanded node with original ID and time layer.
            Approach description: Store parameters and initialize search attributes.

            :Input: ori_vertex_id:original graph vertex id; time: how many minutes when leave start point; global_id: time * n + ori_vertex_id becomes a unique id for the node.

            :Time complexity:
                Best case: O(1)
                Worst case: O(1)
            :Time complexity analysis:
                Attribute assignments only.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(1)
            :Space complexity analysis: Lists and attributes initialized.
        """
        self.ori_vertex_id = ori_vertex_id
        self.time = time
        self.global_id = global_id  # if we have total 1000 nodes, global_id is [0, 999]
        self.edges = []
        self.position = None

        self.visited = False
        self.cost = inf
        self.time_spent = inf
        self.previous = None

class MapGraph:
    def __init__(self, roads, stations, friend_start):
        """
            Function description: Build static graph of vertices and edges, track stations and friend start.
            Approach description: Compute max ID, create vertices, add edges and station flags.

            :Input: roads: list of (u,v,cost,time); stations: list of (station_id,travel_time); friend_start.

            constructor scans roads and stations to determine the maximum location ID, builds a Vertex list of that size,
            converts roads to adjacency lists, marks train stations with their travel times, and saves the friend’s
            starting station for later time‑expanded graph simulation.

            :Time complexity:
                Best case: O(|R| + |L|)
                Worst case: O(|R| + |L|)
            :Time complexity analysis:
                Scanning roads and initializing |L|+1 vertices.
            :Space complexity:
            Input space: O(|R| + |T|)
            Auxiliary space: O(|L| + |R| + |T|)
            :Space complexity analysis: Storing vertices and edge lists.
        """
        self.stations = []
        self.friend_start = friend_start

        maximum_id = -1
        for road in roads:
            maximum_id = max(maximum_id, road[0], road[1])  # road[0]:start ; road[1]:end

        for station_id, regular_loc_id in stations:
            maximum_id = max(maximum_id, station_id)
        self.total_location_num = maximum_id

        self.vertices = []
        for i in range(self.total_location_num + 1):
            vertex = Vertex(i)
            self.vertices.append(vertex)

        self.create_edges(roads)
        self.create_stations(stations)

    def reset_all_nodes(self):
        """
            Function description: Reset all search attributes of time-expanded nodes.
            Approach description: Iterate all_nodes and restore defaults.

            :Time complexity:   N = C × |L| time-layered nodes
                Best case: O(N)
                Worst case: O(N)
            :Time complexity analysis:
                Must visit all N time-expanded nodes to reset them.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(1)
            :Space complexity analysis: In-place resets.
        """
        for node in self.all_nodes:
            if node:
                node.visited = False
                node.cost = inf
                node.time_spent = inf
                node.previous = None

    def dijkstra(self, start_node_id):
        """
            Function description: Run Dijkstra on time-expanded graph from start_node_id.
            Approach description: Reset nodes, init MinHeap, get_min and relax edges.

            :Input: start_node_id, index in all_nodes.

            :Time complexity:
                Best case: O(M + N log N)
                Worst case: O(M log N)
            :Time complexity analysis:
                Best case when few relaxations occur, but initializing heap and resets cost O(N), then each of M edges considered once;
                worst case each of M edges triggers heap update costing O(log N), yielding O(M log N).
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(N + M)
            :Space complexity analysis: Nodes and heap storage.
        """
        self.reset_all_nodes()
        discovered = MinHeap(len(self.all_nodes))
        start_node = self.all_nodes[start_node_id]
        start_node.cost = 0
        start_node.time_spent = 0
        discovered.add((start_node, 0, 0))

        while len(discovered) > 0:
            vertex = discovered.get_min()
            node, time_spent_reach, cost_spend_reach = vertex

            node.visited = True

            for edge in node.edges:
                to_node = edge.target_vertex
                current_cost, current_time = edge.weight
                total_cost = cost_spend_reach + current_cost
                total_time = time_spent_reach + current_time

                if total_cost < to_node.cost or (total_cost == to_node.cost and total_time < to_node.time_spent):
                    to_node.cost = total_cost
                    to_node.time_spent = total_time
                    to_node.previous = node
                    if to_node.position is not None:
                        discovered.update(to_node, total_time, total_cost)
                    else:
                        discovered.add((to_node, total_time, total_cost))

    def create_edges(self, roads):
        """
            Function description: Add directed edges to vertices based on roads list.
            Approach description: Append Edge objects to each Vertex.edges.

            :Input: roads list.

            :Time complexity:
                Best case: O(|R|)
                Worst case: O(|R|)
            :Time complexity analysis:
                One pass through all R roads.
            :Space complexity:
            Input space: O(|R|)
            Auxiliary space: O(|R|)
            :Space complexity analysis: Storing Edge instances.
        """
        for u, v, cost, time in roads:
            self.vertices[u].edges.append(Edge(self.vertices[v], (cost, time)))

    def create_stations(self, stations):
        """
            Function description: Mark station vertices and store station times.
            Approach description: Set is_station True and record in self.stations.

            :Input: stations list.

            :Time complexity:
                Best case: O(T)
                Worst case: O(T)
            :Time complexity analysis:
                One pass through T stations (T <= 20 constant).
            :Space complexity:
            Input space: O(|T|)
            Auxiliary space: O(|T|)
            :Space complexity analysis: Storing T tuples in station list.
        """
        for station_id, time in stations:
            self.vertices[station_id].is_station = True
            self.stations.append((station_id, time))

    def friend_index(self):
        """
            Function description: Return index of friend_start in stations list.
            Approach description: Linear search.

            :Output, return or postcondition: friend_index or None.

            :Time complexity:
                Best case: O(1)
                Worst case: O(T)
            :Time complexity analysis:
                Best case when friend_start is first in list;
                worst case requires scanning all T stations.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(1)
            :Space complexity analysis: Constant.
        """
        for i in range(len(self.stations)):
            station_id, time_cost = self.stations[i]
            if station_id == self.friend_start:
                return i
        return None

    def friend_movement_route(self, friend_start_index, total_time):
        """
            Function description: Compute friend arrival times and station IDs over one loop.
            Approach description: Iterate while current_time < total_time.

            :Input: friend_start_index: where index is friend start; total_time: loop one time train station spend how many minutes.
            :Output, return or postcondition: two lists (times, station_ids).

            :Time complexity:
                Best case: O(total_time / max_travel_time)
                Worst case: O(total_time)
            :Time complexity analysis:
                Each loop iteration adds one station visit; bounded by total_time / min travel time >= iterations <= total_time when min travel_time=1.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(k)
            :Space complexity analysis: k = number of stops <= total_time.
        """
        friend_times = []
        friend_stations = []
        current_time = 0
        index = friend_start_index

        while current_time < total_time:
            station_id, travel_time = self.stations[index]
            friend_times.append(current_time)
            friend_stations.append(station_id)
            current_time += travel_time
            index = (index + 1) % len(self.stations)

        return friend_times, friend_stations

    def node_every_location_every_time_layer(self, total_time):
        """
            Function description: Build time-expanded nodes and edges including intercept edges.
            Approach description: Create C·|L| nodes, copy road edges each layer, add intercept to sink.

            :Input: total_time: loop one time train station spend how many minutes.
            :Output, return or postcondition: None (builds self.all_nodes, self.virtual_node).

            For each road u→v with travel_time t, link node(u, current_time) → node(v,  (current_time + t) % total_time)
            Here, '% total_time' ensures that the time loops within the period of the train loop.
            Compute friend’s schedule and for each arrival at (station, t),  add zero-weight edge → virtual_node.
            The zero-cost interception edge indicates that you can successfully intercept the site at the same time.

            :Time complexity:
                Best case: O(C·(|L|+|R|))
                Worst case: O(C·(|L|+|R|))
            :Time complexity analysis:
                Layering involves nested loops over C time layers, L locations, and R edges.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(C × |L| + C × |R|)
            :Space complexity analysis: Creating C·L nodes and their edges.
        """
        n = self.total_location_num + 1
        self.total_nodes = n * total_time
        self.virtual_node = self.total_nodes
        self.all_nodes = [None] * (self.total_nodes + 1)

        for t in range(total_time):
            for v in range(n):
                global_id = t * n + v
                self.all_nodes[global_id] = Node(v, t, global_id)

        self.all_nodes[self.virtual_node] = Node(0, 0, self.virtual_node)

        for current_time in range(total_time):
            for u in range(n):
                from_node = self.all_nodes[current_time * n + u]
                for edge in self.vertices[u].edges:
                    cost, time = edge.weight
                    v = edge.target_vertex.id
                    next_t = (current_time + time) % total_time
                    to_node = self.all_nodes[next_t * n + v]
                    from_node.edges.append(Edge(to_node, (cost, time)))

        friend_index = self.friend_index()
        friend_times, friend_stations = self.friend_movement_route(friend_index, total_time)

        for i in range(len(friend_times)):
            t = friend_times[i] % total_time
            s = friend_stations[i]
            global_id = t * n + s
            self.all_nodes[global_id].edges.append(Edge(self.all_nodes[self.virtual_node], (0, 0)))

    def tracking_back(self, start_node_id, virtual_node_id):
        """
            Function description: Backtrack from virtual_node to start to build the route.
            Approach description: Follow Node.previous pointers and reverse list.

            :Input: start_node_id: int; virtual_node_id: int.
            :Output, return or postcondition: List of original vertex IDs representing path.

            :Time complexity:
                Best case: O(1)
                Worst case: O(|L|)
            :Time complexity analysis:
                Best case when immediate intercept at start;
                worst case backtracking visits up to |L| nodes.
            :Space complexity:
            Input space: O(1)
            Auxiliary space: O(|L|)
            :Space complexity analysis: Path list length <= |L|.
        """
        path = []
        current = self.all_nodes[virtual_node_id].previous
        while current is not None and current.global_id != start_node_id:
            path.append(current.ori_vertex_id)
            current = current.previous
        path.append(self.all_nodes[start_node_id].ori_vertex_id)
        path.reverse()
        return path

def intercept(roads, stations, start, friendStart):
    """
        Function description: Compute minimal cost/time route to intercept friend on train loop.
        Approach description: Build time-expanded graph, run Dijkstra, backtrack path.

        :Input: roads, stations, start, friendStart as defined in assignment.
        :Output, return or postcondition: (totalCost, totalTime, route) or None if impossible.

        For assignment spec, the max station number is 20 and 5mins within train stations. that means 100 layers.
        But we cannot make any assumption about maximum layers. that means how many layers should be based on
        total time spent traversing a train station. and friend always loop in the train stations.

        Sum station travel times to get loop period C - Determine the number of "time layers"
        instead of fixing the maximum number of layers.
        Build time‑expanded graph with C layers and a single virtual_node for all intercepts.
        Run Dijkstra from (start, t=0), backtrack once virtual_node reached.

        :Time complexity:
            Best case: O(|R| + |L|)
            Worst case: O(|R| log |L|)
        :Time complexity analysis:
            Best case when intercept achievable quickly with few relaxations;
            worst case when exploring full time-expanded graph of size O(C·|L|) with M=O(C·|R|) edges, yielding O(M log N) around O(|R| log |L|).

        C (total_time) is constant:
        Number of stations T <= 20, each travel time <= 5 → C = sum up all travel_time <= 100.
        Hence the number of time‑layers C does not grow with |L| or |R|.

        complexity is O(|R| log |L|):
        Graph has N = C·|L| = O(|L|) nodes, M = C·|R| = O(|R|) edges.
        Dijkstra on adjacency lists costs O(M log N) = O(|R| log |L|).

        :Space complexity:
        Input space: O(|R| + |T|)
        Auxiliary space: O(C × (|L| + |R|))
        :Space complexity analysis: Graph and heap storage.
        Input is roads and stations list. Auxiliary includes time-expanded nodes and edges, MinHeap, path reconstruction.
    """
    total_time = 0
    for station_id, time in stations:
        total_time += time

    graph = MapGraph(roads, stations, friendStart)
    graph.node_every_location_every_time_layer(total_time)

    n = graph.total_location_num + 1
    start_node_id = 0 * n + start
    graph.dijkstra(start_node_id)

    virtual_node = graph.virtual_node
    intercept_node = graph.all_nodes[virtual_node]
    if intercept_node.cost == inf:
        return None

    path = graph.tracking_back(start_node_id, virtual_node)
    return (intercept_node.cost, intercept_node.time_spent, path)










