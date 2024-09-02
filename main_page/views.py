from itertools import repeat

from django.shortcuts import render, redirect
from .models import (Dish, DishCategory, WhyUsBlock,
                     AboutUsText, Gallery, HeroSlider,
                     Event, EventText, Chef, ChefSocial,
                     Review)
from .forms import UserReservationForm, UserContactForm

def main_page_view(request):
    if request.method == 'POST':
        if request.POST.get('form_type') == 'book_a_table':
            user_reservation = UserReservationForm(request.POST)
            if user_reservation.is_valid():
                user_reservation.save()
                return redirect('/#book-a-table')

        if request.POST.get('form_type') == 'contact_us':
            user_contact = UserContactForm(request.POST)
            if user_contact.is_valid():
                user_contact.save()
                return redirect('/#contact')

    if request.method == 'GET':
        categories = DishCategory.objects.filter(is_visible=True)
        dishes = Dish.objects.filter(is_visible=True).filter(is_special=False)
        special_dishes = Dish.objects.filter(is_special=True).filter(is_visible=True)
        why_us_blocks = WhyUsBlock.objects.filter(is_visible=True)
        about_us_texts = AboutUsText.objects.filter(is_visible=True, is_video_link=False)
        about_us_video = AboutUsText.objects.filter(is_visible=True, is_video_link=True).first()
        gallery = Gallery.objects.filter(is_visible=True)
        hero_sliders = HeroSlider.objects.filter(is_visible=True)
        events = Event.objects.filter(is_visible=True)
        event_texts = EventText.objects.filter(is_visible=True)
        chefs = Chef.objects.filter(is_visible=True)
        chef_social = ChefSocial.objects.filter(is_visible=True)
        reviews = Review.objects.filter(is_visible=True)

        user_reservation = UserReservationForm()
        user_contact = UserContactForm()

        context = {
            'categories': categories,
            'dishes': dishes,
            'special_dishes': special_dishes,
            'why_us_blocks': why_us_blocks,
            'about_us_texts': about_us_texts,
            'about_us_video': about_us_video,
            'gallery': gallery,
            'hero_sliders': hero_sliders,
            'events': events,
            'event_texts': event_texts,
            'chefs': chefs,
            'chef_social': chef_social,
            'reviews': reviews,

            'user_reservation': user_reservation,
            'user_contact': user_contact,
        }

        return render(request, 'main_page.html', context=context)
