import json

def format_data(data):
    formatted_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            if "links" in value:
                formatted_value = value["links"]
            else:
                formatted_value = format_data(value)
        else:
            formatted_value = None
        formatted_data[key] = formatted_value
    return formatted_data

with open('chatgpt.json', 'r') as f:
    data = json.load(f)

formatted_data = format_data(data)
print(json.dumps(formatted_data, indent=2))

with open('chatgpt.json', 'w',encoding='utf-8') as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=2)
