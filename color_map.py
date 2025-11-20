def get_color_map_value(x, maximum, palette_size):
    # TODO - For now, we only support palette sizes of 2 and implement it this way.
    # We want to instead have an implementation that has a proper color map
    assert palette_size == 2
    return 0 if x == maximum else 1
