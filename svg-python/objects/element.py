#base element for all svg objects

from typing import Union


class element:
    _count = int()

    def __init__(self, tag : str, pos_x=0, pos_y=0, rot=0, w=10, h=10, id : str = str(_count)) -> None:
        # general stuff
        self.properties = dict()
        self.properties["x"] = pos_x
        self.properties["y"] = pos_y
        self.properties["w"] = w
        self.properties["h"] = h
        self.properties["rot"] = rot
        self.properties["id"] = str(tag + id)
        self.tag = tag

        #add to main buffer
        
        element._count += 1
        pass

    '''
    returns a tuple with an elements given x and y position and rotation 
    format: (x, y, rotation)
    '''
    def get_position_rotation(self) -> tuple:
        return (self.properties.get("x"), self.properties.get("y"), self.properties.get("rot"))

    def set_rotation(self, rotation : Union[int, float]):
        self.properties.get("rot") = rotation

    '''
    change x and y position of the element, set a parameter None if it shouldn't be changed 
    '''
    def set_position(self, x : Union[int, float, None] = None, y : Union[int, float, None] = None):
        #check if not None
        if x != None: self.properties["x"] = x
        if y != None: self.properties["y"] = y
        pass

    '''
    Adds or update a given property
    '''
    def add_update_property(self, property : Union[str, tuple], value=None):
        self.properties[property] = value
        pass

    '''
    removes and or returns value of given property -> raises KeyError if property doesn't exist
    '''
    def remove_pop_property(self, property : str):
        return self.properties.pop(property)


    def _get_id(self):
        return self.properties.get("id")


    '''
    (internal) generates a tag to give out to parser
    '''
    def _generate_tag(self):
        tag = str("<" + self.tag + " ")

        for key in self.properties.keys():
            tag += '"' + key + '"' + "=" + '"' + str(self.properties.get()) + '"' + " "

        return tag + "/>"
