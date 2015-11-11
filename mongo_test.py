__author__ = 'Tobias'

from pymongo import MongoClient
client = MongoClient()
db = client.test_database
posts = db.posts
import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

post_id = posts.insert_one(post).inserted_id

post = {"author": "Mike",
        "video": "http://youtu.be/45845345",
        "tags": ["mongodb", "java", "pymongo"],
        "date": datetime.datetime.utcnow()}

post_id = posts.insert_one(post).inserted_id

#print(posts.find_one())

posts_found = posts.find({"video": "http://youtu.be/45845345"})
for p in posts_found:
    print(p)

#print(posts.find_one({"tags": "python"}))

posts.find_one({"_id": post_id})

