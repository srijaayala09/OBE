from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Department(models.Model):

    name= models.CharField(max_length=200,null=True)
    faculty_name = models.ForeignKey(Faculty,max_length=200,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.name



class Student(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=20,null=True)
    roll= models.IntegerField(null=True)
    exam_roll=models.IntegerField(null=True)
    name = models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    batch = models.IntegerField(null=True)
    #department = models.CharField(max_length=200, null=True)
    department = models.ForeignKey(Department,null=True,on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True,default="propic1.jpg", blank=True)

    def __str__(self):
        #return "%s %d %d %s %s %d %s" % (self.registration_no, self.roll,self.exam_roll,self.name,self.email,self.batch,self.department)
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    STATUS=[
        ('Active','Active'),
        ('LPR','LPR'),
        ('Leave','Leave'),
        ('Retired','Retired')
    ]
    #registration_no = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=200,null=True)
    designation = models.CharField(max_length=200,null=True)
    #department = models.CharField(max_length=200, null=True)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=11,null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    profile_pic = models.ImageField(null=True,default="propic1.jpg", blank=True)

    def __str__(self):
        return self.name

class Session(models.Model):
    STATUS=[
        ('Running','Running'),
        ('Finished','Finished'),
    ]
    #registration_no = models.CharField(max_length=20,null=True)
    startYear = models.CharField(max_length=200,null=True)
    endYear = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.startYear

class AssignSession(models.Model):
    department=models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
    session =models.ForeignKey(Session,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return "%s %s" % (self.department, self.session)



class Semester(models.Model):
    STATUS=[
        ('1st Year 1st Semester','1st Year 1st Semester'),
        ('1st Year 2nd Semester','1st Year 2nd Semester'),
        ('2nd Year 1st Semester','2nd Year 1st Semester'),
        ('2nd Year 2nd Semester','2nd Year 2nd Semester'),
        ('3rd Year 1st Semester','3rd Year 1st Semester'),
        ('3rd Year 2nd Semester','3rd Year 2nd Semester'),
        ('4th Year 1st Semester','4th Year 1st Semester'),
        ('4th Year 2nd Semester','4th Year 2nd Semester'),

    ]

    semester = models.CharField(max_length=200,null=True,choices=STATUS)

    def __str__(self):
        return self.semester

class AssignSemester(models.Model):
    session = models.ForeignKey(AssignSession,max_length=300,null=True,on_delete=models.SET_NULL)
    semester = models.ForeignKey(Semester,max_length=300,null=True,on_delete=models.SET_NULL)
    result_status = models.CharField(default='PENDING', null=True, max_length=20,
                            choices=[('PUBLISHED', 'PUBLISHED'), ('PENDING', 'PENDING')])


    def __str__(self):
        return "%s %s"%(self.session,self.semester)

class Course(models.Model):
    STATUS=[
        (1,1),
        (2,2),
        (3,3),

    ]

    TYPE=[
        ('Lab','Lab'),
        ('Theory','Theory'),
    ]

    course_code= models.CharField(max_length=200,null=True)
    course_name= models.CharField(max_length=200,null=True)
    credit= models.IntegerField(null=True,choices=STATUS)
    course_type= models.CharField(max_length=200,null=True,choices=TYPE)

    def __str__(self):
        return self.course_name


class AssignCourse(models.Model):

    semester = models.ForeignKey(AssignSemester,max_length=200,null=True,on_delete=models.SET_NULL)
    course = models.ForeignKey(Course,max_length=200,null=True,on_delete=models.SET_NULL)
    format = models.CharField(max_length=200,null=True,choices=[('OBE','OBE'),('NonOBE','NonOBE')])
    completion = models.CharField(default='PENDING',max_length=20,null=True,choices=[('ASSIGNED', 'ASSIGNED'),('PENDING', 'PENDING')])
    def __str__(self):
        return "%s  %s %s"% (self.semester,self.course,self.format)

class AssignStudent(models.Model):
    semester = models.ForeignKey(AssignSemester, max_length=200, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, max_length=200, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "%s  %s" % (self.semester, self.student)

class AssignTeacher(models.Model):
    course=models.ForeignKey(AssignCourse,null=True,on_delete=models.SET_NULL)
    teacher=models.ForeignKey(Teacher,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return "%s  %s" % (self.course,self.teacher)

class AssignChairman(models.Model):
    chairman = models.ForeignKey(Teacher,null=True,on_delete=models.SET_NULL)
    department = models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return "%s  %s" % (self.chairman,self.department)

class AssignExamCommittee(models.Model):
    member=models.ForeignKey(Teacher,null=True,on_delete=models.SET_NULL)
    semester= models.ForeignKey(AssignSemester,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return "%s %s" % (self.member,self.semester)


class NonObeMark(models.Model):
    course = models.ForeignKey(AssignCourse, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(AssignStudent,null=True,on_delete=models.SET_NULL)
    #course = models.ForeignKey(AssignCourse,null=True,on_delete=models.SET_NULL)
    tt1 = models.IntegerField(default=-1,null=True)
    tt2 = models.IntegerField(default=-1,null=True)
    tt3 = models.IntegerField(default=-1,null=True)
    att = models.IntegerField(default=-1,null=True)
    sem = models.IntegerField(default=-1,null=True)
    mark = models.CharField(default='PENDING',null=True,max_length=20,choices=[('ASSIGNED','ASSIGNED'),('PENDING','PENDING')])
    def avg(self):
        return (self.tt1+self.tt2+self.tt3)/3
    def total(self):
        tt= self.avg(self)
        return tt+self.att+self.sem
    def __str__(self):
        return "%s %s %d %d %d %d %d" % (self.student.student.name, self.course.course.course_name,self.tt1,self.tt2,self.tt3,self.att,self.sem)

class ObeMark(models.Model):
    course = models.ForeignKey(AssignCourse, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(AssignStudent, null=True, on_delete=models.SET_NULL)
    # course = models.ForeignKey(AssignCourse,null=True,on_delete=models.SET_NULL)
    tt1 = models.IntegerField(default=0, null=True)
    tt2 = models.IntegerField(default=0, null=True)
    tt3 = models.IntegerField(default=0, null=True)
    att = models.IntegerField(default=0, null=True)
    co1 = models.IntegerField(default=0, null=True)
    co2 = models.IntegerField(default=0, null=True)
    co3 = models.IntegerField(default=0, null=True)
    co4 = models.IntegerField(default=0, null=True)
    co5 = models.IntegerField(default=0, null=True)
    mark = models.CharField(default='PENDING', null=True, max_length=20,
                            choices=[('ASSIGNED', 'ASSIGNED'), ('PENDING', 'PENDING')])

    def __str__(self):
        return "%s %s " % (self.student.student.name, self.course.course.course_name)


