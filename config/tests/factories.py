import factory

from config.product.models import Brand, Category, Product, ProductImage, ProductLine


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "Category_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "Brand-%d" % n)


# the product is a little different because is uses foreign keys and
# we have to declare them
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "test_product"
    description = "test_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
    is_active = True


class ProductLineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductLine

    price = 10.00
    sku = "1234"
    stock_qty = 1
    product = factory.SubFactory(ProductFactory)
    is_active = True


class ProductImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductImage

    alternative_text = "test alternative"
    url = "test.jpg"
    productline = factory.SubFactory(ProductLine)
    order = 1
