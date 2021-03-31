from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

class studentrec(db.Model):
    student_id= db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(20), nullable=False)
    last_name= db.Column(db.String(20), nullable=False)
    dob= db.Column(db.String(20), nullable=False)
    amount_due= db.Column(db.Integer, nullable=False)

    def __init__(self, student_id,first_name,last_name,dob,amount_due):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.amount_due = amount_due
 
    def __repr__(self):
        return f"{self.student_id}:{self.amount_due}"

'''@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        amount_due = request.form['amount_due']

        position = request.form['position']
        stud = studentrec(student_id=student_id, name=name, first_name=first_name, last_name = last_name, amount_due=amount_due,dob=dob)
        db.session.add(stud)
        db.session.commit()
        return redirect('/data')



@app.route('/data')
def RetrieveDataList():
    students = studentrec.query.all()
    return render_template('datalist.html',students = students)


@app.route('/data/<int:id>')
def RetrieveSingleEmployee(id):
    employee = studentrec.query.filter_by(employee_id=id).first()
    if employee:
        return render_template('data.html', employee = employee)
    return f"Employee with id ={id} Doenst exist"




@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    employee = studentrec.query.filter_by(employee_id=id).first()
    if request.method == 'POST':
        if employee:
            db.session.delete(employee)
            db.session.commit()
 
            name = request.form['name']
            age = request.form['age']
            position = request.form['position']
            employee = EmployeeModel(employee_id=id, name=name, age=age, position = position)
 
            db.session.add(employee)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Employee with id = {id} Does nit exist"
 
    return render_template('update.html', employee = employee)

    

'''





















@app.route('/', methods= ['POST','GET'])
def ind():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        student_id = request.form['student_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        amount_due = request.form['amount_due']
        stud = studentrec(student_id=student_id, first_name=first_name, last_name = last_name, amount_due=amount_due,dob=dob)
        db.session.add(stud)
        db.session.commit()
        return redirect('/data')
            

        #except:
            #return "Some issue while adding "

    else:
        tasks= studentrec.query.all()
        return render_template('index.html', tasks= tasks)


if __name__ == "__main__":
    app.run(debug=True)


