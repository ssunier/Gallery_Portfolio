from django.http import HttpResponse
from django.template import RequestContext, Context, loader

from portfolio.models import Gallery, Music

# Create your views here.
def index(request):
  template = loader.get_template('portfolio/index.html')
  context = Context({''})
  return HttpResponse(template.render(context))

def gallery(request):
  latest_gallery_list=Gallery.objects.order_by('-post_date')
  template = loader.get_template('portfolio/gallery.html')
  context = RequestContext(request, {
    'latest_gallery_list': latest_gallery_list,
    })
  return HttpResponse(template.render(context))

def music(request):
  latest_music_list = Music.objects.order_by('-post_date')[:5]
  template = loader.get_template('portfolio/music.html')
  context = RequestContext(request, {'latest_music_list': latest_music_list,})
  return HttpResponse(template.render(context))

def about(request):
  return HttpResponse("Hello you have found leila's about me page")