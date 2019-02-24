class_threshold = 90.0
method_threshold = 90.0
block_threshold = 90.0
line_threshold = 90.0


def set_threshold(settings):
    """
    Parse settings and store thresholds
    :param settings:
    """
    global class_threshold
    global method_threshold
    global block_threshold
    global line_threshold
    thresholds = settings.split(':')
    class_threshold = float(thresholds[0])
    method_threshold = float(thresholds[1])
    block_threshold = float(thresholds[2])
    line_threshold = float(thresholds[3])


def get_threshold(coverage_type):
    """
    Return the threshold set for the given coverage type
    :param coverage_type: <string>, one of "class", "method", "block", "line"
    :return: <double> coverage thredhold in percentage [0-100]
    """
    if coverage_type == "class":
        return class_threshold
    elif coverage_type == "method":
        return method_threshold
    elif coverage_type == "block":
        return block_threshold
    elif coverage_type == "line":
        return line_threshold
