from flask import Flask

app=Flask(__name__)

app.secret_key='milan'

import project.com.controller

