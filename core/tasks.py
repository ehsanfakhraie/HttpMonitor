import requests
from django.conf import settings
from core.models import URLs, Requests


def check_urls():
    print('Checking URLs...')
    urls = URLs.objects.filter(deleted_at=None)
    for url in urls:
        try:
            response = requests.get(url.address)
            print(response.status_code)
            status_code = response.status_code
            if status_code >= 400:
                url.failed_times += 1
                url.save()
            else:
                request = Requests.objects.create(url=url, result=status_code)
        except requests.exceptions.RequestException as e:
            request = Requests.objects.create(url=url, result=False)
            url.failed_times += 1
            url.save()
