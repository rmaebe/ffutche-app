from django.db import models



class Applicant(models.Model):
    username = models.CharField(max_length=45, primary_key=True, unique=True)
    firstname = models.CharField(max_length=45)
    middlename = models.CharField(max_length=45, null=True)
    lastname = models.CharField(max_length=45)
    sex = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    phone2 = models.CharField(max_length=45, null=True)
    address = models.CharField(max_length=45)
    address2 = models.CharField(max_length=45, null=True)
    dob_day = models.CharField(max_length=45)
    dob_month = models.CharField(max_length=45)
    dob_year = models.CharField(max_length=45)
    city_of_birth = models.CharField(max_length=45)
    state_of_birth = models.CharField(max_length=45)
    martial_status = models.CharField(max_length=45)
    school_year = models.CharField(max_length=45)
    school_name = models.CharField(max_length=45)
    school_city = models.CharField(max_length=45)
    school_country = models.CharField(max_length=45)
    school_class = models.CharField(max_length=45)
    school_grade = models.CharField(max_length=45)
    school_rank = models.CharField(max_length=45)
    school_degree = models.CharField(max_length=45)
    tuition = models.CharField(max_length=45)
    books = models.CharField(max_length=45)
    furniture = models.CharField(max_length=45)
    transport = models.CharField(max_length=45)
    clothing = models.CharField(max_length=45)
    recreation = models.CharField(max_length=45)
    other_exp = models.CharField(max_length=45)
    total_expenses = models.CharField(max_length=45)
    parent_support = models.CharField(max_length=45)
    loan = models.CharField(max_length=45)
    school_break_activities = models.CharField(max_length=45)
    friend_support = models.CharField(max_length=45)
    other_rev = models.CharField(max_length=45)
    total_revenue = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'applicant'

    def __str__(self):
        return self.username



class School(models.Model):
    schoolID = models.CharField(max_length=45, primary_key=True)
    name = models.CharField(max_length=45)
    address1 = models.CharField(max_length=45)
    address2 = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    country = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    contact_name = models.CharField(max_length=45)
    contact_phone1 = models.CharField(max_length=45)
    contact_phone2 = models.CharField(max_length=45)

    def __str__(self):
        return self.schoolID


class Student_Education(models.Model):
    school_year = models.CharField(max_length=45)
    school_name = models.CharField(max_length=45, primary_key=True)
    school_city = models.CharField(max_length=45)
    school_country = models.CharField(max_length=45)
    school_Se_class = models.CharField(max_length=45)
    school_grade = models.CharField(max_length=45)
    school_rank = models.CharField(max_length=45)
    school_degree = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'student_education'

    def __str__(self):
        return self.school


class Scholarship(models.Model):
    scholarship_id = models.CharField(max_length=45, primary_key=True)
    denomination = models.CharField(max_length=45)
    referred_studies = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    criteria = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'scholarship'

    def __str__(self):
        return self.scholarship_id



class Scholarship_Donation(models.Model):
    scholarshipID = models.CharField(max_length=45)
    donorID = models.CharField(max_length=45)
    amount = models.CharField(max_length=45)
    academic_year = models.CharField(max_length=45)

    def __str__(self):
        return self.scholarshipID


class Tuition_Fee(models.Model):
    tuition = models.CharField(max_length=45)
    books = models.CharField(max_length=45)
    furniture = models.CharField(max_length=45)
    transport = models.CharField(max_length=45)
    clothing = models.CharField(max_length=45)
    recreation = models.CharField(max_length=45)
    other_exp = models.CharField(max_length=45)
    total_expenses = models.CharField(max_length=45)
    parent_support = models.CharField(max_length=45)
    loan = models.CharField(max_length=45)
    school_break_activities = models.CharField(max_length=45)
    friend_support = models.CharField(max_length=45)
    other_rev = models.CharField(max_length=45)


    class Meta:
        managed = True
        db_table = 'tuition_fees'

    def __str__(self):
        return self.schoolID


class Donor(models.Model):
    username = models.CharField(max_length=45, primary_key=True)
    firstname = models.CharField(max_length=45)
    middlename = models.CharField(max_length=45, null=True)
    lastname = models.CharField(max_length=45)
    sex = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    phone2 = models.CharField(max_length=45, null=True)
    address = models.CharField(max_length=45)
    address2 = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'donor'

    def __str__(self):
        return self.username

class Parent(models.Model):
    username = models.CharField(max_length=45, primary_key=True)
    firstname = models.CharField(max_length=45)
    middlename = models.CharField(max_length=45, null=True)
    lastname = models.CharField(max_length=45)
    sex = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    phone2 = models.CharField(max_length=45, null=True)
    address = models.CharField(max_length=45)
    address2 = models.CharField(max_length=45, null=True)
    dob_day = models.CharField(max_length=45)
    dob_month = models.CharField(max_length=45)
    dob_year = models.CharField(max_length=45)
    city_of_birth = models.CharField(max_length=45)
    state_of_birth = models.CharField(max_length=45)
    martial_status = models.CharField(max_length=45)
    num_children = models.CharField(max_length=45)
    occupation = models.CharField(max_length=45)
    emp_name = models.CharField(max_length=45)
    emp_add = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'parent'

    def __str__(self):
        return self.username
