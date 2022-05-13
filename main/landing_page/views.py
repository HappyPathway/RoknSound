from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.base import View
from django.http import JsonResponse
import json
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from uuid import uuid4
from django.http import Http404
from django.db import transaction
from django.views.decorators.cache import never_cache

from rentals.models import Equipment, EquipmentMedia, EquipmentType


class LandingPage(View):

    def get(self, request):
        my_response = render(request, "landing_page.html", )
        my_response['Cache-Control'] = "no-cache"
        my_response['Pragma'] = "no-cache"
        my_response['Expires'] = 0
        return my_response