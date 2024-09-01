from django.contrib import admin
from .models import (Dish,
                     DishCategory,
                     WhyUsBlock,
                     AboutUsText,
                     Gallery,
                     HeroSlider,
                     Event,
                     EventText,
                     Chef,
                     ChefSocial,
                     Review)

admin.site.register(Dish)
admin.site.register(DishCategory)
admin.site.register(WhyUsBlock)
admin.site.register(AboutUsText)
admin.site.register(Gallery)
admin.site.register(HeroSlider)
admin.site.register(Event)
admin.site.register(EventText)
admin.site.register(Chef)
admin.site.register(ChefSocial)
admin.site.register(Review)

