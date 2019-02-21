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
        
    def get_html(self):
        """
        Get html for coverage row
        """
        return "<td>cell 1</td><td>cell 2</td>\n"
    
