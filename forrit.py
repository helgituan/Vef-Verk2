from bottle import *
import os

@route('/')
def index():
    return "<h2> Verkefni 2</h2>" \
            "<a href =/lidur> Liður A </a>" \
            "<a href =/verk> Liður B </a>"

@route('/lidur')
def lidur():
    return "<h1>Verkefni 2</h1>" \
            "<a href =/lidur/a> Liður A </a>" \
            "<a href =/lidur/b> Liður B</a>" \
            "<a href =/lidur/c> Liður C</a>"

@route('/lidur/<n>')
def param(n):
    return "<h1> This is my page " + n + "</h1>" \
            "<a href =/lidur>til baka </a>"

@route('/verk')
def mynd():
    return "<h1> Veldu þinn uppáhalds mynd</h1>" \
            '<a href="/result?mynd=mynd1"><img src="/static/mynd1.jpg" width="300"></a>' \
            '<a href="/result?mynd=mynd2"><img src="/static/mynd2.jpg" width="300"></a>'

@route('/result')
def result():
    mynd = request.query.mynd

    return '<h2> þú valdir ' + mynd + ' </h2>' \
            '<img src="/static/'+mynd+'.jpg" width="1920">'



@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./myfiles')

@error(404)
def error404(error):
    return '<h1>Þessi síða er ekki til </h1>'


run(host='0.0.0.0',port=os.environ.get('PORT'))
