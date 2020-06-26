from django.shortcuts import render, redirect
import random
import datetime

def makeString(place, money):
    now=datetime.datetime.now()
    date_time=now.strftime("%Y/%d/%m %I:%M %p")
    if place == 'casino':
        if money>0:
            temp_dict={
                'message':f'Entered a casino and gained {money} gold... Woo ({date_time})',
                'color':''
            }
            return f'Entered a casino and gained {money} gold... Woo ({date_time})','green'
        else:
            return f'Entered a casino and lost {abs(money)} gold... Ouch ({date_time})','red'
    else:
        return f'Earned {money} from the {place}! ({date_time})','green'

def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'activities' not in request.session:
        request.session['activities']=[]
    return render(request, 'index.html')

def process_money(request,place):
    if place == 'farm':
        gold=random.randint(10,20)
    elif place == 'cave':
        gold=random.randint(5,10)
    elif place == 'house':
        gold=random.randint(2,5)
    else:
        gold=random.randint(-50,50)

    request.session['gold']+=gold
    request.session['activities'].append(makeString(place, gold))
    return redirect('/')

def new_game(request):
    request.session.clear()
    return redirect('/')



