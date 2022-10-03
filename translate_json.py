import argparse
from http import client
from importlib.resources import contents
import json
from urllib import response
import boto3

#arguments
parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")
parser.add_argument(
    '--file',
    dest='filename',
    help="The path to the input file. The file should be valid json",
    required=True)

args = parser.parse_args()

#functions

def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
        return contents['Input'][0]

def translate_text(**kwargs):
    client =  boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)

#Main function - used to call other functions

def main ():
    kwargs = open_input()
    translate_text(**kwargs)

if __name__=="__main__":
    main()