from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Employees, Attendance, EmployeeLeaves, SalaryTransactions, Departments, EmployeePersonalInfo, EmployeeContacts, EmployeeBankDetails, EmployeeBankDetails, EmployeeAssets, EmployeeGoals
from .models import Notifications, Events
from .decorators import login_required_custom, role_required
from django.contrib.auth.hashers import check_password, make_password
from django.db.models import Q
from django.http import JsonResponse
# from django.core.mail import send_mail
# from django.conf import settings
# from django.utils import timezone
# from datetime import timedelta, date
# import random
# from .models import Employees, PasswordResetOTP, EmployeePersonalInfo, EmployeeContacts, Departments, Attendance, EmployeeLeaves, SalaryTransactions, EmployeeBankDetails, EmployeeAssets, EmployeeGoals
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = Employees.objects.get(email=email)
        except Employees.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return render(request, "login.html")

        # If you are storing plain passwords (not recommended):
        if user.password == password:
            if not user.is_active:
                messages.error(request, "Your account is inactive. Please contact admin.")
                return render(request, "login.html")

            # Set session variables
            request.session["user_id"] = user.id
            request.session["user_type"] = user.user_type

            # Redirect based on user type
            if user.user_type == "Admin":
                return redirect("dashboard")
            elif user.user_type == "HR":
                return redirect("/hr_dashboard/")
            else:
                return redirect("employees_dashboard")
        else:
            messages.error(request, "Invalid email or password")
            return render(request, "login.html")

    return render(request, "login.html")


# def login_view(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         try:
#             user = Employees.objects.get(email=email)
#         except Employees.DoesNotExist:
#             messages.error(request, "Invalid email or password")
#             return render(request, "login.html")

#         # Use model helper to validate hashed password
#         if user.check_password(password):
#             if not user.is_active or user.resignation_date:
#                 messages.error(request, "Your account is inactive or resigned. Please contact admin.")
#                 return render(request, "login.html")

#             # Set session variables
#             request.session["user_id"] = user.id
#             request.session["user_type"] = user.user_type

#             # Redirect based on user_type
#             if user.user_type == "Admin":
#                 return redirect("dashboard")
#             elif user.user_type == "HR":
#                 return redirect("hr_dashboard")
#             else:
#                 return redirect("employees_dashboard")
#         else:
#             messages.error(request, "Invalid email or password")
#             return render(request, "login.html")

#     return render(request, "login.html")


# # ---------- Forgot Password (Send OTP) ----------
# def forgot_password(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         try:
#             employee = Employees.objects.get(email=email)
#         except Employees.DoesNotExist:
#             messages.error(request, "If the email is registered, you will receive an OTP shortly.")
#             return render(request, "forgot_password.html")

#         # create OTP
#         otp_value = "{:06d}".format(random.randint(0, 999999))
#         expires = timezone.now() + timedelta(minutes=15)  # 15 minute expiry

#         otp_obj = PasswordResetOTP.objects.create(
#             employee=employee,
#             otp=otp_value,
#             expires_at=expires
#         )

#         # send email (requires EMAIL settings configured)
#         subject = "Your HRMS password reset OTP"
#         message = f"Hello {employee.name},\n\nUse this OTP to reset your password: {otp_value}\nIt will expire in 15 minutes.\n\nIf you did not request this, ignore this email."
#         from_email = settings.DEFAULT_FROM_EMAIL if hasattr(settings, "DEFAULT_FROM_EMAIL") else None
#         recipient_list = [employee.email]

#         try:
#             send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#         except Exception as e:
#             # In production you should log this error.
#             messages.error(request, "Failed to send OTP email. Contact admin or check email settings.")
#             # Still allow flow for dev/test by showing message
#             return render(request, "forgot_password.html")

#         # redirect to otp verify page with request_id to avoid exposing otp id
#         return redirect('verify_otp')  # we'll keep OTP lookup by employee email in form

#     return render(request, "forgot_password.html")


# # ---------- Verify OTP ----------
# def verify_otp(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         otp_input = request.POST.get("otp")

#         try:
#             employee = Employees.objects.get(email=email)
#         except Employees.DoesNotExist:
#             messages.error(request, "Invalid email or OTP.")
#             return render(request, "verify_otp.html")

#         # find latest unused OTP for this employee
#         otp_qs = PasswordResetOTP.objects.filter(employee=employee, used=False).order_by('-created_at')
#         if not otp_qs.exists():
#             messages.error(request, "No OTP found or it has expired.")
#             return render(request, "verify_otp.html")

#         otp_obj = otp_qs.first()
#         if otp_obj.expires_at < timezone.now():
#             messages.error(request, "OTP expired. Please request a new one.")
#             return render(request, "verify_otp.html")

#         if otp_obj.otp != otp_input:
#             messages.error(request, "Invalid OTP.")
#             return render(request, "verify_otp.html")

#         # mark used
#         otp_obj.used = True
#         otp_obj.save()

#         # set a temporary session flag to allow password reset
#         request.session['password_reset_employee_id'] = employee.id
#         request.session['password_reset_allowed'] = True
#         return redirect('reset_password_confirm')

#     # GET
#     return render(request, "verify_otp.html")


# # ---------- Reset Password (after OTP verification) ----------
# def reset_password_confirm(request):
#     if request.method == "POST":
#         if not request.session.get('password_reset_allowed'):
#             messages.error(request, "OTP verification required.")
#             return redirect('forgot_password')

#         emp_id = request.session.get('password_reset_employee_id')
#         employee = get_object_or_404(Employees, id=emp_id)

#         new_password = request.POST.get("new_password")
#         confirm_password = request.POST.get("confirm_password")

#         if not new_password or new_password != confirm_password:
#             messages.error(request, "Passwords do not match.")
#             return render(request, "reset_password_confirm.html")

#         # set hashed password
#         employee.set_password(new_password)
#         employee.save()

#         # clear session keys
#         request.session.pop('password_reset_employee_id', None)
#         request.session.pop('password_reset_allowed', None)

#         messages.success(request, "Password updated successfully. Please login.")
#         return redirect('login')

#     return render(request, "reset_password_confirm.html")



@login_required_custom
@role_required("Admin")
def dashboard(request):
    user_id = request.session["user_id"]
    admin_user = Employees.objects.filter(id=user_id).first()

    total_employees = Employees.objects.count()
    total_departments = Departments.objects.count()
    total_attendance = Attendance.objects.count()

    return render(request, "dashboard.html", {
        "AdminUser": admin_user,
        "total_employees": total_employees,
        "total_departments": total_departments,
        "total_attendance": total_attendance,
    })


@login_required_custom
@role_required("HR")
def hr_dashboard(request):
    user_id = request.session["user_id"]
    total_employee = Employees.objects.filter(is_active=True).count()
    total_attendance = Attendance.objects.filter(attendance_date__month=timezone.now().month).count()
    pending_leaves = EmployeeLeaves.objects.filter(status="Pending").count()

    return render(request, "hr_dashboard.html", {
        "total_employee": total_employee,
        "total_attendance": total_attendance,
        "pending_leaves": pending_leaves,
    })


@login_required_custom
@role_required("Employee")
def employees_dashboard(request):
    if request.session["user_id"]:
        user=request.session["user_id"]
        personal_info = EmployeePersonalInfo.objects.filter(id=user).first()
        contacts = EmployeeContacts.objects.filter(employee_code=user).first()
        # department = id.department
        employee = Employees.objects.filter(id=user).first()
        attendance = Attendance.objects.filter(employee_code=user).order_by('-attendance_date')[:10]
        leaves = EmployeeLeaves.objects.filter(employee_code=user).order_by('-applied_date')[:5]
        payrolls = SalaryTransactions.objects.filter(employee_code=user).order_by('-id')[:5]
        print(personal_info)
        context = {
            "employee": employee,
            "employee_personal_info": personal_info,
            "employee_contacts": contacts,
            # "department": department,
            "attendance": attendance,
            "employee_leaves": leaves,
            "salary_transactions": payrolls,
        }
        return render(request, "employees_dashboard.html", context)
    else:
        return redirect("/logout/")
    
    
    
def home(request):
    return render(request, "index.html")


def reset_password(request):
    return render(request, "password_reset_form.html")

@login_required_custom
@role_required("Admin")

def manage_employees(request):
    employees = Employees.objects.all()

    # --- Status Filter ---
    status = request.GET.get('status')
    if status == '1':  # Active
        employees = employees.filter(is_active=True)
    elif status == '0':  # Inactive
        employees = employees.filter(is_active=False)

    # --- Search Filter (optional) ---
    query = request.GET.get('q', '')
    if query:
        employees = employees.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(role__icontains=query)
        )

    context = {
        'employees': employees,
    }
    return render(request, "admin/manage_employees.html", context)

@login_required_custom
@role_required("Admin")
def add_employee(request):
    departments = Departments.objects.all()
    if request.method == 'POST':
        Employees.objects.create(
            employee_code=request.POST.get('employee_code'),
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            role=request.POST.get('role'),
            designation=request.POST.get('designation'),
            department_id=request.POST.get('department_id'),
            reporting_manager_id=request.POST.get('reporting_manager_id'),
            employment_type=request.POST.get('employment_type'),
            work_location=request.POST.get('work_location'),
            doj=request.POST.get('doj'),
            dol=request.POST.get('dol'),
            resignation_date=request.POST.get('resignation_date'),
            is_active=True if request.POST.get('is_active') == '1' else False,
            user_type=request.POST.get('user_type'),
        )
        return redirect('manage_employees')

    return render(request, "admin/add_employee.html", {'departments': departments})


@login_required_custom
@role_required("Admin")
def edit_employee(request, employee_id):
    employee = Employees.objects.get(id=employee_id)

    if request.method == "POST":
        employee.name = request.POST.get("name")
        employee.email = request.POST.get("email")
        employee.role = request.POST.get("role")
        employee.designation = request.POST.get("designation")
        employee.department_id = request.POST.get("department_id")
        employee.reporting_manager_id = request.POST.get("reporting_manager_id")
        employee.employment_type = request.POST.get("employment_type")
        employee.work_location = request.POST.get("work_location")
        employee.user_type = request.POST.get("user_type")

        # ✅ Handle dates safely
        doj = request.POST.get("doj")
        dol = request.POST.get("dol")
        resignation_date = request.POST.get("resignation_date")

        employee.doj = doj if doj else None
        employee.dol = dol if dol else None
        employee.resignation_date = resignation_date if resignation_date else None

        # ✅ Handle active/inactive properly
        employee.is_active = True if request.POST.get("is_active") in ["1", "on", "true", "True"] else False

        employee.save()
        return redirect("manage_employees")

    departments = Departments.objects.all()
    return render(request, "admin/edit_employee.html", {"employee": employee, "departments": departments})


@login_required_custom
@role_required("Admin")
def delete_employee(request, employee_id):
    employee = get_object_or_404(Employees, id=employee_id)
    employee.delete()
    messages.success(request, f"{employee.name} deleted successfully.")
    return redirect("manage_employees")

@login_required_custom
@role_required("Admin")
# Attendance management
def manage_attendance(request):
    attendance = Attendance.objects.all().order_by("-attendance_date")
    return render(request, "admin/manage_attendance.html", {"attendance": attendance})

@login_required_custom
@role_required("Admin")
# Leave management
def manage_leave(request):
    leaves = EmployeeLeaves.objects.all().order_by("-applied_date")
    return render(request, "admin/manage_leave.html", {"leaves": leaves})

@login_required_custom
@role_required("Admin")
# Payroll management
def manage_payroll(request):
    payrolls = SalaryTransactions.objects.all().order_by("-id")
    return render(request, "admin/manage_payroll.html", {"payrolls": payrolls})

@login_required_custom
@role_required("Admin")
# Reports section
def manage_reports(request):
    return render(request, "admin/manage_reports.html")

@login_required_custom
@role_required("Admin")
# Settings section
def manage_settings(request):
    return render(request, "admin/manage_settings.html")

def logout_view(request):
    request.session.flush()
    messages.success(request, "You have been logged out securely.")
    return redirect("login")


@login_required_custom
@role_required('HR')  # Only HR can create events
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        event_date = request.POST.get('event_date')
        created_by = request.user.employee  # Assuming request.user links to Employees

        Events.objects.create(
            title=title,
            description=description,
            event_date=event_date,
            created_by=created_by
        )
        # Create notifications for all employees
        employees = Employees.objects.all()
        for emp in employees:
            Notifications.objects.create(
                employee=emp,
                title=f"New Event: {title}",
                message=description
            )
        messages.success(request, "Event added and notifications sent!")
        return redirect('events_list')

    return render(request, 'hrms/add_event.html')

@login_required_custom
def notifications_list(request):
    notifications = Notifications.objects.filter(employee=request.user.employee).order_by('-notification_date')
    return render(request, 'hrms/notifications.html', {'notifications': notifications})

@login_required_custom
def mark_notification_read(request, notification_id):
    notification = Notifications.objects.get(id=notification_id, employee=request.user.employee)
    notification.is_read = True
    notification.save()
    return JsonResponse({'status': 'success'})

@login_required_custom
def calendar_view(request):
    return render(request, 'hrms/calendar.html')


def view_employee(request, id):
    employee = get_object_or_404(Employees, id=id)
    return render(request, 'admin/view_employee.html', {'employee': employee})
