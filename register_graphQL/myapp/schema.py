import graphene
from graphene_django import DjangoObjectType
from graphene import Schema, ObjectType, Field, String, List, Int,InputObjectType
# from graphene import *
# from graphene_django import *
from myapp.models import *


class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant

class RestaurantInput(graphene.InputObjectType): #error like "AttributeError: 'Options' object has no attribute 'name'.""
    phone = graphene.String(required=True)
    name = graphene.String(required=True)
class CreateRestaurant(graphene.Mutation):
    ####input
    class Arguments: 
        # restaurant_data = RestaurantInput(required=True)
        name = graphene.String()
        phone = graphene.String()

    ##output
    id = graphene.Int()
    name = graphene.String()
    phone = graphene.String()
    # restaurant = graphene.Field(Restaurant)

    # def mutate(self,info,restaurant_data=None):
        # restaurant = Restaurant(name=restaurant_data.name, phone=restaurant_data.phone)
    def mutate(self,info,name,phone):
        restaurant = Restaurant(name = name, phone=phone)
        restaurant.save()
        # return CreateRestaurant(Restaurant=restaurant)
        return CreateRestaurant(
                id=restaurant.id,
                name=restaurant.name,
                phone=restaurant.phone,
            )


class UserType(DjangoObjectType): #ObjectType = building block used to define the relationship between Fields in your Schema
    class Meta:
        model = UserModel
         
class AddressType(DjangoObjectType):
    class Meta:
        model = AddressModel
class CatType(DjangoObjectType):
    class Meta:
        model = Cat
class CreateAddress(graphene.Mutation):
    city = graphene.String()
    zipcode = graphene.String()

    class Arguments:
        city = graphene.String()
        zipcode  = graphene.String()
    
    def mutate(self,info, city, zipcode):
        address = AddressModel(city=city,  zipcode=zipcode)
        address.save()

        return CreateAddress(
            id=address.id,
            city=address.city,
            zipcode=address.zipcode,
        )

class CreateUser(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    last_name = graphene.String()

    class Arguments:
        name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, name, last_name):
        user = UserModel(name=name, last_name=last_name)
        user.save()

        return CreateUser(
            id=user.id,
            name=user.name,
            last_name=user.last_name,
        )

# class CreateCat(graphene.Mutation):
#     class Meta:
#         model = Cat
#         foreign_key_extras = {"owner": {"type": "CreateUserInput"}}


class Query(graphene.ObjectType):
    users = List(UserType) #use List to get all users
    user =  Field(UserType, id=Int()) #use Field to get specific user

    cats = List(CatType)
    cat = Field(CatType, id=Int())

    res = List(RestaurantType)

    def resolve_users(parent, info): #we need resolve method to get field
        return UserModel.objects.all()
    def resolve_user(parent,info,id): # not to be (self, info,id) !!!! and id is need to be passed
        if id is not None:
            return UserModel.objects.get(id=id)
        return None
    def resolve_cats(parent, info): #we need resolve method to get field
        return Cat.objects.all()
    def resolve_user(parent,info,id): # not to be (self, info,id) !!!! and id is need to be passed
        if id is not None:
            return Cat.objects.get(id=id)
        return None

    def resolve_res(parent, info): #we need resolve method to get field
            return Restaurant.objects.all()
    
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_res = CreateRestaurant.Field()



schema = graphene.Schema(
    query = Query,
    mutation = Mutation
    )
