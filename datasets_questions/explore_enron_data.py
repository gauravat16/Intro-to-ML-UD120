#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

poi_guys = open("../final_project/poi_names.txt","r")

print len(enron_data)

count =0;
data = dict()
count_sal = 0;
count_mail = 0;
count_payments = 0;
for i in enron_data:
    print i
    print enron_data[i]
    if (enron_data[i]["poi"] == 1):
        count = count + 1;


    if (enron_data[i]["salary"] != "NaN"):
        count_sal=count_sal+1;

    if (enron_data[i]["email_address"] != "NaN"):
        count_mail=count_mail+1;

    if (enron_data[i]["total_payments"] == "NaN" and enron_data[i]["poi"] == 1):
        count_payments = count_payments + 1;

print count,count_sal,count_mail,count_payments

count =0
for j in poi_guys.readlines():
    count = count + 1;
print count -2

print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["LAY KENNETH"]["total_stock_value"]

