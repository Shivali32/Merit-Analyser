from django.db import models
from passlib.hash import pbkdf2_sha256
# Create your models here.
from django_mysql.models import ListCharField
from django.contrib.auth.models import User

class UserDetails(User):
    #username = models.CharField(db_index=True,max_length = 100)
    user_id = models.CharField(unique=True,db_index=True,max_length = 10)
    #email = models.EmailField(unique = True,db_index = True)
    contact_number = models.CharField(max_length=10,unique = True)
    #password = models.CharField(max_length=300)
    user_type = models.CharField(max_length = 7)
    def verify_password(self,raw_pwd):
        return pbkdf2_sha256.verify(raw_pwd,self.password)
    def str(self):
        return self.username

class Class(models.Model):
    class_id = models.CharField(unique=True, db_index=True, max_length=4)

    class_name = models.CharField(unique=True, max_length = 100)

    def str(self):
        return self.class_name


class Teacher(models.Model):

    teacher_name = models.CharField(max_length = 100, null = False)

    teacher_id = models.CharField(unique=True,db_index= True,max_length=10)

    teacher_email = models.EmailField(db_index  =True,unique = True)

    teacher_password = models.CharField(max_length=300)

    teacher_contact = models.CharField(max_length = 10)
    #teacher_gender = models.CharField(max_length = 6)

    # for password verification during login
    def verify_password(self,raw_pwd):
        return pbkdf2_sha256.verify(raw_pwd,self.teacher_password)

    def str(self):
        return self.teacher_name


'''class Subject(models.Model):

    subject_id = models.CharField(unique=True, db_index=True, max_length=10)

    class_id = models.ForeignKey(Class,on_delete=models.CASCADE)

    subject_name = models.CharField(max_length=100)

    teacher_id = models.ForeignKey(Teacher, on_delete = models.CASCADE)

    def str(self):
        return self.subject_name'''

class Student(models.Model):

    student_name = models.CharField(max_length = 100, null = False)

    student_id = models.CharField(unique=True,db_index= True,max_length=10)

    student_email = models.EmailField(db_index  =True,unique = True)

    student_password = models.CharField(max_length=300)

    #student_gender = models.CharField(max_length = 6)
    
    student_rollno = models.CharField(max_length = 6)

    #student_classid = models.ForeignKey(Class,on_delete=models.CASCADE)
    student_classid = models.ForeignKey(Class,on_delete=models.CASCADE)
    student_contact = models.CharField(max_length = 10)
    # A student can be assigned maximum 999 number of tests only
    tests_assigned = ListCharField(
        base_field=models.CharField(max_length=20),
        size=999,
        max_length=(999 * 21)  # 999 * 10 character nominals, plus commas
    )
    
    # for password verification during login
    def verify_password(self,raw_pwd):
        return pbkdf2_sha256.verify(raw_pwd,self.student_password)

    def str(self):
        return self.student_name


class Test(models.Model):

    test_id = models.CharField(unique=True,db_index= True,max_length=10)

    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    '''subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)'''
    test_name = models.CharField(max_length =20, null =False)

    passing_marks = models.IntegerField(default=0)
    max_marks = models.IntegerField(default=0)
    csv_filename = models.CharField(max_length = 50)
    # Maximum 999 number of students can be assigned a test, check if Size can be removed.
    class_assigned = models.ForeignKey(Class,on_delete=models.CASCADE)


    def str(self):
        return self.test_id+self.teacher_id+self.subject_id
    
'''class TeacherReports(models.Model):
    filename = models.CharField(max_length =20,null=False)
    report_id =models.CharField(max_length = 10, null=False)
    test_name = models.CharField(max_length = 30, null= False)
    plots = {}'''
