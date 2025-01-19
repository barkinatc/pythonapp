import os
from flask import Flask, render_template, redirect
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from classes import *  


app = Flask(__name__)
app.config.update(dict(SECRET_KEY='yoursecretkey'))


import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    # MongoDB bağlantı URI'sini ortam değişkeninden al
    mongo_uri = os.getenv("MONGO_URI", "mongodb://root:I1U88AfsUt@mongodb-0.mongodb-headless.default.svc.cluster.local:27017,mongodb-1.mongodb-headless.default.svc.cluster.local:27017,mongodb-2.mongodb-headless.default.svc.cluster.local:27017/admin?replicaSet=rs0")

    # MongoDB'ye bağlan
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    db = client['TaskManager']

    # Bağlantıyı test et
    client.server_info()
    print(f"MongoDB bağlantısı başarılı! {mongo_uri}")

except ConnectionFailure as e:
    print(f"MongoDB bağlantısı başarısız. Hata: {e}")
    exit(1)




if db.settings.count_documents({'name': 'task_id'}) <= 0:
    print("task_id bulunamadı, oluşturuluyor...")
    db.settings.insert_one({'name': 'task_id', 'value': 0})


def updateTaskID(value):
    task_id = db.settings.find_one({'name': 'task_id'})['value']
    task_id += value
    db.settings.update_one(
        {'name': 'task_id'},
        {'$set': {'value': task_id}}
    )


def createTask(form):
    title = form.title.data
    priority = form.priority.data
    shortdesc = form.shortdesc.data
    task_id = db.settings.find_one({'name': 'task_id'})['value']
    
    task = {'id': task_id, 'title': title, 'shortdesc': shortdesc, 'priority': priority}
    db.tasks.insert_one(task)
    updateTaskID(1)  
    return redirect('/')


def deleteTask(form):
    key = form.key.data
    title = form.title.data

    if key:
        db.tasks.delete_many({'id': int(key)})
    else:
        db.tasks.delete_many({'title': title})

    return redirect('/')


def updateTask(form):
    key = form.key.data
    shortdesc = form.shortdesc.data
    
    db.tasks.update_one(
        {"id": int(key)},
        {"$set": {"shortdesc": shortdesc}}
    )
    return redirect('/')


def resetTask(form):
    db.tasks.drop() 
    db.settings.drop()  
    db.settings.insert_one({'name': 'task_id', 'value': 0}) 
    return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def main():
    
    cform = CreateTask(prefix='cform')
    dform = DeleteTask(prefix='dform')
    uform = UpdateTask(prefix='uform')
    reset = ResetTask(prefix='reset')

   
    if cform.validate_on_submit() and cform.create.data:
        return createTask(cform)
    if dform.validate_on_submit() and dform.delete.data:
        return deleteTask(dform)
    if uform.validate_on_submit() and uform.update.data:
        return updateTask(uform)
    if reset.validate_on_submit() and reset.reset.data:
        return resetTask(reset)

   
    docs = db.tasks.find()
    data = [doc for doc in docs]  

    return render_template('home.html', cform=cform, dform=dform, uform=uform, data=data, reset=reset)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
