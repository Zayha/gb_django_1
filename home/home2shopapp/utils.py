from django.utils import timezone


def upload_to(instance, filename):
    now = timezone.now()
    year = now.year
    month = now.month
    day = now.day
    return f'product_photos/{year}/{month}/{day}/{filename}'
