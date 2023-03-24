from django.http import HttpResponse
from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from .models import Company, Client


# TODO
# Направи с Кронджоб да проверява кой има РД (клиент или фирма) и да ми праща email

def check_for_birthday(request):
    datetime_now = timezone.now()
    now_day, now_month = datetime_now.day, datetime_now.month
    # TODO VRASHTA Queryset za tova ne dava res
    data = {'client_birth_day_today': [], 'client_birth_day_this_month': [],
            'company_birth_day_today': [], 'company_birth_day_this_month': []}

    data['client_birth_day_today'] = list(Client.objects.filter(birthday__day=now_day, birthday__month=now_month))
    data['client_birth_day_this_month'] = list(Client.objects.filter(birthday__month=now_month))

    data['company_birth_day_today'] = list(
        Company.objects.filter(created_date__day=now_day, created_date__month=now_month))
    data['company_birth_day_this_month'] = list(Company.objects.filter(created_date__month=now_month))

    return HttpResponse(data)


if __name__ == "__main__":
    print("Executed when invoked directly!!")
else:
    print("Executed when imported")
