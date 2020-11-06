from blog.views import update_blog
import graphene
from graphene.types.mutation import Mutation
from blog.schema.blog_schema import Blog, BlogModel, CreateBlog, UpdateBlog


class Query(graphene.ObjectType):

    blogs = graphene.List(Blog)
    blog = graphene.Field(
        Blog,
        id=graphene.Int(required=True)
    )

    
    def resolve_blogs(self, info):
        return BlogModel.objects.all()

    def resolve_blog(self, info, id):
        return BlogModel.objects.get(pk=id)


class Mutations(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    update_blog = UpdateBlog.Field()