import requests
from rules import allow_rule, deny_rule, allow_rule_2, allow_rule_3, allow_department_rule
from jwt_functions import get_jwt, validate_jwt, password, patient_emails, staff_emails, admin_emails
from adding_and_removing_rules import create_rule, del_rule
from staff_tables import get_staff_tables, check_staff_member

response = get_jwt(staff_emails['zmc'], password)
print(response)
jwt = response['body']['resource_obj']['access']
# print(validate_jwt(jwt))

# response = create_rule(jwt, allow_department_rule)
# print(response)


staff_response = check_staff_member(jwt)
# print(staff_response)

# check_staff_member(jwt, hospital='ZMC')

# def validate_rules(jwt)

def get_rules(jwt, grantor_id, grantee_id):
    url = 'http://localhost:30001/v1/api/getRules'
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }
    data = {
        "filters": [
            {
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

check = get_rules(jwt, 118, 270)
print(check)

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

# rules = get_rules(jwt, 118, 270)
# print(rules)
# tags = sum_up_rules(rules)
# print(tags)

def validate_doctor(group_ids):
    if 'MEDICAL_STAFF' in group_ids:
        return True
    else:
        return False

def validate_admin(group_ids):
    if 'MEDICAL_ADMIN' in group_ids:
        return True
    else:
        return False

def validate_patient(group_ids):
    if 'PATIENT' in group_ids:
        return True
    else:
        return False

# check = validate_doctor(jwt['body']['groupIDs'])
# print(check)
