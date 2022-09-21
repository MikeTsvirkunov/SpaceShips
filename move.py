from objects import Object
from math import cos, sin, pi


class Action:
    def action(self, obj, time):
        pass


class MoveFront(Action):
    def action(self, obj, time=1):
        if obj.param_exist("coord") and obj.param_exist("speed") and type(obj) is Object:
            obj.set_param("coord", (obj.get_param("coord")[0] + obj.get_param("speed")[0] * time,
                                    obj.get_param("coord")[1] + obj.get_param("speed")[1] * time))
        else:
            raise TypeError


class MoveRotation(Action):
    def action(self, obj, t=1):
        if obj.param_exist("angle") and obj.param_exist("speed") and type(obj) is Object:
            x, y = obj.get_param("coord")[0], obj.get_param("coord")[1]
            angle = obj.get_param("rotation_speed")
            obj.set_param("angle", obj.get_param("angle") + angle)
            obj.set_param("speed", (x*cos(pi * angle * t / 180) - y*sin(pi * angle * t / 180),
                                    y*cos(pi * angle * t / 180) - x*sin(pi * angle * t / 180)))
        else:
            raise TypeError

