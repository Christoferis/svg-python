from element import element


'''
representation of an svg group
'''

class group(element):

    def __init__(self, pos_x=0, pos_y=0, rot=0, id=str(element._count)) -> None:
        super().__init__("g", pos_x=pos_x, pos_y=pos_y, rot=rot, id=id)

        self.elements = list()

    '''
    add any element
    '''
    def add_element(self, element : element):
        self.elements.append(element)

    '''
    remove and return element by id in the group
    '''
    def pop_element(self, id : str):
        
        if len(self.elements > 0):
            for element in self.elements:
                if element._get_id() == id:
                    delete = element
                    pass

            return self.elements.pop(self.elements.index(delete))
        else:
            raise KeyError


    #override since its a group object
    def _generate_tag(self):
        tag = str("<" + self.tag + " ")

        for key in self.properties.keys():
            tag += '"' + key + '"' + "=" + '"' + str(self.properties.get()) + '"' + " "

        tag += ">"

        for element in self.elements:
            tag += "\n\t" + element._generate_tag()
        
        return tag + "\n<" + self.tag + "/>"


