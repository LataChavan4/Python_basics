import requests

data = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
data.raise_for_status()
qsn = data.json()
question_data = qsn["results"]
print(question_data)
