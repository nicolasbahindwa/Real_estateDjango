import pytest

def test_user_str(base_user):
    """ Test the custom user model string representation"""
    assert base_user.__str__() == f"{base_user.username}"

def test_user_short_name(base_user):
    """ Test the custom user model short name property"""
    short_name = f"{base_user.username}"
    assert base_user.get_short_name == short_name

def test_user_full_name(base_user):
    """ Test the custom user model full name property"""
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name == full_name

def test_base_user_email_is_normalized(base_user):
    """ Test the custom user model email normalization"""
    email = "nicola@REALESTATE.COM"
    assert base_user.email == email.lower()

def test_super_user_email_is_normalized(super_user):
    """ Test the custom superuser model email normalization"""
    email = "alpha@REALESTATE.COM"
    assert super_user.email == email.lower()

def super_user_is_not_staff(user_factory):
    """ Test that an error is raised when an admin is not a staff."""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert  str(err.value) == "Superuser must have is_staff=True."

def test_super_user_is_not_superuser(use_factory):
    """ Test that an error is raised when an admin is not a superuser."""
    with pytest.raises(ValueError) as err:
        use_factory.create(is_superuser=False, is_staff=True)
    assert  str(err.value) == "Superuser must have is_superuser=True."

def test_create_user_with_no_email(user_factory):
    """ Test that an error is raised when a user is created without an email."""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User account: An email address is required"

def test_create_use_with_no_username(use_factory):
    """ Test that an error is raised when a user is created without a username."""
    with pytest.raises(ValueError) as err:
        use_factory.create(username=None)
    assert str(err.value) == "User must submit a username"

def test_create_user_with_no_first_name(user_factory):
    """ Test that an error is raised when a user is created without a first name."""
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "User must submit a first name"

def test_create_user_with_no_last_name(user_factory):
    """ Test that an error is raised when a user is created without a last name."""
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "User must submit a last name"


def test_create_superuser_with_no_email(super_user_factory):
    """ Test that an error is raised when a superuser is created without an email."""
    with pytest.raises(ValueError) as err:
        super_user_factory.create(email=None)
    assert str(err.value) == "Superuser account: An email address is required"


def test_user_email_incorrect(user_factory):
    """Test that an Error is raised when a non valid email is provided"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email="realestate.com")
    assert str(err.value) == "You must provide a valid email address"

def test_create_superuser_with_no_password(user_factory):
    """Test creating a superuser without a password raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=True, password=None)
    assert str(err.value) == "Superuser must submit a password."