from flask import Flask, redirect, url_for, render_template, request
import sqlite3


app=Flask(__name__)
@app.route('/')
def display():
    return render_template('first.html')

@app.route('/index', methods =['POST'])
def display2():
    if request.method=='POST':
        a= request.form['n1']
    return render_template('index,html', data=a)

@app.route('/<int:d>')
def home(d):
    if (d%2)==0:
        return "%s is an even number"%d
    else:
        return "%s is an odd number"%d

@app.route('/t1', methods=['POST'])
def firsttask():
    if request.method=='POST':
        a1=int(request.form['n11'])
        a2 = int(request.form['n2'])
        a3 = int(request.form['n3'])
        a4 = int(request.form['n4'])
        a5 = int(request.form['n5'])
        a6 = int(request.form['n6'])
        b=[]
        b.append(a1)
        b.append(a2)
        b.append(a3)
        b.append(a4)
        b.append(a5)
        b.append(a6)
        h=[]
        for i in b:
            if i%2 !=0:
                h.append(i)
        return render_template('task1.html', data1=h)


@app.route('/t2', methods=['POST'])
def secondtask():
    if request.method=='POST':
        s1=int(request.form['a11'])
    if(s1%4==0)and (s1%3==0):
        a= "the number is divisible by 3 and 4"
    elif (s1%4==0):
        a= "the number is divisible by 4"
    elif (s1%3==0):
        a='the number is divisible by 3'
    else:
        a="the number is not divisible by 3 and 4"
    return render_template('task2.html', answer=a)

@app.route('/t3', methods=['POST'])
def thirdtask():
    if request.method=='POST':
        s3 = int(request.form['s2'])
    x=[]
    for i in range(s3+1):
        x.append(i*i)
    return render_template('task3.html', answer2=x)


@app.route('/t4', methods=['POST'])
def fourthtask():
    if request.method == 'POST':
        s5= request.form['s4']
    count=0
    count1=0
    for i in s5:
       if i=='m':
           count= count+1
    for j in s5:
        if j=='a':
            count1= count1+1

    return render_template('first.html', answer3=count, answer4=s5, answer5=count1)

@app.route('/t5', methods=['POST'])
def fifthtask():
    if request.method=='POST':
        b3=int(request.form['b1'])
        b4= int(request.form['b2'])
    start=b3
    end=b4
    arr=[]
    for i in range(start,end+1):
        if i%5==0:
            arr.append(i)
    return render_template('task5.html', answer6=arr)


@app.route('/third')
def third():
    return redirect(url_for('home', d='JOJO'))

@app.route('/img')
def imagetask():
    return render_template('imagetask.html')

@app.route('/database')
def sqldisplay():
    return render_template('sqlite3.html')

@app.route('/database',methods=['POST'])
def sqlite():
    if request.method=='POST':
        roll=int(request.form['db1'])
        name=request.form['db2']
        age= int(request.form['db3'])
        conn=sqlite3.connect('student.db')
        #conn.execute("create table student(rollnumber INT, name TEXT, age INT)")
        conn.execute("insert into student values(?,?,?)",(roll,name,age))
        conn.commit()
        #print("Values inserted successfully")
        conn.close()
    return ("Inserted Successfully")

@app.route('/table', methods =['GET'])
def sqltabledisplay():
    if request.method=='GET':
        conn=sqlite3.connect('student.db')
        display= conn.execute("select * from student")
    return render_template('displaytable.html', sql=display)

@app.route('/task1', methods =['GET'])
def sqlTask1():
    if request.method=='GET':
        conn=sqlite3.connect('student.db')
        display1= conn.execute("select * from student where age >= 20")
    return render_template('sqlTask1.html', sqlT1=display1)

@app.route('/task2', methods =['GET'])
def sqlTask2():
    if request.method=='GET':
        conn=sqlite3.connect('student.db')
        display1= conn.execute("select * from student where rollnumber between 5 and 10")
    return render_template('sqlTask2.html', sqlT2=display1)


@app.route('/task3', methods =['GET'])
def sqlTask3():
    if request.method=='GET':
        conn=sqlite3.connect('student.db')
        display1= conn.execute("select * from student order by name")
    return render_template('sqlTask3.html', sqlT3=display1)

@app.route('/task4', methods =['GET'])
def sqlTask4():
    if request.method=='GET':
        conn=sqlite3.connect('student.db')
        display1= conn.execute("select * from student where name like 's%n'")
    return render_template('sqlTask4.html', sqlT4=display1)

@app.route('/task5', methods =['GET'])
def sqlTask5():
    if request.method=='GET':
        conn=sqlite3.connect('student.db')
        display1= conn.execute("select * from student where rollnumber %2 =0")
    return render_template('sqlTask5.html', sqlT5=display1)





if __name__ == '__main__':
    app.run(debug=True)
