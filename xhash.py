from datetime import date

# Import writer class from csv module
from csv import DictWriter


class XHash(object):

    def __init__(self, name, username,  pwd, code):
        self.name = name
        self.username = username
        self.pwd = pwd
        self.coded = code
        self.day_created = str(date.today())
    
    def saveToDB(self):
        # Save pwd to excel db
        # only save name, coded and times
        
        # list of column names
        field_names = ['name', 'username', 'code', 'day_created']
        # Dictionary that we want to add as a new row
        values = {'name': self.name, 'username': self.username, 'code': self.coded, 'day_created': self.day_created}
        
        with open('static/data.csv', 'a') as f_object:
            # Pass the file object and a list
            # of column names to DictWriter()
            # You will get a object of DictWriter
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            # Pass the dictionary as an argument to the Writerow()
            dictwriter_object.writerow(values)
 

    def changeDateToday(self):
        self.day_created = str(date.today())

    def __str__(self):
        message = f'Username: {self.username} - Program: {self.name}'
        return message
    