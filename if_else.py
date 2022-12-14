import json
#This one uses json string as an input

json_string = """
{
     "Input" : [
        {
            "Text" : "I am learning to code in AWS",
            "SourceLanguageCode" : "en",
            "TargetLanguageCode" : "fr"
        }
            ]
    
}

    """

json_input = json.loads(json_string) #We use loads as we load from a string

#Define two variables to store the language code from the input

SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0] ['TargetLanguageCode']

# The if statement checks to see if the language code is the same as the source code

if SourceLanguageCode == TargetLanguageCode:
    print("The Source Language is same as the Target Language - Stopping")

else:
    print("The Source Language and Target Language are different - Proceeding")