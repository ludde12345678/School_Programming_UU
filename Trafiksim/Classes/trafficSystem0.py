from statistics import mean, median
from time import sleep
from trafficComp import Vehicle
import destinations
import trafficComp as tc

# Execute this file to run program

class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        """Initialize all components of the traffic
        system."""
        # Creates all the stuff for our traffic sim
        self.time = 0 # the time, just a number that counts up for every step
        self.lane_right = tc.Lane(5) # the right lane with a length of 5
        self.lane_left = tc.Lane(5) # the left lane with a length of 5
        self.s1 = tc.Light(10, 8) # a stoplight that will sit between the lanes
        self.dest = destinations.Destinations() # the premade class that makes the cars 
        self.queue = [] # the queue for cars waiting to enter the fist lane

    def snapshot(self):
        """Print a snap shot of the current state of the system."""
        # uses the __str__ functions of the classes combined to make a very nice output of the whole system
        q = "["
        for x in self.queue:
            q += f"{x.destination}, "
        q += "]"
        print(f'Time step {self.time}: {str(self.lane_left)} {str(self.s1)} {str(self.lane_right)} {q}')

    def step(self):
        """Take one time step for all components."""
        self.time += 1 # increses time by 1
        self.lane_left.remove_first() # removes the car to the left, if there is a car there, that car has now been deleted
        self.lane_left.step() # makes all the cars on the left lane move 1 step
        if self.s1.is_green() and self.lane_left.last_free(): # if the traffic light is green and the next slot is not occupied
            self.lane_left.enter(self.lane_right.remove_first()) # move a car from the right to the left lane, if a car can be moved
        self.s1.step() # takes 1 step for the traffic light
        self.lane_right.step() # makes all the cars on the right lane move 1 step 
        vehicle = self.dest.step() # checks if a new car is created this step, if vehicle == None, no new car is to be created, otherwise if its a destination, a car should be created this step
        if vehicle != None: # if a car should be created
            self.queue.append(Vehicle(vehicle, self.time)) # creates a new car with vehicle as destination and self.time as the borntime, and adds it to the queue
        if self.lane_right.last_free() and len(self.queue) >= 1: # if the lane is free and there is a car in the queue
            self.lane_right.enter(self.queue.pop(0)) # takes the car on index 0 and puts it in the right lane
            
            

    def in_system(self):
        """Return the number of vehicles in the system."""
        # cars in laft lane + cars in right lane + cars is queue
        return self.lane_left.number_in_lane() + self.lane_right.number_in_lane() + len(self.queue)
#region
    # def print_statistics(self):
    #    # Only used in the voluntary assignment
    #     """Print statistics about the run."""
    #     # Implement this method.
#endregion



def main():
    ts = TrafficSystem()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()