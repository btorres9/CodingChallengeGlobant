from flask import Flask,jsonify,request
from insertdata import insert_data

app=Flask(__name__)

@app.route("/")
def root():
    insert_data()
    return "Hello Word!"

@app.route("/user/<username>")
def getusername(username):
    parametro1=request.args.get('parametro1')
    return f'Hola mi nombre es {username},{parametro1}'

@app.route("/test",methods=['POST'])
def insert():
    data=request.get_json()
    x=jsonify(data)
    # insert_data()
    return (x)

# if __name__ == "__main__": 
#     app.run(debug=True)
