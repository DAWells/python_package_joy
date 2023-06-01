from boxed.boxed import make_box


def test_all_rows_equal_width():
    width = 20
    text = "Box"
    block = "#"
    flatpack = make_box(width, "Box", "#")
    widths = [len(row) for row in flatpack]
    assert all([w == width for w in widths]), f"{width}, {text}, {block}"
