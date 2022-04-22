from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    favorite_pizza = ["Pepperoni","Cheese","Mashroom"]
    return render_template("index.html", favorite_pizza = favorite_pizza)

@app.route('/user/<name>')

def user(name):
 return render_template("user.html",user_name= name)
    
#create custom Error Pages

#Invalid URL
@app.errorhandler(404)

def page_not_found(e):
     return render_template("404.html"), 404


#Internal Server URL
@app.errorhandler(500)

def page_not_found(e):
     return render_template("500.html") ,500

if __name__ == '__main__':
    app.run(debug=True)