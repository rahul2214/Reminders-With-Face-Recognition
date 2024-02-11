from flask import Flask, render_template, request 
import face_recognition
import cv2
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12670554:rkxGaIVEjx@sql12.freesqldatabase.com/sql12670554'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Task(db.Model):
    _tablename_ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    task = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date)


with app.app_context():
    db.create_all()

cap = cv2.VideoCapture(0)



@app.route('/')
def index():
    tasks = Task.query.all()
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
             
             print("No faces detected in the frame.")

        else:
             
             face_encodings_cam = face_recognition.face_encodings(rgb_frame)[0]

        match_1 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_1)   
        match_2 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_2)    
        match_3 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_3)    
        match_4 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_4)    



        if match_1[0]:
            name = "architha"
            return render_template('index.html', name = name)
        
        elif match_2[0]:
            name = "rahul"
            return render_template('index.html', name = name)
        
        elif match_3[0]:
            name = "prabhas"
            return render_template('index.html', name = name)
        
        elif match_4[0]:
            name = "bhanu"
            return render_template('index.html', name = name)
        
        
        
        


@app.route('/add_task', methods=['GET','POST'])
def sucess():
       
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
             
             print("No faces detected in the frame.")

        else:
             
             face_encodings_cam = face_recognition.face_encodings(rgb_frame)[0]

        match_1 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_1)    
        match_2 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_2)    
        match_3 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_3)    
        match_4 = face_recognition.compare_faces(face_encodings_cam, face_encodings_img_4)    



      
        if match_1[0]:
            username = "architha"
            name = request.form.get('username')
            task = request.form.get('task')
            date = request.form.get('date')
            
            if name == username :
              new_task = Task(name=name, task=task, date=date)
              db.session.add(new_task)
              db.session.commit()

              return render_template('sucess.html')

            else :
                return render_template('failure.html')

        
        elif match_2[0]:
   
           username = "rahul"
           name = request.form.get('username')
           task = request.form.get('task')
           date = request.form.get('date')
            
            
           if name == username :
              new_task = Task(name=name, task=task, date=date)
              db.session.add(new_task)
              db.session.commit()

              return render_template('sucess.html')

           else :
                return render_template('failure.html')


       
        elif match_3[0]:
   
           username = "prabhas"
           name = request.form.get('username')
           task = request.form.get('task')
           date = request.form.get('date')
            
            
           if name == username :
              new_task = Task(name=name, task=task, date=date)
              db.session.add(new_task)
              db.session.commit()

              return render_template('sucess.html')

           else :
                return render_template('failure.html')


           
        elif match_4[0]:
   
           username = "Bhanu"
           name = request.form.get('username')
           task = request.form.get('task')
           date = request.form.get('date')
            
            
           if name == username :
              new_task = Task(name=name, task=task, date=date)
              db.session.add(new_task)
              db.session.commit()

              return render_template('sucess.html')

           else :
                return render_template('failure.html')

      
        else:
            print("Invalid")


if __name__ == '__main__':
    app.run(debug = True , port = 8080)
