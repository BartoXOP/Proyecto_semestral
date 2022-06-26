from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Perrito, Raza
from .forms import PerritoForm
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.

