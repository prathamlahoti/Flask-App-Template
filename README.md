# Flask Application Template

By default __Flask__ doesn't provide some application structure, then we have to create it from scratch. It would be better to get rid of this routine. So, I designed a mundane application structure to proceed to my projects development.
__P.S.__ Unless you're using Flask for web-sites development or small apps this architecture might look redundant. It will be faster to implement your own architecture, than edit this one.

___

#### There are few steps before start deploying the application:

1) Create Virtual Environment And Run It:
```
python -m venv venv
source venv/bin/activate
```

2) Install All Necessary Modules:
```
pip install flask
pip install flask-sqlalchemy
```

3) Clone This Repo
___
#### If all steps above are successfully passed, you could try to run our application:
```
 python3.6 run.py
 ```

#### Open your browser and visit [localhost](127.0.0.1:5000). If u see "Hello, World!", than it looks working.

