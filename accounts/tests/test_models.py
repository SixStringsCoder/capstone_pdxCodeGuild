import pytest
from mixer.backend.django import mixer
from accounts.models import profile_upload_handler
pytestmark = pytest.mark.django_db



# class TestUser:
#     def test_profile_upload_handler(self):
#         user = mixer.blend('accounts.User')
#         result = profile_upload_handler(instance=image, filename='stamp_image.jpg')
#         assert isinstance(result, str) is True, 'must return a string'
#         assert result == "stamps/owner.jpg", 'incorrect path generated by handler.'


