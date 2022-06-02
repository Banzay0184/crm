from django.db import models
from users.models import *


class Employess(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sur_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    position = models.CharField(max_length=255)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.sur_name


class Department(models.Model):
    name = models.CharField(max_length=255)
    employess = models.ManyToManyField(Employess, related_name='eployess')
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_group_status(self):
        return StatusGroup.objects.get(departament=self)


class StatusGroup(models.Model):
    result_status = models.PositiveIntegerField(default=0)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='status_group')

    def __str__(self):
        return self.project.name

    def sum_status(self):
        a = Status.objects.filter(status_group=self)
        b = []
        for item in a:
            z = item.status
            b.append(z)
        result = sum(b) / len(b)
        return int(result)


class Status(models.Model):
    title = models.CharField(max_length=255)
    status = models.PositiveIntegerField(default=0)
    status_group = models.ForeignKey(StatusGroup, related_name='status', on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '/' + str(self.status) + '%'


class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Lead(models.Model):
    SEARCH_TRAFFIC = {
        ('INSTAGRAM', 'Instagram'),
        ('TELEGRAM', 'Telegram'),
        ('SARAFAN', 'sarafan'),
    }

    SALES_FUNNEL = {
        ('Ожидание', 'Ожидание'),
        ('звонок', 'звонок'),
        ('встреча', 'встреча'),
        ('договор', 'договор'),
        ('завершон', 'завершон'),
        ('Архив', 'Архив'),
    }
    sur_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255)
    numbers = models.CharField(max_length=10)
    service = models.ForeignKey(Service, related_name='service', on_delete=models.CASCADE, default='')
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    employees = models.ForeignKey(Employess, on_delete=models.CASCADE, default='')
    search_traffic = models.CharField(max_length=255, choices=SEARCH_TRAFFIC, default='ISTAGRAM')
    sales_funnel = models.CharField(max_length=255, choices=SALES_FUNNEL, default='Ожидание')
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.sur_name


class Project(models.Model):
    STATUS_PAY = {
        ('Оплачено', 'Оплачено'),
        ('Аванс', 'Аванс'),
        ('Ожидание', 'Ожидание'),
    }

    name = models.CharField(max_length=255)
    name_lead = models.ForeignKey(Lead, related_name='name_lead', on_delete=models.CASCADE, default='',null=True, blank=True)
    address = models.CharField(max_length=255, )
    numbers = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default='')
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    data_end = models.DateField(db_index=True)
    status_pay = models.CharField(max_length=255, choices=STATUS_PAY, default='Ожидание')

    def get_group_status(self):
        return StatusGroup.objects.get(project=self)

    def __str__(self):
        return self.name
