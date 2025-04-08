def safe_div(x, y):
    """This function divides two numbers and avoids division by zero

        Obtained from:
        https://www.yawintutor.com/zerodivisionerror-division-by-zero/

    :param x: x-value
    :param y: y-value
    :return: c: result
    """

    if y == 0:
        c = 0.0
    else:
        c = x / y
    return c


def callback(show_ind_prog, pbar):
    """This callback function updates the progress bar

    :param show_ind_prog: Boolean indicating if progress bar should be shown
    :param pbar: progress-bar-object instance
    :return: None
    """

    if show_ind_prog:
        pbar.update()
