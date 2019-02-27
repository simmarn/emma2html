from coverage import Coverage


class Entity:
    """
    Contains coverage information for one entity (package, srcfile, class,..)
    """

    def __init__(self, xmlnode, outputd=None):
        """
        Constructor. Parses xml and creates table rows

        Parameters
        ----------
        xmlnode :   Element
                    xml root for entity
        outputd :   CoverageDocument
                    subdocument containing detailed coverage information
        """
        self.xmlnode = xmlnode
        self.outputd = outputd
        self.coverage_list = list()

        for child in xmlnode:
            if child.tag == 'coverage':
                self.coverage_list.append(Coverage(child))

    def get_html(self):
        """
        Get html for coverage table
        """
        content = list()

        content.append("       <p><table style=\"width:600px;table-layout:fixed\">\n")
        #content.append("       <p><table style=\"width:100%\">\n")
        content.append("          <tr>\n")
        content.append("            <th colspan=3>" + self.get_entity_name() + "</th>\n")
        content.append("          </tr>\n")
        
        for row in self.coverage_list:
            content.append("            " + row.get_html())
            
        content.append("          </tr>\n")
        content.append("       </table></p>\n")
        
        return content

    def get_entity_name(self):
        """
        Get the name of the entity
        :return: (string) entity name
        """
        if self.xmlnode.tag == "all":
            return str(self.xmlnode.get('name'))
        else:
            return self.xmlnode.tag + " " + str(self.xmlnode.get('name'))

    def get_entity_type(self):
        """
        Get the type of entity
        :return: (string) type of entity (package, file, class, ...)
        """
        if self.xmlnode.tag == "all":
            return "package"
        else:
            return self.xmlnode.tag

    def get_coverage(self, coverage_type):
        """
        Return the coverage object specified by the coverage type
        :param coverage_type: (CoverageType)
        :return: (Coverage)
        """
        for coverage in self.coverage_list:
            if coverage.get_coverage_type() == coverage_type:
                return coverage
