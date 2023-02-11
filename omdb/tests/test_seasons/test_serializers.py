import pytest
from seasons.serializers import SeasonSerializer
from seasons.models import Season

from rest_framework.utils.serializer_helpers import ReturnList
from rest_framework.renderers import JSONRenderer


@pytest.mark.django_db
def test_post_serializer(dummy_db_instances):
    # given
    post_serializer = SeasonSerializer(Season.objects.all(), many=True)
    # when
    content = JSONRenderer().render(post_serializer.data)
    # then
    assert type(post_serializer.data) == ReturnList
    assert type(content) == bytes
