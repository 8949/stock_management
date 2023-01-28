# -*- coding: utf-8 -*-
from csv import reader
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render,redirect


from django.http import HttpResponseRedirect
from .models import Employee, Iteams
from .forms import IteamsForm

class IteamsList(ListView): 
    model = Iteams

class IteamsDetail(DetailView): 
    model = Iteams

class IteamsCreate(SuccessMessageMixin, CreateView): 
    model = Iteams
    form_class = IteamsForm
    success_url = reverse_lazy('Iteams_list')
    success_message = "Iteams successfully created!"
    
def create_iteam(request):
    if request.method == "POST": 
         
        form = IteamsForm(request.POST, request.FILES)  
        print("<<<<<<<<<<<<<<<<<<<  form   >>>>>>>>>>>>>>>>",request.POST,    ">>>>"  ,request.FILES)
        iteam_code = request.POST['iteam_code']
        iteam_name = request.POST['iteam_name']
        iteam_mes_para = request.POST['iteam_mes_para']
        iteam_qty = request.POST['iteam_qty']
        image = request.POST['image']
        supplier_name = request.POST['supplier_name']
        employee_name = request.POST['employee_name']
        employee_id = Employee.objects.get(id =employee_name)
        
        iteam = Iteams(iteam_code=iteam_code,iteam_name=iteam_name,iteam_mes_para=iteam_mes_para,iteam_qty=iteam_qty,supplier_name=supplier_name,
                       image=image,employee_name=employee_id)
        iteam.save()
        return redirect('/')  
        
    else:  
        form = IteamsForm() 
        return render(request,'products/iteams_form.html',{'form':form}) 
        # return reader(request ,'products/iteams_form.html', {'form' :form } )


class IteamsUpdate(SuccessMessageMixin, UpdateView): 
    model = Iteams
    form_class = IteamsForm
    success_url = reverse_lazy('Iteams_list')
    success_message = "Iteams successfully updated!"

class IteamsDelete(SuccessMessageMixin, DeleteView):
    model = Iteams
    success_url = reverse_lazy('Iteams_list')
    success_message = "Iteams successfully deleted!"


