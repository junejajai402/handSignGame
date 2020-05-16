from pymongo import MongoClient
client = MongoClient()
#client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017')

db = client['pymongo_test']
#posts=db.testCollection

posts = db.posts
#post_data = {
#    'title': 'Python and MongoDB',
#    'content': 'PyMongo is fun, you guys',
#    'author': 'Scott',
#    'age': 1
#}
#result = posts.insert_one(post_data)
#print('One post: {0}'.format(result.inserted_id))

#post_1 = {
#    'title': 'Python and MongoDB',
#    'content': 'PyMongo is fun, you guys',
#    'author': 'Scott',
#    'age': 3
#}
#post_2 = {
#    'title': 'Virtual Environments',
#    'content': 'Use virtual environments, you guys',
#    'author': 'Scott',
#    'age': 10
#}
#post_3 = {
#    'title': 'Learning Python',
#    'content': 'Learn Python, it is easy',
#    'author': 'Bill',
#    'age': 20
#}

#new_result = posts.insert_many([post_1, post_2, post_3])
#print('Multiple posts: {0}'.format(new_result.inserted_ids))

#print(new_result)

bills_post = posts.find({'age':{'$gte':10}})
#print(bills_post)
for x in bills_post:
    print(x)
