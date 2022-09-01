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

    context = {
        'adventure': adventure,
    }

    return render(request, 'adventures/adventure_detail.html', context)


def excursion_detail(request):
    """ A view to show excursion details """

    excursions = Excursion.objects.all()
    countries = None

    if request.GET:
        if 'country' in request.GET:
            countries = request.GET['country'].split(',')
            excursions = excursions.filter(country__name__in=countries)
            countries = Country.objects.filter(name__in=countries)

    context = {
        'excursions': excursions,
    }

    return render(request, 'adventures/excursion_detail.html', context)
