from coverage import Coverage


class Entity:
    """
    Contains coverage information for one entity (package, srcfile, class,..)
    """

    def __init__(self, xml_node, sub_doc=None):
        """
        Constructor. Parses xml and creates table rows

        Parameters
        ----------
        xml_node :  Element
                    xml root for entity
        sub_doc :   CoverageDocument
                    sub document containing detailed coverage information
        """
        self.xml_node = xml_node
        self.sub_doc = sub_doc

        self.coverage_list = list()

        for child in xml_node:
            if child.tag == 'coverage':
                self.coverage_list.append(Coverage(child))

    def get_entity_name(self):
        """
        Get the name of the entity
        :return: (string) entity name
        """
        name = str(self.xml_node.get('name'))

        # Append web link if there is a sub document
        if self.sub_doc is not None:
            name = "<a href=\"" + self.sub_doc.filename + "\">" + name + "</a>"

        return name

    def get_entity_type(self):
        """
        Get the type of entity
        :return: (string) type of entity (package, file, class, ...)
        """
        if self.xml_node.tag == "all":
            return "package"
        else:
            return self.xml_node.tag

    def get_coverage(self, coverage_type):
        """
        Return the coverage object specified by the coverage type
        :param coverage_type: (CoverageType)
        :return: (Coverage)
        """
        for coverage in self.coverage_list:
            if coverage.get_coverage_type() == coverage_type:
                return coverage

    def write_sub_document(self):
        """
        Write sub document to disk
        """
        if self.sub_doc is not None:
            self.sub_doc.write_file()
