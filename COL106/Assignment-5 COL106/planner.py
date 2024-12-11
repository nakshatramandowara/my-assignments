from flight import Flight


class Planner:
    def __init__(self, flights: list[Flight]):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.flights = flights
        self.m = len(flights) 
        self.max_city = 0
        for flight in flights:
            self.max_city = max(self.max_city, flight.start_city, flight.end_city)
        self.max_city += 1  # due to zero indexing
        self.Graph = [
            [] for _ in range(self.max_city)
        ]  # list of vertices has length max_city,Graph is an adjacency list
        for flight in flights:
            self.Graph[flight.start_city].append(flight)

    def backtrack(self,flight):
        lst=[]
        while(flight):
            lst.append(flight)
            flight=flight.last_flight
        return lst[::-1]
    
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying:
        The route has the least number of flights, and within routes with same number of flights,
        arrives the earliest
        """
        if start_city == end_city:
            return []
        for flight in self.flights:
            flight.last_flight = None
            flight.path_length = float("inf")

        priority_queue = Queue(self.m)
        for flight in self.Graph[start_city]:
            if flight.departure_time >= t1 and flight.arrival_time <= t2:
                flight.path_length = 1
                priority_queue.enqueue(flight)

        my_flight = None
        while not priority_queue.is_empty():
            flight = priority_queue.dequeue()
            if flight.end_city == end_city:
                if not my_flight or (flight.path_length, flight.arrival_time) < (my_flight.path_length,my_flight.arrival_time):
                    my_flight = flight
                    continue
                elif(flight.path_length>my_flight.path_length):
                    break
            for plane in self.Graph[flight.end_city]:  # for edges in adjacency list of curr flight
                if (
                    flight.arrival_time + 20 <= plane.departure_time
                    and plane.arrival_time <= t2 and flight.path_length + 1 < plane.path_length
                ):
                        plane.path_length = 1 + flight.path_length
                        plane.last_flight = flight
                        priority_queue.enqueue(plane)

        return self.backtrack(my_flight)

    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying:
        The route is a cheapest route
        """
        if start_city == end_city:
            return []
        for flight in self.flights:
            flight.last_flight = None
            flight.path_length = float("inf")

        priority_queue = Heap()
        for flight in self.Graph[start_city]:
            if flight.departure_time >= t1 and flight.arrival_time <= t2:
                flight.path_length = flight.fare
                priority_queue.insert(flight)

        my_flight = None
        while not priority_queue.is_empty():
            flight = priority_queue.extract()
            if flight.end_city == end_city:
                my_flight = flight
                break
            for plane in self.Graph[
                flight.end_city
            ]:  # for edges in adjacency list of curr flight
                if (
                    flight.arrival_time + 20 <= plane.departure_time
                    and plane.arrival_time <= t2
                ):
                    new_fare = flight.path_length + plane.fare

                    if new_fare < plane.path_length:
                        plane.path_length = new_fare
                        plane.last_flight = flight
                        priority_queue.insert(plane)

        return self.backtrack(my_flight)

    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying:
        The route has the least number of flights, and within routes with same number of flights,
        is the cheapest
        """
        if start_city == end_city:
            return []
        for flight in self.flights:
            flight.last_flight = None
            flight.path_length = (float("inf"), float("inf"))

        Priority_queue = Heap()

        for flight in self.Graph[start_city]:
            if flight.departure_time >= t1 and flight.arrival_time <= t2:
                flight.path_length = (1, flight.fare)
                Priority_queue.insert(flight)

        my_flight = None
        while not Priority_queue.is_empty():
            flight = Priority_queue.extract()
            if flight.end_city == end_city:
                my_flight = flight
                break

            for plane in self.Graph[
                flight.end_city
            ]:  # for edges in adjacency list of curr flight
                if (
                    flight.arrival_time + 20 <= plane.departure_time
                    and plane.arrival_time <= t2
                ):
                    new_fare = flight.path_length[1] + plane.fare
                    if (flight.path_length[0] + 1, new_fare) < plane.path_length:
                        plane.path_length = (flight.path_length[0] + 1, new_fare)
                        plane.last_flight = flight
                        Priority_queue.insert(plane)

        return self.backtrack(my_flight)
    
    



class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.n = 0
        self.l = 0
        self.r = 0

    def enqueue(self, object):
        self.n += 1
        self.queue[self.r] = object
        self.r = (self.r + 1) % self.size

    def dequeue(self):
        self.n -= 1
        x, self.queue[self.l] = self.queue[self.l], None
        self.l = (self.l + 1) % self.size
        return x

    def is_empty(self):
        if self.n == 0:
            return True
        else:
            return False


class Heap:
    """
    Class to implement a heap with general comparison function
    """

    def fare_comparator(x, y):
        return x.path_length < y.path_length

    def __init__(self, comparison_function=fare_comparator):
        # Write your code here
        self.comparator = comparison_function
        self.heap_array = []

    def MIN_downheap(self, i):
        l = 2 * i + 1
        r = 2 * i + 2
        smallest = i
        length = len(self.heap_array)
        if l < length and (
            self.comparator(self.heap_array[l], self.heap_array[smallest])
        ):  # A[l]<A[smallest]
            smallest = l
        if r < length and (
            self.comparator(self.heap_array[r], self.heap_array[smallest])
        ):  # A[r]<A[smallest]
            smallest = r
        if smallest != i:
            self.heap_array[i], self.heap_array[smallest] = (
                self.heap_array[smallest],
                self.heap_array[i],
            )  # swap A[i] with the smallest of the 3
            self.MIN_downheap(smallest)

    def MIN_upheap(self, i):
        if i <= 0:
            return
        parent = (i - 1) // 2

        if self.comparator(
            self.heap_array[i], self.heap_array[parent]
        ):  # A[i]<A[parent]
            self.heap_array[i], self.heap_array[parent] = (
                self.heap_array[parent],
                self.heap_array[i],
            )  # swap upwards
            self.MIN_upheap(parent)  # recursive call
        else:
            return  # do nothing

    def is_empty(self):
        return not len(self.heap_array)

    def insert(self, value):

        self.heap_array.append(value)

        self.MIN_upheap(len(self.heap_array) - 1)

    def extract(self):

        self.heap_array[0], self.heap_array[-1] = (
            self.heap_array[-1],
            self.heap_array[0],
        )  # swap root and last element
        root = self.heap_array.pop()
        self.MIN_downheap(0)
        return root
