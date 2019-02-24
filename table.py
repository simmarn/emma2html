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

        content.append("       <p><table style=\"width:600px;table-layout:fixed\">\n")
        #content.append("       <p><table style=\"width:100%\">\n")
        content.append("          <tr>\n")
        content.append("            <th colspan=3>" + self.get_header() + "</th>\n")
        content.append("          </tr>\n")
        
        for row in self.rowlist:
            content.append("            " + row.get_html())
            
        content.append("          </tr>\n")
        content.append("       </table></p>\n")
        
        return content

    def get_header(self):
        if (self.xmlnode.tag == "all"):
            return str(self.xmlnode.get('name'))
        else:
            return self.xmlnode.tag + " " + str(self.xmlnode.get('name'))