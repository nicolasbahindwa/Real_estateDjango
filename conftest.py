import pytest
from pytest_factoryboy import register
from tests.factories import ProfileFactory, UserFactory

register(ProfileFactory)
register(UserFactory)

@pytest.fixture
def base_user(db, use_factory):
    new_user = use_factory.create()
    return new_user

@pytest.fixture
def super_user(db, use_factory):
    new_user = use_factory.create(is_superuser=True, is_staff=True)
    return new_user

@pytest.fixture
def profile(db, profile_factory):
    user_profile = profile_factory.create()
    return user_profile