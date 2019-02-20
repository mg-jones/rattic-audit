import os
import sys

from flask import Flask, Response, redirect, url_for

SECRET_KEY = 'S\x16_\xe7\x84\xa33\x99\xa8\xc3\x9d\xc3\xbe_\xb6e\x89\xcc\x86mS\xb0]X'
app = Flask(__name__)
app.config.from_object(__name__)

lib_path = os.path.dirname(os.path.realpath(__file__))
lib_path = lib_path + '/lib'
sys.path.append(lib_path)
import rattic_db


@app.route('/')
def rootpath():
    return redirect(url_for('all'))


@app.route('/all')
def all():
    rdb = rattic_db.RatticDB()
    all_strengths = rdb.query_all()
    return Response(all_strengths, mimetype='application/json')


@app.route('/group/<groupname>')
def groupsearch(groupname):
    rdb = rattic_db.RatticDB()
    group_strength = rdb.query_group(groupname)
    return Response(group_strength, mimetype='application/json')
