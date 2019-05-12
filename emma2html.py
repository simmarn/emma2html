#!/usr/bin/python

import os
import getopt
import sys
import xml.etree.ElementTree
import shutil
import glob

import thresholds
from coverage_document import CoverageDocument


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
    main_doc = CoverageDocument(xml_doc.getroot(), "index")

    # create directory
    report_dir = os.path.join(os.getcwd(), main_doc.file_path)
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    else:
        # delete all files in directory
        for the_file in os.listdir(report_dir):
            file_path = os.path.join(report_dir, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path) # uncomment to remove subdir
            except Exception as e:
                print(e)

    # create html docs
    main_doc.write_file()

    # Copy all javascript files to output dir
    for file in glob.glob(os.path.join(os.path.dirname
                                           (os.path.abspath
                                                (sys.modules[CoverageDocument.__module__].__file__)
                                            ), "html", r'*.js')):
        shutil.copy(file, report_dir)

    print("Created coverage report in folder CoverageReport")

    sys.exit()


if __name__ == "__main__":
    main()
