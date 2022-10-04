class Vehicle:
    """Represents vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        """Creates the vehicle with specified properties."""
        # puts the variables in the class(instance)
        self.destination = destination
        self.borntime = borntime
    def __str__(self):
        """String representation of a vehicle"""
        
        return f"Vehicle({self.destination}, {self.borntime})"

class Lane:
    """Represents a lane with (possibly) vehicles"""

    def __init__(self, length):
        """Creates a lane of specified length."""
        # Creates a list filled with None for the length of the lane
        self.lane = [None for i in range(length)]
    def __str__(self):
        """String representation of lane contents."""
        # Makes a string representation of correct format
        returnString = "["
        for val in self.lane:
            returnString += f"{val.destination if val != None else str('.') } "
        return returnString + "]"

    def enter(self, vehicle):
        """Called when a new vehicle enters the end of the lane."""
        # Places that vehicle at the end of the list
        self.lane[-1] = vehicle
    def last_free(self):
        """Reports whether there is space for a vehicle at the
        end of the lane."""
        # Checks of the last place of the list is None or empty
        return self.lane[-1] == None
    def step(self):
        """Execute one time step."""
        # Loops through the lane and moves every vehicle forward if there is space and vehicle is not on the first spot(index 0)
        for index ,val  in enumerate(self.lane):
            if self.lane[index-1] is None and index-1 >= 0:
                self.lane[index-1] = self.lane[index]
                self.lane[index] = None;
            
    def get_first(self):
        """Return the first vehicle in the lane, or None."""
        # If lane at index 0(first place) is a vehicle, return that vehicle
        
        if self.lane[0] is not None:
            return self.lane[0]
    def remove_first(self):
        """Remove the first vehicle in the lane.
           Return the vehicle removed.
           If no vehicle is a the front of the lane, returns None
           without removing anything."""
           # not the nicest solution but fuck it
           # probably dont do this solution, use a loop and an if statement instead
           # I will explain this anyway tho
        returnval = self.lane.pop(0) # Pops, or removes the vehicle at the first place(index 0) and assign it to returnval
        self.lane.insert(0, None if returnval is not None else returnval) # insert back into the list(at index 0) either None, if returnval is a vehicle(aka first spot was a vehicle) or the returnval if it is None(so it will insert none or none, i said it was a bad solution)
        return returnval # return either a vehicle or none
    def number_in_lane(self):
        """Return the number of vehicles currently in the lane."""
        # loops through the list and adds 1 to counter everytime it finds a vehicle
        counter = 0
        for x in self.lane:
            if x != None:
                counter += 1
        return counter # returns the number of vehicles it found

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
    # just counts up 1 for every step
    step_timer = 0
    

    def __init__(self, period, green_period):
        """Create a light with the specified timers."""
        # insert the values into the class(technically the instance), you need to do this to access period and green_preiod in the other functions(methods)
        self.period = period
        self.green_period = green_period

    def __str__(self):
        """Report current state of the light."""
        # prints it with correct format
        return f"( {str('G')  if self.is_green() else str('R')} )"

    def step(self):
        """Take one light time step."""
        # takes one step aka adds 1 to the step_counter
        self.step_timer += 1

    def is_green(self):
        """Return whether the light is currently green."""
        # returns true if stepTimer modulus period is less then the green period(check my math if u dont belive me)
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
    # a thing you put into a file to make it run only if you are specifically running that file
    main()