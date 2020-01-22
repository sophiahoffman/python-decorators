
# had to add self as an argument so it passes through to function in the call from inside class
def sort_by_name(decorated):
    def sort_asc(self):
        return f"{decorated(self)} ORDER BY last_name ASC, first_name ASC"
    return sort_asc


class Queries:

    @sort_by_name
    def customers(self):
        return "SELECT * FROM Customer"

    def coffins(self):
        return "SELECT * FROM Coffin"

    @sort_by_name
    def employees(self):
        return "SELECT * FROM Employee"

    def gravestones(self):
        return "SELECT * FROM GraveStones"

    @sort_by_name
    def deceased(self):
        return "SELECT * FROM Deceased"

    def obelisks(self):
        return "SELECT * FROM Obelisk"

    @sort_by_name
    def vendors(self):
        return "SELECT * FROM Vendor"


if __name__ == "__main__":
    queries = Queries()
    print(queries.customers())