The Search API is a RESTful API that allows you to search for data in a database.

It is used in the following way:
```bash	
curl "https://gollnickdatarag.azurewebsites.net/api/rag?query=An%20welchen%20Wochentagen%20finden%20die%20Kurse%20statt%3F"
```
The API returns the following JSON:
```json
{"answer": "Die Kurse finden an f\u00fcnf aufeinanderfolgenden Tagen von Montag bis Freitag statt."}
```