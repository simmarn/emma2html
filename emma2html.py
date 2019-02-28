#!/usr/bin/python

import os
import getopt
import sys
import xml.etree.ElementTree

import thresholds
from document import CoverageDocument


"""
emma2html.py

Parses an coverage xml file generated by EclEmma and outputs html CoverageReport
"""
def usage():
    print('Usage: emma2html.py -i <inputfile> -s <coverage settings>')
    print('Example: emma2html -i vstest.coveragexml -s 90:90:90:90')


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:s:", ["help", "input=", "settings="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    input_file = None
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--input"):
            input_file = a
        elif o in ("-s", "--settings"):
            thresholds.set_threshold(a)
        else:
            usage()
            sys.exit(2)
    if args and args[0] != '-':
        usage()
        sys.exit(2)
    if len(opts) == 0:
        usage()
        sys.exit(2)

    if input_file is not None:
        # Read xml file
        xml_doc = xml.etree.ElementTree.parse(input_file)

    # Parse xml file
    maindoc = CoverageDocument(xml_doc.getroot(), "index")
    
    # create directory
    report_dir = os.path.join(os.getcwd(), maindoc.filepath)
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    
    # create html docs
    maindoc.write_file()

    print("Created coverage report in folder CoverageReport")
    
    sys.exit()


if __name__ == "__main__":
    main()
