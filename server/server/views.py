from django.http import JsonResponse
from django.http import HttpResponse

films = {
    0:{'title':"La vérité si je mens 2", 'year':"2001", 'imgUrl':"./images/film1.jpg"},
    1:{'title':"La tour montparnasse infernale", 'year':"2001", 'imgUrl':"./images/film2.jpg"},
    2:{'title':"Astérix et Obélix mission Cléopâtre", 'year':"2002", 'imgUrl':"./images/film3.jpg"},
    3:{'title':"OSS177 Le caire Nid d'espions", 'year':"2006", 'imgUrl':"./images/film4.jpg"}
}

def hello(request):
  return JsonResponse(films)
  #return JsonResponse({'response_text':'hello hello world!'})
