
from .models import Resume
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import Recruiter_register,resume_submit
from django.http import JsonResponse





class submitresume(CreateView):
    model = Resume

    fields = ['Name','Age','Qualification','Email','Phone_number','About_Me','Skills']


class userformview(View):
    form_class=Recruiter_register
    template_name='submitresume/login.html'

    # displays blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    #submits the filled form
    def post(self, request):
        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)

            #clean normalized data

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #return user object if credentials are correct

            user = authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('submitresume:login')


        return render(request, self.template_name, {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resumes = Resume.objects.all()
                return redirect('submitresume:index')
            else:
                return render(request, 'submitresume/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'submitresume/login.html', {'error_message': 'Invalid login'})
    elif request.method == "get":
        return redirect('submitresume:index')
    return render(request, 'submitresume/login.html')


def detail(request, resume_id):
    if not request.user.is_authenticated():
        return redirect('submitresume:login')
    else:
        user = request.user
        resume = get_object_or_404(Resume, pk=resume_id)
        return render(request, 'submitresume/detail.html', {'resume': resume, 'user': user})




def logout_user(request):
    logout(request)
    form = Recruiter_register(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('submitresume:login')

def index(request):
    if not request.user.is_authenticated():
        return redirect('submitresume:login')
    else:
        resumes = Resume.objects.all()
        return render(request, 'submitresume/index.html', {'resumes': resumes})





def select_resume(request, resume_id):
    resume = get_object_or_404(Resume, pk=resume_id)
    try:
        if resume.is_selected:
            resume.is_selected = False
        else:
            resume.is_selected = True
        resume.save()
    except (KeyError, resume.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return redirect('submitresume:detail',resume_id)


def selected_list(request):
    if not request.user.is_authenticated():
        return redirect('submitresume:login')
    else:
        resumes = Resume.objects.filter(is_selected=True)
        return render(request, 'submitresume/index.html', {'resumes': resumes})


class resume_form(View):
    model = Resume
    form_class=resume_submit
    template_name='submitresume/submit_resume.html'
    template_success='submitresume/Success.html'

    # displays blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    #submits the filled form
    def post(self, request):
        form=self.form_class(request.POST)

        if form.is_valid():

            Resume=form.save(commit=False)
            resume = Resume
            #clean normalized data

            resume.Name=form.cleaned_data['Name']
            resume.Age=form.cleaned_data['Age']
            resume.Qualification=form.cleaned_data['Qualification']
            resume.Email = form.cleaned_data['Email']
            resume.Phone_number=form.cleaned_data['Phone_number']
            resume.About_Me=form.cleaned_data['About_Me']
            resume.Skills=form.cleaned_data['Skills']


            resume.save()
            return render(request, self.template_success, {'form': form})
        else:

            return render(request, self.template_name, {'form': form})











