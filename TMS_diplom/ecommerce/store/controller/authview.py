from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from store.forms import CustomUserForm


def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            subject = 'Спасибо за регистрацию ! Добро пожаловать на сайт, i-Shop!'
            message = f'Спасибо за регистрацию, {username} .Залетайте на сайт i-Shop! У нас самые лучшие цены в городе!'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            form.save()
            messages.success(request, 'Регистрация прошла успещно! Авторизуйтесь, чтобы продолжить')
            # html_template = 'register_email.html'
            # html_message = render_to_string(html_template)
            # subject = 'Welcome to Service-Verse'
            # email_from = settings.EMAIL_HOST_USER
            # #recipient_list = [email]
            # message = EmailMessage(subject, html_message,
            #                        email_from)
            # message.content_subtype = 'html'
            # message.send()
            #return redirect('success')
            return redirect('/login')
    context = {'form':form}
    return render(request, 'store/auth/register.html', context)



def success(request):
    return render(request, 'success.html')



def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Вы уже вошли в систему!')
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request, 'Вход в систему успешно выполнен!')
                return redirect('/')
            else:
                messages.error(request, 'Неправильно введено Имя пользователя или Пароль!')
                return redirect('/login')

        return render(request, 'store/auth/login.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Выход из системы выполнен успешно!')
    return redirect('/')
