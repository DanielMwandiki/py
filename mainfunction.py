import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text ='I am Learning to code in AWS',
        SourceLanguageCode='en',
        TargetLanguageCode='fr'
    )
    print(response) #print contents inside variable 'response'

def main():
    translate_text() # calls the translate_text() function to the main() function

if __name__=="__main__":  # if the variable __name__ is equal to "__main__" then call the main function.
    main()


