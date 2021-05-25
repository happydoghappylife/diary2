from django.shortcuts import redirect, get_object_or_404, render
from .models import Mydiary
from .forms import MydiaryForm
from django.contrib.auth.decorators import login_required

def diarycover(request):
    diarynum = Mydiary.objects.count
    return render(request, 'diarycover.html',{'diarynum' : diarynum})

@login_required(login_url='userlogin')
def diaryindex(request):
    diarycontents = Mydiary.objects.all()
    return render(request, 'diaryindex.html', {'diarycontents' : diarycontents})

@login_required(login_url='userlogin')
def diarydetails(request,id):
    contents = get_object_or_404(Mydiary, pk = id)
    return render(request, 'diarydetails.html', {'contents' : contents})

@login_required(login_url='userlogin')
def newdiary(request):
    form = MydiaryForm()
    return render(request,'newdiary.html', {'form' : form})

@login_required(login_url='userlogin')
def creatediary(request):
    form = MydiaryForm(request.POST, request.FILES)
    new_diary = form.save(commit=True)
    new_diary.save()
    return redirect('diarydetails', new_diary.id)

@login_required(login_url='userlogin')
def diaryupdate(request, id):
    edit_diary = Mydiary.objects.get(id = id)
    return render(request, 'diaryupdate.html', {'contents' : edit_diary})

@login_required(login_url='userlogin')
def update(request, id):
    update_diary = Mydiary.objects.get(id = id)
    update_diary.title = request.POST['diarytitle']
    update_diary.body = request.POST['diarybody']
    update_diary.save()
    return redirect('diarydetails', update_diary.id)

@login_required(login_url='userlogin')
def delete(request,id):
    delete_diary = Mydiary.objects.get(id = id)
    delete_diary.delete()
    return redirect('diaryindex')