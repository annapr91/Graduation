from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, BadHeaderError
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView, FormView
from requests import request

from .forms import RegisUserForm, RegistrationKind, LoginUserForm, PasswordReset, UserNameChange
from .models import Child, Kindergarden
from mainpage.forms import PasswordChangingForm

User = get_user_model()
# Create your views here.
class RegisterUser(CreateView):
    form_class = RegisUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('registration')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('first')


class PasswordsChange(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_complete')


def success_password(request):
    return render(request, 'passwordcompleted.html', {})


def registchildren(request):
    id = request.user.id
    form = RegistrationKind()

    if request.method == 'POST':
        form = RegistrationKind(request.POST, instance=Child())
        form.instance.roditeli_id = id

        if form.is_valid():
            sad_id = form.instance.det_sads_id
            sad = Kindergarden.objects.get(id=sad_id)
            if sad.free_places == True:
                sad.num_register_child += 1
                sad.save()
                form.instance.ochered = sad.num_register_child
                form.save()
            else:
                raise ValidationError("No free palces available . Please try later or check other kindergardens")

            return redirect('/')

    return render(request, 'registrchild.html', {'form': form, 'id': id})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('first')


def mydata(request):
    child= Child.objects.filter(roditeli_id=request.user)
    if request.method == 'POST':
        user_form  = UserNameChange(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('/')
    else:
        user_form = UserNameChange(instance=request.user)


    return render(request, 'password/name_change.html',{'data': child,'user_form': user_form })



def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordReset(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            data_name = password_reset_form.cleaned_data['username']
            print(data)
            print(data_name)
            associated_users = User.objects.filter(email=data, username=data_name)
            print(associated_users)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    # email_template_name = "main/password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string('password/password_reset_email.txt', c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/")
    password_reset_form = PasswordReset()
    return render(request=request, template_name="password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


# class NameChange(LoginRequiredMixin, FormView):
#     form = UserNameChange
#     template_name = 'password/name_change.html'
#     reverse_lazy= '/'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# def name_change(request):
#     if request.method == 'POST':
#         user_form  = UserNameChange(request.POST, instance=request.user)
#         if user_form.is_valid():
#             user_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='mydata')
#     else:
#         user_form = UserNameChange(instance=request.user)
#
#     return render(request, 'password/name_change.html',{'user_form': user_form})