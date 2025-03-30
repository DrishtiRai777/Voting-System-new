from datetime import datetime
from django import forms
from .models import OrganizationDetails, AdministrativeDetails, Usersdetail

class OrganizationDetailsForm(forms.Form):
    ORGANIZATION_TYPE_CHOICES = [
        ('StudentClub', 'Student Club'),
        ('AcademicDepartment', 'Academic Department'),
        ('AdministrativeOffice', 'Administrative Office'),
        ('FacultySenate', 'Faculty Senate'),
    ]
    organization_name=forms.CharField(max_length=255)
    #type=forms.CharField(max_length=255)
    type = forms.ChoiceField(choices=ORGANIZATION_TYPE_CHOICES)
    address=forms.CharField(max_length=255)
    contact_person_name=forms.CharField(max_length=255)
    email_address=forms.CharField(max_length=255)
    linkedin_id=forms.CharField(max_length=255)
    def __str__(self):
        return self.organization_name

'''class AdministrativeDetailsForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Choose not to disclose', ' Choose not to disclose'),
        ]
    POSITION_CHOICES = [
        ('President', 'President'),
        ('VicePresident', 'Vice President'),
        ('Secretary', 'Secretary'),
        ('Treasurer', 'Treasurer'),
        ('Chairperson', 'Chairperson')
        ('FacultyAdvisor', 'Faculty Advisor')
        ('DepartmentHead', 'Department Head')
        ('Dean', 'Dean')
        ('Director', 'Director')
        ('Coordinator', 'Coordinator'),
        
    ]
    name_of_admin=forms.CharField(max_length=200)
    date_of_birth=forms.DateField()
    gender=forms.ChoiceField(choices=GENDER_CHOICES)
    institution_name=forms.ModelChoiceField(queryset=AdministrativeDetails.objects.all())
    branch=forms.CharField(max_length=50)
    contact_number=forms.CharField(max_length=20)
    email_address_of_admin=forms.CharField(max_length=255)
    position_or_title=forms.ChoiceField(choices=POSITION_CHOICES)
    seceretary_name=forms.CharField(max_length=200)
    phone_number=forms.CharField(max_length=20)
    email_address_of_seceretary=forms.CharField(max_length=255)
    team_member_1_name=forms.CharField(max_length=200)
    contact_number_of_member_1=forms.CharField(max_length=20)
    email_address_of_member_1=forms.CharField(max_length=255)
    team_member_2_name=forms.CharField(max_length=200)
    contact_number_of_member_2=forms.CharField(max_length=20)
    email_address_of_member_2=forms.CharField(max_length=255)
    def __str__(self):
        return self.name_of_admin'''

class AdministrativeDetailsForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Choose not to disclose', 'Choose not to disclose'),
    ]
    POSITION_CHOICES = [
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('Secretary', 'Secretary'),
        ('Treasurer', 'Treasurer'),
        ('Chairperson', 'Chairperson'),
        ('Faculty Advisor', 'Faculty Advisor'),
        ('Department Head', 'Department Head'),
        ('Dean', 'Dean'),
        ('Director', 'Director'),
        ('Coordinator', 'Coordinator'),
    ]
    name_of_admin = forms.CharField(max_length=200)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    institution_name = forms.CharField(max_length=255)
    branch = forms.CharField(max_length=50)
    college_id = forms.CharField(max_length=255)
    contact_number = forms.CharField(max_length=20)
    email_address_of_admin = forms.EmailField()
    position_or_title = forms.ChoiceField(choices=POSITION_CHOICES)
    secretary_name = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=20)
    email_address_of_secretary = forms.EmailField()
    team_member_1_name = forms.CharField(max_length=200)
    contact_number_of_member_1 = forms.CharField(max_length=20)
    email_address_of_member_1 = forms.EmailField()
    team_member_2_name = forms.CharField(max_length=200, required=False)
    contact_number_of_member_2 = forms.CharField(max_length=20, required=False)
    email_address_of_member_2 = forms.EmailField(required=False)

    def __str__(self):
        return self.name_of_admin
    
    '''def clean_date_of_birth(self):
        date_str = self.cleaned_data['date_of_birth']
        try:
            return datetime.strptime(date_str, '%d-%m-%Y').date()
        except ValueError:
            raise forms.ValidationError("Please enter date in DD-MM-YYYY format")'''

class AdministrativeDetailsForm1(forms.ModelForm):
    class Meta :
        model = AdministrativeDetails
        #fields = '__all__'
        fields=['username', 'password'] 


    

