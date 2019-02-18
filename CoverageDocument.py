import Table


class CoverageDocument:
    """
    Parse xml and create html page
    """

    def __init__(self, root, name):
        """
        Constructor. Parses xml and creates tables or sub documents

        Parameters
        ----------
        root :  Element
                xml root for document
        name :  string
                document name
        """
        self.root = root
        self.name = name
        self.tables = list()

        docroot = root

        if root.tag == 'report':
            for child in root:
                if child.tag == 'stats':
                    newtable = Table.Table(child)
                    self.tables.append(newtable)
                elif child.tag == 'data':
                    newtable = Table.Table(child[0])
                    self.tables.append(newtable)
                    docroot = child[0]

        for child in docroot:
            if child.tag == 'all':
                newtable = Table.Table(child)
                self.tables.append(newtable)
            elif (child.tag == 'package') or\
                    (child.tag == 'srcfile') or\
                    (child.tag == 'class') or\
                    (child.tag == 'method'):
                newtable = Table.Table(child, CoverageDocument(child, child.get('name')))
                self.tables.append(newtable)

        print(docroot.tag + " " + name)
