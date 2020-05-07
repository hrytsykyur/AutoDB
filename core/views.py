from django.shortcuts import render
from core.models import *
from django.http import HttpResponseRedirect

def get_one_post_value(x,request):
    if len(request.POST.getlist(x)) == 1:
        value = request.POST.getlist(x)[0]
        return value

def main(request):
    return render(request, 'main.html')

def request_handler(request,model,template):
    if request.method == 'POST':
        action = request.POST.getlist('action')[0]
        id_post = request.POST.getlist('id')
        amount = request.POST.getlist('amount')
        if action == 'to_ordered':
            if len(id_post) == 1 and len(amount) == 1 and id_post != [''] and amount != ['']:
                id_post = int(id_post[0])
                amount = int(amount[0])
                obj = model.objects.get(id=id_post)
                obj_amount = obj.amount_available
                if obj_amount > 0:
                    amount_to_set = obj_amount - amount
                    obj.amount_available = amount_to_set
                    obj.save()
                    try:
                        que = Ordered.objects.get(parent=id_post)
                        tri = True
                    except Ordered.DoesNotExist:
                        que = None
                        tri = False
                    if tri:
                        new_amount = que.amount + amount
                        que.amount = new_amount
                        que.save()
                    else:
                        Ordered.objects.create(parent=obj, amount = amount)
                return HttpResponseRedirect(request.path_info)
        elif action == 'search':
            detail_number_check = get_one_post_value('detail_number_check', request)
            description_number_check = get_one_post_value('description_number_check', request)
            detail_number = get_one_post_value('detail_number', request)
            description_number = get_one_post_value('description_number', request)
            if detail_number_check == 'on' and description_number_check == 'on':
                data = []
                info = model.objects.filter(detail_number=detail_number, description_number=description_number).values()
                for i in info:
                    i.pop('generalinfo_ptr_id', None)
                    id = i.get('id')
                    i.pop('id', None)
                    i.update({'id':str(id)})
                    data.append(i)
            elif detail_number_check == 'on':
                data = []
                info = model.objects.filter(detail_number=detail_number).values()
                for i in info:
                    i.pop('generalinfo_ptr_id', None)
                    id = i.get('id')
                    i.pop('id', None)
                    i.update({'id':str(id)})
                    data.append(i)
            elif description_number_check == 'on':
                data = []
                info = model.objects.filter(description_number=description_number).values()
                for i in info:
                    i.pop('generalinfo_ptr_id', None)
                    id = i.get('id')
                    i.pop('id', None)
                    i.update({'id':str(id)})
                    data.append(i)

            return render(request,template,{'data':data})


    try:
        que = model.objects.all()
        tri = True
    except model.DoesNotExist:
        que = None
        tri = False
    data = []
    if tri:
        for a in que:
            info = model.objects.filter(id=a.id).values()
            for i in info:
               i.pop('generalinfo_ptr_id', None)
               id = i.get('id')
               i.pop('id', None)
               i.update({'id':str(id)})
               data.append(i)
    return render(request,template,{'data':data})


def ordered(request):
    if request.method == 'POST': 
        id_post = request.POST.getlist('id')
        amount = request.POST.getlist('amount')
        if len(id_post) == 1 and len(amount) == 1 and id_post != "" and amount != "":
            id_post = int(id_post[0])
            amount = int(amount[0])
        ordered_obj = Ordered.objects.get(id=id_post)
        submodel = Ordered.objects.filter(id=id_post).values()
        for i in submodel:
            parent_id = i['parent_id']
        ordered_amount = ordered_obj.amount
        if ordered_amount > 0:
            amount_to_set = ordered_amount - amount
            try:
                que = GeneralInfo.objects.get(id=parent_id)
                tri = True
            except GeneralInfo.DoesNotExist:
                que = None
                tri = False
            if tri:
                if amount_to_set > 0:
                    ordered_obj.amount = amount_to_set
                    ordered_obj.save()
                    initial_amount = que.amount_available
                    saved_amount = initial_amount + amount
                    que.amount_available = saved_amount
                    que.save()
                elif amount_to_set <= 0:
                    initial_amount = que.amount_available + amount
                    que.amount_available = initial_amount
                    que.save()
                    ordered_obj.delete()
                return HttpResponseRedirect(request.path_info)


            elif amount_to_set <= 0:
                try:
                    que = GeneralInfo.objects.get(id=parent_id)
                    tri = True
                except GeneralInfo.DoesNotExist:
                    que = None
                    tri = False
                if tri:
                    initial_amount = que.amount_available + amount
                    que.amount_available = initial_amount
                    que.save()
                ordered_obj.delete()
                return HttpResponseRedirect(request.path_info)

        
    try:
        que = Ordered.objects.all()
        tri = True
    except Ordered.DoesNotExist:
        que = None
        tri = False
    needed_fields = ['detail_number', 'price', 'description', 'description_number']
    data = []
    if tri:

        for a in que:
            id = a.id
            nbr = Ordered.objects.get(id=id).amount
            
            product = GeneralInfo.objects.get_subclass(id=a.parent.id)
            data1 = {name: getattr(product,name) for name in needed_fields }
            data1.update({'num':nbr})
            data1.update({'id':id})
            data.append(data1)
    return render(request,'ordered.html',{'data':data})


def tip(request):
    model = Tip
    template = 'tip.html'
    return request_handler(request,model,template)

def thrust(request):
    model = Thrust
    template = 'thrust.html'
    return request_handler(request,model,template)

def steel_wheel(request):
    model = SteelWheel
    template = 'steel_wheel.html'
    return request_handler(request,model,template)

def anthers(request):
    model = Anthers
    template = 'anthers.html'
    return request_handler(request,model,template)

def brakepads(request):
    model = BrakePads
    template = 'brakepads.html'
    return request_handler(request,model,template)

def filter(request):
    model = Filter
    template = 'filter.html'
    return request_handler(request,model,template)


def bearing(request):
    model = Filter
    template = 'bearing.html'
    return request_handler(request,model,template)