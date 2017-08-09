from datetime import datetime
from django.shortcuts import render,redirect,get_object_or_404
from django.db import transaction

from .models import Equipment
from .forms import EquipmentForm
from .models import Client,Leasing,LeasingEquipments
from .forms import ClientForm
from .models import Site3, Tipo, Tipo_publicaciones, Provincia_biotica, Provincia, Rasgos, Ad_cultural, Periodo, Publicaciones, Localidad

# Create your views here.
def index(request):
    return render(request,'equipment_rental/index.html')

def list_equipments(request):
    equipments = Equipment.objects.all()
    return render(request,'equipment_rental/equipments/list.html',{'equipments': equipments} )

def edit_equipment(request,equipment_pk=None):
    equipment = get_object_or_404(Equipment,pk=equipment_pk) if equipment_pk else None
    if request.method =='POST':
        if 'submit' in request.POST:
            form = EquipmentForm(request.POST,instance=equipment)
            if form.is_valid():
                equipment = form.save(commit=False)
                equipment.stock_available = equipment.stock - Leasing.objects.filter(equipments=equipment).count()
                equipment.save()
                return redirect('equipment_rental:list_equipments')
    else:
         form= EquipmentForm(instance=equipment)

    return render(request,'equipment_rental/equipments/edit.html',{'form': form})

def delete_equipment(request,equipment_pk=None):
    equipment = get_object_or_404(Equipment,pk=equipment_pk) if equipment_pk else None
    equipment.delete()

    equipments = Equipment.objects.all()
    return render(request, 'equipment_rental/equipments/list.html', {'equipments': equipments})

def list_clients(request):
    clients = Client.objects.all()
    return render(request,'equipment_rental/Clients/list.html',{'clients': clients} )

def edit_client(request,client_pk=None):
    client = get_object_or_404(Client,pk=client_pk) if client_pk else None
    if request.method =='POST':
        if 'submit' in request.POST:
            if client_pk:
               # client = get_object_or_404(Client, pk=client_pk)
                form = ClientForm(request.POST,instance=client)
            else:
                form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('equipment_rental:list_clients')
    else:
         form= ClientForm(instance=client)

    return render(request,'equipment_rental/Clients/edit.html',{'form': form})

def delete_client(request,client_pk=None):
    client = get_object_or_404(Client, pk=client_pk) if client_pk else None
    client.delete()

    clients = Client.objects.all()
    return render(request, 'equipment_rental/Clients/list.html', {'clients': clients})

def new_leasing(request):
    if request.method == 'POST':
        try:
            client = Client.objects.get(pk=request.POST['client'])
            return_date =  request.POST['return_date']

            equipments = [{'e': Equipment.objects.get(pk=e),'n':n} for e,n in zip(request.POST.getlist('equipment[]'), request.POST.getlist('quantity[]'))
                         ]
        except KeyError:
            pass
        else:
            with transaction.atomic():
                l = Leasing(client=client,total_price=0,return_date=return_date, lease_record=datetime.now())
                l.save()
                cost = 0
                ##q=0
                for eq in equipments:
                    le = LeasingEquipments(leasing=l,equipment=eq['e'],quantity=eq['n'])
                    le.save()
                    ##le.equipment.stock_available -= int(eq['n'])
                    le.equipment.stock_available = le.equipment.stock_available - int(le.quantity)
                    ##cost += eq['e'].daily_lease_price * int (eq['n'])
                    cost += le.equipment.daily_lease_price * int(le.quantity)

                l.total_price = cost
                l.save()
        return redirect('equipment_rental:index')
    else:
        clients = Client.objects.all()
        equipment = Equipment.objects.filter(stock_available__gt=0)

    return render(request,"equipment_rental/leasings/new.html",{'clients': clients,'equipments': equipment})

def view_leasing(request):
    leasing = Leasing.objects.all()
    return render(request,'equipment_rental/leasings/view_leasing.html',{'leasings': leasing} )

def delete_leasing(request,leasing_pk=None):
    leasing = get_object_or_404(Leasing, pk=leasing_pk) if leasing_pk else None
    leasing.delete()

    leasing = Leasing.objects.all()
    return render(request,'equipment_rental/leasings/view_leasing.html',{'leasings': leasing} )

def map(request):
    site = Site3.objects.all()
    tipo = Tipo.objects.all()
    provincia = Provincia.objects.all()
    prov_bio = Provincia_biotica.objects.all()
    tipo_pub = Tipo_publicaciones.objects.all()
    rasgo_cul = Rasgos.objects.all()
    ad_cultural = Ad_cultural.objects.all()
    periodo = Periodo.objects.all()
    pub = Publicaciones.objects.all()
    localidad = Localidad.objects.all()
    if request.method =='GET':
        f_prov = request.GET.get('check_prov')
        f_provbio = request.GET.get('check_provbio')
    else:
        f_prov = "";
        f_provbio = "";
    return render(request, 'sites/mapping/map.html', {'fs_prov':f_prov,'fs_provbio':f_provbio,'pubs':pub,'locs':localidad,'sites':site,'tipos':tipo,'provincias':provincia,'provs_bio':prov_bio,'tipos_pub':tipo_pub,'rasgos':rasgo_cul,'ads_cultural':ad_cultural,'periodos':periodo})