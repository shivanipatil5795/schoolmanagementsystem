from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from parent.forms import ParentForm
from parent.models import Parent
# Create your views here.
def std(request):
    if request.method == "POST":
        form = ParentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ParentForm()
    return render(request,'index.html',{'form':form})
def show(request):
    parent = Parent.objects.all()
    return render(request,"show.html",{'parent':parent})
def edit(request, id):
    parent = Parent.objects.get(id=id)
    return render(request,'edit.html', {'parent':parent})
def update(request, id):
    parent = Parent.objects.get(id=id)
    form = ParentForm(request.POST, instance = parent)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'parent': parent})
def destroy(request, id):
    parent = Parent.objects.get(id=id)
    parent.delete()
    return redirect("/show")