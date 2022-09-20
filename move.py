from objects import Object

class Action:
    def action(self, object, time):
        pass


class MoveFront(Action):
    def action(self, obj, time=1):

        if obj.param_exist("coord") and obj.param_exist("speed") and type(obj) is Object:
            obj.set_param("coord",
                             (obj.get_param("coord")[0] + obj.get_param("speed")[0] * time,
                              obj.get_param("coord")[1] + obj.get_param("speed")[1] * time))
        else:
            raise TypeError

