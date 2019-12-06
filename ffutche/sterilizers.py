from rest_framework import serializers
from .models import Donor, Scholarship, Applicant, Parent

class DonorSerlizer(serializers.ModelSerializer):
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

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = [
            'scholarship_id',
            'denomination',
            'referred_studies',
            'amount',
            'description',
            'criteria',
        ]


class ApplicantSerializer(serializers.ModelSerializer):
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

class ParentSerializer(serializers.ModelSerializer):
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

