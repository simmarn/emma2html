import thresholds

from coverage_enum import CoverageType


class Coverage:
    """
    Contains coverage information
    """

    def __init__(self, xmlnode):
        """
        Constructor. Saves coverage xml

        Parameters
        ----------
        xmlnode :   Element
        """
        self.xmlnode = xmlnode

        values = self.xmlnode.get('value').split()
        self.percentage = float(values[0][:-1]) # remove '%', convert to float
        self.quotient = values[1]

    def format_percentage(self):
        if self.percentage == 100:
            return "100%"
        else:
            return format(self.percentage, '.2f') + "%"

    def get_bgcolor(self):
        cov_type = self.xmlnode.get('type')[:-3]
        if self.percentage > thresholds.get_threshold(cov_type):
            return "green"
        else:
            return "red"

    def get_coverage(self):
        """
        Get coverage
        :return: (string) coverage information
        """
        cov_info = self.format_percentage() + " " + self.quotient
        return cov_info

    def get_coverage_type(self):
        """
        Get coverage type
        :return: (CoverageType)
        """
        type = self.xmlnode.get('type')
        if "class" in type:
            return CoverageType.CLASS
        elif "method" in type:
            return CoverageType.METHOD
        elif "block" in type:
            return CoverageType.BLOCK
        elif "line" in type:
            return CoverageType.LINE

