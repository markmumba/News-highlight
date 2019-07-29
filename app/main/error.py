from flask import render_template
from . import main

@main.errorhandler(404)
def four_O_four(error):

    return render_template('fourOfour.html'),404
    