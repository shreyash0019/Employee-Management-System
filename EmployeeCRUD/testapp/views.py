from django.shortcuts import render, redirect, get_object_or_404
from testapp.models import Employee
from testapp.forms import EmployeeForm
from django.contrib.auth.decorators import login_required

# View for retrieving the list of employees
@login_required
def retrive_view(request):
    emp_list = Employee.objects.all()
    print(f"Employees passed to template")
    return render(request, 'testapp/index.html', {'emp_list': emp_list})

# View for inserting new employee data
@login_required
def insert_view(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print("emp added")
        return redirect('/')
    return render(request, 'testapp/insert.html', {'form': form})

# View for deleting an employee
@login_required
def delete_view(request, id):
    try:
        # Fetch the specific employee instance
        employee = Employee.objects.get(id=id)
        employee.delete()  # Call delete on the instance
        print(f"Employee with ID {id} deleted.")
    except Employee.DoesNotExist:
        print(f"Employee with ID {id} does not exist.")
    return redirect('/')

# View for updating employee data
@login_required
def update_view(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        print(f"Employee with ID {id} updated.")
        return redirect('/')
    return render(request, 'testapp/update.html', {'form': form})

# View for displaying employee details
@login_required
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    return render(request, 'employee_detail.html', {'employee': employee})

# settings.py
LOGIN_URL = 'login'  # Replace with your login URL name
