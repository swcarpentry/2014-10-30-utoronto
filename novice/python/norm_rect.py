# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 20:03:46 2014

@author: pauline
"""
def normalize_rectangle(rect):
    '''Normalizes a rectangle so that it ias at the origin and 1.0 units long on the longer axis'''
    assert len(rect) == 4, 'Rectangles must contain 4 coordinates'
    x0, y0, x1, y1 = rect
    assert x0 < x1, 'Invalid x coordinates'
    assert y0 < y1, ' Invalid y coordinates'
    
    dx = x1-x0
    dy = y1-y0
    if dx> dy:
        scaled = float(dx)/dy
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx)/dy
        upper_x, upper_y = scaled, 1.0
        
    assert 0 < upper_x <=1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <=1.0, 'Calculated upper Y coordinate invalid'
    
    return(0,0, upper_x, upper_y)
