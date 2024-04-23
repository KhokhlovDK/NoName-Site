import random

from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)
list = ['Ann','Dany','Oly','Kate','Vany']
lastpage = ''

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/cardAnn')
def cardAnn():
    global lastpage
    lastpage = 'Ann'
    return render_template("cardAnn.html")

@views.route('/cardDany')
def cardDany():
    global lastpage
    lastpage = 'Dany'
    return render_template("cardDany.html")

@views.route('/cardKate')
def cardKate():
    global lastpage
    lastpage = 'Kate'
    return render_template("cardKate.html")

@views.route('/cardOly')
def cardOly():
    global lastpage
    lastpage = 'Oly'
    return render_template("cardOly.html")

@views.route('/cardVany')
def cardVany():
    global lastpage
    lastpage = 'Vany'
    return render_template("cardVany.html")

@views.route('/card')
def card():
    rnd = random.randint(0,4)
    htmlName = 'card' + list[rnd]
    return redirect(url_for('views.' + htmlName))

@views.route('/left')
def left():
    index = GetIndexLeft()
    htmlName = 'card' + list[index]
    return redirect(url_for('views.' + htmlName))

@views.route('/right')
def right():
    index = GetIndexRight()
    htmlName = 'card' + list[index]
    return redirect(url_for('views.' + htmlName))

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/zayivka')
def zayivka():
    return render_template("zayivka.html")

def GetIndexLeft():
    global lastpage
    index = list.index(lastpage)
    index -= 1
    if index == -1:
        index = 4
    return index

def GetIndexRight():
    global lastpage
    index = list.index(lastpage) + 1
    if index == 5:
        index = 0
    return index