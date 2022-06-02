from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def leads(request):
    leads = Lead.objects.all()
    form = Leadsform()
    if request.method == 'POST':
        form = Leadsform(request.POST)
        if form.is_valid():
            form.save()
    form = Leadsform()
    return render(request, 'leads.html', {'leads': leads, 'form': form, })


def update_lead(request, pk):
    service = request.GET.get('service')
    employees = request.GET.get('employees')
    sales_funnel = request.GET.get('sales_funnel')
    address = request.GET.get('address')
    lead = Lead.objects.filter(pk=pk).update(
        service=service,
        employees=employees,
        sales_funnel=sales_funnel,
        address=address
    )
    return redirect('crm:sales_funnel')


def delete_lead(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return render(request, 'leads.html', {'lead': lead})

def delete_project(request, pk):
    lead = Project.objects.get(pk=pk)
    lead.delete()
    return render(request, 'project.html', {'lead': lead})


def sales_funnel(request):
    leads = Lead.objects.all()
    wait = leads.filter(sales_funnel='Ожидание')
    call = leads.filter(sales_funnel='звонок')
    meeting = leads.filter(sales_funnel='встреча')
    treaty = leads.filter(sales_funnel='договор')
    completed = leads.filter(sales_funnel='завершон')
    archive = leads.filter(sales_funnel='Архив')
    form = UpdateLead(request.GET or None)
    return render(request, 'sales_funnel.html', {'lead': leads,
                                                 'wait': wait,
                                                 'call': call,
                                                 'meeting': meeting,
                                                 'treaty': treaty,
                                                 'completed': completed,
                                                 'archive': archive,
                                                 'form': form
                                                 })


def projects(request):
    STATUSES = {
        'arch': ['план стен эскиз', 'Генплан', 'план стен', 'план кровля', 'план обороду', 'Разрез', 'рабоччи фасад',
                 'фасад детал узел', 'пол', 'столярка', 'внутренни отделка', 'наружная отделка', '3D обём', '3D рендр',
                 '3D фотошоп', 'смета учун обём', 'сотув плани', 'архсовет (тулови)', ],

        'design': ['Дизайн интерьера', 'Дизайн Экстерьера', 'Развертка стен', ],

        'const': ['расчот', 'котлован', 'подушка', 'фундамент', 'колонна выпуск', 'перемичка', 'лестница',
                  'лифт', 'колонна', 'ригель', 'развертка стен, кладка стен', 'кровля', 'парапет', 'крилцо',
                  'диафрагма, связ', 'обш.данные', 'обём', ],
    }

    employess = Employess.objects.get(user=request.user)
    projects = Project.objects.filter(department__employess=employess)
    form = Projectform(request.POST or None, request.FILES or None)
    if form.is_valid() and request.method == 'POST':
        lead = Lead.objects.get(pk=form['name_lead'].value())
        dep = Department.objects.get(pk=form['department'].value())
        project = Project.objects.create(
            name=form['name'].value(),
            name_lead=lead,
            address=form['address'].value(),
            numbers=form['numbers'].value(),
            department=dep,
            data_end=form['data_end'].value(),
            status_pay=form['status_pay'].value(), )
        print(dep.slug)
        status_group = StatusGroup.objects.create(
            result_status=0, project=project)
        default_statuses = STATUSES[dep.slug]

        for stat in default_statuses:
            Status.objects.create(title=stat, status=0, status_group=status_group)
        # form.save()
    form = Projectform()
    return render(request, 'project.html', {
        'projects': projects,
        'form': form,
    })


def change_status(request, pk):
    st = int(request.GET.get('status'))
    if st >= 0:
        status = Status.objects.get(pk=pk)
        status.status = st
        status.save()
        return redirect('crm:project')
