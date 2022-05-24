# Spam-Detection-Flask deploy

การทำ machine learning แยกข้อความ sms ที่เป็น spam

## model เทรนด้วยเทคนิค tf-idf และใช้ classification ด้วย SVM
> https://github.com/serversuck/spam/blob/main/spammodel.pkl



## การติดตั้ง
> git clone https://github.com/serversuck/spam.git
> pip install -r requirements.txt

## Run flask framework
> python app.py

## การทดสอบแบบ html form
http://localhost:5000

## การทดสอบแบบAPI
http://localhost:5000/api?msg=เงินกู้ของท่านได้รับการพิจารณาแล้ว

## Heroku deploy
> heroku login

> heroku git:remote -a myapp
 
> git add .; git commit -m "add requirements.txt"; git push heroku master
