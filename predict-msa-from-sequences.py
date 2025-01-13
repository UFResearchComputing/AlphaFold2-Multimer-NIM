import requests
import json

url = "http://0:8000/protein-structure/alphafold2/multimer/predict-msa-from-sequences"
sequences = ["MNVIDIAIAMAI", "IAMNVIDIAAI"]  # Replace with the actual sequences you want to perform structure prediction on.

headers = {
    "content-type": "application/json"
}

data = {
    "sequences": sequences,
    "databases": ["uniref90", "mgnify", "small_bfd"]
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.ok:
    print("Request succeeded:", response.json())
else:
    print("Request failed:", response.status_code, response.text)
