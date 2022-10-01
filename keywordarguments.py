# from http import client
from http import client
from typing import Text
from urllib import response
import boto3

# def translate_text(text,source_language_code,target_language_code):
#     client = boto3.client('translate')
#     response = client.translate_text(
#         Text=text,
#         SourceLanguageCode=source_language_code,
#         TargetLanguageCode=target_language_code
#     )
#     print(response)

# def main():
#     translate_text('I am learning to code in AWS','en','fr')

# if __name__=="__main__":
#     main()


def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)

def main():
    translate_text(Text='I am learning to code in aws', SourceLanguageCode='en', TargetLanguageCode='fr')

if __name__=="__main__":
    main()