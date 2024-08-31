from itertools import repeat

from django.shortcuts import render
from .models import Dish, DishCategory, WhyUsBlock, AboutUsText, Gallery, HeroSlider
from .forms import UserReservationForm

def main_page_view(request):
    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True).filter(is_special=False)
    special_dishes = Dish.objects.filter(is_special=True).filter(is_visible=True)
    why_us_blocks = WhyUsBlock.objects.filter(is_visible=True)
    about_us_texts = AboutUsText.objects.filter(is_visible=True, is_video_link=False)
    about_us_video = AboutUsText.objects.filter(is_visible=True, is_video_link=True).first()
    gallery = Gallery.objects.filter(is_visible=True)
    hero_sliders = HeroSlider.objects.filter(is_visible=True)

    user_reservation = UserReservationForm()

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'why_us_blocks': why_us_blocks,
        'about_us_texts': about_us_texts,
        'about_us_video': about_us_video,
        'gallery': gallery,
        'hero_sliders': hero_sliders,

        'user_reservation': user_reservation,
    })
