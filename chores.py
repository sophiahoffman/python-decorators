

def assignment(task):
    def assigned(role):
        return f"{task(role)} by the {role}."
    return assigned

@assignment
def laundry(role):
    return "The dirty laundry was cleaned"

@assignment
def garbage(role):
    return "The garbage was taken out"

@assignment
def dust(role):
    return "The house was dusted"

@assignment
def groom(role):
    return "The dog was brushed"

print(laundry("kids"))
print(garbage("mom"))
print(dust("dad"))
print(groom("dog"))

