from flask import Flask
import ulid
import json

app = Flask(__name__)

@app.route('/')
def get_id():
    arr = []
    res = {}
    res['unique_id'] = ulid.new().str
    arr.append(res)
    return json.dumps(arr)

@app.route('/multiple/<int:nb>')
def get_multiple_id(nb):
    arr = []
    try: 
        if int(nb):
            for i in range(nb):
                res = {}
                res['unique_id'] = ulid.new().str
                arr.append(res)
    except:
            res = {}
            res['unique_id'] = 'not a number'
            arr.append(res)
    return json.dumps(arr)




if __name__ == "__main__":
    app.run(host='0.0.0.0',port="80")

