import requests
from rules import allow_rule, deny_rule, allow_rule_2, allow_rule_3

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

# response = validate_jwt(jwt)
# print(response)

def create_rule(jwt, rule):
    url = "http://localhost:30001/v1/api/rule"
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.request("POST", url, headers=headers, json=rule)
        if response.status_code == 200:
            return {"status_code": response.status_code, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": response.text}
    except Exception as e:
        print("Failed to make request. Reason: {}​".format(str(e)))

# rule_id_2 = create_rule(jwt, allow_rule_2)
# rule_id_3 = create_rule(jwt, allow_rule_3)
# rule_id_4 = create_rule(jwt, deny_rule)

# print(rule_id_2)
# print(rule_id_3)
# print(rule_id_4)

allow_rule_id = 'RULE_8e87c6bb-1166-4463-86b9-a8536c917a5c'
allow_rule_id_2 = 'RULE_8985ec49-b6d8-4054-8556-8d41ece8890e'
allow_rule_id_3 = 'RULE_2a95ab90-fcee-4801-8f90-55dae9550292'
deny_rule_id = 'RULE_f11f763b-b32d-4104-8c70-b39f39d9656f'
deny_rule_id_2 = 'RULE_80cee90a-3414-4505-818c-822844baa842'

def del_rule(jwt, rule_id):
    url = f"http://localhost:30001/v1/api/rule/{rule_id}"
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.delete(url, headers=headers)
        if response.status_code == 200:
            return {"status_code": response.status_code, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": response.text}
    except Exception as e:
        print("Failed to make request. Reason: {}​".format(str(e)))

# deleted_rule = del_rule(jwt, deny_rule_id)
# print(deleted_rule)

def get_rules(jwt, grantor_id, grantee_id):
    url = 'http://localhost:30001/v1/api/getRules'
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }
    data = {
        "filters": [{
                "filterType": "SIMPLE",
                "key": "grantor.id",
                "value": grantor_id
            },
            {
                "filterType": "NOT_EXPIRED"
            },
            {
                "filterType": "SIMPLE",
                "key": "grantee.id",
                "value": grantee_id
            }

        ]
    }
    response = requests.request('POST', url, headers=headers, json=data)
    return response.json()

rules = get_rules(jwt, 118, 270)

def sum_up_rules(rules):
    allow_tags = set()
    deny_tags = set()
    for rule in rules:
        print(rule)
        for tag in rule['access']:
            if rule['action'] == 'ALLOW':
                allow_tags.add(tag['name'])
            if rule['action'] == 'DENY':
                deny_tags.add(tag['name'])

    results = allow_tags ^ deny_tags
    return list(results)

    
tags = sum_up_rules(rules)
print(tags)