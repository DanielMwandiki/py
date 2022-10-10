import json

from if_else import SourceLanguageCode, TargetLanguageCode

# A defined list of languages supported by Amazon Translate
languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF","nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it","ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es","sw","sv","tl","ta","th","tr","uk","ur","vi"]

#Use a json string as an input

json_string = """
{
    "Input" :[
        {
            "Text" : "I am learning to code in AWS",
            "SourceLanguageCode" : "en",
            "TargetLanguageCode" : "fr"
            }
    ]
}
"""

json_input = json.loads(json_string)
#Define language code as a variable

SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# Uses an if-elif-else statements to check that the SourceLanguageCode is in the languages list.

if SourceLanguageCode == TargetLanguageCode:
    print("The SourceLanguageCode is same as TargetLanguageCode - Nothing to do ")
elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
    print("Neither the SourceLanguageCode and TargetLanguage are valid - Stopping")
elif SourceLanguageCode not in languages:
    print("The SourceLanguageCode is not valid - Stopping")
elif TargetLanguageCode not in languages:
    print("The TargetLanguage is not valid - Stopping")
elif SourceLanguageCode in languages and TargetLanguageCode in languages:
    print("The SourceLanguageCode and TargetLanguageCode are valid - Proceeding")
else:
    print("There is an issue")