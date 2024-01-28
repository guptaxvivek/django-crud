from django.shortcuts import render, redirect
from .models import INFOList

# Create your views here.
def myview(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        INFOList.objects.create(name=name, email=email, phone=phone)

    obj = INFOList.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'templates/index.html', context=context)

def edit(request, pk):
    editOBJ = INFOList.objects.get(email=pk)
    if request.POST:
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        editOBJ.name = name
        editOBJ.phone = phone
        editOBJ.save()

    objs = INFOList.objects.all()
    context = {
        'obj': objs,
        'editOBJ':editOBJ,
    }
    return render(request, 'templates/index.html', context=context)

def delete(request, pk):
    obj = INFOList.objects.get(email=pk)
    obj.delete()
    return redirect(request.META.get('HTTP_REFERER'))