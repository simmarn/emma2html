import os

from entity import Entity
from doc_generator import DocGenerator
from coverage_enum import CoverageType


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
        self.filename = self.name + ".html"
        self.entities = list()

        doc_root = root

        if root.tag == 'report':
            for child in root:
                # if child.tag == 'stats':
                #    new_table = Table(child)
                #    self.tables.append(new_table)
                if child.tag == 'data':
                    new_table = Entity(child[0])
                    self.entities.append(new_table)
                    doc_root = child[0]

        for child in doc_root:
            if (child.tag == 'all') or (child.tag == 'method'):
                new_table = Entity(child)
                self.entities.append(new_table)
            elif (child.tag == 'package') or\
                    (child.tag == 'srcfile') or\
                    (child.tag == 'class'):
                new_table = Entity(child, CoverageDocument(child, child.get('name')))
                self.entities.append(new_table)

        # print(doc_root.tag + " " + name)

    def write_file(self):
        """
        Write html file to disk
        """
        filename = os.path.join(self.filepath, self.name + ".html")

        file = DocGenerator(filename)

        if self.name == "index":
            h1 = "Code Coverage Report"
        else:
            h1 = self.root.tag + " " + self.name

        file.set_title("Code Coverage Report - " + self.root.tag + " " + self.name)
        file.set_header1(h1)
        file.set_entity_type(self.entities[0].get_entity_type())

        for entity in self.entities:
            class_cov = entity.get_coverage(CoverageType.CLASS)
            method_cov = entity.get_coverage(CoverageType.METHOD)
            block_cov = entity.get_coverage(CoverageType.BLOCK)
            line_cov = entity.get_coverage(CoverageType.LINE)
            file.add_row(entity.get_entity_name(), class_cov, method_cov, block_cov, line_cov)
            # write entity sub document if it exist
            entity.write_sub_document()

        file.write_document()
