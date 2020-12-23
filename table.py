from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/tables")
def show_tables():
    data = pd.read_csv('static/css/LINE.csv',',')
    #data.set_index(['ID'], inplace=True)
    #data.index.id = None
    return render_template('template.html', tables=[data.to_html(classes='data', index=False)], titles=data.columns.values)


if __name__ == "__main__":
    app.run(debug=True)