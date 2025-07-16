"""The script accepts a JSON file with questions for the survey."""
"""It creates survey using API request and JSON data."""


import requests, json, sys

try:
    filename=sys.argv[1]
except IndexError:
    print("Usage: python3 task2.py <filename>.")
    print("Tip: You can use the 'secrets.txt' file as an example; it is included in the provided materials")


with open(filename, "r") as file:
    for line in file:
        ACCESS_TOKEN=line.split('"')[1]

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}


def create_questions_string_json(input_json_list, question_str, answers_list):
    new_question = {
        "headings": [
            {
                "heading": question_str
            }
        ],
        "family": "single_choice",
        "subtype": "vertical",
        "answers": {
            "choices":[
                {
                    "text": answers_list[0]
                },
                {
                    "text": answers_list[1]
                },
                {
                    "text": answers_list[2]
                }
            ],
            "other":[
                {
                    "text": "Other",
                    "num_chars": 100,
                    "num_lines": 3
                }
            ]
        }
    }
    input_json_list.append(new_question)


def create_page_json(pages_list, questions_list, page_nr):
    new_page = {
        "title": page_nr,
        "questions": questions_list
    }
    pages_list.append(new_page)


    
with open("task2_survey.json", "r") as f:
    data = json.load(f)

survey_name = list(data.keys())[0]
string_question = ""
answers_list = []
pages_list = []

for page in list(data[survey_name].keys()):
    
    questions_list_for_page = []
    
    for question_num, metadata in data[survey_name][page].items():
        for item, item_text in metadata.items():
            if isinstance(item_text, list):
                answers_list = item_text
            else:
                string_question = item_text
        create_questions_string_json(questions_list_for_page, string_question, answers_list)
    
    create_page_json(pages_list, questions_list_for_page, page)


survey_data = {
    "title": survey_name,
    "pages": pages_list
}

url = "https://api.surveymonkey.com/v3/surveys"

response = requests.post(url, headers=headers, json=survey_data)

if response.status_code == 201:
    print("Survey created successfully!")
    survey = response.json()
    print(json.dumps(survey, indent=2))
else:
    print(f"Failed to create survey: {response.status_code}")
    print(response.json())

