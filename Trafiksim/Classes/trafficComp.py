class Vehicle:
    """Represents vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        """Creates the vehicle with specified properties."""
        self.destination = destination
        self.borntime = borntime
    def __str__(self):
        return f"Vehicle({self.destination}, {self.borntime})"

class Lane:
    """Represents a lane with (possibly) vehicles"""

    def __init__(self, length):
        """Creates a lane of specified length."""
        self.lane = [None for i in range(length)]
    def __str__(self):
        """String representation of lane contents."""
        returnString = "["
        for val in self.lane:
            returnString += f"{val.destination if val != None else str('.') } "
        return returnString + "]"

    def enter(self, vehicle):
        """Called when a new vehicle enters the end of the lane."""
        self.lane[-1] = vehicle
    def last_free(self):
        """Reports whether there is space for a vehicle at the
        end of the lane."""
        return self.lane[-1] == None
    def step(self):
        """Execute one time step."""
        for index ,val  in enumerate(self.lane):
            if self.lane[index-1] is None and index-1 >= 0:
                self.lane[index-1] = self.lane[index]
                self.lane[index] = None;
            
    def get_first(self):
        """Return the first vehicle in the lane, or None."""
        for x in self.lane:
            if x is not None:
                return x
    def remove_first(self):
        """Remove the first vehicle in the lane.
           Return the vehicle removed.
           If no vehicle is a the front of the lane, returns None
           without removing anything."""
           #not the nicest solution but fuck it
        returnval = self.lane.pop(0)
        self.lane.insert(0, None if returnval is not None else returnval)
        return returnval
    def number_in_lane(self):
        """Return the number of vehicles currently in the lane."""
        counter = 0
        for x in self.lane:
            if x != None:
                counter += 1
        return counter

def demo_lane():
    """For demonstration of the class Lane"""
    a_lane = Lane(10)
    print(a_lane)
    v = Vehicle('N', 34)
    a_lane.enter(v)
    print(a_lane)

    a_lane.step()
    print(a_lane)
    for i in range(20):
        if i % 2 == 0:
            u = Vehicle('S', i)
            a_lane.enter(u)
        a_lane.step()
        print(a_lane)
        if i % 3 == 0:
            print('  out: ',
                  a_lane.remove_first())
    print('Number in lane:',
          a_lane.number_in_lane())


class Light:
    """Represents a traffic light"""
    step_timer = 0
    

    def __init__(self, period, green_period):
        """Create a light with the specified timers."""
        self.period = period
        self.green_period = green_period

    def __str__(self):
        """Report current state of the light."""
        return f"( {str('G')  if self.is_green() else str('R')} )"

    def step(self):
        """Take one light time step."""
        self.step_timer += 1

    def is_green(self):
        """Return whether the light is currently green."""
        return True if (self.step_timer) % (self.period) < self.green_period else False


def demo_light():
    """Demonstrats the Light class"""
    a_light = Light(7, 3)
    for i in range(15):
        print(i, a_light,
              a_light.is_green())
        a_light.step()


def main():
    """Demonstrates the classes"""
    print('\nLight demonstration\n')
    demo_light()
    print('\nLane demonstration')
    demo_lane()


if __name__ == '__main__':
    main()