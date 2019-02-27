import datetime
from coverage import Coverage

class DocGenerator:
    """
    Class that generates a html document from html template
    """
    def __init__(self, filename):
        """
        Constructor. Read template files
        :param filename: filename as a string, e.g. "/home/user/CoverageReport/index.html"
        """
        self.filename = filename

        doc_template = open("doc_template.html", "r")
        self.document = doc_template.read()
        doc_template.close()

        row_template = open("row_template.html", "r")
        self.table_row = row_template.read()
        row_template.close()

        self.table = ""

    def set_title(self, title):
        """
        Set the document filename
        :param title: (string) title of document
        """
        self.document = self.document.replace("%DOC_TITLE%", title)

    def set_header1(self, header):
        """
        Set the header level 1
        :param header: (string) header text
        """
        self.document = self.document.replace("%HEADER1%", header)

    def set_entity_type(self, type):
        """
        Set the type of the table
        :param type: (string) type
        """
        self.document = self.document.replace("%ENTITY_TYPE%", type)

    def add_row(self, entity_name, class_c, method_c, block_c, line_c):
        """
        Add a row to table
        :param entity_name: (string) description of entity or entity name
        :param class_c: (Coverage) class coverage
        :param method_c:  (Coverage) method coverage
        :param block_c: (Coverage) block coverage
        :param line_c:  (Coverage) line coverage
        """
        row = self.table_row.replace("%ENTITY%", entity_name)
        row = row.replace("%CLASS_COLOR%", class_c.get_bgcolor()).replace("%CLASS_COV%", class_c.get_coverage())
        row = row.replace("%METHOD_COLOR%", method_c.get_bgcolor()).replace("%METHOD_COV%", method_c.get_coverage())
        row = row.replace("%BLOCK_COLOR%", block_c.get_bgcolor()).replace("%BLOCK_COV%", block_c.get_coverage())
        row = row.replace("%LINE_COLOR%", line_c.get_bgcolor()).replace("%LINE_COV%", line_c.get_coverage())

        self.table = self.table + row

    def write_document(self):
        """
        Write document
        """
        self.document = self.document.replace("%ROWS%", self.table)
        self.document = self.document.replace("%TIMESTAMP%", str(datetime.datetime.now()).split('.')[0])

        doc = open(self.filename, "w")
        doc.write(self.document)
        doc.close()
