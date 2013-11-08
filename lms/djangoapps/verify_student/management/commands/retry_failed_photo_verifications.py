"""
Django admin commands related to verify_student
"""

from verify_student.models import SoftwareSecurePhotoVerification
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    This method finds those PhotoVerifications with a status of
    MUST_RETRY and attempts to verify them.
    """
    help = 'Retries SoftwareSecurePhotoVerifications that are in a state of \'must_retry\''

    def handle(self, *args, **options):
        attempts_to_retry = SoftwareSecurePhotoVerification.objects.filter(status='must_retry')
        print("Attempting to retry {0} failed submissions".format(len(attempts_to_retry)))
        for index, attempt in enumerate(attempts_to_retry):
            print("Retrying submission #%s\n".format(index))
            attempt.submit()
        print("Done resubmitting failed photo verifications")
