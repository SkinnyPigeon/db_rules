import requests
from rules import allow_rule, deny_rule

jwts = {
    'ustan': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2NDQ1ODczLCJqdGkiOiIyZGU4MTYxZGVkNjc0OGFiYjNmMzM0ZDdmMjBhOTA2ZSIsInVzZXJJRCI6MTE3LCJpc3MiOiJTZXJ1bXNBdXRoZW50aWNhdGlvbiIsImlhdCI6MTYzNTg0MTA3Mywic3ViIjoicHBwMUB1c3Rhbi5jb20iLCJncm91cElEcyI6WyJQQVRJRU5UIl0sIm9yZ0lEIjoiVVNUQU4iLCJkZXB0SUQiOm51bGwsImRlcHROYW1lIjpudWxsLCJzdGFmZklEIjpudWxsLCJuYW1lIjpudWxsLCJhdWQiOiJodHRwczovL3NoY3Muc2VydW1zLmNzLnN0LWFuZHJld3MuYWMudWsvIn0.ENfiS5_mSIuvvrKEfTPDC9sQjZQb63L_FLix2Gk58_Q',
    'fcrb': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2NDQ2MTM2LCJqdGkiOiI4NmU1ZjFkZTBhZGU0MWNkYjZjYTM0MzFkYmIzOGJjOSIsInVzZXJJRCI6MTE5LCJpc3MiOiJTZXJ1bXNBdXRoZW50aWNhdGlvbiIsImlhdCI6MTYzNTg0MTMzNiwic3ViIjoicHBwMUBmY3JiLmNvbSIsImdyb3VwSURzIjpbIlBBVElFTlQiXSwib3JnSUQiOiJGQ1JCIiwiZGVwdElEIjpudWxsLCJkZXB0TmFtZSI6bnVsbCwic3RhZmZJRCI6bnVsbCwibmFtZSI6bnVsbCwiYXVkIjoiaHR0cHM6Ly9zaGNzLnNlcnVtcy5jcy5zdC1hbmRyZXdzLmFjLnVrLyJ9.5BRjOT7wN07OI4kItX2nPXnGmzMALcDlpOn0LRdxGCU',
    'zmc': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2NDQ2MjQ2LCJqdGkiOiI3NjBkZTFjNjk0NmM0ZDgwYWFhYjQzNGE2YTFmYzViYSIsInVzZXJJRCI6MTE4LCJpc3MiOiJTZXJ1bXNBdXRoZW50aWNhdGlvbiIsImlhdCI6MTYzNTg0MTQ0Niwic3ViIjoicHBwMUB6bWMuY29tIiwiZ3JvdXBJRHMiOlsiUEFUSUVOVCJdLCJvcmdJRCI6IlpNQyIsImRlcHRJRCI6bnVsbCwiZGVwdE5hbWUiOm51bGwsInN0YWZmSUQiOm51bGwsIm5hbWUiOm51bGwsImF1ZCI6Imh0dHBzOi8vc2hjcy5zZXJ1bXMuY3Muc3QtYW5kcmV3cy5hYy51ay8ifQ.hHhSlsOQdI9mSLxBHJqzcnIsoNSwCXI44gkMEhzB11Q'
}

jwt = jwts['zmc']
print(jwt)

def validate_jwt(jwt):
    url = "https://authentication.serums.cs.st-andrews.ac.uk/ua/verify_jwt/"
    payload = ""
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            return {"status_code": response.status_code, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": response.text}
    except Exception as e:
        print("Failed to make request. Reason: {}​".format(str(e)))

response = validate_jwt(jwt)
print(response)

def create_rule(jwt, rule):
    pass

def del_rule(jwt, rule_id):
    pass


def get_rules(jwt):
    url = 'http://localhost:30001/v1/api/getRules'
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }
    data = {
        "filters": [{
                "filterType": "SIMPLE",
                "key": "grantor.id",
                "value": "david@acc.com"
            }
        ]
    }
    response = requests.request('POST', url, headers=headers, json=data)
    print(response.text)

get_rules(jwt)
    