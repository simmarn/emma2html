import datetime
import os

from table import Table


class CoverageDocument:
    """
    Parse xml and create html page
    """
    filepath = "CoverageReport"
    
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
            if (child.tag == 'all') or\
                (child.tag == 'method'):
                newtable = Table(child)
                self.tables.append(newtable)
            elif (child.tag == 'package') or\
                    (child.tag == 'srcfile') or\
                    (child.tag == 'class'):
                newtable = Table(child, CoverageDocument(child, child.get('name')))
                self.tables.append(newtable)

        print(docroot.tag + " " + name)

    def write_file(self):
        """
        Write html file to disk
        """
        filename = os.path.join(self.filepath, self.name + ".html")
        
        content = self.get_content()
        
        file = open(filename, 'w')
        
        for row in content:
            file.write(row)
           
        file.close()
        
    def get_content(self):
        """
        Get file content and return as a list of rows 
        """
        content = self.get_header()
        
        for table in self.tables:
            content = content + table.get_html()
        
        content = content + self.get_footer()
        
        return content
        
    def get_header(self):
        """
        Create html document header
        """
        if self.name == "index":
            h1 = "Code Coverage Report"
        else:
            h1 = self.root.tag + " " + self.name

        header = list()
        header.append("<html>\n")
        header.append("   <head>\n")
        header.append("       <title>Code Coverage Report - " + self.root.tag + " " + self.name + "</title>\n")
        header.append("       <style>\n")
        header.append("       table, th, td {\n")
        header.append("         border: 1px solid black;\n")
        header.append("         border-collapse: collapse;\n")
        header.append("         padding: 5px;\n")
        header.append("         }\n")
        header.append("       </style>\n")
        header.append("   </head>\n")
        header.append("   <body>\n")
        header.append("        <h1>" + h1 + "</h1>\n")

        return header

    def get_footer(self):
        """
        Create html document footer
        """
        now = str(datetime.datetime.now()).split('.')[0]

        footer = list()
        footer.append("       <p><i>Created by emma2html at " + now + "</i></p>\n")
        footer.append("   </body>\n")
        footer.append("</html>")

        return footer
