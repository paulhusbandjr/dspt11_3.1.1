import sqlite3
import pandas as pd

df = pd.read_csv('../../buddymove_holidayiq.csv',
                 names=['User_Id', 'Sports', 'Religious', 'Nature',
                        'Theatre', 'Shopping', 'Picnic'],
                 skiprows=1)
con = sqlite3.connect('buddymove_holidayiq.sqlite3')
con_rowfactory = sqlite3.Row
curs = con.cursor()
review = df.to_sql('review', con, if_exists='replace')
num_users = """select count('user id') from review"""
nature_and_shopping_reviewers = """select count('user id')
                                   from review 
                                   where Nature >= 100
                                   and Shopping >= 100"""
avg_num_reviews = """select avg(Sports), avg(Religious), avg(Nature), 
                     avg(Theatre), avg(Shopping), avg(Picnic) from review"""

print('Number of rows: ', curs.execute(num_users).fetchall()[0][0])
print('Number of reviewers with 100 reviews in Nature and Shopping: ',
      curs.execute(nature_and_shopping_reviewers).fetchall()[0][0])
print('Average number of reviews: ', curs.execute(avg_num_reviews).fetchall())

con.close()
