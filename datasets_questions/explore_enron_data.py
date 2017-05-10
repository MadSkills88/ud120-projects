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
print "number of people: ", len(enron_data)
print "number of features: ", len(enron_data["SKILLING JEFFREY K"])
poi_count = 0
for person in enron_data:
    if enron_data[person]["poi"] == 1: poi_count +=1
print "persons of interest: ", poi_count
print "JAMES PRENTICE: total stock value: ", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "WESLEY COLWELL: number of messages to poi: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "JEFFREY K SKILLING: value of exercized stock options: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
