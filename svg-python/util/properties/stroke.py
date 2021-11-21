'''
A Module to provide Functions as Properties to add to Elements 
In this Module: Everything that concerns the stroke attribute on Elements
'''


def stroke_color(color : str):
    return ("stroke", color)

def stroke_opacity(alpha : int):
    return ("stroke-opacity", alpha)


