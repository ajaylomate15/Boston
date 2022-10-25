from flask import Flask,jsonify,request,render_template
import numpy as np
import json
import pickle
import config
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'AjayAjay1504'
app.config['MYSQL_DB'] = 'boston_db'
mysql = MySQL(app)

@app.route("/")
def home_api():
    return render_template('index.html')


@app.route("/predict_price",methods=['GET','POST'])
def predict():

    with open(config.DATA_PATH,'r') as f:
        boston_data = json.load(f)

    with open(config.MODEL_PATH,'rb') as f:
        boston_model = pickle.load(f)

    test_array = np.zeros(len(boston_data['columns'])) # taking len of list of columns i.e  len(list(x.columns))

    data = request.form
    
    test_array[0] = eval(data['CRIM'])
    a = test_array[0]
    test_array[1] = eval(data['ZN'])
    b = test_array[1]
    test_array[2] = eval(data['INDUS'])
    c = test_array[2]
    test_array[3] = eval(data['CHAS'])
    d = test_array[3]
    test_array[4] = eval(data['NOX'])
    e = test_array[4]
    test_array[5] = eval(data['RM'])
    f = test_array[5]
    test_array[6] = eval(data['AGE'])
    g = test_array[6]
    test_array[7] = eval(data['DIS'])
    h = test_array[7]
    test_array[8] = eval(data['RAD'])
    i = test_array[8]
    test_array[9] = eval(data['TAX'])
    j = test_array[9]
    test_array[10] = eval(data['PTRATIO'])
    k = test_array[10]
    test_array[11] = eval(data['B'])
    l = test_array[11]
    test_array[12] = eval(data['LSTAT'])
    m = test_array[12]

    output = boston_model.predict([test_array])

    cursor = mysql.connection.cursor()
    query = 'CREATE TABLE IF NOT EXISTS boston (CRIM VARCHAR(20),ZN VARCHAR(20),INDUS VARCHAR(20),CHAS VARCHAR(20),NOX VARCHAR(20),RM VARCHAR(20),AGE VARCHAR(20),DIS VARCHAR(20),RAD VARCHAR(20),TAX VARCHAR(20),PTRATIO VARCHAR(20),B VARCHAR(20),LSTAT VARCHAR(20),output VARCHAR(20))'
    cursor.execute(query)
    cursor.execute('INSERT INTO boston (CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,output) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(a,b,c,d,e,f,g,h,i,j,k,l,m,output))
    mysql.connection.commit()
    cursor.close()

    return render_template('index1.html',output=output)


if __name__ == "__main__":
    app.run(port=config.PORT_NO)


