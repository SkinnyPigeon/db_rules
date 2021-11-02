import requests
from rules import allow_rule, deny_rule, allow_rule_2, allow_rule_3
from jwt_functions import get_jwt, validate_jwt, password, patient_emails, staff_emails, admin_emails
from adding_and_removing_rules import create_rule, del_rule

jwt = get_jwt(patient_emails['zmc'], password)
jwt_decoded = validate_jwt(jwt['body']['resource_obj']['access'])
print(jwt_decoded)

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

# rules = get_rules(jwt, 118, 270)

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

    
# tags = sum_up_rules(rules)
# print(tags)