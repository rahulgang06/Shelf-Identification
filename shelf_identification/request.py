import requests

url = 'http://localhost:8000/api/identify-shelf-shapes/'  # 
data = {
    "layout_data": [
        ['G', 'G', 'G', 'M', 'M', 'M', 'M'],
        ['G', 'B', 'G', 'M', 'N', 'N', 'M'],
        ['G', 'G', 'G', 'M', 'N', 'N', 'M'],
        ['B', 'B', 'B', 'B', 'B', 'N', 'N']
    ]
}

response = requests.post(url, json=data)

if response.status_code == 200:
    json_response = response.json()
    print(json_response)
else:
    print("Error:", response.status_code)
