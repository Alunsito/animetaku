from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect, Http404
from .models import anime, user, review
from django.urls import reverse
from django.template import loader
from django.views import generic

def index(anime,request):
    latest_anime = anime.objects.order_by('-release_date')[:5]
    context={'latest_anime': latest_anime}
    return render(request, 'index.html', context)

def user_registered(request, user_id):
    info = get_object_or_404(user, pk=user_id)
    return render(request, 'detail.html', {'name': info})

def anime_review(request, review_id):
    anime_item = get_object_or_404(anime, spk=review_id)
    try:
        selected_review = review.text_post.get(pk=request.POST['review'])
    except (KeyError, anime_item.DoesNotExist):
        return render(request, 'animeapp/detail.html', {
            'anime': anime,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_review.votes += 1
        selected_review.save()
    return HttpResponseRedirect(reverse('animeapp:reviews', args=(review_id.user.post)))

class IndexView(generic.ListView):
    template_name = "animeapp/index.html"
    context_object_name = 'latest_anime'
    def get_queryset(self):
        return anime.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = anime
    template_name = 'animeapp/detail.html'


    
