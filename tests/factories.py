import factory
from django.db.models.signals import post_save
from faker import Faker
from real_estate.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile

faker = Faker()

@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AUTH_USER_MODEL

    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())
    username = factory.LazyAttribute(lambda x: faker.unique.user_name())
    # email = factory.LazyAttribute(lambda x: faker.unique.email())
    email = factory.LazyAttribute(lambda x: f"nicolas@realestate.com")
    password = factory.PostGenerationMethodCall('set_password', 'password123')
    is_active = True
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)

@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    phone_number = factory.LazyAttribute(lambda x: faker.phone_number())
    about_me = factory.LazyAttribute(lambda x: faker.paragraph(nb_sentences=3))
    license = factory.LazyAttribute(lambda x: faker.unique.random_number(digits=6))
    profile_photo = factory.LazyAttribute(lambda x: f"{faker.word()}.{faker.file_extension(category='image')}")
    gender = factory.LazyAttribute(lambda x: faker.random_element(elements=('Male', 'Female', 'Other')))
    country = factory.LazyAttribute(lambda x: faker.country())
    city = factory.LazyAttribute(lambda x: faker.city())
    is_buyer = factory.Faker('boolean', chance_of_getting_true=50)
    is_seller = factory.Faker('boolean', chance_of_getting_true=50)
    is_agent = factory.Faker('boolean', chance_of_getting_true=20)
    rating = factory.LazyAttribute(lambda x: faker.pyfloat(left_digits=1, right_digits=1, positive=True, min_value=1, max_value=5))
    num_reviews = factory.LazyAttribute(lambda x: faker.random_int(min=0, max=100))