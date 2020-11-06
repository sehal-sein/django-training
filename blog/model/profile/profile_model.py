from django.db import models

# Create your models here.
class ProfileModel(models.Model):
    name = models.TextField()
    username = models.TextField()
    email = models.TextField()


    @staticmethod
    def get_list_of_profiles():
        return ProfileModel.objects.all()

    def get_profile_by_id(id):
        return ProfileModel.objects.get(pk=id)