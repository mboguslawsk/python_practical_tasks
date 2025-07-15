# The script should accept a JSON file with questions for the survey and a text file with a list of email addresses.
import requests
import http.client

filename="secrets.txt"
with open(filename, "r") as file:
    for line in file:
        ACCESS_TOKEN=line.split('"')[1]

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}


survey_data = {
    "title": "My Sample Survey",
    "pages": [
        {
            "title": "Page 1",
            "questions": [
                {
                    "headings": [
                        {
                            "heading": "Which monkey would you rather have as a pet?"
                        }
                    ],
                    "position": 1,
                    "family": "single_choice",
                    "subtype": "vertical",
                    "answers": {
                        "choices":[
                            {
                                "text": "Capuchin"
                            },
                            {
                                "text": "Mandrill"
                            },
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
            ]
        }
    ]
}


url = "https://api.surveymonkey.com/v3/surveys"

response = requests.post(url, headers=headers, json=survey_data)

if response.status_code == 201:
    print("Survey created successfully!")
    survey = response.json()
    print(json.dumps(survey, indent=2))
else:
    print(f"Failed to create survey: {response.status_code}")
    print(response.text)


# conn = http.client.HTTPSConnection("api.surveymonkey.com")

# payload = "{\"title\":\"GD SURVEY BM\",\"from_template_id\":\"\",\"from_survey_id\":\"\",\"from_team_template_id\":\"\",\"nickname\":\"My Survey\",\"language\":\"en\",\"buttons_text\":{\"next_button\":\"string\",\"prev_button\":\"string\",\"exit_button\":\"string\",\"done_button\":\"string\"},\"custom_variables\":{},\"footer\":true,\"folder_id\":\"\",\"theme_id\":1506280,\"quiz_options\":{\"is_quiz_mode\":true,\"default_question_feedback\":{\"correct_text\":\"string\",\"incorrect_text\":\"string\",\"partial_text\":\"string\"},\"show_results_type\":\"string\",\"feedback\":{\"ranges_type\":\"string\",\"ranges\":[{\"min\":0,\"max\":0,\"message\":\"string\"}]}},\"pages\":[{\"questions\":[\"See formatting question types for more details\"]}]}"

# headers = {
#     'Content-Type': "application/json",
#     'Accept': "application/json",
#     'Authorization': f"Bearer {ACCESS_TOKEN}"
#     }

# conn.request("POST", "/v3/surveys", payload, headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))