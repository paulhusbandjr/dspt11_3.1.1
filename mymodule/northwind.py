import sqlite3

# connect to the database
con = sqlite3.connect("../northwind_small.sqlite3")
cur = con.cursor()

""" Requested queries."""

# get the 10 most expensive items by UnitPrice
expensive_items = """select UnitPrice from Product order by UnitPrice desc limit 10"""
expensive_items_result = cur.execute(expensive_items).fetchall()

# get the average hire age
avg_hire_age = """select avg(HireDate-BirthDate) from Employee"""
avg_hire_age_result = cur.execute(avg_hire_age).fetchall()

# get the average hire age by city
avg_age_by_city = """select city, avg(HireDate-BirthDate) from Employee
                     group by city"""
avg_age_by_city_result = cur.execute(avg_age_by_city).fetchall()

# get the 10 most expensive items by UnitPrice and supplier
ten_most_expensive = """select UnitPrice, CompanyName  from Product
                        left join Supplier
                        on Product.SupplierId = Supplier.Id 
                        order by UnitPrice desc limit 10"""
ten_most_expensive_result = cur.execute(ten_most_expensive).fetchall()

# get the largest category by unique ids
largest_category = """select max(countids), CategoryName as maxids from (select count(CategoryId) as countids, CategoryName from Product
                      left join Category
                      on Product.CategoryId=Category.Id
                      group by CategoryName)
                      """
largest_category_result = cur.execute(largest_category).fetchall()

# get the employee with the most territories

