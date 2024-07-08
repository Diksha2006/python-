class bird:
    def intro(self):
        print("THRER ARE MANY TYPES OF BIRDS")
    def flight(self):
        print("SOME OF THE BIRDS CAN FLY AND SOME CAN'T FLY")
class sparrow(bird):
    def flight(self):
        print("SPARROW CAN FLY")
class ostrich(bird):
    def flight(self):
        print("OSTRICH CAN  NOT FLY") 
bboj=bird()
bboj.intro()
bboj.flight()
sobj=sparrow()
sobj.intro()
sobj.flight()
oobj=ostrich()
oobj.intro()
oobj.flight()
                           