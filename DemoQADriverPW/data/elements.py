MAIN_XPATH = {
    'text_box': '//span[contains(text(), "Text Box")]',
    'check_box': '//span[contains(text(), "Check Box")]',
    'radio_button': '//span[contains(text(), "Radio Button")]',
    'web_tables': '//span[contains(text(), "Web Tables")]',
    'buttons': '//span[contains(text(), "Buttons")]',
    'links': '//span[contains(text(), "Links")]',
}

TEXT_BOX = {
    'INPUT': {
        'full_name': '//*[@id="userName"]',
        'email': '//*[@id="userEmail"]',
        'current_address': '//*[@id="currentAddress"]',
        'permanent_address': '//*[@id="permanentAddress"]'
    },
    'BUTTON': {
        "submit": '//*[@id="submit"]'
    },
    'READ_ALL_PARAMS': {
        'result': '//*[@id="output"]'
    }
}


CHECK_BOX = {
    'BUTTON': {
        'expand': '//*[@id="tree-node"]/div/button[1]',
        'collapse': '//*[@id="tree-node"]/div/button[2]'
    },
    'CHECK_BOX': {
        'home': '//*[@id="tree-node"]/ol/li/span/label/span[1]',
        'desktop': '//*[@id="tree-node"]/ol/li/ol/li[1]/span/label/span[1]',
        'notes': '//*[@id="tree-node"]/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]',
        'downloads': '//*[@id="tree-node"]/ol/li/ol/li[3]/span/label/span[1]'
    },
    'READ_ALL_PARAMS': {
        'result': '//*[@id="result"]'
    }
}

WEB_TABLES = {
    'INPUT': {
        'first_name': '//*[@id="firstName"]',
        'last_name': '//*[@id="lastName"]',
        'email': '//*[@id="userEmail"]',
        'age': '//*[@id="age"]',
        'salary': '//*[@id="salary"]',
        'department': '//*[@id="department"]'
    },
    'BUTTON': {
        'add': '//*[@id="addNewRecordButton"]',
        'submit': '//*[@id="submit"]',
    }
}