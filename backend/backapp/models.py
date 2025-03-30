from django.db import models

# Create your models here.
'''class gender_type(models.TextChoices):
    MALE = 'Male', 'male'
    FEMALE = 'Female', 'female'
    OTHER = 'Other', 'other'
    NOT_DISCLOSED = 'Not Disclosed', 'Choose not to disclose' '''

class OrganizationDetails(models.Model):
    organization_name = models.CharField(db_column='Organization Name', primary_key=True, max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=False)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    contact_person_name = models.CharField(db_column='Contact Person Name', max_length=255, blank=True, null=False)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_address = models.CharField(db_column='Email Address', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    linkedin_id = models.CharField(db_column='LinkedIn ID', max_length=255, blank=True, null=True)  

class AdministrativeDetails(models.Model):
    admin_id = models.AutoField(db_column='Admin ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name_of_admin = models.CharField(db_column='Name of Admin', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_birth = models.DateField(db_column='Date of Birth', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gender = models.CharField(db_column='Gender', max_length=100, blank=True, null=False)  # Field name made lowercase.
    institution_name = models.CharField(db_column='Instituition Name', max_length=255)
    branch = models.CharField(db_column='Branch', max_length=50, blank=True, null=True)  # Field name made lowercase.
    college_id=models.CharField(db_column='College ID', max_length=255, blank=True, null=True)
    contact_number = models.CharField(db_column='Contact Number', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_address_of_admin = models.CharField(db_column='Email Address Of Admin', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    position_or_title = models.CharField(db_column='Position or Title', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    secretary_name = models.CharField(db_column='Secretary Name', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phone_number = models.CharField(db_column='Phone Number', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_address_of_secretary = models.CharField(db_column='Email Address Of Secretary', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    team_member_1_name = models.CharField(db_column='Team Member 1 Name', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_number_of_member_1 = models.CharField(db_column='Contact Number of Member 1', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_address_of_member_1 = models.CharField(db_column='Email Address of Member 1', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    team_member_2_name = models.CharField(db_column='Team Member 2 Name', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_number_of_member_2 = models.CharField(db_column='Contact Number of Member 2', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email_address_of_member_2 = models.CharField(db_column='Email Address of Member 2', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    username = models.CharField(db_column='Username', max_length=255, blank=True, null=True)
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)

class Usersdetail(models.Model):
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    date_of_birth = models.DateField(blank=True, null=False)
    user_image = models.BinaryField(blank=True, null=True)
    password = models.CharField(max_length=255)
    aadhar_card_no = models.BinaryField(blank=True, null=False, primary_key=True)
    signature = models.BinaryField(blank=True, null=False)
    address = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=False)
    city = models.CharField(max_length=255, blank=True, null=False)
    gender = models.CharField(db_column='Gender', max_length=100, blank=True, null=False)  # This field type is a guess.
    contact = models.CharField(max_length=20, blank=True, null=False)