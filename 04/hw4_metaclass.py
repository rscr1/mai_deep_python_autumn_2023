class CustomMeta(type):
    '''Meta class'''
    def __new__(mcs, name, bases, classdict):
        '''Meta class constructor'''
        def custom_setattr(self, _name, _value):
            '''Custom function setattr'''
            self.__dict__['custom_' + _name] = _value

        new_classdict = {}
        for attr_name, attr_value in classdict.items():
            if not attr_name.startswith("__"):
                new_classdict["custom_" + attr_name] = attr_value
            else:
                new_classdict[attr_name] = attr_value
        new_classdict['__setattr__'] = custom_setattr
        return super().__new__(mcs, name, bases, new_classdict)

class CustomClass(metaclass=CustomMeta):
    '''Custom class'''
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
