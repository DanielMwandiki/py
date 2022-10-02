from urllib import response
import boto3

# def translate_text(**kwargs):
#     client = boto3.client('translate')
#     response = client.translate_text(**kwargs)
#     print(response)

# kwargs = {
#     "Text" : "I am learning to code in AWS",
#     "SourceLanguageCode" : "en",
#     "TargetLanguageCode" : "fr"
# }

# def main():
#     translate_text(**kwargs)

# if __name__=="__main__":
#     main()

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response)

text = input("Provide the text you want translated : ")
source_language_code = input("Provide the two letter source language code : ")
target_language_code = input("Provide the two letter target language code : ")

def main():
    translate_text(
        Text = text,
        SourceLanguageCode = source_language_code,
        TargetLanguageCode = target_language_code
    )

if __name__=="__main__":
    main()