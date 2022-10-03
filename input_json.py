import json
from textwrap import indent

#use json string as input

json_string  = """
{
    "input" : [
        {
         "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]

}
"""

def main():
    json_inputs = json.loads(json_string)
    #indented_format = json.dumps(json_inputs, indent=2)
    text = json_inputs['input'][0]['Text']
    source_language_code = json_inputs['input'][0]['SourceLanguageCode']
    target_language_code = json_inputs['input'][0]['TargetLanguageCode']
    print(text, source_language_code,target_language_code)

if __name__=="__main__":
    main()
