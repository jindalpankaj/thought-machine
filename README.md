Thought Machine
---

This is an experimental web-app where user-input thoughts, instead of users, are central entities. New thoughts are matched against all previously entered thoughts using semantic search (done using pre-trained BERT models). Thoughts are initialized using data from Reddit (r/showerthoughts) using PRAW (the Python wrapper for Reddit API). Past similar thoughts are displayed in a textual way for now (planning to work more on visualization aspects using tag-cloud like features).

Made using Python (Flask), HTML (Bootstrap), JavaScript (jQuery), and I am using SQLite as the database to store users and thoughts.


