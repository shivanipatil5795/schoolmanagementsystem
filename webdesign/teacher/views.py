from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from teacher.forms import TearcherForm
from teacher.models import Teacher
# Create your views here.
def std(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = TeacherForm()
    return render(request,'index.html',{'form':form})
def show(request):
    students = Teacher.objects.all()
    return render(request,"show.html",{'teacher':teacher})
def edit(request, id):
teacher = Teacher.objects.get(id=id)
    return render(request,'edit.html', {'teacher':teacher})
def update(request, id):
    Teacher = Teacher.objects.get(id=id)
    form = TeacherForm(request.POST, instance = student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'teacher': teacher})
def destroy(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect("/show")