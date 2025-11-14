# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class Assets(models.Model):
#     asset_name = models.CharField(max_length=100, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     serial_number = models.CharField(max_length=100, blank=True, null=True)
#     purchase_date = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'assets'


# class Attendance(models.Model):
#     employee_code = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employee_code', to_field='employee_code', blank=True, null=True)
#     attendance_date = models.DateField(blank=True, null=True)
#     check_in = models.TimeField(blank=True, null=True)
#     check_out = models.TimeField(blank=True, null=True)
#     work_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     status = models.CharField(max_length=20, blank=True, null=True)
#     remarks = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'attendance'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class Departments(models.Model):
#     department_id = models.AutoField(primary_key=True)
#     department_name = models.CharField(unique=True, max_length=100)
#     description = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'departments'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class EmployeeAppraisals(models.Model):
#     employee_code = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employee_code', to_field='employee_code', blank=True, null=True)
#     appraisal_period = models.CharField(max_length=20, blank=True, null=True)
#     self_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     manager_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     feedback = models.TextField(blank=True, null=True)
#     appraisal_date = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee_appraisals'


# class EmployeeAssets(models.Model):
#     employee_code = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employee_code', to_field='employee_code', blank=True, null=True)
#     asset = models.ForeignKey(Assets, models.DO_NOTHING, blank=True, null=True)
#     issued_date = models.DateField(blank=True, null=True)
#     return_date = models.DateField(blank=True, null=True)
#     condition_on_return = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee_assets'


# class EmployeeBankDetails(models.Model):
#     employee_code = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employee_code', to_field='employee_code', blank=True, null=True)
#     bank = models.CharField(max_length=100, blank=True, null=True)
#     account_no = models.CharField(max_length=50, blank=True, null=True)
#     ifsc = models.CharField(max_length=20, blank=True, null=True)
#     pan = models.CharField(max_length=20, blank=True, null=True)
#     aadhar = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee_bank_details'


# class EmployeeContacts(models.Model):
#     employee_code = models.OneToOneField('Employees', models.DO_NOTHING, db_column='employee_code', primary_key=True)
#     mobile_no = models.CharField(max_length=15, blank=True, null=True)
#     alternate_no = models.CharField(max_length=15, blank=True, null=True)
#     contact_no = models.CharField(max_length=15, blank=True, null=True)
#     permanent_address = models.TextField(blank=True, null=True)
#     present_address = models.TextField(blank=True, null=True)
#     emergency_contact_person = models.CharField(max_length=100, blank=True, null=True)
#     emergency_contact_no = models.CharField(max_length=15, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee_contacts'


# class EmployeeGoals(models.Model):
#     employee_code = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employee_code', to_field='employee_code', blank=True, null=True)
#     goal_description = models.TextField(blank=True, null=True)
#     target_date = models.DateField(blank=True, null=True)
#     status = models.CharField(max_length=20, blank=True, null=True)
#     created_date = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee_goals'


# class EmployeeLeaves(models.Model):
#     employee_code = models.ForeignKey('Employees', models.DO_NOTHING, db_column='employee_code', to_field='employee_code', blank=True, null=True)
#     leave_type = models.ForeignKey('LeaveTypes', models.DO_NOTHING, blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)
#     reason = models.TextField(blank=True, null=True)
#     status = models.CharField(max_length=20, blank=True, null=True)
#     applied_date = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee_leaves'


# class EmployeePersonalInfo(models.Model):
#     id = models.IntegerField()
#     employee_code = models.OneToOneField('Employees', models.DO_NOTHING, db_column='employee_code', primary_key=True)
#     father_name = models.CharField(max_length=100, blank=True, null=True)
#     dob = models.DateField(blank=True, null=True)
#     gender = models.CharField(max_length=10, blank=True, null=True)
#     blood_group = models.CharField(max_length=10, blank=True, null=True)
#     qualification = models.CharField(max_length=100, blank=True, null=True)
#     functional_area = models.CharField(max_length=100, blank=True, null=True)
#     skills = models.TextField(blank=True, null=True)
#     certifications = models.TextField(blank=True, null=True)
#     work_history = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employee_personal_info'


# class Employees(models.Model):
#     employee_code = models.CharField(unique=True, max_length=20)
#     name = models.CharField(max_length=100)
#     role = models.CharField(max_length=50, blank=True, null=True)
#     designation = models.CharField(max_length=100, blank=True, null=True)
#     department = models.ForeignKey(Departments, models.DO_NOTHING, blank=True, null=True)
#     reporting_manager = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
#     employment_type = models.CharField(max_length=50, blank=True, null=True)
#     work_location = models.CharField(max_length=100, blank=True, null=True)
#     is_active = models.IntegerField(blank=True, null=True)
#     doj = models.DateField(blank=True, null=True)
#     date_of_leaving = models.DateField(blank=True, null=True)
#     resignation_date = models.DateField(blank=True, null=True)
#     email = models.CharField(unique=True, max_length=100, blank=True, null=True)
#     password = models.CharField(max_length=255, blank=True, null=True)
#     user_type = models.CharField(max_length=8, blank=True, null=True)
#     created_date = models.DateTimeField(blank=True, null=True)
#     updated_date = models.DateTimeField(blank=True, null=True)
#     created_by = models.CharField(max_length=100, blank=True, null=True)
#     updated_by = models.CharField(max_length=100, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'employees'


# class Events(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     event_date = models.DateField()
#     created_by = models.ForeignKey(Employees, models.DO_NOTHING, db_column='created_by')
#     created_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'events'


# class LeaveTypes(models.Model):
#     leave_type = models.CharField(max_length=50)
#     description = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'leave_types'


# class Notifications(models.Model):
#     employee = models.ForeignKey(Employees, models.DO_NOTHING)
#     title = models.CharField(max_length=255)
#     message = models.TextField(blank=True, null=True)
#     is_read = models.IntegerField(blank=True, null=True)
#     notification_date = models.DateTimeField(blank=True, null=True)
#     event = models.ForeignKey(Events, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'notifications'


# class SalaryStructure(models.Model):
#     employee_code = models.ForeignKey(Employees, models.DO_NOTHING, db_column='employee_code', to_field='employee_code', blank=True, null=True)
#     monthly_ctc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     annual_ctc_without_bonus = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#     annual_ctc_with_bonus = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
#     basic_ctc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     hra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     conveyance_allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     medical_allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     telephone_reimbursement = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     uniform_allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     lta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     special_allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     bonus_eligible = models.IntegerField(blank=True, null=True)
#     revision_month = models.CharField(max_length=20, blank=True, null=True)
#     last_revision_date = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'salary_structure'


# class SalaryTransactions(models.Model):
#     employee_code = models.ForeignKey(Employees, models.DO_NOTHING, db_column='employee_code', to_field='employee_code', blank=True, null=True)
#     month_year = models.CharField(max_length=10, blank=True, null=True)
#     total_days = models.IntegerField(blank=True, null=True)
#     working_days = models.IntegerField(blank=True, null=True)
#     gross_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     total_deductions = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     net_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     tds = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     advance_deduction = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     leave_deduction = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     professional_tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     employee_pf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     esic = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     total_monthly_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     inhand_pay = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     employer_epf = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     employer_esic = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     bonus_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     remarks = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'salary_transactions'


# class Test(models.Model):
#     name = models.TextField(blank=True, null=True)
#     employee_code = models.TextField(blank=True, null=True)
#     designation = models.TextField(blank=True, null=True)
#     is_active = models.IntegerField(blank=True, null=True)
#     father_name = models.TextField(db_column='Father Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     dob = models.TextField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
#     mobile_no = models.TextField(db_column='Mobile No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     alternate_no = models.TextField(db_column='Alternate No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     blood_group = models.TextField(db_column='Blood group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     total_exp = models.TextField(db_column='Total Exp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     highest_qualification = models.TextField(db_column='Highest Qualification', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     functional_area = models.TextField(db_column='Functional Area', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     bank = models.TextField(db_column='Bank', blank=True, null=True)  # Field name made lowercase.
#     account_no = models.TextField(db_column='Account No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     ifsc = models.TextField(db_column='IFSC', blank=True, null=True)  # Field name made lowercase.
#     pan = models.TextField(db_column='PAN', blank=True, null=True)  # Field name made lowercase.
#     adhar_number = models.TextField(db_column='Adhar Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     permanent_address = models.TextField(db_column='Permanent Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     present_address = models.TextField(db_column='Present Address', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     emergency_contact_person = models.TextField(db_column='Emergency Contact Person', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     emergency_contact_no = models.TextField(db_column='Emergency Contact No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     doj = models.TextField(blank=True, null=True)
#     email_id = models.TextField(db_column='Email ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     work_email = models.TextField(db_column='Work Email', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     contact_no = models.TextField(db_column='Contact No', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     date_of_leaving = models.TextField(blank=True, null=True)
#     doc_link = models.TextField(db_column='Doc Link', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
#     myunknowncolumn = models.TextField(db_column='MyUnknownColumn', blank=True, null=True)  # Field name made lowercase.
#     myunknowncolumn_0_field = models.TextField(db_column='MyUnknownColumn_[0]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     myunknowncolumn_1_field = models.TextField(db_column='MyUnknownColumn_[1]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     myunknowncolumn_2_field = models.TextField(db_column='MyUnknownColumn_[2]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     myunknowncolumn_3_field = models.TextField(db_column='MyUnknownColumn_[3]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     myunknowncolumn_4_field = models.TextField(db_column='MyUnknownColumn_[4]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#     myunknowncolumn_5_field = models.TextField(db_column='MyUnknownColumn_[5]', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

#     class Meta:
#         managed = False
#         db_table = 'test'
