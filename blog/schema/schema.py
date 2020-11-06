import graphene
from blog.schema.blog_schema import Blog, BlogModel
from blog.schema.profile.profile_schema import Profile
from blog.model.blog_managment_model import BlogManagment


class Query(graphene.ObjectType):

    blogs = graphene.List(
        Blog,
        size=graphene.Int(required=True),
        page=graphene.Int(required=True)
    )
    blog = graphene.Field(
        Blog,
        id=graphene.Int(required=True)
    )

    profiles = graphene.List(Profile)


    def resolve_blogs(self, info, size, page):

        blogs =  BlogModel.objects.filter(id__gt=4)
        skip = size * (page-1)
        blogs = blogs[skip:]
        blogs = blogs[:size]

        print(BlogModel.objects.filter(id__gt=4).count())


        # temp_array = [9,8,7,6,5,4,3,2,1]
        # temp_array = temp_array[3:]
        # temp_array = temp_array[:2]

        # print(temp_array)
        return blogs

    def resolve_blog(self, info, id):
        return BlogModel.objects.get(pk=id)

    def resolve_profiles(self, info):
        return BlogManagment.get_list_of_profiles()
