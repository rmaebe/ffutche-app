from django import forms
from .models import Donor, Applicant, Parent
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Scholarship

class DonorForm(forms.ModelForm):
    username = forms.CharField(label='User Name')
    firstname = forms.CharField(label='First Name')
    middlename = forms.CharField(label='Middle Name', required=False)
    lastname = forms.CharField(label='Last Name')
    CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    sex = forms.CharField(label='Gender', widget=forms.Select(choices=CHOICES))
    type = forms.CharField(initial='Donor', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    phone = forms.CharField(label='Primary Phone')
    phone2 = forms.CharField(label='Secondary Phone', required=False)
    address = forms.CharField(label='Street Address')
    address2 = forms.CharField(label='Address', required=False)
    email = forms.EmailField(label='Email')

    class Meta:
        model = Donor
        fields = [
            'username',
            'firstname',
            'middlename',
            'lastname',
            'sex',
            'type',
            'phone',
            'phone2',
            'address',
            'address2',
            'email',
        ]

        def clean_username(self):
            username = self.cleaned_data['username']
            if Applicant.objects.filter(username=username).exists():
                raise forms.ValidationError("User already exists")
            return username

class RawDonorForm(forms.Form):
    username = forms.CharField(label='User Name')
    firstname = forms.CharField(label='First Name')
    middlename = forms.CharField(label='Middle Name', required=False)
    lastname = forms.CharField(label='Last Name')
    CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    sex = forms.ChoiceField(label='Gender', widget=forms.RadioSelect, choices=CHOICES)
    type = forms.CharField(initial='Donor', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    phone = forms.CharField(label='Primary Phone')
    phone2 = forms.CharField(label='Secondary Phone', required=False)
    address = forms.CharField(label='Street Address')
    address2 = forms.CharField(label='Address', required=False)
    email = forms.EmailField(label='Email')


class ApplicantForm(forms.ModelForm):
    username = forms.CharField(label='User Name' )
    firstname = forms.CharField(label='First Name')
    middlename = forms.CharField(label='Middle Name', required=False)
    lastname = forms.CharField(label='Last Name')
    CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    sex = forms.CharField(label='Gender', widget=forms.Select(choices=CHOICES))
    type = forms.CharField(initial='Applicant', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    phone = forms.CharField(label='Primary Phone')
    phone2 = forms.CharField(label='Secondary Phone', required=False)
    address = forms.CharField(label='Street Address')
    address2 = forms.CharField(label='Address', required=False)
    dob_day = forms.CharField(label='Day of Birth')
    dob_month = forms.CharField(label='Month of Birth')
    dob_year = forms.CharField(label='Year of Birth')
    city_of_birth = forms.CharField(label='City of Birth')
    state_of_birth = forms.CharField(label='Country of Birth')
    CHOICES2 = [('Never Married', 'Never Married'), ('Married', 'Married'), ('Separated', 'Separated'),
                ('Divorced', 'Divorced'), ('Widow', 'Widow')]
    martial_status = forms.CharField(label='Martial Status', widget=forms.Select(choices=CHOICES2))
    school_year = forms.CharField(label='School Year Completed')
    school_name = forms.CharField(label='School Name')
    school_city = forms.CharField(label='School City')
    school_country = forms.CharField(label='School Country')
    school_class = forms.CharField(label='Class')
    school_grade = forms.CharField(label='Grade')
    school_rank = forms.CharField(label='Rank')
    school_degree = forms.CharField(label='Degree')
    tuition = forms.CharField(label='Tuition Amount')
    books = forms.CharField(label='Book Amount')
    furniture = forms.CharField(label='Furniture Amount')
    transport = forms.CharField(label='Transport Amount')
    clothing = forms.CharField(label='Clothing Amount')
    recreation = forms.CharField(label='Recreation Amount')
    other_exp = forms.CharField(label='Other Expenses')
    total_expenses = forms.CharField(label='Total Expenses')
    parent_support = forms.CharField(label='Parent Support')
    loan = forms.CharField(label='Loan Amount')
    school_break_activities = forms.CharField(label='School Break Jobs')
    friend_support = forms.CharField(label='Friend Support')
    other_rev = forms.CharField(label='Other Revenue')
    total_revenue = forms.CharField(label='Total Revenue')

    class Meta:
        model = Applicant
        fields = [
            'username',
            'firstname',
            'middlename',
            'lastname',
            'sex',
            'type',
            'phone',
            'phone2',
            'address',
            'address2',
            'dob_day',
            'dob_month',
            'dob_year',
            'city_of_birth',
            'state_of_birth',
            'martial_status',
            'school_year',
            'school_name',
            'school_city',
            'school_country',
            'school_class',
            'school_grade',
            'school_rank',
            'school_degree',
            'tuition',
            'books',
            'furniture',
            'transport',
            'clothing',
            'recreation',
            'other_exp',
            'total_expenses',
            'parent_support',
            'loan',
            'school_break_activities',
            'friend_support',
            'other_rev',
        ]

    def clean_username(self):
        username = self.cleaned_data['username']
        if Applicant.objects.filter(username=username).exists():
            raise forms.ValidationError("User already exists")
        return username

class RawApplicantForm(forms.Form):
    username = forms.CharField(label='User Name')
    firstname = forms.CharField(label='First Name')
    middlename = forms.CharField(label='Middle Name', required=False)
    lastname = forms.CharField(label='Last Name')
    CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    sex = forms.CharField(label='Gender', widget=forms.Select(choices=CHOICES))
    type = forms.CharField(initial='Applicant', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    phone = forms.CharField(label='Primary Phone')
    phone2 = forms.CharField(label='Secondary Phone', required=False)
    address = forms.CharField(label='Street Address')
    address2 = forms.CharField(label='Address', required=False)
    dob_day = forms.CharField(label='Day of Birth')
    dob_month = forms.CharField(label='Month of Birth')
    dob_year = forms.CharField(label='Year of Birth')
    city_of_birth = forms.CharField(label='City of Birth')
    state_of_birth = forms.CharField(label='Country of Birth')
    CHOICES2 = [('Never Married', 'Never Married'), ('Married', 'Married'), ('Separated', 'Separated'),
                ('Divorced', 'Divorced'), ('Widow', 'Widow')]
    martial_status = forms.CharField(label='Martial Status', widget=forms.Select(choices=CHOICES2))
    school_year = forms.CharField(label='School Year Completed')
    school_name = forms.CharField(label='School Name')
    school_city = forms.CharField(label='School City')
    school_country = forms.CharField(label='School Country')
    school_class = forms.CharField(label='Class')
    school_grade = forms.CharField(label='Grade')
    school_rank = forms.CharField(label='Rank')
    school_degree = forms.CharField(label='Degree')
    tuition = forms.CharField(label='Tuition Amount')
    books = forms.CharField(label='Book Amount')
    furniture = forms.CharField(label='Furniture Amount')
    transport = forms.CharField(label='Transport Amount')
    clothing = forms.CharField(label='Clothing Amount')
    recreation = forms.CharField(label='Recreation Amount')
    other_exp = forms.CharField(label='Other Expenses')
    total_expenses = forms.CharField(label='Total Expenses')
    parent_support = forms.CharField(label='Parent Support')
    loan = forms.CharField(label='Loan Amount')
    school_break_activities = forms.CharField(label='School Break Jobs')
    friend_support = forms.CharField(label='Friend Support')
    other_rev = forms.CharField(label='Other Revenue')
    total_revenue = forms.CharField(label='Total Revenue')

class ParentForms(forms.ModelForm):
    username = forms.CharField(label='User Name')
    firstname = forms.CharField(label='First Name')
    middlename = forms.CharField(label='Middle Name', required=False)
    lastname = forms.CharField(label='Last Name')
    CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    sex = forms.CharField(label='Gender', widget=forms.Select(choices=CHOICES))
    type = forms.CharField(initial='Donor', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    phone = forms.CharField(label='Primary Phone')
    phone2 = forms.CharField(label='Secondary Phone', required=False)
    address = forms.CharField(label='Street Address')
    address2 = forms.CharField(label='Address', required=False)
    city_of_birth = forms.CharField(label='City of Birth')
    state_of_birth = forms.CharField(label='Country of Birth')
    CHOICES2 = [('Never Married', 'Never Married'), ('Married', 'Married'), ('Separated', 'Separated'),
                ('Divorced', 'Divorced'), ('Widow', 'Widow')]
    martial_status = forms.CharField(label='Martial Status', widget=forms.Select(choices=CHOICES2))
    num_children = forms.CharField(label='Number of Children')
    occupation = forms.CharField(label='occupation')
    emp_name = forms.CharField(label='Employer Name')
    emp_add = forms.CharField(label='Employer Address')


    class Meta:
        model = Parent
        fields = [
            'username',
            'firstname',
            'middlename',
            'lastname',
            'sex',
            'type',
            'phone',
            'phone2',
            'address',
            'address2',
            'dob_day',
            'dob_month',
            'dob_year',
            'city_of_birth',
            'state_of_birth',
            'martial_status',
            'num_children',
            'occupation',
            'emp_name',
            'emp_add',
        ]

        def clean_username(self):
            username = self.cleaned_data['username']
            if Parent.objects.filter(username=username).exists():
                raise forms.ValidationError("User already exists")
            return username