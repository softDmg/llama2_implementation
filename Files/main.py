# main.py
import requests

def generate_response(user_input):
    headers = {"Content-Type": "application/json"}
    base_url = "https://b308-34-143-139-150.ngrok-free.app"  # Update this with your actual base URL
    endpoint = f"{base_url}/generate"
    response = requests.post(endpoint, headers=headers, json={
        "inputs": "\n\n### Instructions:\n" + user_input + "\n\n### Response:\n",  # Use 'inputs'
        "parameters": {"stop": ["\n", "###"]}  # Use 'parameters' for additional options like 'stop'
    })

    print("Raw response:", response.text)  # Log the raw response

    try:
        return response.json()
    except ValueError:
        return {"error": "Invalid JSON response"}
