#Hierarchy
#Course
#course section
#episode

from django.db import models
import uuid
from django.db.models.fields.related import ForeignKey

class Sector(models.Model):
    name = models.CharField(max_length=255)
    sector_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    related_course=models.ManyToManyField('Courses')
    sector_image=models.ImageField(upload_to )

class Course(models.Model):
    title=models.CharField(maxlength=255)
    description=models.TextField()
    created=models.DateTimeField(auto_now_add= True)
    updated=models.DateTimeField(auto_now_add= True)
    #author=models.ForeignKey(models.ForeignKey)
    language=models.Charfield(maxlength=50)
    course_section=models.ManyToManyField('CourseSection')
    comments=models.ManyToManyField('Comment')
    image_url=models.ImageField(upload_to='course_images')
    course_uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)

class CourseSection( models.Model):
    section_title=models.CharField(max_length=255)
    episodes=models.ManyToManyField('episode')

class Episode(models.Model):
    title=models.CharField(max_length=255)
    file=models.FileField(upload_to='course_videos')
    length=models.DecimalField(max_length=10, decimal_places=2)


class Comment(models.Model):
    user=models.ForeignKey(User)
    message=models.TextField()
    created=models.DateTimeField(auto_now=True)


#course section
#episode



