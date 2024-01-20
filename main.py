from flask import Flask, render_template, send_file, request, json

app = Flask(__name__)
#hgvhgfvhgcvhgc


@app.route('/')
def deliver_home_page_to_user():
  return render_template('home.html')



@app.route('/contact')
def deliver_contact_page_to_user():
  return render_template('Contact.html')


@app.route('/policy')
def deliver_policy_page_to_user():
  return render_template('policy.html')


@app.route('/tasksearch')
def deliver_tasksearch_page_to_user():
  return render_template('tasksearch.html')

@app.route('/message?#')
def deliver_message_page_to_user():
  return render_template('message.html')

@app.route('/register')
def deliver_register_page_to_user():
  return render_template('register.html')


@app.route('/cemessage?#')
def deliver_profile1_page_to_user():
  return render_template('profile1.html')


@app.route('/kmmessage?#')
def deliver_profile2_page_to_user():
  return render_template('profile2.html')



@app.route('/jdmessage?#')
def deliver_profile3_page_to_user():
  return render_template('profile3.html')

@app.route('/login')

def deliver_profile3_page_to_user():
  return render_template('login.html')

@app.route('/login' , methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    if username and password:
        return json.dumps({'validation': validateUser(username, password)})
    return json.dumps({'validation': False})



def validateUser(username, password):
    return True



# ---------------- BOOTSTRAP STUFF ----------------

@app.route('/css/mdb.min.css')
def bootstrap_css():
   return send_file('Hackathon/mdbootstrap/css/mdb.min.css')

@app.route('/plugins/css/all.min.css')
def bootstrap_plugin_css():
   return send_file('Hackathon/mdbootstrap/plugins/css/all.min.css')

@app.route('/js/mdb.min.js')
def bootstrap_js():
   return send_file('Hackathon/mdbootstrap/js/mdb.min.js')

@app.route('/plugins/js/all.min.js')
def bootstrap_plugin_js():
   return send_file('Hackathon/mdbootstrap/plugins/js/all.min.js')

app.debug = True
app.run(port=5000)

