from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User
import hashlib
# Create your views here.


def reg_view(request):
    # sign-up
    if request.method == 'GET':
        return render(request, 'user/signUp.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if username == '':
            return render(request, 'user/usernameNull.html')

        if password1 != password2:
            return render(request, 'user/passwordNotMatch.html')



        old_users = User.objects.filter(username=username)
        if old_users:
            return render(request, 'user/usernameUsed.html')

        m = hashlib.md5()
        m.update(password1.encode())
        password_hashed = m.hexdigest()

        try:
            newUser = User.objects.create(username=username, password=password_hashed)
        except Exception as e:
            print('--create user error %s' % e)
            return render(request, 'user/usernameUsed.html')

        request.session['username'] = username
        request.session['username'] = newUser.id


        return HttpResponseRedirect('user/login')


def login_view(request):

    if request.method == "GET":
        if request.session.get('username') and request.session.get('userid'):
            return HttpResponseRedirect('/course/section')
        cookie_username = request.COOKIES.get('username')
        cookie_userid = request.COOKIES.get('userid')
        if cookie_username and cookie_userid:
            request.session['username'] = cookie_username
            request.session['userid'] = cookie_userid
            return HttpResponseRedirect('/course/section')

        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--login user error %s' % e)
            return render(request, 'user/loginError.html')

        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            return render(request, 'user/loginError.html')

        request.session['username'] = username
        request.session['userid'] = user.id

        resp = HttpResponseRedirect('/course/section')
        if 'remember' in request.POST:
            resp.set_cookie('username', username, 3600*24)
            resp.set_cookie('userid', user.id, 3600*24)


        return resp



def logout_view(request):
    # if request.method == 'GET':
    #     if request.session.get('username') and request.session.get('userid'):
    #         try:
    #             request.session.clear()
    #         except Exception as e:
    #             print('--logout error %s' % e)
    #         return HttpResponseRedirect('/index/main')

    if 'username' in request.session:
        del request.session['username']

    if 'userid' in request.session:
        del request.session['userid']

    resp = HttpResponseRedirect('/index/main')
    if 'username' in request.COOKIES:
        resp.delete_cookie('username')

    if 'userid' in request.COOKIES:
        resp.delete_cookie('userid')

    return resp

