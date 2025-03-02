from django.shortcuts import render, redirect, get_object_or_404
from .mongo_utils import create_employee, read_employee, update_employee, delete_employee, db
from bson.objectid import ObjectId


def employee_list(request):
    employees = list(db.employees.find())
    for employee in employees:
        employee['id'] = str(employee['_id'])
    return render(request, 'employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        employee_data = {
            "name": request.POST['name'],
            "age": request.POST['age'],
            "department": request.POST['department'],
            "salary": request.POST['salary'],
            "hire_date": request.POST['hire_date'],
            "projects": [],
        }
        create_employee(employee_data)
        return redirect('employee_list')
    return render(request, 'employee_create.html')

def employee_update(request, employee_id):
    employee_id = ObjectId(employee_id)
    employee = read_employee(employee_id)
    if request.method == 'POST':
        update_data = {
            "name": request.POST['name'],
            "age": request.POST['age'],
            "department": request.POST['department'],
            "salary": request.POST['salary'],
            "hire_date": request.POST['hire_date'],
        }
        update_employee(employee_id, update_data)
        return redirect('employee_list')
    return render(request, 'employee_update.html', {'employee': employee})

def employee_delete(request, employee_id):
    employee_id = ObjectId(employee_id)
    employee = read_employee(employee_id)
    if request.method == 'POST':
        delete_employee(employee_id)
        return redirect('employee_list')
    return render(request, 'employee_delete.html', {'employee': employee})