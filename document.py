import datetime

from table import Table


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
                    newtable = Table(child)
                    self.tables.append(newtable)
                elif child.tag == 'data':
                    newtable = Table(child[0])
                    self.tables.append(newtable)
                    docroot = child[0]

        for child in docroot:
            if child.tag == 'all':
                newtable = Table(child)
                self.tables.append(newtable)
            elif (child.tag == 'package') or\
                    (child.tag == 'srcfile') or\
                    (child.tag == 'class') or\
                    (child.tag == 'method'):
                newtable = Table(child, CoverageDocument(child, child.get('name')))
                self.tables.append(newtable)

        print(docroot.tag + " " + name)

    @property
    def get_header(self):
        """
        Create html document header
        """
        if self.name == "index":
            h1 = "Code Coverage Report"
        else:
            h1 = self.root.tag + " " + self.name

        header = list()
        header.append("<html>")
        header.append("   <head><title>Code Coverage Report - " + self.root.tag + " " + self.name + "</title></head>")
        header.append("   <body>")
        header.append("       <h1>" + h1 + "</h1>")

        return header

    @property
    def get_footer(self):
        """
        Create html document footer
        """
        now = str(datetime.datetime.now()).split('.')[0]

        footer = list()
        footer.append("   <p><i>Created by emma2html at " + now + "</i></p>")
        footer.append("   </body>")
        footer.append("</html>")

        return footer
