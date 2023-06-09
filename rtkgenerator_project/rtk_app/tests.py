from django.test import TestCase
from django.db import models
from django import template

#register = template.Library()
#from django.template.defaultfilters import floatformat
#
#@register.filter
#def percent(value):
#  if value is None:
#    return None
#  return floatformat(value * 100.0, 2) + '%' 
#
#print(percent(50))

#500 + 5 = 525

print( 500 + 500 * 0.01 * 5)