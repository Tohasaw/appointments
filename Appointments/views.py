from django.http import JsonResponse
from django.shortcuts import render
from datetime import date as dateType
from .forms import *
from .models import *
from datetime import datetime, timedelta

# Create your views here.
def apps_customer_new(request):
  appointments = WorkingTime.objects.all()
  length = 60
  form = AppsCustomerNewForm(request.GET)
  if form.is_valid():
    if form.cleaned_data['date']:
      appointments = appointments.filter(table__date=form.cleaned_data['date'])
    if form.cleaned_data['employee']:
      appointments = appointments.filter(employee_id=form.cleaned_data['employee'])
    if form.cleaned_data['service']:
      length = PriceListPosition.objects.filter(id=form.cleaned_data['service']).service.length

  context={
    'form':form,
    'apps': appointments,
    'length': length
  }
  return render(request, 'apps/apps_customer_new.html', context)

def apps_customer_getdate(request):
  employee_id = request.GET.get('employee_id')
  currentDate = dateType.today()

  workingTime = WorkingTime.objects.filter(employee=employee_id, table__date__gte=currentDate)
  date_list = [str(working_time.table.date) for working_time in workingTime]

  data = {
      'available_days': date_list,
  }

  return JsonResponse(data)

def apps_customer_gettime(request):
  service_id = request.GET.get('service_id')
  employee_id = request.GET.get('employee_id')
  selected_date = request.GET.get('selected_date')

  service = Service.objects.get(id=service_id)
  workingTime = WorkingTime.objects.get(employee=employee_id, table__date=selected_date)
  apps = Appointment.objects.filter(workingTime_id=workingTime.id)
  startTime = workingTime.startTime
  endTime = workingTime.endTime

  data = {}
  interval = timedelta(minutes=30)
  currentTime = startTime
  timeSlots = [currentTime]

  while currentTime < endTime:
    currentTime = (datetime.combine(datetime.today(), currentTime) + interval).time()
    timeSlots.append(currentTime)

  for app in apps:
    timeSlots = [t for t in timeSlots if not (app.startTime <= t < app.endTime)]
    if timeSlots[len(timeSlots) - 1] == app.endTime :
      timeSlots.remove(timeSlots[len(timeSlots) - 1])

  #for slot in timeSlots:
  #  timeSlots = [t for t in timeSlots if not (app.startTime <= t < app.endTime)]
  #  if timeSlots[len(timeSlots) - 1] == app.endTime :
  #    timeSlots.remove(timeSlots[len(timeSlots) - 1])

  data = {
    'available_time_slots': timeSlots,
  }

  return JsonResponse(data)

# EMPLOYEE VIEWS

def apps_employee_list(request):
  user_id = request.user.id
  appointments = Appointment.objects.filter(workingTime__employee_id=user_id)

  context={
    'apps': appointments,
  }

  return render(request, 'apps/apps_employee_list.html', context)
