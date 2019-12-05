import thresholds

from coverage_enum import CoverageType


class Coverage:
    """
    Contains coverage information
    """
    def __init__(self, xml_node):
        """
        Constructor. Saves coverage xml

        Parameters
        ----------
        xml_node :   Element
        """
        self.xml_node = xml_node

        values = self.xml_node.get('value').split()
        self.percentage = float(values[0][:-1]) # remove '%', convert to float
        self.quotient = values[1]

    def format_percentage(self):
        if self.percentage == 100:
            return "100%"
        else:
            return format(self.percentage, '.2f') + "%"

    def get_bgcolor(self):
        if self.percentage > thresholds.get_threshold(self.get_coverage_type):
            return "green"
        else:
            return "red"

    def get_coverage(self):
        """
        Get coverage
        :return: (string) coverage information
        """
        cov_info = self.format_percentage()
        return cov_info

    def get_missed(self):
        """
        Get missed items
        :return: (string) missed number of items
        """
        quot_list = self.quotient.replace("(", "").replace(")", "").split("/")
        covered_items = int(quot_list[0])
        total_items = int(quot_list[1])
        return total_items - covered_items

    @property
    def get_coverage_type(self):
        """
        Get coverage type
        :return: (CoverageType)
        """
        node_type: str = self.xml_node.get('type')
        if "class" in node_type:
            return CoverageType.CLASS
        elif "method" in node_type:
            return CoverageType.METHOD
        elif "block" in node_type:
            return CoverageType.BLOCK
        elif "line" in node_type:
            return CoverageType.LINE

