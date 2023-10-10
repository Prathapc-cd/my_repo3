from django.http import HttpResponse
from django.template import loader
from .models import Mobile


def whatsapp(request):
  mymobile=Mobile.objects.all().values()
  template = loader.get_template('whats_app.html')
  context = {
    'mymobile': mymobile,
  }
  return HttpResponse(template.render(context, request))
  r
 