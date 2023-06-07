from django.shortcuts import render, get_object_or_404
from .models import RealtyType, Realty, Owner
from cart.forms import CartAddRealtyForm
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .forms import RealtyForm
from django.core.exceptions import PermissionDenied
import requests

def realty_list(request, realty_type_name = None):
    realty_type = None
    types = RealtyType.objects.all()
    realties = Realty.objects.all();

    if realty_type_name:
        realty_type = get_object_or_404(RealtyType, name = realty_type_name)
        realties = realties.filter(type = realty_type)

    sort = request.GET.get('sort')
    if sort == 'ascending':
        realties = realties.order_by('cost')
    elif sort == 'descending':
        realties = realties.order_by('-cost')

    return render(request, 'store/realty/list.html',
                  {
                      'type': realty_type,
                      'types': types,
                      'realties': realties,
                  })


def realty_detail(request, id):
    realty = get_object_or_404(Realty, id=id)
    cart_realty_form = CartAddRealtyForm()
    joke = requests.get('https://official-joke-api.appspot.com/jokes/programming/random').json()[0]

    return render(request, 'store/realty/detail.html', {'realty': realty,
                                                   'cart_realty_form': cart_realty_form,
                                                   'joke': joke['setup'] + joke['punchline']})


 
# сохранение данных в бд
def realty_create(request):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    form = RealtyForm()

    if request.method == "POST":
        
        realty = Realty.objects.create(name=request.POST.get('name'),
                                        owner=Owner.objects.get(id=request.POST.get('owner')),
                                        cost=request.POST.get('cost'),
                                        type=RealtyType.objects.get(id=request.POST.get('type')),
                                        description=request.POST.get('description'),
                                        image=request.FILES.get('image'))

        realty.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "store/realty/create.html", {"form" : form})
    
 
# изменение данных в бд
def realty_edit(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    try:
        realty = Realty.objects.get(id=id)
        form = RealtyForm(initial={'name':realty.name, 'owner':realty.owner,
                                    'cost':realty.cost, 'type':realty.type,
                                    'description':realty.description, 'image':realty.image })

        if request.method == "POST":
            realty.owner=Owner.objects.get(id=request.POST.get('owner'))
            realty.cost=request.POST.get('cost')
            realty.type=RealtyType.objects.get(id=request.POST.get('type'))
            realty.description=request.POST.get('description')
            if request.FILES.get('image') != None:
                realty.image=request.FILES.get('image')

            realty.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "store/realty/edit.html", {"realty": realty, "form" : form})
    except realty.DoesNotExist:
        return HttpResponseNotFound("<h2>realty not found</h2>")
     
# удаление данных из бд
def realty_delete(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("You do not have access to this page.")

    try:
        realty = Realty.objects.get(id=id)
        realty.delete()
        return HttpResponseRedirect("/")
    except realty.DoesNotExist:
        return HttpResponseNotFound("<h2>realty not found</h2>")
