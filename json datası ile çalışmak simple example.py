# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:31:04 2021

@author: sabo
"""

import json
data ='{"firstname" : "Burak","lastname":"alkaya"}'
y = json.loads(data)
print(y["lastname"])
print(y["firstname"])

customer ={
    "firstname":"Burak",
    "email":"hadbfvadbsv@gmail.com",
    "adress":"hatay samandağ"
    }

customerJson=json.dumps(customer)
print(customer)