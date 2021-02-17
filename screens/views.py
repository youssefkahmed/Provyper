from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.core.mail import send_mail
import requests
from screens.models import Appointment
from screens.models import Company
from json import dumps


def home(request):
    return HttpResponse(render(request, "screens/home.html"))


def request_appointment(request):
    country_codes = requests.get('https://restcountries.eu/rest/v2/all').json()
    companies = dumps([comp.as_dict(comp.name, comp.countries)
                       for comp in Company.objects.all()])
    return render(request, "screens/request.html", {'country_codes': country_codes, 'companies': companies})


def confirmation(request):

    # Saving The Appointment
    first_name = request.POST["firstName"]
    last_name = request.POST["lastName"]
    email = request.POST["email"]
    phone_number = int(
        request.POST["countryCode"] + request.POST["phoneNumber"])
    countries = request.POST.getlist("opCountries")
    company_name = request.POST["companyName"]
    objectives = request.POST.getlist("objectives")
    description = request.POST["description"]

    appointment = Appointment(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        company=company_name,
        description=description
    )

    appointment.set_countries(countries)
    appointment.set_objectives(objectives)

    appointment.save()

    # Saving The Newly-Added Company
    company = Company(name=company_name)
    company.set_countries(countries)

    company.save()

    send_mail('Provyper Appointment Confirmation', 'Thank you for choosing Provyper!\nYour request has been successfully sent, and someone from our team should be contacting you soon.',
              'youssefkahmed@gmail.com', [email], fail_silently=False)

    email_msg = 'A new appointment has been booked by a client. Appointment details:\nFirst Name: ' + first_name + \
        '\nLast Name: ' + last_name + '\nEmal: ' + email + \
        '\nPhone Number: ' + str(phone_number) + '\nOperation Countries: '
    for country in countries:
        email_msg += country + ' '
    email_msg += '\nCompany: ' + company_name + '\nObjectives: '
    for objective in objectives:
        email_msg += objective + ' '
    email_msg += '\nExtra Details: ' + description

    send_mail('New Appointment Request', email_msg,
              'youssefkahmed@gmail.com', ['youssefkahmed@gmail.com'], fail_silently=False)

    return HttpResponse(render(request, "screens/confirmation.html"))
