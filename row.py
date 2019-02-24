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
        return "<tr><td>" + self.xmlnode.get('type') + "</td><td>" + format(self.percentage, '.2f')\
               + "</td><td>" + self.quotient + "</td></tr>\n"
