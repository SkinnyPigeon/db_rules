allow_rule = {
    "grantor": {
        "type": "INDIVIDUAL",
        "id": "118"
    },
    "grantee": {
        "type": "INDIVIDUAL",
        "id": "122",
        "orgId": "ZMC"
    },
    "access": [
        {
            "name": "diagnostic"
        }
    ],
    "expires": "2022-07-13T19:55:00.000Z",
    "action": "ALLOW"
}

allow_rule_2 = {
    "grantor": {
        "type": "INDIVIDUAL",
        "id": "118"
    },
    "grantee": {
        "type": "INDIVIDUAL",
        "id": "122",
        "orgId": "ZMC"
    },
    "access": [
        {
            "name": "diagnostic"
        },
        {
            "name": "operations"
        }
    ],
    "expires": "2022-07-13T19:55:00.000Z",
    "action": "ALLOW"
}

allow_rule_3 = {
    "grantor": {
        "type": "INDIVIDUAL",
        "id": "118"
    },
    "grantee": {
        "type": "INDIVIDUAL",
        "id": "122",
        "orgId": "ZMC"
    },
    "access": [
        {
            "name": "patient_address"
        }
    ],
    "expires": "2022-07-13T19:55:00.000Z",
    "action": "ALLOW"
}

deny_rule = {
    "grantor": {
        "type": "INDIVIDUAL",
        "id": "118"
    },
    "grantee": {
        "type": "INDIVIDUAL",
        "id": "122",
        "orgId": "ZMC"
    },
    "access": [
        {
            "name": "diagnostic"
        }
    ],
    "expires": "2022-07-13T19:55:00.000Z",
    "action": "DENY"
}

allow_department_rule = {
    "grantor": {
        "type": "INDIVIDUAL",
        "id": "118"
    },
    "grantee": {
        "type": "DEPARTMENT",
        "id": "4",
        "orgId": "ZMC"
    },
    "access": [
        {
            "name": "diagnostic"
        }
    ],
    "expires": "2022-07-13T19:55:00.000Z",
    "action": "ALLOW"
}