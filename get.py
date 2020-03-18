from flask import Flask,jsonify,request,render_template
import json
import os

app = Flask(__name__)

languages = [{'name':'Java'},{'name':'CPP'},{'name':'Python'}]
@app.route('/',methods=['GET'])
def test():
    return render_template('hello.html')

@app.route('/lang',methods=['GET'])
def test1():
    return jsonify({'languages':languages})

@app.route('/lang/<string:name>',methods=['GET'])
def test2(name):
    langs= [language for language in languages if language['name']==name]
    return jsonify({'language':langs[0]})

@app.route('/lang',methods=['POST'])
def test3():
    temp = request.get_data()
    temp  = json.loads(temp)
    with open('name.txt','a') as f:
        f.write(str(temp))
        f.write('\n')
    print(temp)
    #language = {'name': request.json['name']}
    global languages
    languages.append(temp)
    return jsonify({'languages':languages})

if(__name__=='__main__'):
      app.run(host='0.0.0.0', port=80, debug=True)

      