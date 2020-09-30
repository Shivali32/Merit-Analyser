from django.shortcuts import render,redirect,HttpResponse
import passlib.hash
from passlib.hash import pbkdf2_sha256
import string
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout
from django.core.files.storage import FileSystemStorage
import random
from MeritAnalyser.models import UserDetails,Teacher,Student,Class,Test


from plotly.offline import plot
import plotly.graph_objects as go

import pandas as pd

import plotly as plt
import os
import plotly.io as pio
import plotly.express as px
from django.core.files.storage import FileSystemStorage
import qrcode
from PIL import Image
import plotly.graph_objects as go
from PIL import ImageFont
from PIL import ImageDraw 
import matplotlib.pyplot as plt
import plotly.express as px

import random
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def showtable(df):
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(["Email-Id", "Marks Scored","Present/Absent"]),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df['Name'], df['Marks'], df['Present']],
               fill_color='lavender',
               align='left'))
    ])
    plot_div = plot(fig,output_type='div',include_plotlyjs=True)
    return plot_div


def showPassFail(df,passing_marks):
    d={"labels":["Pass","Fail"],"values":[0,0]}
    print('**************PASSING MARKS RECEIVED: ',passing_marks)
    def diction(x):
        if int(x)>passing_marks:
            d["values"][0]+=1
        else:
            d["values"][1]+=1
        return
    
    df=df['Marks'].apply(diction)
    fig = go.Figure(data=[go.Pie(labels=d["labels"], values=d["values"], hole=.3)])
    plot_div = plot(fig,output_type='div',include_plotlyjs=True)
    return plot_div


def showGradeBargraph(df):
    d1={"Grades":['A+','A','B+','B','C','F'],"Number of Students":[0,0,0,0,0,0]}
    def grade(x):
        if x>90:
            d1['Number of Students'][0]+=1
        elif x>80:
            d1['Number of Students'][1]+=1
        elif x>70:
            d1['Number of Students'][2]+=1
        elif x>60:
            d1['Number of Students'][3]+=1
        elif x>50:
            d1['Number of Students'][4]+=1
        else:
            d1['Number of Students'][5]+=1
        return
    df=df['Marks'].apply(grade)
    fig = px.bar(d1, x='Grades', y='Number of Students')
    
    plot_div = plot(fig,output_type='div',include_plotlyjs=True)
    return plot_div
    

def showAveragePieChart(df):
    averageMarks=df["Marks"].mean()
    print("Average Marks are")
    print(averageMarks)
    highestMark=df["Marks"].max()
    print("Highest Marks are")

    print(highestMark)
    topper=df[[ 'Name']][df.Marks == df.Marks.max()]
    print(topper)
    d3={"labels":["Below Average","Average ","Above Average"],"values":[0,0,0]}
    def averaging(x):
        if (averageMarks+10)>x>(averageMarks-10):
            d3['values'][1]+=1
        elif x<(averageMarks-10):
            d3['values'][0]+=1
        elif x>(averageMarks+10):
            d3['values'][2]+=1

        return
    df=df['Marks'].apply(averaging)
    fig = go.Figure(data=[go.Pie(labels=d3["labels"], values=d3["values"], hole=.3)])


    plot_div = plot(fig,output_type='div',include_plotlyjs=True)
    return plot_div

def showAbsentPieChart(df):
    d={"labels":["Absent","Present"],"values":[0,0]}

    def diction(x):
        if x==0:
            d["values"][0]+=1
        else:
            d["values"][1]+=1
        return
    df=df['Present'].apply(diction)
    fig = go.Figure(data=[go.Pie(labels=d["labels"], values=d["values"], hole=.3)])


    plot_div = plot(fig,output_type='div',include_plotlyjs=True)
    return plot_div


'''subject = "DSA"
testNumber = "1"'''








def home(request):

    def scatter_map():
        mapbox_access_token = "pk.eyJ1IjoidmlwZXJzdmVuZCIsImEiOiJja2E0NGV0NjcwYWllM2dtdmQ0NnpoYW5pIn0.hYJV-dqqe-RxsthI5fb_VQ"

        fig = go.Figure(go.Scattermapbox(
        lat=['18.5560176', '18.562268730769993', '18.55298685', '18.515143', '18.537726050431523', '18.5087265', '18.5298629', '18.511483249999998', '18.5291854', '18.6582', '18.5721375', '18.484346993744882', '18.460760162725872', '18.5095844', '18.54200045206177', '18.52765433880996', '18.505923699999997', '18.559174681233216', '18.55593608255426', '18.5710074', '18.586984987973846', '18.583178487202247', '18.511166', '18.449257873152785', '18.516447', '18.47531015', '18.4765304', '18.4887558', '18.473988', '18.505813', '18.449437378342818', '18.502911', '18.464626685772817', '18.4840446', '18.531607533055084', '18.52213492911108']
,
        lon=['73.8094612', '73.78487101278952', '73.75500526891248', '73.8170469', '73.96691978790464', '73.83086905279255', '73.8760869', '73.7920424736547', '73.8334444', '73.8046793', '73.8788439', '73.80055749560111', '73.85550277899736', '73.8585026', '73.80701296906541', '73.82952378849852', '73.80637532380953', '73.92101769695793', '73.83683021403759', '73.8383273', '73.88068030420885', '73.90078124564857', '73.928155', '73.85162745570236', '73.84643403866933', '73.81187112070381', '73.8560547', '73.86667669847294', '73.889073', '73.86884', '73.82225418212326', '73.927152', '73.91903734249948', '73.90168419768577', '73.9217239202194', '73.86262273714576'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=['Zandra', 'Garth', 'Jarvis', 'Kendall', 'Margeret', 'Soo', 'Weston', 'Abbey', 'Frank', 'Lara', 'Indira', 'Madlyn', 'Divina', 'Catalina', 'Yoko', 'Kayleigh', 'Agueda', 'Libbie', 'Renetta', 'Lashaun', 'Jesus', 'Larissa', 'Elvia', 'Ilona', 'Codi', 'Lorinda', 'Jacki', 'Joan', 'Nicolasa', 'Adena', 'Eryn', 'Reyes', 'Melany', 'Zofia', 'Viola', 'Reyes', ],
    ))

        fig.update_layout(
            autosize=True,
            hovermode='closest',
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=dict(
                    lat=18.5560176,
                    lon=73.8094612
                ),
                pitch=0,
                zoom=10
            ),
        )
        plot_div = plot(fig,output_type='div',include_plotlyjs=True)
        return plot_div
        
    k=scatter_map() 
    context={'plot':k,'name':"Nihar"}
    return render(request,'home/welcome.html',context)



# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    '''if request.method == 'POST':
        email_id = request.POST.get('username')
        password = request.POST.get('password')
        if len(UserDetails.objects.all().filter(email_id = email_id))==1:

            if(UserDetails.objects.all().filter(email_id = email_id)[0].verify_password(password)):
                user_object = {'user_type' : UserDetails.objects.all().filter(email_id = email_id)[0].user_type, 
                                'user_auth':True,
                                'user_id':UserDetails.objects.all().filter(email_id = email_id)[0].user_id
                                }
                return redirect(request,'index.html',user_object)
        else:
            return HttpResponse('Invalid Credentials')'''
    
    if request.method == 'POST':
        email_id = request.POST.get('username')
        password = request.POST.get('password')

        try:
            username = UserDetails.objects.filter(email=email_id)[0].username
        except:
            return redirect('/index')
        print('YOUR USERNAME is', username, 'YOUR PWD IS: ',password)
        user = authenticate(username = username,password = password)

        if user:
            print('user try1  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', user.get_username)
            if user.is_active:
                print('user try2 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', user)
                auth_login(request, user)
                #return HttpResponseRedirect(request.GET.get('next',settings.LOGIN_REDIRECT_URL))
                print('auth_ successful !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                return render(request,'index.html')
        else:
            return HttpResponse("Auth Failed BROOO")
    return render(request,'login.html')
def register(request):
    
    if request.method == 'POST':
        print('register called with post')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        usertype = request.POST.get('usertype')

        user_id = ''.join(random.choices(string.ascii_uppercase + string.digits,k= 10))
        password_enc = pbkdf2_sha256.hash(password,rounds = 12000,salt_size = 32)
        print('SAVING PASSWORD as: ',password)
        userobject = UserDetails(user_type=usertype, username=user_id, user_id=user_id, email=email, contact_number=phone,password=password )
        userobject.set_password(password)
        userobject.save()
        print('USER OBJECT SAVED. CHECK DB')

        if usertype == 'student':
            rollno = request.POST.get('rollno')
            #student classid is foreign key, investigating on it
            classid = request.POST.get('classid')
            class_student = Class.objects.filter(class_id__exact = classid)[0]

            student_object = Student(student_name = username, student_id = user_id, student_email = email, student_password = password_enc,student_rollno =rollno,student_contact=phone,student_classid = class_student )

            student_object.save()
            print('STUDENT OBJECT SAVED')

            return redirect('login.html')
        elif usertype == 'teacher':
            teacher_object = Teacher(teacher_name=username,teacher_id = user_id, teacher_email=email, teacher_password=password_enc, teacher_contact=phone )
            teacher_object.save()
            print('TEACHER OBJECT SAVED')

            return redirect('login.html')

    return render(request,'register.html')

def register_student(request):
    return render(request, 'register_as_student.html')

def register_teacher(request):
    print('********************************************************************you have called register_as_teacher')
    return render(request,'register_as_teacher.html')


def random_func(request):
    if request.user.is_authenticated:
        return HttpResponse('You came here authenticated')
    else:
        return HttpResponse('You came here without auth Sorry')

def create_test(request):
    if request.method =="POST":
        uploaded_file = request.FILES['document']

        teacher_id = request.POST.get('teacherid')#

        teacher_obj  = Teacher.objects.all().filter(teacher_id=teacher_id)[0]

        testname = request.POST.get('testname')#

        max_marks = request.POST.get('maxmarks')#
        passing_marks = request.POST.get('passingmarks')
        classname = request.POST.get('classname')
        class_found = Class.objects.all().filter(class_name=classname)[0]


        testid = ''.join(random.choices(string.ascii_uppercase + string.digits,k= 10))

        test_object = Test(test_id = testid, test_name=testname, max_marks=max_marks, passing_marks=passing_marks, class_assigned = class_found,teacher_id=teacher_obj)        

        fs = FileSystemStorage()

        filename_gen = uploaded_file.name.split('.')
        print(filename_gen)
        randomnumber = str(random.randint(1000,9999))

        filename = filename_gen[0]+randomnumber+'.'+filename_gen[1]

        fs.save(filename,uploaded_file)

        test_object = Test(test_id = testid, test_name=testname, max_marks=max_marks, passing_marks=passing_marks, class_assigned = class_found,teacher_id=teacher_obj,csv_filename=filename)
        #print(os.path.join(BASE_DIR,'media'))
        test_object.save()
        df = pd.read_csv (os.path.join(BASE_DIR,'media')+'\\'+filename)
        #Remove absent students and show the piechart
        absent_plot = showAbsentPieChart(df)
        df=df[df.Present != 0]
        #Show Grade Bar Graph
        grade_plot = showGradeBargraph(df)
        #Show Average pie chart
        avg_plot = showAveragePieChart(df)
        passfail = showPassFail(df,int(passing_marks))

        table = showtable(df)
        plot_dict = {'absent_plot':absent_plot,'grade_plot':grade_plot,'avg_plot':avg_plot,'passfail':passfail,'table':table,'testid':testid}
        return render(request,'report.html',plot_dict)
    else:
        return render(request, 'create_test.html')

def demodashboard(request):
    return render(request, 'dashboard.html')

def show_report(request,testid):
    test_object = Test.objects.all().filter(test_id  =testid)[0]
    filename = test_object.csv_filename
    max_marks = test_object.max_marks
    passing_marks = test_object.passing_marks

    df = pd.read_csv (os.path.join(BASE_DIR,'media')+'\\'+filename)
    #Remove absent students and show the piechart
    absent_plot = showAbsentPieChart(df)
    df=df[df.Present != 0]
    #Show Grade Bar Graph
    grade_plot = showGradeBargraph(df)
    #Show Average pie chart
    avg_plot = showAveragePieChart(df)
    passfail = showPassFail(df,int(passing_marks))

    table = showtable(df)
    plot_dict = {'absent_plot':absent_plot,'grade_plot':grade_plot,'avg_plot':avg_plot,'passfail':passfail,'table':table,'testid':testid}
    return render(request,'report.html',plot_dict)



def ReportCard(request):
    studentID="A2AUVRD5EC"
    firstName = Student.objects.filter(student_id=studentID)[0]
    print(firstName)
    #Pass link for qr code,First name,lastname,studentid or roll numebr
    generateReportCard("LINK","Nikhil","Kulkarni",studentID)
    return render(request,'ReportCard.html')


def generate(studentURL,name,studentSurname,studentId):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(studentURL)
    qr.make(fit=True)
    img1 = qr.make_image(fill_color="black", back_color="white")

    img = Image.open("MeritAnalyser/static/images/charts/template.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("MeritAnalyser/static/images/charts/arial.ttf", 30)
    draw.text((65, 400),name,(10,90,100),font=font)
    draw.text((65, 525),studentSurname,(10,90,100),font=font)
    draw.text((65, 650),str(studentId),(10,90,100),font=font)

    
    return img1,img


def merge_img(ReportCard, QRcode):
    layer = Image.new('RGBA', ReportCard.size, (0,0,0,0))
    QRcode = QRcode.resize((150, 150))
    layer.paste(QRcode, (100, 900))
    piechart= Image.open("MeritAnalyser/static/images/charts/fig1.png")
    piechart = piechart.resize((350, 350))

    layer.paste(piechart,(450,40))
    graph1= Image.open("MeritAnalyser/static/images/charts/fig2.png")
    graph1 = graph1.resize((350, 350))

    layer.paste(graph1,(450,440))


    graph2= Image.open("MeritAnalyser/static/images/charts/fig3.png")
    graph2 = graph2.resize((350, 350))

    layer.paste(graph2,(450,820)) 

    return Image.composite(layer, ReportCard, layer)



def generateReportCard(studentURL,studentName,studentLastName,RollNumber):
    #generate Charts here and save in MeritAnalyser/static/images/charts as fig1,fig2,fig3
    QRcode,ReportCard=generate(studentURL,studentName,studentLastName,RollNumber)
    img = merge_img(ReportCard, QRcode)
    img.save('MeritAnalyser/static/images/ReportCards/ReportCard'+str(RollNumber)+'.jpg')

    return