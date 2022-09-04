from django.shortcuts import render, get_object_or_404
from .models import Adventure, Category, Excursion, Country

# Create your views here.


def all_adventures(request):
    """ A view to show all adventures, including sorting and search queries """

    adventures = Adventure.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            adventures = adventures.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'adventures': adventures,
        'current_categories': categories,
    }

    return render(request, 'adventures/adventures.html', context)


def adventure_detail(request, adventure_id):
    """ A view to show adventure details """

    adventure = get_object_or_404(Adventure, pk=adventure_id)
    request.session['adventure_id'] = adventure.id

    context = {
        'adventure': adventure,
    }

    return render(request, 'adventures/adventure_detail.html', context)


def excursion_detail(request, country):
    """ A view to show excursion details """

    excursions = Excursion.objects.all()
    excursions = excursions.filter(country__name__contains=country)
    adventure_id = request.session.get('adventure_id', None)

    context = {
        'excursions': excursions,
        'adventure_id': adventure_id
    }

    return render(request, 'adventures/excursion_detail.html', context)
