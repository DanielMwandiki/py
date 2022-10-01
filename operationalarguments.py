from http import client
from urllib import response
import boto3

# def translate_text():
#     client = boto3.client('translate')
#     response = client.transalte_text(
#         Text='I am learning to code in AWS',
#         SourceLanguageCode='en',
#         TargetLanguageCode='fr'
#     )
#     print(response)

# def main():
#     translate_text()

# if __name__=="__main__":
#     main() 

def translate_text(text,source_language_code,target_language_code): #defined positonal arguments inside ()
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text, #remove hard coded value
        SourceLanguageCode=source_language_code, #used positional arguments
        TargetLanguageCode=target_language_code
    )
    print(response)

def main():
    translate_text('I am learning to code in AWS','en','fr') # we provide the value for the arguments when we call the function in the correct positional order.

if __name__=="__main__":
    main()