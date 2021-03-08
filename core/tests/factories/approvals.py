import factory
from faker import Faker

from core.models import Approvals
from core.tests.factories.release import ReleaseFactory

fake = Faker()


class ApprovalsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Approvals
        django_get_or_create = ("token",)

    token = fake.uuid4()
    approved = fake.pybool()
    email = fake.email()
    release = factory.SubFactory(ReleaseFactory)
