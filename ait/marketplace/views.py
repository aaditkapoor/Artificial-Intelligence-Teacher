from django.shortcuts import render, render_to_response
from .models import MarketPlace
import datetime
from django.http import HttpResponseRedirect, HttpResponse
import random
from ait.models import DataModel

def home(request):
	data = MarketPlace.objects.all().order_by("packId","by","subject","email").distinct("packId","by","subject","email")

	return render_to_response("market_home.html",{"data":data})



def add_item(request):
	by = request.GET.get("name","")
	email = request.GET.get("email","")
	subject = request.GET.get("subject","")
	date = datetime.datetime.now()

	if by and email and subject:
		request.session['by'] = by
		request.session['email'] = email
		request.session['subject'] = subject
		request.session['packId'] = random.randint(1,10000)
		return render_to_response("market_add_next.html", {"given":True,"name":by, "email":email,"subject":subject})
	else:
		return render_to_response("market_add.html")


def step_two_add_market(request):
	if request.session.get("by") and request.session.get("email") and request.session.get("subject") and request.session.get("packId"):
		by = request.session.get("by")
		email = request.session.get("email")
		subject = request.session.get("subject")
		i = request.session.get("packId")
		date = datetime.datetime.now()

		if request.GET.get("question") and request.GET.get("answer"):
			MarketPlace.objects.create(packId=i,by=by, email=email, subject=subject, question=request.GET.get("question"), answer = request.GET.get("answer"), date_uploaded=date)
			return render_to_response("market_add_next.html", {"given":True,"name":by, "email":email,"subject":subject,"alert":"Added the question"})
		else:
			return render_to_response("market_add.html")
	else:
		return HttpResponseRedirect("/market_home/")


def install(request):
	id = request.GET.get("id","")
	if id:
		if MarketPlace.objects.filter(packId=id).exists():
			if check_logged_in(request):
				username = request.session.get("username")
				data = MarketPlace.objects.filter(packId=id)
				for i in data:
					DataModel.objects.create(username=username, question=i.question, answer=i.answer)
				return HttpResponseRedirect("/?success=True")
			else:
				return HttpResponse("Not logged in!")
		else:
			return HttpResponse("error!!")
	else:
		return HttpResponse("error!")




def check_logged_in(request):
	if request.session.get("username") is not None and request.session.get("name_been_put") and request.session.get("email") is not None:
		return True
	else:
		return False

def exit_session_market(request):
	request.session['by'] = False
	request.session['email'] = False
	request.session['subject'] = False
	request.session['packId']=False


	return HttpResponseRedirect("/market_home/")
