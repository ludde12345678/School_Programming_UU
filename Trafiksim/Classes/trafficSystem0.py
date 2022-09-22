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
        self.time = 0
        self.lane_right = tc.Lane(5)
        self.lane_left = tc.Lane(5)
        self.s1 = tc.Light(10, 8)
        self.dest = destinations.Destinations()
        self.queue = []

    def snapshot(self):
        """Print a snap shot of the current state of the system."""
        q = "["
        for x in self.queue:
            q += f"{x.destination}, "
        q += "]"
        print(f'Time step {self.time}: {str(self.lane_left)} {str(self.s1)} {str(self.lane_right)} {q}')

    def step(self):
        """Take one time step for all components."""
        self.time += 1
        self.lane_left.remove_first()
        self.lane_left.step()
        if self.s1.is_green() and self.lane_left.last_free():
            self.lane_left.enter(self.lane_right.remove_first())
        self.s1.step()
        self.lane_right.step()
        vehicle = self.dest.step()
        if vehicle != None:
            self.queue.append(Vehicle(vehicle, self.time))
        if self.lane_right.last_free() and len(self.queue) >= 1:
            self.lane_right.enter(self.queue.pop(0))
            
            

    def in_system(self):
        """Return the number of vehicles in the system."""
        return self.lane_left.number_in_lane() + self.lane_right.number_in_lane() + len(self.queue)
#region
    # def print_statistics(self):
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