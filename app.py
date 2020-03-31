from flask import Flask
from flask import request, after_this_request
from flask import redirect, make_response
from flask import session, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Flask!</h1>'

@app.route('/login')
def login():
    print("首部字段："+request.headers['Referer'])
    name = request.args.get('name', '')
    src_url = request.args.get('src')
    g.nnnn = name
    login = False
    if name == 'sxh':
        login = True
    if login:
        session['login_user'] = 'name_is_sxh'
    return 'login succeed'
        

@app.route('/age/<int:year>', methods=['GET'])
def getAge(year):
    hello = "halyy wood."
    user = ''
    if 'login_user' in session:
        user = session.get('login_user')
    print('login_user:' + user)

    @after_this_request
    def after(response):
        response.set_cookie('sxh', hello)
        return response

    print(type(request))
    name = request.args.get('name', 'Nick')
    # return '<h1>Age of %s is %d!</h1>' % (name, 19 + year), 301, {("Location", "https://www.iqiyi.com")}
    #return redirect('https://www.iqiyi.com')
    # return redirect(url_for())
    # resp = make_response('<h1>Age of %s is %d!</h1>' % (name, 19 + year))
    # resp.set_cookie('name', 'Nick', max_age= 1800)
    # resp.set_cookie('name2', 'Nick2')
    # return resp
    return 'name:%s' % (g.nnnn)

@app.before_request
def beforeAny():
    print("Hello...")

@app.route('/page1')
def get_page1():
    return '<h2>This is Page 1.<a href=\'/login?src=/page1\'>Login here</a></h2>'
