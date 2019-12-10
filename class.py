# Example to show how to use python classes and objects...

class Flights:

    def __init__(self,origin,destination,duration):
        self.origin=origin
        self.destination=destination
        self.duration=duration

    def print_info(self):
        print(f"origin:{self.origin}")
        print(f"destination:{self.destination}")
        print(f"duration:{self.duration}")

    def delay(self,amount):
        self.duration+=amount


def main():
    f = Flights(origin="New Delhi", destination="Seattle", duration=1080)
    f.delay(20)
    f.print_info()

if __name__=="__main__":
    main()