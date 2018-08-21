from django.shortcuts import render

# Create your views here.
from .models import *

from django.contrib.auth.decorators import login_required, permission_required    
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render_to_response
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from braces.views import StaffuserRequiredMixin, SuperuserRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django import forms
from .forms import *
from django.db import transaction
from django.shortcuts import render
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm, PasswordChangeForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
import csv
from django.http import HttpResponse

@login_required
def checkauth(request):
    if request.user.is_staff:
        #your logic here
        return redirect("allprojects/")# or your url name
    if request.user.is_authenticated:
        #your logic here
        return redirect("users/")# or your url name   


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project

@login_required 
def success(request):

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'success.html',)    
    
@staff_member_required
def allprojects(request):
    
    allprojects=Project.objects.all()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'ptslogin.html',
        context={"allprojects":allprojects})

@staff_member_required
def completedprojects(request):
    
    allprojects =Project.objects.all()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'completedprojects.html',
        context={"allprojects":allprojects})

@login_required
def users(request):
    groups = request.user.groups.all()
    projects = Project.objects.all()
    finlist = []
    
    for project in projects:
        grp = project.access_personnel.all()
        if set(groups).intersection(grp):
            finlist.append(project)
        
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'users.html',
        context={"finlist":finlist,})


class ProjectDocumentinstanceCreate(StaffuserRequiredMixin, CreateView):
    model = Project
    template_name = "portal/project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy('allprojects')


class ProjectDocumentinstanceUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = "portal/project_form.html"
    form_class = ProjectForm
    
class ProjectDelete(StaffuserRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('allprojects')

class ProjectDocumentreviewUpdate(StaffuserRequiredMixin, UpdateView):
    model = Documentinstance
    fields = ['comment', 'feedback_document', 'reviewed_status']
    
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect("success/")

@login_required
def documents(request,pk):
    
    refdict = {}
    
    mnecatx = Category.objects.filter(title="M&E")
    if mnecatx:
        refdict["mne"] = mnecatx[0]
    
    iddcatx = Category.objects.filter(title="Interior Design")
    if iddcatx:
        refdict["idd"] = iddcatx[0]
    
    arccatx = Category.objects.filter(title="Architecture")
    if arccatx:    
        refdict["arc"] = arccatx[0]
    
    komphx = Phase.objects.filter(title="Kick-off Meeting")
    if komphx:
        refdict["kom"] = komphx[0]
    
    codphx = Phase.objects.filter(title="Concept DAP")
    if codphx:
        refdict["cod"] = codphx[0]

    mocphx = Phase.objects.filter(title="Mockup DAP")
    if mocphx:
        refdict["moc"] = mocphx[0]

    ddaphx = Phase.objects.filter(title="Design Drawing Approved")
    if ddaphx:
        refdict["dda"] = ddaphx[0]

    conphx = Phase.objects.filter(title="Construction")
    if conphx:
        refdict["con"] = conphx[0]

    popphx = Phase.objects.filter(title="POP Team Formalised")
    if popphx:
        refdict["pop"] = popphx[0]

    istphx = Phase.objects.filter(title="Integrated Systems Test")
    if istphx:
        refdict["ist"] = istphx[0]  
    
    comphx = Phase.objects.filter(title="Completed")
    if comphx:
        refdict["com"] = comphx[0]    
    
    url = request.path
    doccat = url[-4:-1]
    docphase = url[-8:-5]
    
    
    final =[]
    alldocuments=Documentinstance.objects.filter(project=pk)
    
    for doc in alldocuments:
        if doc.phase == refdict[docphase]:
            if doc.category == refdict[doccat]:
                final.append(doc) 
#        if doccat == 'mne':
#            if docphase == 'kom':
#                if doc.phase == komph:
#                    if doc.category == mnecat:
#                        final.append(doc) 

                    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'docs.html',
        context={"alldocuments":alldocuments,"doccat":doccat, "docphase":docphase,
                 "final":final,
                 })

#def projectsuccess(request):
#
#    return render(request, 'projectsuccess.html',
#         context={})

class documentdetail(LoginRequiredMixin,generic.DetailView):
    model = Documentinstance    

@staff_member_required    
def documentscreate(request, pk):
    
    refdict = {}
    
    mnecatx = Category.objects.filter(title="M&E")
    if mnecatx:
        refdict["mne"] = mnecatx[0]
    
    iddcatx = Category.objects.filter(title="Interior Design")
    if iddcatx:
        refdict["idd"] = iddcatx[0]
    
    arccatx = Category.objects.filter(title="Architecture")
    if arccatx:    
        refdict["arc"] = arccatx[0]
    
    komphx = Phase.objects.filter(title="Kick-off Meeting")
    if komphx:
        refdict["kom"] = komphx[0]
    
    codphx = Phase.objects.filter(title="Concept DAP")
    if codphx:
        refdict["cod"] = codphx[0]

    mocphx = Phase.objects.filter(title="Mockup DAP")
    if mocphx:
        refdict["moc"] = mocphx[0]

    ddaphx = Phase.objects.filter(title="Design Drawing Approved")
    if ddaphx:
        refdict["dda"] = ddaphx[0]

    conphx = Phase.objects.filter(title="Construction")
    if conphx:
        refdict["con"] = conphx[0]

    popphx = Phase.objects.filter(title="POP Team Formalised")
    if popphx:
        refdict["pop"] = popphx[0]

    istphx = Phase.objects.filter(title="Integrated Systems Test")
    if istphx:
        refdict["ist"] = istphx[0]  
    
    comphx = Phase.objects.filter(title="Completed")
    if comphx:
        refdict["com"] = comphx[0]    
    
    url = request.path
    doccat = url[-11:-8] #gives category in string
    docphase = url[-15:-12] #gives phase in string
    fincat = refdict[doccat]
    finphase = refdict[docphase]     
    
    if request.method == 'POST':
        post=Documentinstance()
        post.refdoc= request.FILES.get('file1')
        post.name = request.POST.get('name')
        post.category = fincat
        post.phase = finphase
        post.project = Project.objects.filter(id=pk)[0]
        post.save()
        
        return render(request, 'documentcreatesuccess.html')  

    else:
        return render(request,'createdoc.html',)

@login_required
def documentupdate(request,pk):
        if request.method == 'POST':
            if request.FILES.get('file1'):
                post=Documentinstance.objects.filter(id=pk)[0]
                post.doc= request.FILES.get('file1')
                post.submitter = request.user
                post.dos = date.today()
                post.save()
                
                return render(request, 'success.html')  

        else:
            return render(request,'updatedoc.html',)

@login_required       
def documentcomment(request,pk):
        post=Documentinstance.objects.filter(id=pk)[0]
        comments = post.comment
        
        return render(request, 'comments.html', context={"comments": comments
                 })  

class documentdelete(StaffuserRequiredMixin, DeleteView):
    model = Documentinstance
    success_url = reverse_lazy('success') 

@staff_member_required     
def ProjectDocumentreviewsucess(request, pk):
        post=Documentinstance.objects.filter(id=pk)[0]
        if post.reviewed_status == "Resubmission Required":
                doc=Documentinstance()
                if (post.name[-2:-1] == "v") or (post.name[-3:-2] == "v"):
                    newname = post.name[:-1]
                    x = str(int(post.name[-1:])+1)
                    newname = newname + x
                else:
                    newname = post.name + "v2"
                doc.dor = date.today()    
                doc.name = newname
                doc.phase = post.phase
                doc.category = post.category
                doc.project = post.project
                doc.save()
                
                return render(request, 'documentreviewsuccess.html')  

        else:
                return render(request,'documentreviewsuccess.html')
    

class templateCreate(StaffuserRequiredMixin, CreateView):
    model = templateset
    template_name = "portal/template_form.html"
    form_class = templatesetForm
    success_url = reverse_lazy('templatelist')

    def get_context_data(self, **kwargs):
        data = super(templateCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['templateinstances'] = templateinstanceFormSet(self.request.POST)
        else:
            data['templateinstances'] = templateinstanceFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        templateinstances = context['templateinstances']
        with transaction.atomic():
            self.object = form.save()

            if templateinstances.is_valid():
                templateinstances.instance = self.object
                templateinstances.save()
        return super(templateCreate, self).form_valid(form)


class templateUpdate(StaffuserRequiredMixin, UpdateView):
    model = templateset
    template_name = "portal/template_form.html"
    form_class = templatesetForm
    success_url = reverse_lazy('templatelist')

    def get_context_data(self, **kwargs):
        data = super(templateUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['templateinstances'] = templateinstanceFormSet(self.request.POST, instance=self.object)
        else:
            data['templateinstances'] = templateinstanceFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        templateinstances = context['templateinstances']
        with transaction.atomic():
            self.object = form.save()

            if templateinstances.is_valid():
                templateinstances.instance = self.object
                templateinstances.save()
        return super(templateUpdate, self).form_valid(form)

class templatesetdelete(StaffuserRequiredMixin, DeleteView):
    model = templateset
    success_url = reverse_lazy('templatelist') 

@staff_member_required
def addtemplate(request,pk):
        tset = templateset.objects.all()
            
        refdict = {}
        
        mnecatx = Category.objects.filter(title="M&E")
        if mnecatx:
            refdict["mne"] = mnecatx[0]
        
        iddcatx = Category.objects.filter(title="Interior Design")
        if iddcatx:
            refdict["idd"] = iddcatx[0]
        
        arccatx = Category.objects.filter(title="Architecture")
        if arccatx:    
            refdict["arc"] = arccatx[0]
        
        komphx = Phase.objects.filter(title="Kick-off Meeting")
        if komphx:
            refdict["kom"] = komphx[0]
        
        codphx = Phase.objects.filter(title="Concept DAP")
        if codphx:
            refdict["cod"] = codphx[0]
    
        mocphx = Phase.objects.filter(title="Mockup DAP")
        if mocphx:
            refdict["moc"] = mocphx[0]
    
        ddaphx = Phase.objects.filter(title="Design Drawing Approved")
        if ddaphx:
            refdict["dda"] = ddaphx[0]
    
        conphx = Phase.objects.filter(title="Construction")
        if conphx:
            refdict["con"] = conphx[0]
    
        popphx = Phase.objects.filter(title="POP Team Formalised")
        if popphx:
            refdict["pop"] = popphx[0]
    
        istphx = Phase.objects.filter(title="Integrated Systems Test")
        if istphx:
            refdict["ist"] = istphx[0]  
        
        comphx = Phase.objects.filter(title="Completed")
        if comphx:
            refdict["com"] = comphx[0]    
        
        url = request.path
        doccat = url[-16:-13] #gives category in string
        docphase = url[-20:-17] #gives phase in string
        fincat = refdict[doccat]
        finphase = refdict[docphase]     
            
        if request.method == 'POST':
            if request.POST.get('templateform'):
                data = request.POST.get('templateform')
                newdata = templateset.objects.filter(name=data)[0]
                alldata = templateinstance.objects.filter(templateset = newdata)
                for tinst in alldata:
                    post = Documentinstance()
                    post.name = tinst.name
                    post.refdoc = tinst.refdoc
                    post.category = fincat
                    post.phase = finphase
                    post.project = Project.objects.filter(id=pk)[0]
                    post.save()
                    
                return render(request, 'addtemplatesuccess.html', context ={"newdata":data})  

        else:
            return render(request,'addtemplate.html', context={"tset": tset
                 })
    
class TemplatesListView(StaffuserRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = templateset
    paginate_by = 10
    
    def get_queryset(self):
        return templateset.objects.all()

@staff_member_required   
def signup(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                return redirect('allprojects')
        else:
            form = SignUpForm()    
    elif request.user.is_staff:
        if request.method == 'POST':
            form = SignUpStaffForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                return redirect('allprojects')
        else:
            form = SignUpStaffForm()

    return render(request, 'signup.html', {'form': form})    

@staff_member_required
def userlist(request):
    superlist = User.objects.filter(is_superuser = False)
    userlist = User.objects.filter(is_superuser = False, is_staff = False)
    return render(request, 'userlist.html', {'userlist': userlist, 'superlist': superlist})    

    
class UpdateProfile(StaffuserRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'groups', 'email',)
    # the combined UserProfile and User exposes.
    template_name = 'user_update.html'
#    slug_field = 'username'
#    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('userlist')

@user_passes_test(lambda u: u.is_superuser)
def change_password(request, pk):
    user1 = User.objects.get(id=pk)
    if request.method == 'POST':
        form = SetPasswordForm(user1, request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('userlist')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SetPasswordForm(user1)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

@staff_member_required    
def change_passwordstaff(request, pk):
    user1 = User.objects.get(id=pk)
    if user1.is_superuser == False or user1.is_staff == False:
        if request.method == 'POST':
            form = SetPasswordForm(user1, request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('userlist')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = SetPasswordForm(user1)
        return render(request, 'accounts/change_password.html', {
            'form': form
        })
    else:
        return HttpResponse('Unauthorized', status=401)

@login_required
def change_ownpassword(request, pk):
    if pk == request.user.id:
        user1 = User.objects.get(id=request.user.id)
        if request.method == 'POST':
            form = PasswordChangeForm(user1, request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('userlist')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(user1)
        return render(request, 'accounts/change_password.html', {
            'form': form
        })
    else:
        return HttpResponse('Unauthorized', status=401)

@user_passes_test(lambda u: u.is_superuser)
def del_user(request, pk):  
    u = User.objects.get(id = pk)
    if request.method == 'POST':
        u.delete() 
        return redirect('userlist')              
    else:    
        return render(request, 'portal/user_confirm_delete.html', context={'detail': u}) 

@staff_member_required    
def del_userstaff(request, pk):  
    u = User.objects.get(id = pk)
    if u.is_superuser == False or user1.is_staff == False:
        if request.method == 'POST':
            u.delete() 
            return redirect('userlist')              
        else:    
            return render(request, 'portal/user_confirm_delete.html', context={'detail': u}) 
    else:
            return HttpResponse('Unauthorized', status=401)

@staff_member_required        
def groupcreate(request):
        if request.method == 'POST':
            if request.POST.get('group1'):
                post=Group()
                post.name= request.POST.get('group1')
                post.save()
                
                return redirect('grouplist') 

        else:
            return render(request,'newgroup.html',)

@staff_member_required
def grouplist(request):
    groups = Group.objects.all()
    return render(request,'grouplist.html', context={'groups': groups})

class groupUpdate(StaffuserRequiredMixin, UpdateView):
    model = Group
    fields = ['name',]
    template_name = "portal/group_form.html"
    success_url = reverse_lazy('grouplist')

@staff_member_required
def del_group(request, pk):  
    u = Group.objects.get(id = pk)
    if request.method == 'POST':
        u.delete() 
        return redirect('grouplist')              
    else:    
        return render(request, 'portal/group_confirm_delete.html', context={'group': u}) 

class CountryCreate(StaffuserRequiredMixin, CreateView):
    model = Country
    fields = ['country',]
    success_url = reverse_lazy('countrylist')
    
class CountryUpdate(StaffuserRequiredMixin, UpdateView):
    model = Country
    fields = ['country',]
    success_url = reverse_lazy('countrylist')

class CountryListView(StaffuserRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = Country
    paginate_by = 100
    
    def get_queryset(self):
        return Country.objects.all()    

class CountryDelete(StaffuserRequiredMixin, DeleteView):
    model = Country
    success_url = reverse_lazy('countrylist')
    
class CityCreate(StaffuserRequiredMixin, CreateView):
    model = City
    fields = ['city',]
    success_url = reverse_lazy('citylist')
    
class CityUpdate(StaffuserRequiredMixin, UpdateView):
    model = City
    fields = ['city',]
    success_url = reverse_lazy('citylist')
    
class CityListView(StaffuserRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = City
    paginate_by = 100
    
    def get_queryset(self):
        return City.objects.all()    

class CityDelete(StaffuserRequiredMixin, DeleteView):
    model = City
    success_url = reverse_lazy('citylist')

@staff_member_required    
def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="projects.csv"'

    writer = csv.writer(response)
    writer.writerow(['Project','Country','City','Kickoff Meeting', 'Date',
                               'Concept DAP', 'Date', 'Mockup DAP', 'Date','Design Drawing Approved', 'Construction','Date', 'POP Team Formalised','Date','IST',
                               'Date', 'Completed','Date', 'Opening Date', 
                               ])


    projobjects = Project.objects.all().values_list('project_name','country','city','kickoff_meeting', 'kickoff_meeting_date',
                                            'concept_DAP', 'concept_DAP_date',
                                        'mockup_DAP','mockup_DAP_date',
                                         'design_drawing_approved', 
                                        'construction', 'construction_date', 'pop_team', 'pop_team_date',
                                        'IST', 'IST_date', 'completion', 'completion_date',
                                        'opening_date',
                                        )
    
    countries = Country.objects.all().values_list('id','country',)
    citylist = City.objects.all().values_list('id','city',)
    
    for proj in projobjects:
        if proj[16] == False:
            for countobj in countries:
                if proj[1] == countobj[0]:
                    projlist = list(proj)
                    projlist.pop(1)
                    countobjlist = list(countobj)
                    projlist.insert(1, countobjlist[1])
                    proj = tuple(projlist)
                    for cityobj in citylist:
                        if proj[2] == cityobj[0]:
                            projlist = list(proj)
                            projlist.pop(2)
                            cityobjlist = list(cityobj)
                            projlist.insert(2,cityobjlist[1])
                            itr = 0
                            while itr < len(projlist):
                                if projlist[itr] == True:
                                    projlist[itr] = "YES"
                                    itr += 1
                                elif projlist[itr] == False:
                                    projlist[itr] = "NO"
                                    itr += 1
                                else:
                                    itr += 1
                            proj = tuple(projlist)
                            writer.writerow(proj)
    return response

@staff_member_required    
def comexport(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="projects.csv"'

    writer = csv.writer(response)
    writer.writerow(['Project','Country','City','Kickoff Meeting', 'Date',
                               'Concept DAP', 'Date', 'Mockup DAP', 'Date','Design Drawing Approved', 'Construction','Date', 'POP Team Formalised','Date','IST',
                               'Date', 'Completed','Date', 'Opening Date', 
                               ])


    projobjects = Project.objects.all().values_list('project_name','country','city','kickoff_meeting', 'kickoff_meeting_date',
                                            'concept_DAP', 'concept_DAP_date',
                                        'mockup_DAP','mockup_DAP_date',
                                         'design_drawing_approved', 
                                        'construction', 'construction_date', 'pop_team', 'pop_team_date',
                                        'IST', 'IST_date', 'completion', 'completion_date',
                                        'opening_date',
                                        )
    
    countries = Country.objects.all().values_list('id','country',)
    citylist = City.objects.all().values_list('id','city',)
    
    for proj in projobjects:
        if proj[16] == True:
            for countobj in countries:
                if proj[1] == countobj[0]:
                    projlist = list(proj)
                    projlist.pop(1)
                    countobjlist = list(countobj)
                    projlist.insert(1, countobjlist[1])
                    proj = tuple(projlist)
                    for cityobj in citylist:
                        if proj[2] == cityobj[0]:
                            projlist = list(proj)
                            projlist.pop(2)
                            cityobjlist = list(cityobj)
                            projlist.insert(2,cityobjlist[1])
                            itr = 0
                            while itr < len(projlist):
                                if projlist[itr] == True:
                                    projlist[itr] = "YES"
                                    itr += 1
                                elif projlist[itr] == False:
                                    projlist[itr] = "NO"
                                    itr += 1
                                else:
                                    itr += 1
                            proj = tuple(projlist)
                            writer.writerow(proj)
    return response

def test(request):

    return render(request, 'test.html',
         context={})
