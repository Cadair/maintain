import json

from django.http import JsonResponse

from .views import get_default_car


def mileage_logs(request):
    """JS: Return mileage log data used for plotting"""
    if request.method == "GET":
        cars = request.GET["car"]
        if len(cars) == 1:
            cars = car[0]

        # Determine whether default car or all cars
        if cars == "all":
            cars = request.user.cars.all()
        elif cars == "default":
            cars = [get_default_car(request)]

        # Plot total mileage
        data = []
        for car in cars:
            logs = car.get_logs
            obj = {
                "label": f"{car.make} {car.model}",
                "data": [{"x": str(log.timestamp), "y": log.mileage} for log in logs],
            }
            data.append(obj)
        return JsonResponse(json.dumps(data), safe=False)
    else:
        return JsonResponse({"error": "GET request required."}, status=400)
