# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import filenameForm
import os
import shutil
from django.core.mail import EmailMessage

def home(request):
    return render(request,'index.html');

def form(request):
    title= 'Welcome'
    #if request.user.is_authenticated():
        #title= "My Title %s" %(request.user)
    form = filenameForm(request.POST or None,request.FILES or None)
    context = {"title": title, "form": form}


    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        context={"title":"Thank You"}


        subject='Confirmation message'
        form_email=form.cleaned_data.get("email_id")
        form_id=form.cleaned_data.get("id1")
        form_file = form.cleaned_data.get("file")
        contact_message='Job id is:'+ str(instance.id1)

        from_email=settings.EMAIL_HOST_USER
        to_email=[from_email,instance.email_id]

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=True,)


        shutil.copy2(r'C:\Users\Mohit\Desktop\alpha_machine\models\randomForest-Model.RData', r'C:\Users\Mohit\Desktop\alpha_machine\user_'+str(instance.id1))
        shutil.copy2(r'C:\Users\Mohit\Desktop\alpha_machine\models\testingNewDataSet.R',
                     r'C:\Users\Mohit\Desktop\alpha_machine\user_' + str(instance.id1))
        #shutil.copy2(r'C:\Users\Mohit\Desktop\alpha_machine\models\neuralNetwork.R',
                     #r'C:\Users\Mohit\Desktop\alpha_machine\user_' + str(instance.id1))
        #shutil.copy2(r'C:\Users\Mohit\Desktop\alpha_machine\models\randomForest.R',
                     #r'C:\Users\Mohit\Desktop\alpha_machine\user_' + str(instance.id1))
        #shutil.copy2(r'C:\Users\Mohit\Desktop\alpha_machine\models\svm.R',
                     #r'C:\Users\Mohit\Desktop\alpha_machine\user_' + str(instance.id1))
        shutil.copy2(r'C:\Users\Mohit\Desktop\alpha_machine\runAllModels.py',
                     r'C:\Users\Mohit\Desktop\alpha_machine\user_' + str(instance.id1))

        folder = r'C:\Users\Mohit\Desktop\alpha_machine\user_'+str(instance.id1)
        file = r'"{}\runAllModels.py"'.format(folder)

        os.chdir(folder)
        os.system('python ' + file)

        subject1 = 'Final file'

        email = EmailMessage(
            subject1,
            'File contains result  ',
            from_email,
            to_email,

        )
        #folder = r'C:\Users\Mohit\Desktop\alpha_machine\user_' + str(instance.id1)
        #files = r'"{}\finalResult.csv"'.format(folder)


        email.attach_file('randomForest-Testing-Result.csv')
        email.send()


    return render(request, "home.html", context)


"""def nam(request):
    title= 'Welcome'
    #if request.user.is_authenticated():
        #title= "My Title %s" %(request.user)
    form = filenameForm(request.POST or None,request.FILES or None)
    context = {"title": title, "form": form}


    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()

        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, instance.email_id]
        subject = 'Final file'

        email = EmailMessage(
            subject,
            'File contanins results of many models ',
            from_email,
            to_email,

        )

        email.attach_file('finalResult.csv')
        email.send()"""









