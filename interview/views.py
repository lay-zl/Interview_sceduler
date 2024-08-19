from django.shortcuts import render,redirect,HttpResponse
from .models import Interview,Hr
from .forms import InterviewForm,HrForm
from django.contrib import messages
from datetime import date,timedelta

# Create your views here.

def only_five(req):
    today = date.today()
    end_day = today + timedelta(days=5)
    data = Interview.objects.filter(date__range=(today,end_day)).order_by('date')
    context={
        'data':data
    }
    return render(req,'only_five.html',context)


def search_by_date(request):
    search_date = request.GET.get('search_date')
    data = Interview.objects.filter(date=search_date) if search_date else Interview.objects.all()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Handle AJAX request
        return render(request, 'partials/interview_table.html', {'data': data})

    return render(request, 'home1.html', {'data': data})

def all_data(req):
    data = Interview.objects.all().order_by('date')
    context={
        'data':data
    }
    return render(req,'home1.html',context)


def add_interview(req):
    if req.method == 'POST':
        form = InterviewForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Added Successfully')
            return redirect('all_data')
        else:
            messages.error(req, 'There was an error with your submission.')
    form = InterviewForm()
    context = {
        'form':form
    }
    return render(req,'add.html',context)

def interview_detail(req,pk):
    data = Interview.objects.get(id=pk)
    context = {
        'data':data
    }
    return render(req,'details.html',context)

def edit(req,pk):
    obj = Interview.objects.get(id=pk)

    if req.method == 'POST':
        form = InterviewForm(req.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(req,'Data Updated Successfully')
            return redirect(f'/interview_detail/{pk}/')

    form = InterviewForm(instance=obj)
    context = {
        'form':form,
    }
    return render(req,'edit.html',context)


def delete(req,pk):
    obj = Interview.objects.get(id=pk)
    obj.delete()
    messages.success(req,'Deleted successfully.')
    return redirect('/')


def with_hr(req):
    data = Hr.objects.all()
    context = {
        'data':data
    }
    return render(req,'hr_call.html',context)

def with_hr_entry(req):
    if req.method == 'POST':
        form = HrForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,'Data enter successfully')
            return redirect('with_hr')
    form = HrForm()
    context = {
        'form':form
    }
    return render(req,'with_hr_entry.html',context)

def edit_hr_entry(req,pk):
    obj=Hr.objects.get(id=pk)

    if req.method == 'POST':
        form = HrForm(req.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(req,'Data updated successfully')
            return redirect('with_hr')
    form = HrForm(instance=obj)
    context={
        'form':form
    }
    return render(req,'with_hr_entry.html',context)

def delete_hr_entry(req,pk):
    obj = Hr.objects.get(id=pk)
    obj.delete()
    messages.success(req,'Entry deleted successfully')
    return redirect('all_data')


