# -*- coding: utf-8 -*-

from flask import Flask, Blueprint, render_template, abort, url_for, redirect, request
from jinja2 import TemplateNotFound

from . import app
from Retrievr import classes

login_form = Blueprint('login_form', __name__, template_folder="templates")

@login_form.route('/web/login', defaults={'page': 'index'}, methods=['GET', 'POST'])
@login_form.route("/web/login/<page>", methods=['GET'])
def show_login_form(page):
    try:
        if page == 'index' and request.method == 'GET':
            return render_template('auth/%s.html' % page)
        elif page == 'index' and request.method == 'POST':
            # add logic here to check against users table for authentication;
            # add session token with context once completed.

            # let's start down that path.
            data = request.form.to_dict()
            classes.user.LoginMethod(login=data.get('login'), password=data.get('password'))

            app.logger.debug("Got files")
            
            return render_template('auth/%s.html' % page)
    except TemplateNotFound:
        return redirect(url_for('login_form.show_login_form'))

