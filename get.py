from flask import Flask,jsonify,request

app = Flask(__name__)

languages = [{'name':'Java'},{'name':'CPP'},{'name':'Python'}]

@app.route('/',methods=['GET'])
def test():
    return jsonify({'message':'Hello World'})

@app.route('/lang',methods=['GET'])
def test1():
    return jsonify({'languages':languages})

@app.route('/lang/<string:name>',methods=['GET'])
def test2(name):
    langs= [language for language in languages if language['name']==name]
    return jsonify({'language':langs[0]})

if(__name__=='__main__'):
    app.run(debug=True)