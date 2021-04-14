# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 11:43:42 2021

@author: p.szaszak
"""

"""Help commands"""


django-admin startproject ....
python manage.py startapp ....

#add app to settings


install requiremnets
pip install freeze-requirements

python -m pip install -r requiremnets.txt 





python manage.py migrate --run-syncdb

pip install django-crispy-forms

CRISPY_TEMPLATE_PACK = 'uni_form'

https://django-crispy-forms.readthedocs.io/en/latest/filters.html


#git init

git add .

git commit -m "first commit"
#git branch -M main
#git remote add origin https://github.com/szaszpeti/Timesheet.git
git push -u origin main


Pythonanawhere
git clone https://github.com/myusername/myproject.git



Start new app
modify wwsgi

consol make migrations





TO UPDATE ON THE SERVER

LOCAL CONSOL:
git add .
git commit -m "second commit"
git push -u origin main


PYTHON ANYWHERE CONSOL:


workon myvenv
go to the django projectfolder

Pull changes
git fetch origin
git reset --hard
git pull


/home/szaszpeti/.virtualenvs/myvenv/lib/python3.7/site-packages/django/contrib/admin/static/admin/

#start = datetime.combine(date.min, Inspection.objects.get(id=3).time_start_1) - datetime.min
    #sum = end-start
    #sum.seconds / 3600 -> hours




 <div class="view" style="background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), url({% static 'img/bg.jpg'  %}); background-repeat: no-repeat; background-size: cover; background-position: center center;">





<div style="background-image: url({% static 'images/cover.jpg' %});">


ucare --pub_key 91a5c89d8f623ed0bb6e --secret 99d2c35bca1cbbd972aa sync 'local_uc/${uuid}/${filename}' --limit 200
