import flask

app = flask.Flask(__name__,
            static_url_path='')
@app.route('/',methods=['GET',])
def home():
    return flask.render_template('start.html')

@app.route('/winning_result',methods=['GET',])
def winning():
    return flask.render_template('result.html')

if __name__ == '__main__':
    app.run()
