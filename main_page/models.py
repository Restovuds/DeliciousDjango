import uuid, os
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


#  Dish category
class DishCategory(models.Model):
    name = models.CharField(max_length=40, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.name} [{self.position}]'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('position',)
        # ordering = ('-position',)


#  Dishes
class Dish(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)


    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_special = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    ingredients = models.CharField(max_length=300)
    description = models.TextField(max_length=1000, blank=True)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    category = models.ForeignKey(DishCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.category.name}] {self.name}: {self.position}'

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'
        ordering = ('category', 'position',)


# Why Us Blocks
class WhyUsBlock(models.Model):
    heading = models.CharField(max_length=50, unique=True)
    text = models.TextField(max_length=150)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.heading} [{self.position}]'

    class Meta:
        verbose_name = 'Why Us Block'
        verbose_name_plural = 'Why Us Blocks'
        ordering = ('-is_visible', 'position')


# About Us Text
class AboutUsText(models.Model):
    short_description = models.CharField(max_length=30)
    is_heading = models.BooleanField(default=False)
    is_paragraph = models.BooleanField(default=False)
    is_unordered_list = models.BooleanField(default=False)
    is_video_link = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)
    text = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.short_description} [{self.position}]'

    class Meta:
        verbose_name = 'About Us Text'
        verbose_name_plural = 'About Us Texts'
        ordering = ('position',)


# Galleries photos
class Gallery(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/gallery/', filename)

    photo = models.ImageField(upload_to=get_file_name, blank=False)
    is_visible = models.BooleanField(default=True)
    short_description = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.short_description} [PK: {self.pk}]'

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
        ordering = ('pk',)


# Hero sliders
class HeroSlider(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/hero/', filename)

    photo = models.ImageField(upload_to=get_file_name, blank=False)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)
    heading = models.CharField(max_length=50, blank=False)
    paragraph = models.TextField(max_length=150, blank=False)

    def __str__(self):
        return f'{self.heading} [{self.position}]'

    class Meta:
        ordering = ('-is_visible', 'position', )
        verbose_name = 'Hero Slider'
        verbose_name_plural = 'Hero Sliders'


# Events
class Event(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/event/', filename)

    name = models.CharField(max_length=50, unique=True)
    price = models.SmallIntegerField()
    image = models.ImageField(upload_to=get_file_name, blank=False)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} [{self.position}]'

    class Meta:
        ordering = ('is_visible', 'position',)
        verbose_name = 'Event'
        verbose_name_plural = 'Events'



# Event texts
class EventText(models.Model):
    text = models.TextField(max_length=500)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    is_paragraph = models.BooleanField(default=True)
    is_unordered_list = models.BooleanField(default=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.text) > 30:
            return f'[{self.event.name}] {self.text[0:30]}... [{self.position}]'
        else:
            return f'{self.text} [{self.position}]'

    class Meta:
        ordering = ('event' ,'is_visible', 'position',)
        verbose_name = 'Event Text'
        verbose_name_plural = 'Event Texts'


# chefs
class Chef(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/chef/', filename)

    name = models.CharField(max_length=50)
    rank = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name, blank=False)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'[{self.position}] {self.name} - {self.rank}'

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'
        ordering = ('is_visible', 'position',)


# chefs social
class ChefSocial(models.Model):
    social_name = models.CharField(max_length=20)
    link = models.URLField(max_length=300)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.chef.name} - {self.social_name}'

    class Meta:
        ordering = ('is_visible', 'position',)
        verbose_name = 'Chefs Social'
        verbose_name_plural = 'Chefs Socials'


# reviews
class Review(models.Model):
    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/review/', filename)

    photo = models.ImageField(upload_to=get_file_name, blank=False, default='')
    name = models.CharField(max_length=50)
    worked_at = models.CharField(max_length=50)
    rating = models.SmallIntegerField(default=5, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    text = models.TextField(max_length=500)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'[{self.position}] {self.name} - {self.rating} stars'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ('position',)


