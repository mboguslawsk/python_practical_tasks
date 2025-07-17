# """The script accepts a JSON file with questions for the survey."""
# """It creates survey using API request and JSON data."""


import requests, json, sys, os

try:
    questions_file = sys.argv[1]
    emails_file = sys.argv[2]
except IndexError:
    print("Usage: python3 task2.py <questions.json> <recipients.txt>")
    sys.exit(1)


ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
if not ACCESS_TOKEN:
    raise RuntimeError("ACCESS_TOKEN not set in environment.")



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



def form_output_data(questions_file):
    with open(questions_file, "r") as f:
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

    return survey_data



def send_api_survey(url, headers, survey_data):

    response = requests.post(url, headers=headers, json=survey_data)

    if response.status_code == 201:
        print("Survey created successfully!")
        survey = response.json()
        print(json.dumps(survey, indent=2))
    else:
        print(f"Failed to create survey: {response.status_code}")
        print(response.json())
    return response.status_code, survey["id"]


def create_email_collector(url, headers, survey_id, collector_name):
    payload = {
        "type": "email",
        "survey_id": survey_id,
        "name": "Basic Email Collector",
        "email": {
            "subject": "Please take our survey",
            "body_text": "We value your feedback. Please complete our short survey."
        }
    }
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'Authorization': "Bearer {access-token}"
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        print("Survey created successfully!")
        survey = response.json()
        print(json.dumps(survey, indent=2))
        return response.json()["id"]
    else:
        print(f"Failed to create email collector: {response.status_code}")
        print(response.json())



survey_data = form_output_data(questions_file)

url = "https://api.surveymonkey.com/v3/surveys"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

status_code, survey_id = send_api_survey(url, headers, survey_data)





collector_name = "Email Collector"
survey_id="419201889"
url = f"https://api.surveymonkey.com/v3/surveys/{survey_id}/collectors"

collector_id = create_email_collector(url, headers, survey_id, collector_name)

print(collector_id)