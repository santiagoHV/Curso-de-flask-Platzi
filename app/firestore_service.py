import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials)

if (not len(firebase_admin._apps)):
  cred = credentials.ApplicationDefault()
  firebase_admin.initialize_app(cred, {
    'projectId': 'your-project-id',
  })

db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_todos(user_id):
    return db.collection('users')\
        .document(user_id).collection('todos').get()