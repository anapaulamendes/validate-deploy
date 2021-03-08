import factory
from faker import Faker

from core.models import Release

fake = Faker()


class ReleaseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Release
        django_get_or_create = ("ReleaseId",)

    ReleaseName = fake.text(max_nb_chars=255)
    ReleaseId = fake.pyint()
    TeamProject = fake.text(max_nb_chars=255)
