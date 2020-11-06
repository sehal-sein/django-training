import graphene
from graphene_django.types import DjangoObjectType
from blog.model.blog_managment_model import ProfileModel
from blog.schema.blog_schema import Blog, BlogModel

class Profile(DjangoObjectType):

    user_blogs = graphene.List(Blog)

    class Meta:
        model = ProfileModel

    def resolve_user_blogs(self, info):
        return BlogModel.objects.filter(posted_by=self.username)