from Classes import *
from Classes.trafficSystem0 import TrafficSystem
from Classes.trafficComp import demo_lane, demo_light;
from time import sleep



demo_light();
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