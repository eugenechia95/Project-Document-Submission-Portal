from django.forms import inlineformset_factory
from django.db import models
from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class DocumentinstanceForm(ModelForm):
    class Meta:
        model = Documentinstance
        exclude = ('id', 'submitter', 'dos', 'resubmission')

DocumentinstanceFormSet = inlineformset_factory(Project, Documentinstance,
                                            form=DocumentinstanceForm, extra=1)

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('id',)

class templateinstanceForm(ModelForm):
    class Meta:
        model = templateinstance
        exclude = ('id',)

templateinstanceFormSet = inlineformset_factory(templateset, templateinstance,
                                            form=templateinstanceForm, extra=1)

class templatesetForm(ModelForm):
    class Meta:
        model = templateset
        exclude = ('id',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, )
    last_name = forms.CharField(max_length=30, required=False, )
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff', 'password1', 'password2',)

class SignUpStaffForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, )
    last_name = forms.CharField(max_length=30, required=False, )
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

