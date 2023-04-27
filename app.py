from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response 
from flask_session import Session
from datetime import timedelta
from user import user
from student import student
from nominee import nominee
from vote import vote
import hashlib

#create Flask app instance
app = Flask(__name__,static_url_path='')

#Configure serverside sessions 
app.config['SECRET_KEY'] = '56hdtryhRTg'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
sess = Session()
sess.init_app(app)


############################ Routes #################################

# home page
@app.route('/')
def home():
    # get the results of the votes
    nominee_obj = nominee()
    nominee_results_dict = nominee_obj.getVotes()

    # disable or enable voting based on whether user is signed in 
    if 'user' in session:
        return render_template('home.html', nominee_results=nominee_results_dict, disabled="")
    else:
        return render_template('home.html', nominee_results=nominee_results_dict, disabled="disabled")

# submits vote
@app.route('/vote', methods=['POST'])
def submitVote():
    # get the database connection
    vote_obj = vote()

    # get data from the request
    nid = request.form.get('nid')
    print('nid:', nid)
    emailid = session.get('user').get('email')
    userid = session.get('user').get('id')

    # insert the vote into the database
    query = "INSERT INTO vmas_votes (nid, emailid, userid) VALUES (%s, %s, %s)"
    vote_obj.cur.execute(query, (nid, emailid, userid))
    vote_obj.conn.commit()

    return 'Vote submitted successfully', 200


#sign in
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template('users/signin.html')
    else:
        email = request.form['email']
        password = request.form['password']
        user_obj = user()
        u = user_obj.checkSignedIn(email, password)

        if u:
            session['user'] = u
            nominee_obj = nominee()
            nominee_results_dict = nominee_obj.getVotes()
            if session.get('user').get('role') == 'admin':
                return render_template('admin.html', nominee_results=nominee_results_dict) # take the disabled out after modifying html
            else:
                return render_template('home.html', nominee_results=nominee_results_dict, disabled="")
        else:
            error = 'Invalid email or password.'
            return render_template('signin.html', error=error)

# admin
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    nominee_obj = nominee()
    nominee_results_dict = nominee_obj.getVotes()
    nominee_obj.pk = 'nid'
    vote_obj = vote()

    # post request handling
    if request.method == 'POST':
        nid = request.form.get('nid')

        # delete a nominee
        if nid:
            sql = """DELETE FROM vmas_votes
                WHERE nid = %s;"""        
            vote_obj.cur.execute(sql, nid) # deletes from vote table
            nominee_obj.deleteById(nid) # deletes from nominee table

        # add a nominee
        elif request.form.get('name'):
            nomineename = request.form.get('name')
            nomineecountry = request.form.get('country')
            status = request.form.get('status')
            musicname = request.form.get('music')
            awardcategory = request.form.get('awardCategory')
            nominatedyear = request.form.get('year')
            
            # insert the nominee data into the database
            query = "INSERT INTO vmas_nominee (nomineename, nomineecountry, status, musicname, awardcategory, nominatedyear) VALUES (%s, %s, %s, %s, %s, %s)"

            nominee_obj.cur.execute(query, (nomineename, nomineecountry, status, musicname, awardcategory, nominatedyear))

        # change role of user to admin
        elif request.form.get('username'):
            username = request.form.get('username')
            sql = "UPDATE vmas_user SET role='admin' WHERE username=%s;"
            nominee_obj.cur.execute(sql, (username,))
            nominee_obj.conn.commit()

    # admin page stuff
    if 'user' in session:
        if session.get('user').get('role') == 'admin':
            return render_template('admin.html', nominee_results=nominee_results_dict)
        else:
            return render_template('home.html', nominee_results=nominee_results_dict, disabled="")
    else:
        return render_template('home.html', nominee_results=nominee_results_dict, disabled="disabled")





# used to handle create account and login
@app.route('/users/manage',methods=['GET','POST'])
def manage_user():
    user_obj = user()
    nominee_obj = nominee()

    action = request.args.get('action')
    pkval = request.args.get('pkval')
    if action is not None and action == 'insert':
        d = {}
        d['name'] = request.form.get('name')
        d['email'] = request.form.get('email')
        d['role'] = request.form.get('role')
        d['password'] = hashlib.md5(request.form.get('password').encode('utf-8')).hexdigest()
        user_obj.set(d)
        user_obj.insert()
    if action is not None and action == 'update':
        user_obj.getById(pkval)
        user_obj.data[0]['name'] = request.form.get('name')
        user_obj.data[0]['email'] = request.form.get('email')
        user_obj.data[0]['role'] = request.form.get('role')
        user_obj.data[0]['password'] = hashlib.md5(request.form.get('password').encode('utf-8')).hexdigest()
        user_obj.update()
        
    if pkval is None:
        nominee_results_dict = nominee_obj.getVotes()
        if 'user' in session:
            return render_template('home.html',nominee_results=nominee_results_dict, disabled="")
        else:
            return render_template('home.html',nominee_results=nominee_results_dict, disabled="disabled")
    if pkval == 'new':
        user_obj.createBlank()
        return render_template('users/add.html',obj = user_obj)
    else:
        user_obj.getById(pkval)
        return render_template('users/manage.html',obj = user_obj)


# stuff left over from tylers code
#test setting a session:
@app.route('/set')
def set():
    session['key'] = 'value'
    return 'ok'

#test getting a session:
@app.route('/get')
def get():
    return session.get('key', 'not set')

@app.route('/test')
def test():
    user = 'Tommy'
    return render_template('test.html',username = user)

# endpoint route for static files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)
      
  
if __name__ == '__main__':
   app.run(host='127.0.0.1',debug=True)  



@app.route('/')
def home():
    if request.method == 'GET':
        return render_template('videos.html')
    
    # get the results of the votes
    nominee_obj = nominee()
    nominee_results_dict = nominee_obj.getVotes()

    # disable or enable voting based on whether user is signed in 
    if 'user' in session:
        return render_template('home.html', nominee_results=nominee_results_dict, disabled="")
    else:
        return render_template('home.html', nominee_results=nominee_results_dict, disabled="disabled")



@app.route('/videos')
def view_videos():
    return render_template('videos.html')


