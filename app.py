from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('template.html')
if __name__ == '__main__':
   app.run()