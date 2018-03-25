
from django.shortcuts import render, redirect

from contactlist.models import Person, Address


def add_person(request):
    if request.method == 'GET':
        return render(request, 'add_person.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        description = request.POST.get('description')
        new_person = Person.objects.create(first_name=first_name, last_name=last_name, description=description)
        return render(request, 'add_person.html', {'new_person': new_person, 'success': True})


def modify_person(request, id):
    modified_person = Person.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'modify_person.html', {'modified_person': modified_person})
    else:
        modified_person.first_name = request.POST.get('first_name')
        modified_person.last_name = request.POST.get('last_name')
        modified_person.description = request.POST.get('description')
        modified_person.save()
        return render(request, 'modify_person.html', {'modified_person': modified_person})


def delete_person(request, id):
    to_delete_person = Person.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'delete_person.html', {'to_delete_person': to_delete_person})
    else:
        to_delete_person.delete()
        return redirect('/show/')


def show_person(request, id):
    to_show = Person.objects.get(id=id)
    return render(request, 'show_person.html', {'to_show': to_show})


def show_all(request):
    people = Person.objects.all()
    return render(request, 'show_all.html', {'people': people})


def add_address(reqeust, id):
    modified_person = Person.objects.get(id=id)
    if reqeust.method == 'GET':
        return render(reqeust, 'add_address.html', {'modified_person': modified_person})
    else:
        city = reqeust.POST.get('city')
        street = reqeust.POST.get('street')
        house_number = reqeust.POST.get('house_number')
        apartment_number = reqeust.POST.get('apartment_number')
        new_address = Address.objects.create(city=city, street=street, house_number=house_number,
                                             apartment_number=apartment_number, person_id=id)
        new_address.
        return render(reqeust, 'add_address.html', {'new_address': new_address, 'modified_person': modified_person,
                                                    'success': True})

def add_email(reqeust, id):
    modified_person = Person.objects.get(id=id)
    if reqeust.method == 'GET':
        return render(reqeust, 'add_address.html', {'modified_person': modified_person})
    else:
        city = reqeust.POST.get('city')
        new_email = Address.objects.create(city=city, street=street, house_number=house_number,
                                             apartment_number=apartment_number, person_id=id)
        return render(reqeust, 'add_address.html',
                      {'new_address': new_address, 'modified_person': modified_person, 'success': True})
