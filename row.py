import thresholds

class Row:
    """
    Parse xml and create html table
    """

    def __init__(self, xmlnode):
        """
        Constructor. Saves row xml

        Parameters
        ----------
        xmlnode :   Element
        """
        self.xmlnode = xmlnode

        values = self.xmlnode.get('value').split()
        self.percentage = float(values[0][:-1]) # remove '%', convert to float
        self.quotient = values[1]

        
    def get_html(self):
        """
        Get html for coverage row
        """
        return "<tr bgcolor=\"" + self.get_bgcolor() + "\"><td>" + self.xmlnode.get('type') + "</td><td>"\
               + self.format_percentage() + "</td><td>" + self.quotient + "</td></tr>\n"

    def format_percentage(self):
        if self.percentage == 100:
            return "100"
        else:
            return format(self.percentage, '.2f')

    def get_bgcolor(self):
        cov_type = self.xmlnode.get('type')[:-3]
        if self.percentage > thresholds.get_threshold(cov_type):
            return "green"
        else:
            return "red"

