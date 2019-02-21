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

    def get_html(self):
        """
        Get html for coverage table
        """
        content = list()
        
        content.append("       <table style==\"width:100%\">\n")
        content.append("          <tr>\n")
        #content.append("            <th>header1</th>\n")
        #content.append("            <th>header2</th>\n")
        
        for row in self.rowlist:
            content.append("            " + row.get_html())
            
        content.append("          </tr>\n")
        content.append("        </table>\n")
        
        return content