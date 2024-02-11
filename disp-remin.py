import face_recognition
import cv2
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import ssl

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12670554:rkxGaIVEjx@sql12.freesqldatabase.com/sql12670554'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_POOL_SIZE'] = 10 


db = SQLAlchemy(app)

class Model(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    task = db.Column(db.String(200))
    date = db.Column(db.Date)

cap = cv2.VideoCapture(0)

@app.route('/', methods=['GET'])
def face_recognition_api():
    
    if request.method == 'GET':
        
        image_1 = face_recognition.load_image_file("ref.jpg")     
        face_locations_img_1 = face_recognition.face_locations(image_1)
        if face_locations_img_1:
          face_encodings_img_1 = face_recognition.face_encodings(image_1, face_locations_img_1)
        else :
         print('face not detected')


        image_2 = face_recognition.load_image_file("ref1.jpg")
        face_locations_img_2 = face_recognition.face_locations(image_2)
        if face_locations_img_2:
          face_encodings_img_2 = face_recognition.face_encodings(image_2, face_locations_img_2)
        else :
          print('face not detected')   


        image_3 = face_recognition.load_image_file("ref2.jpg")
        face_locations_img_3 = face_recognition.face_locations(image_3)
        if face_locations_img_3:
          face_encodings_img_3 = face_recognition.face_encodings(image_3, face_locations_img_3)
        else :
          print('face not detected')   


        image_4 = face_recognition.load_image_file("ref3.jpg")
        face_locations_img_4 = face_recognition.face_locations(image_4)
        if face_locations_img_4:
          face_encodings_img_4 = face_recognition.face_encodings(image_4, face_locations_img_4)
        else :
          print('face not detected')

        while True:
          ret, frame = cap.read()
          face_locations_cam = face_recognition.face_locations(frame)

          rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

          if len(face_locations_cam) == 0:
            
            message = 'no faces detected in the frame'
            return jsonify(message)
          else:
            face_encodings_cam = face_recognition.face_encodings(rgb_frame)[0]
        
          match_1 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_1)
          match_2 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_2)    
          match_3 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_3)    
          match_4 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_4)  


          if match_1[0]:
            name = "architha"
            current_date = datetime.now().date()
            data = Model.query.filter_by(name="architha", date=current_date).with_entities(Model.task).all()
            msg = "You have no reminders for today" if not data else None
            data_list = [task[0] for task in data]
            if data_list :
              
              return jsonify("Hello, {}".format(name), data_list)
               
            else  :
              return jsonify(msg)


          elif match_2[0]:
            name = "Rahul"
            current_date = datetime.now().date()
            data = Model.query.filter_by(name="Rahul", date=current_date).with_entities(Model.task).all()
            msg = "You have no reminders for today" if not data else None
            data_list = [task[0] for task in data]
            if data_list :
              return jsonify("Hello, {}".format(name), data_list)
            else  :
              return jsonify(msg)
           

          elif match_3[0]:
            name = "prabhas"
            current_date = datetime.now().date()
            data = Model.query.filter_by(name="prabhas", date=current_date).with_entities(Model.task).all()
            msg = "You have no reminders for today" if not data else None
            data_list = [task[0] for task in data]
            if data_list :
              return jsonify("Hello, {}".format(name), data_list)
            else  :
              return jsonify(msg)
              

          elif match_4[0]:
            name = "bhanu"
            current_date = datetime.now().date()
            data = Model.query.filter_by(name="bhanu", date=current_date).with_entities(Model.task).all()
            msg = "You have no reminders for today" if not data else None
            data_list = [task[0] for task in data]
            if data_list :
              return jsonify("Hello, {}".format(name),"\n", data_list)
            else  :
              return jsonify(msg)
            
          else :
            msg = "you are not a valid user "
            return jsonify(msg)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)

