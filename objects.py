class Object:
    def __init__(self, params):
        if type(params) is dict and all(type(i) is str for i in params):
            self.params = params
        else:
            raise TypeError

    def get_param(self, param):
        if type(param) is str:
            return self.params[param]
        else:
            raise TypeError

    def set_param(self, param, mean):
        if type(param) is str:
            self.params[param] = mean
        else:
            raise TypeError

    def param_exist(self, param):
        return param in self.params
