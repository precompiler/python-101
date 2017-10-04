class Car:
    def __init__(self, top_speed):
        self._top_speed = top_speed

p = Car(300)
print(p._top_speed)
p._top_speed = 20
print(p._top_speed)

class Plane:
    def __init__(self, top_speed):
        self._top_speed = top_speed
    @property
    def top_speed(self):
        return self._top_speed
    @top_speed.setter
    def top_speed(self, top_speed):
        if 0 <= top_speed <= 3000:
            self._top_speed = top_speed
        else:
            raise ValueError("Top speed value range [0, 3000]")

pn = Plane(1000)
print(pn.top_speed)
pn.top_speed = 2000
print(pn.top_speed)
pn.top_speed = 6000