#!/usr/bin/env python

def make_box(width, text, block):
    top = f"{block*width}"
    spacer = f"#{' ' * (width - 2)}#"
    sidespaces = round((width - len(text))/2)-2
    filling = f"#{' ' * sidespaces}{text}{' ' * sidespaces}#"
    box = [top, spacer, filling, spacer, top]
    return box

def assemble_box(box):
    box = "\n".join(box)
    return box

def get_box(width, text, block="#"):
    box = make_box(width, text, block)
    box = assemble_box(box)
    return box


