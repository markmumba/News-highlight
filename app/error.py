from flask import render_template
from app import app

@app.errorhandler(404)
def four_O_four(error):

    return render_template('fourOfour.html'),404
    