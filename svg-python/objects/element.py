#base element for all svg objects

from typing import Union
import util

# an abstract base class for concepts in svg (use for groups, visual elements like rects etc.)
class base:
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
        
        base._count += 1
        pass

    '''
    returns a tuple with an elements given x and y position and rotation 
    format: (x, y, rotation)
    '''
    def get_position_rotation(self) -> tuple:
        return (self.properties.get("x"), self.properties.get("y"), self.properties.get("rot"))

    def set_rotation(self, rotation : Union[int, float]):
        self.properties["rot"] = rotation

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
    def set_property(self, property : Union[str, tuple], value=None):
        self.properties[property] = value
        pass

    def get_property(self, property):
        return self.properties[property]

    '''
    removes and or returns value of given property -> raises KeyError if property doesn't exist
    '''
    def remove_property(self, property : str):
        return self.properties.pop(property)

    '''
    a function for directly setting x, y and z
    '''
    def set_position_rotation(self, x : int = None, y : int = None, rot : int = None):
        if x != None:
            self.set_property("x", x)

        if y != None:
            self.set_property("y", y)

        if rot != None:
            self.set_property("rot", rot)

    def _get_id(self):
        return self.properties.get("id")

    '''
    (internal) generates a tag to give out to parser
    '''
    def _generate_tag(self):
        tag = f"<{self.tag} "

        for key in self.properties.keys():
            tag += f'"{key}"="{self.properties.get()}" '

        return f"{tag}/>"


#a base class for all visual elements
class visual(base):

    def __init__(self, tag: str, pos_x=0, pos_y=0, rot=0, w=10, h=10, id: str = str(_count)) -> None:
        super().__init__(tag, pos_x=pos_x, pos_y=pos_y, rot=rot, w=w, h=h, id=id)

        self.properties["fill-color"] = util.color.RED
        self.properties["opacity"] = 100
        self.properties["stroke-color"] = util.color.BLUE
        self.properties["stroke-width"] = 1

    def set_fill(self, color : str):
        self.set_property("fill-color", color)
        pass

    def set_opacity(self, alpha : int):
        self.set_property("opacity", alpha)
        pass