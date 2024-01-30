from django.core.exceptions import ValidationError
from django.db import models


def validate_image_size(image):
    width, height = image.width, image.height
    if width != 300 or height != 210:  # Corrected image size
        raise ValidationError(f'The image must be exactly 300x211 pixels. Current size is {width}x{height} pixels.')


# Create your models here.
class Gallery(models.Model):
    gallery_img = models.ImageField(upload_to='gallery/', validators=[validate_image_size])
    gallery_title = models.CharField(max_length=50)
    gallery_description = models.TextField()

    def __str__(self):
        return self.gallery_title


def team_validate_image_size(image):
    width, height = image.width, image.height
    if width != 265 or height != 265:  # Corrected image size
        raise ValidationError(f'The image must be exactly 265x265 pixels. Current size is {width}x{height} pixels.')


class Team(models.Model):
    member_img = models.ImageField(upload_to='team/',)
    member_name = models.CharField(max_length=200)
    member_title = models.CharField(max_length=200)
    department = models.CharField(max_length=200, blank=True)
    institution = models.CharField(max_length=200, blank=True)
    linkedin_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
