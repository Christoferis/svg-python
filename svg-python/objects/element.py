#base element for all svg objects

class element:

    def __init__(self, tag : str, pos_x=0, pos_y=0, rot=0) -> None:
        # general stuff
        self.attributes = dict()
        self.attributes["x"] = pos_x
        self.attributes["y"] = pos_y
        self.attributes["rot"] = rot
        self.tag = tag
        pass

    '''
    returns a tuple with an elements given x and y position and rotation 
    format: (x, y, rotation)
    '''
    def get_position_rotation(self) -> tuple:
        return (self.attributes["x"], self.attributes["y"], self.attributes["rot"])

    def set_rotation(self, rotation):
        self.attributes["rot"] = rotation

    def set_position(x=None, y=None):
        self.attributes
        pass

    '''
    Adds or update a given Attribute
    '''
    def add_update_attribute(self, attribute : str, value):
        self.attributes[attribute] = value
        pass

    '''
    removes and or returns value of given attribute -> raises KeyError if Attribute doesn't exist
    '''
    def remove_pop_attribute(self, attribute : str):
        return self.attributes.pop(attribute)


    '''
    (internal) generates a tag to give out to parser
    '''
    def _generate_tag():
        pass
