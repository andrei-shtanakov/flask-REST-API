import json, requests

headers = {
    'Accept': 'application/json',
}

payload = {
    "rangeEnd": "2020-09-06T00:00:00",
    "rangeStart": "2020-09-02T00:00:00",
    "graphs": [
        {
            "formula": "CPULoad5min*1r"
        }
    ],
    "data": {
        "CPULoad5min": {
            "range": [
                "2020-09-02T00:01:49",
                "2020-09-02T00:06:37",
                "2020-09-02T00:11:36",
                "2020-09-02T00:16:54",
                "2020-09-02T00:21:35",
                "2020-09-02T00:26:32"
            ],
            "values": [
                123,
                112,
                78,
                111,
                111,
                95
            ]
        }
    }
}

r = requests.post('http://127.0.0.1:8000/', headers=headers, json=payload)
print(r.status_code)
z = json.loads(r.text)
print(z)
