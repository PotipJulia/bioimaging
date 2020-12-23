from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
app = Flask(__name__)


@app.route('/myroute', methods=['POST'])
def myroute():
   flask_file = request.files['file']
   if not flask_file:
      return 'Upload a CSV file'

   data = []
   stream = codecs.iterdecode(flask_file.stream, 'utf-8')
   for row in csv.reader(stream, dialect=csv.excel):
      if row:
         data.append(row)

   return jsonify(data)

@app.route('/')
def home():
   return render_template('template.html')
if __name__ == '__main__':
   app.run()