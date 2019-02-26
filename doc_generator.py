import datetime


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

    def set_table_type(self, type):
        """
        Set the type of the table
        :param type: (string) type
        """
        self.document = self.document.replace("%TYPE%", type)

    def add_row(self, row_type, class_color, class_coverage, method_color,
                method_coverage, block_color, block_coverage, line_color, line_coverage):
        """
        Add a row to table
        :param row_type: (string) description of row
        :param class_color: (string) background color of class coverage cell
        :param class_coverage: (string) class coverage text
        :param method_color:  (string) background color of method coverage cell
        :param method_coverage: (string) method coverage text
        :param block_color: (string) background color of block coverage cell
        :param block_coverage: (string) block coverage text
        :param line_color: (string) background color of line coverage cell
        :param line_coverage:  (string) line coverage text
        """
        row = self.table_row.replace("%TYPENAME%", row_type)
        row = row.replace("%CLASS_COLOR%", class_color).replace("%CLASS_COV%", class_coverage)
        row = row.replace("%METHOD_COLOR%", method_color).replace("%METHOD_COV%", method_coverage)
        row = row.replace("%BLOCK_COLOR%", block_color).replace("%BLOCK_COV%", block_coverage)
        row = row.replace("%LINE_COLOR%", line_color).replace("%LINE_COV%", line_coverage)

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
