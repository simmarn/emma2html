from coverage_enum import CoverageType
class_threshold = 90.0
method_threshold = 90.0
block_threshold = -1.0
line_threshold = 90.0


def set_threshold(settings: str):
    """
    Parse settings and store thresholds
    :param settings: <str> is the format x:y:z:w where x, y, z, and w are values that can be converted to float
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


def get_threshold(coverage_type: CoverageType) -> float:
    """
    Return the threshold set for the given coverage type
    :param coverage_type: <CoverageType>, one of "class", "method", "block", "line"
    :return: <float> coverage threshold in percentage [0-100]
    """
    if coverage_type is CoverageType.CLASS:
        return class_threshold
    elif coverage_type is CoverageType.METHOD:
        return method_threshold
    elif coverage_type is CoverageType.BLOCK:
        return block_threshold
    elif coverage_type is CoverageType.LINE:
        return line_threshold
