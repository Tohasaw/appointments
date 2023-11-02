from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Job (models.Model):
  name = models.TextField()

  def __str__(self):
    return f"{self.name}"

  class Meta:
    verbose_name="Должность",
    verbose_name_plural="Должности"

class Employee (AbstractUser):
  job = models.ForeignKey(Job, on_delete=models.CASCADE,verbose_name="Должность")
  hiringDate =  models.DateField(verbose_name='Дата приема')
  dismissDate = models.DateField(verbose_name='Дата увольнения', null=True, blank=True)
  birthDate = models.DateField(verbose_name='Дата рождения', null=True, blank=True)

  class Meta:
    verbose_name="Сотрудник",
    verbose_name_plural="Сотрудники"

class Table (models.Model):
  date = models.DateField()

  def __str__(self):
    return f"{self.date}"

  class Meta:
    verbose_name="Дата",
    verbose_name_plural="Расписание"
    ordering = ['-date']

class WorkingTime (models.Model):
  startTime = models.TimeField(verbose_name="Начало рабочего времени")
  endTime = models.TimeField(verbose_name="Конец рабочего времени")
  table = models.ForeignKey(Table, on_delete=models.CASCADE,verbose_name="Дата")
  employee = models.ForeignKey(User, on_delete=models.CASCADE,related_name='workingtime_employee_set',verbose_name="Сотрудник")

  def __str__(self):
    return f"{self.table.date} {self.startTime.strftime('%H:%M')}-{self.endTime.strftime('%H:%M')} для {self.employee.first_name[0]}. {self.employee.last_name}"

  class Meta:
    verbose_name="Рабочие часы",
    verbose_name_plural="Рабочие часы"

class PriceList (models.Model):
  approvalDate = models.DateField()

  def __str__(self):
    return f"Прайс-лист от {self.approvalDate}"

  class Meta:
    verbose_name="Прайс-лист",
    verbose_name_plural="Прайс-листы"

class Service (models.Model):
  title = models.TextField(verbose_name="Наименование")
  description = models.TextField(verbose_name="Описание")
  length = models.IntegerField(verbose_name="Длительность")

  def __str__(self):
    return self.title

  class Meta:
    verbose_name="Услуга",
    verbose_name_plural="Услуги"

class PriceListPosition (models.Model):
  price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Цена")
  service = models.ForeignKey(Service, on_delete=models.CASCADE,verbose_name="Услуга")
  priceList = models.ForeignKey(PriceList, on_delete=models.CASCADE,verbose_name="Прайс-лист")

  def __str__(self):
    return f"{self.service.title} за {self.price}Р."

  class Meta:
    verbose_name="Позиция прайс-листа",
    verbose_name_plural="Позиции прайс-листа"

class Appointment (models.Model):
  startTime = models.TimeField(verbose_name="Врема начала приема")
  endTime = models.TimeField(verbose_name="Время окончания приема")
  workingTime = models.ForeignKey(WorkingTime, on_delete=models.CASCADE,verbose_name="Рабочие часы")
  priceListPosition = models.ForeignKey(PriceListPosition, on_delete=models.CASCADE,verbose_name="Позиция прайс-листа")
  client = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Клиент", null=True,blank=True)

  #def __str__(self):
  #  return f"{self.startTime}-{self.endTime} в {self.table.date} для {self.employee.first_name[0]}."

  class Meta:
    verbose_name="Запись на прием",
    verbose_name_plural="Записи на прием"

