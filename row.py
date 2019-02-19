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
