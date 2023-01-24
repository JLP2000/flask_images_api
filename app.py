from flask import Flask, jsonify, request, render_template, flash, redirect
from flask_cors import CORS
from flask_mail import Mail, Message
from controllers import images
from werkzeug import exceptions
from forms import LoginForm, CreatePostForm
import requests

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'testjosh1507'
app.config['MAIL_PASSWORD'] = 'wqjhgpebghrpkljo'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

sign_up_bool = False


app.config['SECRET_KEY'] = 'you-will-never-guess'
msg = Message("Welcome to Image API", sender="testjosh1507@gmail.com", recipients=["josh15phan@gmail.com"])
# mail.send(msg)
@app.route("/", methods=['GET', 'POST'])
def welcome():

    form = LoginForm()
    # print(sign_up_bool)
    if form.validate_on_submit():
        flash('Sign up requested for email {}'.format(form.email.data))
        msg.add_recipient(form.email.data)
        
        global sign_up_bool
        sign_up_bool = True
        return redirect("/")
        
    return render_template("email.html", images=image()[0].get_json(), form=form, is_signed_up=sign_up_bool)

@app.route("/create", methods=["GET", "POST"])
def createForm():
    form = CreatePostForm()

    if form.validate_on_submit():
        flash('Title {}'.format(form.title.data))
        flash('Description {}'.format(form.description.data))
        flash('URL {}'.format(form.url.data))
        code = requests.post('http://127.0.0.1:5000/api/images', json={"title": form.title.data, "description": form.description.data, "url": form.url.data}) 
        print(code)
        
     
        return redirect("/")

    return render_template("create_post.html", form=form)

    

@app.route("/api")
def api_main():
    return "Welcome to the images API"

@app.route("/api/images", methods = ["GET", "POST"])
def image():
    fns = {
        'GET': images.index,
        'POST': images.create
    }

    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route("/api/images/<int:image_id>", methods = ["GET", "PUT", "DELETE"])
def image_handler(image_id):
    fns = {
        'GET': images.show,
        'PUT': images.update,
        'DELETE': images.destroy        
    }

    resp, code = fns[request.method](request, image_id)
    print(resp)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def error_404(err):
    return jsonify({"message": f"Oops.. {err}"}), 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
