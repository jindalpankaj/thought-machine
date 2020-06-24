from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime as dt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import sys # for printing to std.err only for debugging purposes
# import reddit

import semantic_search as ss

# setting up the SQLite db named thought_db
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'thought_db_2.db?check_same_thread=False')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


# creating table User in thought_db
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(120), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username

# creating table Thought in thought_db
class Thought(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thought_text = db.Column(db.String(), nullable=False)
    # TODO: create timestamp variable, and foreign key UserID after creating the User table (learn table-relationships)

    def __repr__(self):
        return self.thought_text


# creating all tables in the DB
# db.create_all()

# Populating the DB with initial data from r/showerthoughts
# r1 = reddit.DataFromReddit()
# post_list = r1.getTopPosts("showerthoughts")
# len(post_list)
#
# for t in post_list:
#     db.session.add(Thought(thought_text=t))
#
# db.session.commit()



# define a decorator for home route
@app.route("/", methods=['GET', 'POST'])
def get_player_name():
    return render_template("index.html")


@app.route("/second_page", methods=['POST'])
def show_second_page():
    # print("In show_second_page beginning... ")
    print("\n Querying previous thoughts started...", file=sys.stderr)
    prev_thoughts = Thought.query.all()
    print("\n Querying previous thoughts ended...", file=sys.stderr)
    prev_thoughts = [w.thought_text for w in prev_thoughts]
    print("\n list of previous thoughts generated...", file=sys.stderr)
    
    new_thought = request.form['tb1_name']
    print("\n new thought received from previous POST request...", file=sys.stderr)
    
    # add time of entering thought with dt.now() to get timestamp
    # Here we can store this in DB or do other processing with the entered thought.
    db.session.add(Thought(thought_text=new_thought))
    print("\n new thought added to the db session...", file=sys.stderr)    
    
    db.session.commit()
    print("\n new thought committed to the db session...", file=sys.stderr)    
    # print(new_thought)

    # num_similar_thoughts = 5 # can change it later or ask the value from user
    threshold_similarity = 0.75 # because number returns even unrelated thoughts
    
    print("\n About to call similar thoughts function now...", file=sys.stderr)    
    similar_thoughts = ss.getSimilarSentences(new_thought, prev_thoughts, threshold_similarity)
    
    print("\n Out of similar thoughts function now, and back to app.py...", file=sys.stderr)    
    # type(similar_thoughts)
    # similar_thoughts = prev_thoughts
    # print(similar_thoughts)
    # Here we can show further pages which show matching thoughts.
    # print("HERe")
    return render_template("second_page.html", new_thought=new_thought, prev_thoughts=similar_thoughts)


# Do not need the below now. Sending data using html form POST instead of jquery!
# @app.route("/_receivedata", methods=['POST'])
# def receive_data():
#     # Here you can store in DB or do other processing with the entered thought.
#     print(request.form['new_thought'])
#     return "OK"


# Running the app
if __name__ == "__main__":
    app.run(port=5000)


# TODO:
# 1. Improve search; Maybe use clustering, or BERT?
# 2. Organize this file - move DB related code in a separate file
# 3. Move the getSimilarSentence function in a separate file (already exists, update it) - Same as where Search would be.
# 4. Incorporate fields other than just thought in the DB. Datetime.
# 5. Create user sign in system, and releated UI changes.