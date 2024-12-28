import json

# Python dictionary
data = {
    "name": "John Doe",
    "age": 30,
    "skills": ["Python", "JavaScript"],
    "is_employed": True
}

# Serialize to JSON string
json_data = json.dumps(data)
print("Serialized JSON:", json_data)
