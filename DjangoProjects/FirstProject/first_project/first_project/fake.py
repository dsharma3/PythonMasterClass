import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()

import random
from faker import Faker
from first_app.models import Category,Blog


category = ['Entertainment','Engineering','Information Technology','Spirituality']
def add_category():
    t = Category.objects.get_or_create(category_name = random.choice(category))[0]
    t.save()
    return t

fake = Faker()
def populate(N=5):
    for entry in range(N):
        category = add_category()
        fake_title = fake.name()
        fake_text = fake.text()

        t = Blog.objects.get_or_create(category = category,title=fake_title,blog_text = fake_text)[0]
        t.save()
        

populate(10)
        