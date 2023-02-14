from django.shortcuts import render
from django.http import JsonResponse
from forex_python.converter import CurrencyRates

def convert_currency(request, amount, source_currency, target_currency):
    cr = CurrencyRates()
    converted_amount = cr.convert(source_currency, target_currency, amount)
    return JsonResponse({'converted_amount': converted_amount})