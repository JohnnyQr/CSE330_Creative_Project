from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from course.models import Course, Comment, Message


def check_login(fn):

    def wrap(request, *args, **kwargs):
        if 'username' not in request.session or 'userid' not in request.session:
            cookie_username = request.COOKIES.get('username')
            cookie_userid = request.COOKIES.get('userid')
            if not cookie_username or not cookie_userid:
                return HttpResponseRedirect('/user/login')
            else:
                request.session['username'] = cookie_username
                request.session['userid'] = cookie_userid


        return fn(request, *args, **kwargs)
    return wrap


@check_login
def add_course(request):
    if request.method == "GET":

        return render(request, 'course/add_course.html')
    elif request.method == 'POST':
        userid = request.session['userid']
        title = request.POST['title']
        instrument = request.POST['instrument']
        content = request.POST['content']
        level = request.POST['level']
        price = request.POST['price']
        location = request.POST['location']
        certification = request.POST['certifi']

        Course.objects.create(title=title, instrument=instrument, content=content,
                              level=level, price=price, location=location,
                              certification=certification, user_id=userid)
        return HttpResponseRedirect('/course/main')



@check_login
def section(request):
    messages = []
    userid = request.session['userid']
    courses = Course.objects.filter(user_id=userid, is_active=True)
    for course in courses:
        try:
            message = Message.objects.get(the_course_id=course.id)
            if message:
                messages.append(message)
        except Exception as e:
            print('get message error %s' % e)


    return render(request, 'course/sections.html', locals())



@check_login
def view_section(request):
    instrument = request.GET.get('instrument')
    try:
        courses = Course.objects.filter(instrument=instrument, is_active=True)
    except Exception as e:
        print('view section error %s' % e)

    return render(request, 'course/main.html', locals())


@check_login
def view_section_filter(request):
    instrument = request.GET.get('instrument')

    if request.method == 'POST':
        level = request.POST['level']
        certifi = request.POST['certifi']
        price = request.POST['price']
        try:
            courses = Course.objects.filter(instrument=instrument, level=level, certification=certifi, price__lte=price, is_active=True)
        except Exception as e:
            print('filter course error %s' % e)

    return render(request, 'course/main.html', locals())



@check_login
def show_all(request):

    courses = Course.objects.filter(is_active=True)

    return render(request, 'course/all.html', locals())



@check_login
def all_filter(request):

    if request.method == 'POST':
        level = request.POST['level']
        certifi = request.POST['certifi']
        price = request.POST['price']
        try:
            courses = Course.objects.filter(level=level, certification=certifi, price__lte=price,
                                            is_active=True)
        except Exception as e:
            print('filter course error %s' % e)

    return render(request, 'course/all.html', locals())



@check_login
def all_filter_location(request):
    if request.method == 'POST':
        location = request.POST['location']
        print(location)
        try:
            courses = Course.objects.filter(location__icontains=location, is_active=True)
        except Exception as e:
            print('filter course error %s' % e)

    return render(request, 'course/all.html', locals())






@check_login
def all_course(request):
    courses = Course.objects.filter(is_active=True)

    return render(request, 'course/main.html', locals())


@check_login
def view_course(request):
    course_id = request.GET.get('course_id')
    try:
        course = Course.objects.get(id=course_id, is_active=True)
        comments = Comment.objects.filter(the_course_id=course_id)


    except Exception as e:
        print('view course error %s' % e)

    return render(request, 'course/viewCourse.html', locals())




@check_login
def add_comment(request):
    course_id = request.GET.get('course_id')
    userid = request.session['userid']
    if request.method == 'POST':
        comment = request.POST['comment']

        Comment.objects.create(content=comment, user_id=userid, the_course_id=course_id)

    return HttpResponseRedirect('/course/view_course?course_id=%s' % course_id)



def send_message_page(request):
    course_id = request.GET.get('course_id')
    userid = request.session['userid']
    course = Course.objects.get(id=course_id)
    return render(request, 'course/sendMessage.html', locals())




@check_login
def send_message(request):
    course_id = request.GET.get('course_id')
    userid = request.session['userid']
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']

        Message.objects.create(title=title, message=message, sender_id=userid, the_course_id=course_id)

    return HttpResponseRedirect('/course/view_course?course_id=%s' % course_id)





@check_login
def view_message(request):
    message_id = request.GET.get('message_id')
    try:
        message = Message.objects.get(id=message_id)

    except Exception as e:
        print('view message error %s' % e)

    return render(request, 'course/viewMessage.html', locals())






@check_login
def update_course(request, course_id):
    try:
        course = Course.objects.get(id=course_id, is_active=True)
    except Exception as e:
        print('update course error %s' % e)
        return render(request, 'course/updateError.html')

    if request.method == 'GET':
        return render(request, 'course/update.html', locals())
    elif request.method == "POST":
        price = request.POST['price']
        level = request.POST['level']
        content = request.POST['content']

        course.price = price
        course.level = level
        course.content = content

        course.save()
        return HttpResponseRedirect('/course/main')





@check_login
def delete_course(request):
    course_id = request.GET.get('course_id')
    try:
        course = Course.objects.get(id=course_id, is_active=True)
    except Exception as e:
        print('delete course error %s' % e)
    course.is_active = False
    course.save()

    return HttpResponseRedirect('/course/main')







