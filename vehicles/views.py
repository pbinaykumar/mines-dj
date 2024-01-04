from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import VehicleStatus, Vehicle
from .serializers import VehicleStatusSerializer, VehicleSerializer

# Create your views here.

@api_view(['GET'])
def vehicle_status(request):
    talcher_q = VehicleStatus.objects.filter(status = '1')
    jharkhand_q = VehicleStatus.objects.filter(status = '2')
    parked_q = VehicleStatus.objects.filter(status = '3')
    weight_q = VehicleStatus.objects.filter(status = '4')
    dumped_q = VehicleStatus.objects.filter(status = '5')
    talcher_data = VehicleStatusSerializer(talcher_q, many=True).data
    jharkhand_data = VehicleStatusSerializer(jharkhand_q, many=True).data
    parked_data = VehicleStatusSerializer(parked_q, many=True).data
    weight_data = VehicleStatusSerializer(weight_q, many=True).data
    dumped_data = VehicleStatusSerializer(dumped_q, many=True).data

    response = {
        'talcher_data':talcher_data,
        'jharkhand_data':jharkhand_data,
        'parked_data':parked_data,
        'weight_data':weight_data,
        'dumped_data':dumped_data,
    }
    return JsonResponse(response, status=200)

@api_view(['GET'])
def vehicle_list(request):
    q = Vehicle.objects.all()
    data = VehicleSerializer(q, many=True).data
    response = {
        'data':data
    }
    return JsonResponse(response, status=200)

@api_view(['GET'])
def vehicle_history(request):
    vehicle_tag_id = request.GET.get('vehicle_tag_id')
    vehicle = Vehicle.objects.get(vehicle_tag_id = vehicle_tag_id)
    q = VehicleStatus.objects.filter(vehicle = vehicle)
    data = VehicleStatusSerializer(q, many=True).data
    response = {
        'data':data
    }
    return JsonResponse(response, status=200)