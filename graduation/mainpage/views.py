from django.contrib.auth import logout
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView

from .forms import ContactForm
from django.conf import settings

from account.models import Kindergarden,Child
from .filters import KindFilter



# Create your views here.
def first(request):
    return render(request, 'first_page.html')


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
        return Kindergarden.objects.filter(name__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        try:
            context['q']= self.request.GET.get('q')
        except Exception:
            raise 404
        return context

class KindergardenInfo(DetailView):
    model = Kindergarden
    pk_url_kwarg = 'sad_id'
    template_name = 'kindergarden_detail.html'
    # context_object_name = 'sad'


    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['child']= Child.objects.filter()
        return context


