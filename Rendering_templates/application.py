from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def introducing():
    return 'Welcome To Rendering_Templates EXAMPLE!'

@app.route('/aomg')
def aomg():
    name = u'Which two rappers represent AOMG?'
    rapper_list = [u'Jay Park', u'Simon Dominic']
    return render_template('rapper_label.html', name=name, rapper_list=rapper_list)

@app.route('/jm')
def jm():
    name = u'Which two rappers represent JUST MUSIC?'
    rapper_list = [u'SWINGS', u'GIRIBOY']
    return render_template('rapper_label.html', name=name, rapper_list=rapper_list)

@app.route('/mkit_rain')
def mkit_rain():
    name = u'Which two rappers represent MKIT RAIN?'
    rapper_list = [u'BLOO', u'NAFLA']
    return render_template('rapper_label.html', name=name, rapper_list=rapper_list)

if __name__ == "__main__":
    app.run(debug = True)
