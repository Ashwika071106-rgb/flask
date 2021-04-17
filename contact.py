from flask import Flask, jsonify, request

#the constructor of this class Flask that we imported takes the name of the current module,
#stored in __name__ as an argument and the variable app is now a Flask object.
contact = Flask(__name__)

tasks = []

@contact.route("/add-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    tasks = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('Contact', ""),
        'done': False
    }
    
    tasks.append(task)
    return jsonify({
        "status":"success",
        #converting the message to a json object and then showing it.
        #We are doing it because most of the time the data we get is in a Json format.
        "message": "Task added succesfully!" 
    })

#create a get method to see all the available tasks.
@contact.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    })

#to run our web application.
if (__name__ == "__main__"):
    #we are keeping debug=True so that the server will reload every time you make some change to the code
    contact.run(debug=True)