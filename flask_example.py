from flask import Flask, request, render_template
import json
app = Flask(__name__)

@app.route("/sendUser", methods=["POST"])
def recieveUser():
    user = request.json
    with open("users.json", mode="r") as db:
        try:
            users = json.load(db)
        except ValueError:
            users = []
    with open("users.json", mode="w") as db:
        users.append(user)
        json.dump(users, db, indent=4)
    return "Success"

@app.route("/viewUsers", methods=["GET"])
def showUsers():
    with open("users.json", mode="r") as db:
        try:
            users = json.load(db)
        except ValueError:
            return "No Users in DB"
    return render_template("viewUsers.html", users=users)

if __name__ == "__main__":
    app.run()
