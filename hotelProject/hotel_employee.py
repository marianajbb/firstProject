from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["employeeProject"]
employees = db["employees"]

def create_employee(employee_data):
    result = employees.insert_one(employee_data)
    return result.inserted_id

def read_employee(employee_id):
    employee = employees.find_one({"_id": employee_id})
    return employee

def update_employee(employee_id, update_data):
    result = employees.update_one({"_id": employee_id}, {"$set": update_data})
    return result.modified_count

def delete_employee(employee_id):
    result = employees.delete_one({"_id": employee_id})
    return result.deleted_count


employee1 = {
    "name": "Bob Johnson",
    "age": 28,
    "department": "IT",
    "salary": 75000,
    "hire_date": "2023-05-15",
    "projects": [],
}

#employee_to_create = create_employee(employee1)
#print(f"Created employee with ID: {employee_to_create}")

#employee_to_read = read_employee(ObjectId("67b61f011e4a68ebe4b7d9c4"))
#print(f"Employee 1: {employee_to_read}")

#employee_to_delete = read_employee(ObjectId("67b630fa3475f43d1758a8e4"))
#deleted_employee = delete_employee(ObjectId("67b630fa3475f43d1758a8e4"))
#print(f"Deleted Employee: {employee_to_delete}")

#employee_to_update = update_employee(ObjectId("67b61f011e4a68ebe4b7d9c4"), {"name" : "Michelle Brown"})
#print(f"Updated Employee: {employee_to_update}")

