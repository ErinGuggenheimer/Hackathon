from flask import Flask, render_template, send_file

app = Flask(__name__)



@app.route('/')
def deliver_home_page_to_user():
  return render_template('home.html')


@app.route('/tasksearch')
def deliver_tasksearch_page_to_user():
  return render_template('tasksearch.html')-

@app.route('/message')
def deliver_message_page_to_user():
  return render_template('message.html')

@app.route('/register')
def deliver_register_page_to_user():
  return render_template('register.html')


@app.route('/login')
def deliver_login_page_to_user():
  return render_template('login.html')



# ---------------- BOOTSTRAP STUFF ----------------

@app.route('/css/mdb.min.css')
def bootstrap_css():
   return send_file('./mdbootstrap/css/mdb.min.css')

@app.route('/plugins/css/all.min.css')
def bootstrap_plugin_css():
   return send_file('./mdbootstrap/plugins/css/all.min.css')

@app.route('/js/mdb.min.js')
def bootstrap_js():
   return send_file('./mdbootstrap/js/mdb.min.js')

@app.route('/plugins/js/all.min.js')
def bootstrap_plugin_js():
   return send_file('./mdbootstrap/plugins/js/all.min.js')

app.debug = True
app.run(port=5000)