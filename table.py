from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/tables")
def show_tables():
    data = pd.read_csv('static/css/LINE.csv',',')
    return render_template('template.html', tables=[data.to_html(classes='data')], titles=data.columns.values)


if __name__ == "__main__":
    app.run(debug=True)