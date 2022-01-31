# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
#
# # create a flask instance
# app = Flask(__name__)
# # add database
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///todo.db"
# # secret key
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # initialize the database
# db=SQLAlchemy(app)
#
#
# class ToDo(db.Model):
#     sno = db.Column(db.integer,primary_key=True)
#     title=db.Column(db.string(200),nullable=False)
#     desc=db.Column(db.string(500),nullable=False)
#     date_created=db.Column(db.DateTime,default=datetime.utcnow)
#
#     def __repr__(self):
#         return f"{self.sno} - {self.title}"
#
#
#
#
#
# @app.route('/')
# def hello_world():
#     return render_template("index.html")
#     return "Hello World!"
#
#
# @app.route('/products')
# def products():
#     return "This is my product."
#
#
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask,render_template, request, Response
# from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URL']='mysql://root:23352022@localhost'




@app.route('/')
def hello_world():
    return render_template("index.html")
    # return "Hello World!"

#json example
@app.route('/products', methods = ['POST'])
def products():
    # receive data from user
    json_data = request.json
    value = json_data["id"]
    name = json_data["name1"]
    # what you wat to do with this data
    print("in post" )
    #return " This is my page."
    return json_data, 205  #Response(status=201)

# Path variable example
@app.route('/products1/<id>/<name>', methods = ['POST'])
def products1(id,name):

    print("in post" + id + name)
    return id + name +" This is my page."

# same URL But method type GET
# @app.route('/products', methods = ['GET'])
# def getproducts():
#     # receive data from user
#     json_data = request.json
#     value = json_data["id"]
#     name = json_data["name1"]
#     # what you wat to do with this data
#     print("in get "+  value)
#     return name + " This is my page."


if __name__=="__main__":
    app.run(debug=True)