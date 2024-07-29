import requests

URL = "https://opentdb.com/api.php"

PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}

question_data = []

try:
    response = requests.get(URL, params=PARAMETERS)
    response.raise_for_status()

    for result in response.json()["results"]:
        new_question = {
            "category": result["category"],
            "type": result["type"],
            "difficulty": result["difficulty"],
            "question": result["question"],
            "correct_answer": result["correct_answer"],
            "incorrect_answers": result["incorrect_answers"]
        }
        question_data.append(new_question)

except:
    print("Exception while calling opentdb API")
