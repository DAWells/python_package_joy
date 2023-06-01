#!/usr/bin/env python
import math


def make_box(width, text, block):
    top = f"{block*width}"
    spacer = f"#{' ' * (width - 2)}#"
    sidespaces = math.floor((width - len(text) - 2) / 2)
    padding = width > 2 * sidespaces + 2 + len(text)
    filling = f"#{' ' * sidespaces}{text}{' ' * (sidespaces+padding)}#"
    box = [top, spacer, filling, spacer, top]
    return box


def assemble_box(box):
    box = "\n".join(box)
    return box


def get_box(width, text, block="#"):
    box = make_box(width, text, block)
    box = assemble_box(box)
    return box
