from element import visual

class rect(visual):

    def __init__(self, pos_x=0, pos_y=0, rot=0, fill : str = "#FF0000", width=10, height=10) -> None:
        super().__init__("rect", pos_x=pos_x, pos_y=pos_y, rot=rot, w=width, h=height)

    pass