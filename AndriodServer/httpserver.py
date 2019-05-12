import os
import sys
import copy
from tornado import ioloop,web
import pymysql
import json

host="127.0.0.1"
user="root"
password="123456"
database_name="dogs"

# use root to connect database
def database_connect():
  return pymysql.connect(host=host,user=user,password=password,db=database_name)

# init database 
def init_database():
  db = None
  try:
    db = database_connect()
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS recordings")
    cursor.execute("DROP TABLE IF EXISTS users")
    sql = """CREATE TABLE users (
      id CHAR(20) PRIMARY KEY,
      password CHAR(50),
      email CHAR(50))
      character set = utf8;"""
    cursor.execute(sql)
    sql = """CREATE TABLE recordings (
      id CHAR(20) NOT NULL,
      recording_id INT,
      date CHAR(20),
      topic CHAR(40),
      description TEXT,
      FOREIGN KEY(id) REFERENCES users(id),
      PRIMARY KEY(id,recording_id))
      character set = utf8;"""
    cursor.execute(sql)
  except Exception as e:
    print (e)
    print ("Database init failed!")
    sys.exit(1)
  finally:
    if db is not None:
      db.close()

def user_add(user_id,user_password,email=None):
  db = None
  try:
    db = database_connect()
    cursor = db.cursor()
    sql = "Insert into users values ('%s','%s','%s')" % (user_id,user_password,email)
    cursor.execute(sql)
    db.commit()
    print("user '%s' register sussful!" % (user_id))
    return "user '%s' register sussful!" % (user_id)
  except Exception as e:
    db.rollback()
    print(e)
    print("user '%s' register failed:%s" % (user_id,e))
    return "user '%s' register failed:%s" % (user_id,e)
  finally:
    if db is not None:
      db.close()

def user_login(user_id,user_password):
  db = None
  results = None
  try:
    db = database_connect()
    cursor = db.cursor()
    sql = "select * from users where id = '%s' AND password = '%s'" % (user_id,user_password)
    cursor.execute(sql)
    results = cursor.fetchall()
  except Exception as e:
    print(e)
    print("user '%s' login failed: %s" % (user_id,e))
    return "user '%s' login failed: %s" % (user_id,e)
  finally:
    if db is not None:
      db.close()
  if len(results) == 0:
    print( "username '%s' or password is wrong!" % (user_id))
    return False
    #return "username '%s' or password is wrong!" % (user_id)
  elif len(results) == 1:
    print("user '%s' login successful!" % (user_id))
    return True
    #return "user '%s' login successful!" % (user_id)
  else:
    return False

class LoginHandler(web.RequestHandler):
  def data_received(self,chunk):
    pass

  def get(self):
    self.set_header("Content-Type","application/json")
    data = {"status":"yes"}
    ret_json = json.dumps(data,sort_keys=True,indent=4,ensure_ascii=False)
    self.write(ret_json)

  def post(self):
    data = json.loads(self.request.body.decode('utf-8'))
    detail = None
    
    if data["command"] == "register":
      detail = user_add(data["username"],data["password"],data["email"])
    elif data["command"] == "login":
      detail = user_login(data["username"],data["password"])
    
    self.set_header("Content-Type","application/json")
    data = {"status":"yes","detail":detail}
    ret_json = json.dumps(data,indent=4,ensure_ascii=False)
    self.write(ret_json)

class FileHandler(web.RequestHandler):
  def data_received(self,chunk):
    pass
  
  def get(self,arg):
    filename = arg[1:]
    try:
      file_content = open(os.path.join(os.path.dirname(__file__),'files',filename),'rb')
    except IOError:
      self.set_status(404)
      return
    self.set_header('Content-Type','application/octet-stream')
    self.add_header('Content-Dispostion','attachment; filename=' + filename)
    self.finish(file_content.read())

  def post(self,arg):
    if self.request.files:
      upload_path = os.path.join(os.path.dirname(__file__),'files')
      filename = self.request.files['file'][0]['filename']
      file_content = self.request.files['file'][0]['body']
      file_path = os.path.join(upload_path,filename)
      with open(file_path,'wb') as upload:
        upload.write(file_content)
      detail = True
    else:
      detail = False  
    self.set_header("Content-Type","application/json")
    data = {"status":"yes","detail":detail}
    ret_json = json.dumps(data,indent=4,ensure_ascii=False)
    self.write(ret_json)

def make_app():
  return web.Application([(r"/login",LoginHandler),(r"/files(/.+)?",FileHandler),])

def main():
  app = make_app()
  app.listen(8888)
  #init_database()
  print("start serving...")
  ioloop.IOLoop.current().start()

if __name__ == '__main__':
  main()

