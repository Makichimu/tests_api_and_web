import json
import os

def save_response_to_file(response, filename='test_ibs\\tests\\api_responses.json'):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)
    with open(filename, 'r') as f:
        api_responses = json.load(f)
    if response.status_code == 204:
        api_responses.append({})
    else:
        api_responses.append(response.json())
    with open(filename, 'w') as f:
        json.dump(api_responses, f, indent=4)

def save_response_to_file_web(response_text, status_code, filename='test_ibs\\tests\\web_responses.json'):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            json.dump([], f)
    with open(filename, 'r') as f:
        web_responses = json.load(f)
    if status_code == 204 or not response_text:
        web_responses.append({})
    else:
        try:
            web_responses.append(json.loads(response_text))
        except json.JSONDecodeError:
            print(f"Warning: could not decode JSON: {response_text}")
            web_responses.append({})
    with open(filename, 'w') as f:
        json.dump(web_responses, f, indent=4)

