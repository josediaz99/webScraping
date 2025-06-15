from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required,current_user
from .models import Note
from . import db
import json
from liftCastCompScrape import fetchEvents
import asyncio
from scrapeAthletes import getAthletes
views = Blueprint('views',__name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    events = asyncio.run(fetchEvents())   # Fetch events from lifticast
    if not events:
        flash('No events found!', category='error')
    else:
        flash(f'Found events!', category='success')
    return render_template("home.html", user=current_user, events=events)

@views.route('/competitions')
def showAthletes():
    link = request.args.get('link')
    athletes = getAthletes(link)
    return render_template('home.html' , athletes = athletes)