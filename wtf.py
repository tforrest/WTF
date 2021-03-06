#!/usr/bin/python
import argparse
import json
import os
import sys

errlog = lambda msg: sys.stderr.write("{}\n".format(msg))


def create_parser():

	parser = argparse.ArgumentParser(
        description="What's this for?\n Enter a term")
	parser.add_argument("term", nargs="*")
	
	return parser
    
def process_args(args):
    
    term_name = " ".join(args.term)
    
    return term_name

def wtf(args):
    filepath = os.path.join(os.path.expanduser('~'), 'Terms.json')
    term_name = process_args(args)

    if os.path.isfile(filepath) and os.access(filepath, os.R_OK):
        try:
            terms_file = open(filepath, "r")
            data = json.load(terms_file)
        except ValueError:
            errlog(
                "Error has occurred loading file. File will be regenerated from scratch")
            terms_file.close()
            terms_file = open(filepath, "w")
            terms_file.write("{}")
        finally:
            terms_file.close()

        if term_name in data:
            print(data[term_name]["proper_capitalization"] + ":")
            print(data[term_name]["description"])
        else:
            print("Term not found!\nUse tf to create a new term.")
            exit(1)

    else:
        if not os.path.isfile(filepath):
            errlog("Terms file not found. Creating a new one.")
            terms_file = open(filepath, "w")
            terms_file.write("{}")
            terms_file.close()
        else:
            errlog("Permissions error with Terms.json\nCheck user permissions")
        exit(1)

if "__main__" == __name__:
    args = create_parser().parse_args()

    wtf(args)
