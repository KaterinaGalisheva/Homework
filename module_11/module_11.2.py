# Интроспекция. Узнать информацию об объекте

import inspect
import pprint 

    
class Some_objects:

    def __init__(self, obj):
        self.obj = obj
        

    def type_object(self):
        return type(self).__name__
    
    def attributes_object(self):
        return [attribute for attribute in dir(self) if not callable(getattr(self, attribute)) and not attribute.startswith('__')]

    def methods_object(self):
        return [method for method in dir(self) if callable(getattr(self, method)) and not method.startswith('__')]
    
    def module_object(self):
        return inspect.getmodule(object).__name__

    def count_object(self):
        return len(str(self))
    
    def get_help(self): 
        get_help = {}
        get_help['type'] = Some_objects.type_object(self.obj)
        get_help['attributes'] = Some_objects.attributes_object(self.obj)
        get_help['methods'] = Some_objects.methods_object(self.obj)
        get_help['module'] = Some_objects.module_object(self.obj)
        get_help['count'] = Some_objects.count_object(self.obj)
        print(f'Информация об объекте {self}: ')
        return get_help


if __name__ == '__main__':

    obj_1 = Some_objects(54)
    obj_2 = Some_objects('my name is Kate')
    obj_3 = Some_objects([1, 2, 3])
    
    pprint.pprint(obj_1.get_help())
    pprint.pprint(obj_2.get_help())
    pprint.pprint(obj_3.get_help())

        