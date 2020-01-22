from queries import Queries

queries = Queries()

print(queries.customers())
print(queries.coffins())
print(queries.employees())



# Output
# SELECT * FROM Customer ORDER BY last_name ASC, first_name ASC
# SELECT * FROM Coffin
# SELECT * FROM Employee ORDER BY last_name ASC, first_name ASC