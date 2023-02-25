from django.contrib.auth import logout
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView
from django_filters.views import FilterView

from .forms import ContactForm
from django.conf import settings

from account.models import Kindergarden,Child
from .filters import KindFilter



# Create your views here.
def first(request):

    value1 = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam cum nostrum reiciendis at autem, quidem optio voluptatum soluta ea dolores!\n" \
             "Lorem ipsum dolor sit amet consectetur adipisicing elit"
    value2= "Kindergarden Aperiam cum nostrum reiciendis at autem, quidem optio voluptatum soluta ea dolores!\n" \
             "Lorem ipsum dolor sit amet consectetur adipisicing elit"
        # "Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam cum nostrum reiciendis at autem, quidem optio voluptatum soluta ea dolores!\n" \
        #     "Lorem ipsum dolor sit amet consectetur adipisicing elit"
    return render(request, 'first_page.html',{'value1': value1,'value2': value2})


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            name = form.cleaned_data['name']

            html = render_to_string('emailform.html', {'subject': subject, 'message': message,'sender': sender,'name': name})
            send_mail(f'{name},{sender} - {subject}', message,
                      settings.EMAIL_HOST_USER, [settings.RECIPIENTS_EMAIL], fail_silently=False,html_message=html)
            return redirect('first')
    return render(request, 'contacts.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

class KidsKindergarden(ListView):
    model = Kindergarden
    template_name = 'buildings.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q','Not found area of kindegarden')
        print(context['q'] )
        context['myfilter']= KindFilter(self.request.GET,queryset=Kindergarden.objects.all())
        print( context['myfilter'])
        return context

    # def get_queryset(self):
    #     sadu = Kindergarden.objects.all()
    #      return sadu

class Search(ListView):
    model=Kindergarden
    template_name = 'buildings.html'

    def get_queryset(self):
        search_query= self.request.GET.get("q")
        if search_query:
            Kindergarden.objects.filter (translations__name__contains = search_query)
            return Kindergarden.objects.filter(translations__name__contains=self.request.GET.get("q"))
        else:
            return Kindergarden.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        print(context)
        return context

class KindergardenInfo(DetailView):
    model = Kindergarden
    pk_url_kwarg = 'sad_id'
    template_name = 'kindergarden_detail.html'
    # context_object_name = 'sad'


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['child']= Child.objects.filter()
        print(context['object'].addition.all())
        print(context['object'].addition)
        return context


def school(request):
    return render(request, "info_school.html")



