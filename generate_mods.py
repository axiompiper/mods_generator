#!/usr/bin/env python
'''Pass the name of the spreadsheet to this script and
it will generate individual mods files for each record
in the mods_files directory, logging the output to dataset_mods.log.
Run './generate_mods.py --help' to see various options.

Notes: 
1. The spreadsheet can be any version of Excel, or a CSV file.
2. See the test files for the format of the spreadsheet/csv file.
3. Unicode - all text strings from xlrd (for Excel files) are Unicode. For xlrd
    numbers, we convert those into Unicode, since we're just writing text out
    to files. The encoding of CSV files can be specified as an argument (if 
    it's not a valid encoding for Python, a LookupError will be raised). The
    encoding of the output files can also be specified as an argument (if
    there's an input character that can't be encoded in the output encoding, a
    UnicodeEncodeError will be raised).

'''
import sys
import os
from argparse import ArgumentParser
from mods_generator import DataHandler, process


if __name__ == '__main__':
    XML_FILES_DIR = "xml_files"
    parser = ArgumentParser()
    parser.add_argument('file_name')
    parser.add_argument('-t', '--type',
                    action='store', dest='type', default='parent',
                    help='type of records (parent or child, default is parent)')
    parser.add_argument('--force-dates',
                    action='store_true', dest='force_dates', default=False,
                    help='force date conversion even if ambiguous')
    parser.add_argument('--copy-parent-to-children',
                    action='store_true', dest='copy_parent_to_children', default=False,
                    help='copy parent data into children')
    parser.add_argument('-s', '--sheet',
                    action='store', dest='sheet', default=1,
                    help='specify the sheet number (starting at 1) in an Excel spreadsheet')
    parser.add_argument('-r', '--ctrl_row',
                    action='store', dest='row', default=2,
                    help='specify the control row number (starting at 1) in an Excel spreadsheet')
    parser.add_argument('-i', '--input-encoding',
                    action='store', dest='in_enc', default='utf-8',
                    help='specify the input encoding for CSV files (default is UTF-8)')
    args = parser.parse_args()
    process(file_name=args.file_name, xml_files_dir=XML_FILES_DIR, sheet=int(args.sheet),
            control_row=int(args.row), force_dates=args.force_dates, object_type=args.type, input_encoding=args.in_enc,
            copy_parent_to_children=args.copy_parent_to_children)
    sys.exit()

