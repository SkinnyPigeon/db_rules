import requests
from jwt_functions import validate_jwt

def get_staff_tables(jwt, hospital):
    url = "http://localhost:5001/staff_tables/departments"
    body = {
        'hospital_id': hospital
    }
    headers = {
        "Authorization": f"Bearer {jwt}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.request("POST", url, headers=headers, json=body)
        if response.status_code == 200:
            return {"status_code": response.status_code, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": response.text}
    except Exception as e:
        print("Failed to make request. Reason: {}​".format(str(e)))

# def check_staff_member(jwt, hospital):
#     try: 
#         response = get_staff_tables(jwt, hospital)
#         jwt_response = validate_jwt(jwt)
#         if response['status_code'] == 200 & jwt_response['status_code'] == 200:
#             staff_table = response['body']
#             for staff_member in staff_table:
#                 if jwt_response['body']['userID'] == staff_member['serums_id']:
#                     print("YUP")
#     except Exception as e:
#         print(f"Error: {e}")


def check_staff_member(jwt):
    id_and_department = {}
    jwt_response = validate_jwt(jwt)
    # print(jwt_response)
    if jwt_response['status_code'] == 200 and 'PATIENT' not in jwt_response['body']['groupIDs']:
        hospital = jwt_response['body']['orgID']
        staff_response = get_staff_tables(jwt, hospital)
        # print(staff_response)
        if staff_response['status_code'] == 200:
            for staff_member in staff_response['body']:
                if jwt_response['body']['userID'] == staff_member['serums_id']:
                    id_and_department['id'] = jwt_response['body']['userID']
                    id_and_department['department'] = staff_member['department_id']
    else:
        print(jwt_response['body']['groupIDs'])
    if bool(id_and_department):
        return id_and_department
    else:
        return False