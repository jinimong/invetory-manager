import graphene

from django.db import transaction

from graphene_django.types import DjangoObjectType

from .models import ProductMaterial, ProductCategory, Product, ProductImage


class ProductMaterialType(DjangoObjectType):
    class Meta:
        model = ProductMaterial


class ProductCategoryType(DjangoObjectType):
    class Meta:
        model = ProductCategory


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class ProductImageType(DjangoObjectType):
    class Meta:
        model = ProductImage


class Query(graphene.ObjectType):
    all_materials = graphene.List(ProductMaterialType)
    all_categories = graphene.List(ProductCategoryType)
    all_products = graphene.List(ProductType)

    def resolve_all_materials(self, info, **kwargs):
        return ProductMaterial.objects.all()

    def resolve_all_categories(self, info, **kwargs):
        return ProductCategory.objects.all()

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()


class CreateProductMaterial(graphene.Mutation):
    material = graphene.Field(ProductMaterialType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, **kwargs):
        material = ProductMaterial(**kwargs)
        material.save()
        return CreateProductMaterial(material=material)


class CreateProductCategory(graphene.Mutation):
    category = graphene.Field(ProductCategoryType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, **kwargs):
        category = ProductCategory(**kwargs)
        category.save()
        return CreateProductCategory(category=category)


class ProductInput(graphene.InputObjectType):
    name = graphene.String()
    barcode = graphene.String(required=False)
    description = graphene.String(required=False)
    materials = graphene.List(graphene.Int, required=False)
    categories = graphene.List(graphene.Int, required=False)
    price = graphene.Int()
    price_with_pees = graphene.Int()


class CreateProduct(graphene.Mutation):
    product = graphene.Field(ProductType)

    class Arguments:
        product_input = ProductInput()

    @transaction.atomic
    def mutate(self, info, product_input):
        m2m_fields = {
            field.name: product_input.pop(field.name)
            for field in Product._meta.many_to_many
            if field.name in product_input
        }
        product = Product(**product_input)
        product.save()

        for field, value in m2m_fields.items():
            getattr(product, field).add(*value)

        return CreateProduct(product=product)


class Mutation(graphene.ObjectType):
    create_material = CreateProductMaterial.Field()
    create_category = CreateProductCategory.Field()
    create_product = CreateProduct.Field()
