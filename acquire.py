import os

import pandas as pd

from env import get_connection


def get_titanic_data():
    

    filename = 'titanic.csv'
    
    if os.path.isfile(filename):
        
        print('found data')
    
        return pd.read_csv(filename)

    else:
        
        print('retrieving data')
        
        url = get_connection('titanic_db')
        
        query = '''
                SELECT *
                FROM passengers
                '''
        
        titanic = pd.read_sql(query, url)
        
        titanic.to_csv(filename, index = 0)
        
        return titanic
    
    
def get_iris_data():

    filename = 'iris.csv'
    
    if os.path.isfile(filename):
        
        print('found data')
    
        return pd.read_csv(filename)

    else:
        
        print('retrieving data')
        
        url = get_connection('iris_db')
        
        query = '''
                SELECT *
                FROM measurements
                LEFT JOIN species ON measurements.species_id =    
                species.species_id
                '''
        
        iris = pd.read_sql(query, url)
        
        iris.to_csv(filename, index = 0)
        
        return iris
    
    
def get_telco_data():

    filename = 'telco.csv'
    
    if os.path.isfile(filename):
        
        print('found data')
    
        return pd.read_csv(filename)

    else:
        
        print('retrieving data')
        
        url = get_connection('telco_churn')
        
        query = '''
                SELECT *
                FROM customer_churn
                '''
        
        telco = pd.read_sql(query, url)
        
        telco.to_csv(filename, index = 0)
        
        return telco
    
    
    