from row import Row


class Table:
    """
    Parse xml and create html table
    """

    def __init__(self, xmlnode, outputd=None):
        """
        Constructor. Parses xml and creates table rows

        Parameters
        ----------
        xmlnode :   Element
                    xml root for table
        outputd :   CoverageDocument
                    subdocument containing detailed coverage information
        """
        self.xmlnode = xmlnode
        self.outputd = outputd
        self.rowlist = list()

        for child in xmlnode:
            if child.tag == 'coverage':
                self.rowlist.append(Row(child))


