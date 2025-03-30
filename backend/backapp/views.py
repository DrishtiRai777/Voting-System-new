from datetime import datetime
import json 
from django.shortcuts import render,HttpResponse , redirect, reverse
from .models import OrganizationDetails, AdministrativeDetails
from django.contrib import messages
from .forms import OrganizationDetailsForm, AdministrativeDetailsForm, AdministrativeDetailsForm1
from django.db import IntegrityError
from .utils.serializers import DateAwareJSONEncoder
# Create your views here.
def main(request):
    return render(request, 'main.html')

def user_login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def org_login(request):
    return render(request, 'org-login.html')



def sign_up(request):
    if request.method == "POST":
        print("hi")
        form = OrganizationDetailsForm(request.POST)
        if form.is_valid():  # MUST check validity first
            try:
                request.session['organization_data'] = form.cleaned_data  # Consistent key
                print("Session data saved:", request.session['organization_data'])
                return redirect('sign_up02')
               
            except Exception as e:
                print("Session save error:", e)
                messages.error(request, "Failed to save your data. Please try again.")
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Form contains errors. Please correct them.")
            redirect('sign_up')
    else:
        form = OrganizationDetailsForm()
    return render(request, 'sign_up-01.html', {'form': form})


    
def sign_up02(request):
    if request.method == "POST":
        print("second")
        form = AdministrativeDetailsForm(request.POST)
        if form.is_valid():
            try:
                admin_data = form.cleaned_data.copy()
                
                # Keep date as date object (don't convert to string yet)
                if 'date_of_birth' in admin_data and admin_data['date_of_birth']:
                    if isinstance(admin_data['date_of_birth'], str):
                        try:
                            admin_data['date_of_birth'] = datetime.strptime(
                                admin_data['date_of_birth'], '%Y-%m-%d'
                            ).date()
                        except ValueError:
                            messages.error(request, "Invalid date format. Please use YYYY-MM-DD")
                            return redirect('sign_up02')
                
                # Use the encoder when storing in session
                serialized_data = json.dumps(admin_data, cls=DateAwareJSONEncoder)
                request.session['admin_data'] = json.loads(serialized_data)
                
                print("Session data saved:", request.session['admin_data'])
                return redirect('sign_up03')
                
            except Exception as e:
                print("Session save error:", e)
                messages.error(request, "Failed to save your data. Please try again.")
        else:
            messages.error(request, "Form contains errors. Please correct them.")
    else:
        form = AdministrativeDetailsForm()
    return render(request, 'sign_up-02.html', {'form': form})

def sign_up03(request):
    if request.method == "POST":
        form = AdministrativeDetailsForm1(request.POST)
        if form.is_valid():
            credentials = {
            'username': request.POST.get('user'),
            'password': request.POST.get('pswd')
          }
            organization_data = request.session.get('organization_data', {})
            print("Organization Data:", organization_data)  # Debugging
            admin_data = request.session.get('admin_data', {})
                
            if not organization_data or not admin_data:
                print("Session data is missing!")
                return redirect('sign_up') 
            try:
                # Convert date string back to date object if needed
              if 'date_of_birth' in admin_data and admin_data['date_of_birth']:
                    try:
                        if isinstance(admin_data['date_of_birth'], str):
                            admin_data['date_of_birth'] = datetime.strptime(
                                admin_data['date_of_birth'], '%Y-%m-%d').date()
                    except ValueError as e:
                        messages.error(request, 
                            "Invalid date format in session data (expected YYYY-MM-DD). "
                            "Please re-enter your birth date.")
                        return redirect('sign_up02')
            except ValueError as e:
                messages.error(request, "Invalid date format in session data. Please re-enter your birth date.")
                return redirect('sign_up02')        
            try:
                # Create and save OrganizationDetails instance
                organization_details = OrganizationDetails(
                    organization_name=organization_data.get('organization_name'),
                    type=organization_data.get('type'),
                    address=organization_data.get('address'),
                    contact_person_name=organization_data.get('contact_person_name'),
                    email_address=organization_data.get('email_address'),
                    linkedin_id=organization_data.get('linkedin_id')
                )
                organization_details.save()

                # Create and save AdministrativeDetails instance
                admin_details = AdministrativeDetails(
                    name_of_admin=admin_data.get('name_of_admin'),
                    date_of_birth=admin_data.get('date_of_birth'),
                    gender=admin_data.get('gender'),
                    institution_name=admin_data.get('institution_name'),
                    branch=admin_data.get('branch'),
                    college_id=admin_data.get('college_id'),
                    contact_number=admin_data.get('contact_number'),
                    email_address_of_admin=admin_data.get('email_address_of_admin'),
                    position_or_title=admin_data.get('position_or_title'),
                    secretary_name=admin_data.get('secretary_name'),
                    phone_number=admin_data.get('phone_number'),
                    email_address_of_secretary=admin_data.get('email_address_of_secretary'),
                    team_member_1_name=admin_data.get('team_member_1_name'),
                    contact_number_of_member_1=admin_data.get('contact_number_of_member_1'),
                    email_address_of_member_1=admin_data.get('email_address_of_member_1'),
                    team_member_2_name=admin_data.get('team_member_2_name'),
                    contact_number_of_member_2=admin_data.get('contact_number_of_member_2'),
                    email_address_of_member_2=admin_data.get('email_address_of_member_2')
                )
                admin_details.save()
                credentials.save()

                # Clear session data
                request.session.pop('organization_data', None)
                request.session.pop('admin_data', None)

                messages.success(request, "All details successfully saved.")
                return redirect('org_dashboard')  # Redirect to the dashboard or success page
            except IntegrityError as e:
                print("Database Error:", e)  # Debugging
                messages.error(request, "An error occurred while saving the data.")
        else:
            print("Form Errors:", form.errors) 
    else:
        form = AdministrativeDetailsForm1()
    return render(request, 'sign_up-03.html', {'form': form})


    

def org_dashboard(request):
    return render(request, 'org-dashboard.html')