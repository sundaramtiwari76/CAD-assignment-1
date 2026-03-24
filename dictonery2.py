employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 25000,
    "city": "Lucknow"
}

print(employee)
#add values
employee["department"] = "IT"
print(employee)
#remove values
employee.pop("salary")
print(employee)
