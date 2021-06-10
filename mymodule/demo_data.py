import sqlite3

""" THIS FILE ASSUMES YOU DO NOT ALREADY HAVE THE DATABASE 'demo_data'
AND THERE IS NO TABLE 'demo'."""

# setup the connection
con = sqlite3.connect('demo_data.sqlite3')
cur = con.cursor()

# testing for existence of demo_table by getting count of tables with same name
n = cur.execute("""SELECT count(name)
               FROM sqlite_master
               WHERE type='table'
               AND name='demo' """)


# to make sure the demo table is fresh, drop it then recreate it
refresh = """drop table demo"""
cur.execute(refresh)
# creating the demo table
create = """create table demo(s varchar(5), x int, y int) """
cur.execute(create)

# inserting data into the table
r1 = """insert into demo (s, x, y) values ('g', 3, 9)"""
r2 = """insert into demo (s, x, y) values ('v', 5, 7)"""
r3 = """insert into demo (s, x, y) values ('f', 8, 7)"""
cur.execute(r1)
cur.execute(r2)
cur.execute(r3)
con.commit()

# requested queries
row_count_query = """select count(s) from demo"""
row_count_result = cur.execute(row_count_query).fetchall()
row_count = row_count_result[0][0]
xy_at_least_5_query = """select count(x), count(y) from demo where x > 4 and y > 4"""
xy_at_least_5_result = cur.execute(xy_at_least_5_query).fetchall()
xy_at_least_5 = xy_at_least_5_result[0][0]
unique_y_query = """select count(distinct(y)) from demo"""
unique_y_result = cur.execute(unique_y_query).fetchall()
unique_y = unique_y_result[0][0]

con.close()
