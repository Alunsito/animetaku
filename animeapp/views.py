from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import anime
from django.template import loader

def index(request):
    latest_anime = anime.objects.order_by('-release_date')[:5]
    context={'latest_anime': latest_anime}
    return render(request, 'index.html')

def user_registered(request, user_id):
    info = get_obj_or_404(user, pk=user_id)
    return render(request, 'detail.html', {'name': name})

def anime_review(request, review_id):
    anime_item = get_object_or_404(anime, spk=name_anime)
    try:
        selected_review = review.text_post.get(pk=request.POST['review'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'animeapp/detail.html', {
            'anime': anime,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_review.votes += 1
        selected_review.save()
    return HttpResponseRedirect(reverse('animeapp:reviews', args=(review.user.post)))