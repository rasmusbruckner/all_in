import numpy as np


def latex_plt(matplotlib):
    """This function updates the matplotlib library to use Latex and changes some default plot parameters

    :param matplotlib: matplotlib instance
    :return: Updated matplotlib instance
    """

    pgf_with_latex = {
        "axes.labelsize": 6,
        "font.size": 6,
        "legend.fontsize": 6,
        "axes.titlesize": 6,
        "xtick.labelsize": 6,
        "ytick.labelsize": 6,
        "figure.titlesize": 6,
        "pgf.rcfonts": False,
    }
    matplotlib.rcParams.update(pgf_with_latex)

    return matplotlib


def cm2inch(*tupl):
    """This function converts cm to inches

    Obtained from: https://stackoverflow.com/questions/14708695/
    specify-figure-size-in-centimeter-in-matplotlib/22787457

    :param tupl: Size of plot in cm
    :return: Converted image size in inches
    """

    inch = 2.54
    if isinstance(tupl[0], tuple):
        return tuple(i / inch for i in tupl[0])
    else:
        return tuple(i / inch for i in tupl)


def label_subplots(f, texts, x_offset=-0.07, y_offset=0.015):
    """This function labels the subplots

     Obtained from: https://stackoverflow.com/questions/52286497/
     matplotlib-label-subplots-of-different-sizes-the-exact-same-distance-from-corner

    :param f: Figure handle
    :param x_offset: Shifts labels on x-axis
    :param y_offset: Shifts labels on y-axis
    :param texts: Subplot labels
    """

    # Get axes
    axes = f.get_axes()

    if isinstance(x_offset, float):
        x_offset = np.repeat(x_offset, len(axes))

    if isinstance(y_offset, float):
        y_offset = np.repeat(y_offset, len(axes))

    axis_counter = 0
    # Cycle over subplots and place labels
    for a, l in zip(axes, texts):
        x = a.get_position().x0
        y = a.get_position().y1
        f.text(x - x_offset[axis_counter], y + y_offset[axis_counter], l, size=12)
        axis_counter += 1
