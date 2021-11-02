
import requests

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
allow_department_id = 'RULE_c2082153-b5cf-4c67-8a85-036c973dd8d3'

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