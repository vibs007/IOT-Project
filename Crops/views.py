from django.shortcuts import render, HttpResponse
from django.contrib import messages
from datetime import timedelta, datetime
import joblib
from .models import Wheat
# After every 7 days the readings are updated
def periodic_update(request):
    if request.method == 'POST':
        Uid_value = request.POST.get('Uid')
        Section_value = request.POST.get('Section')
        Temp_value = request.POST.get('Temp')
        Pressure_value = request.POST.get('Pressure')
        CO2_value = request.POST.get('CO2')
        Weight_value = request.POST.get('Weight')

        Items = Wheat.objects.filter(uid=Uid_value,section_id=Section_value)

        if Items.exists():
            for item in Items:
                item.Temp = Temp_value
                item.CO2 = CO2_value
                item.Pressure = Pressure_value
                item.Weight = Weight_value
                your_object.save()
    return HttpResponse("Stock updated")

def add_stock(request):
    if request.method == 'POST':
        # Section_value = request.POST.get('Section')
        Uid_value = request.POST.get('Uid')
        # Food_Type = request.POST.get('Food_Type')
        Temp_value = request.POST.get('Temp')
        Humidity_value = request.POST.get('Humidity')
        Weight_value = request.POST.get('Weight')
        CO2_value = request.POST.get('CO2')
        O2_value = request.POST.get('O2')
        Ethylene_value = request.POST.get('Ethylene')
        Light_value = request.POST.get('Light_Value')
        # Date_of_harvest_value = request.POST.get('Date_of_harvest')
        # Date_of_harvest_value = datetime.strptime(Date_of_harvest_value, '%Y-%m-%d')
        # current_date = timezone.now().date()
        # Est_date_of_exp_value = timedelta(days=182) + Date_of_harvest_value

        new_record = Wheat.objects.create(
            Uid=Uid_value,
            # Section=Section_value,
            # Food_Type=Food_Type,
            Temp=Temp_value,
            Humidity=Humidity_value,
            Weight=Weight_value,
            CO2=CO2_value,
            O2=O2_value,
            Ethylene=Ethylene_value,
            Light_Value=Light_value,
            # Date_of_harvest=Date_of_harvest_value,
            # Est_date_of_exp=Est_date_of_exp_value
        )
    return HttpResponse("Stock added")
    
def alerts(request):
    custom_message = request.GET.get('custom_message', None)

    if custom_message:
        messages.warning(request, custom_message)
    return HttpResponse("Alert Recieved")

# def pred_price(uid_value):
#    model = joblib.load('price_pred.pkl')
#    unique_section_ids = Wheat.objects.filter(Uid=uid_value).values_list('Section',flat=True).distinct()
#    Pred_price_dict = {}
#    for section_id in unique_section_ids:
#         try:
#             item = Wheat.objects.get(Uid=uid_value, Section=section_id)
#         except Wheat.DoesNotExist:
#             item = None
#         predicted_price = model.predict(item.Date_of_harvest)
#         Pred_price_dict[section_id] = predicted_price
#    return Pred_price_dict

def home(request):
    registered_username = request.session.get('registered_username')
    # section_prices = pred_price(registered_username)
    Items = Wheat.objects.filter(Uid=registered_username)
    return render(request, 'home.html', {'registered_username': registered_username,'Items':Items})


