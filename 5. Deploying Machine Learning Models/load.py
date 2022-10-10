#!/usr/bin/env python
# coding: utf-8

import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as model_in:
    model = pickle.load(model_in)
with open(dv_file, 'rb') as dv_in:
    dv = pickle.load(dv_in)


customer = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

#DictVectorizer expects a list of dictionaries
X = dv.transform([customer])
y_pred = model.predict_proba(X)[0,1]
churn = y_pred >= 0.5

result = {
    'churn_probability': y_pred, #np float into python float
    'churn': churn #np boolean into python boolean
}

#we return a dictionary that will be converted into a json with jsonify
print(result)