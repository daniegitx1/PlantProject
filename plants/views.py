from django.shortcuts import render
from .models import PlantsData


def view_names_edit(request):
    if request.method == 'POST':
        # Handle form submission
        plant_id = request.POST.get('plant_id')
        new_name = request.POST.get('new_name')

        try:
            plant = PlantsData.objects.get(id=plant_id)
            plant.name = new_name
            plant.save()
        except PlantsData.DoesNotExist:
            # Handle case where plant ID doesn't exist
            pass

    # Retrieve all plant data
    plants_data = PlantsData.objects.all()

    return render(request, 'plants/index.html', {'plants_data': plants_data})
