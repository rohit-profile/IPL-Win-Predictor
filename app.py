from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

pipe = pickle.load(open('model.pkl', 'rb'))

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad','Bangalore','Mumbai','Indore','Kolkata','Delhi',
'Chandigarh','Jaipur','Chennai','Cape Town','Port Elizabeth',
'Durban','Centurion','East London','Johannesburg','Kimberley',
'Bloemfontein','Ahmedabad','Cuttack','Nagpur','Dharamsala',
'Visakhapatnam','Pune','Raipur','Ranchi','Abu Dhabi',
'Sharjah','Mohali','Bengaluru']


@app.route('/')
def home():
    return render_template("index.html", teams=sorted(teams), cities=sorted(cities))


@app.route('/predict', methods=['POST'])
def predict():

    batting_team = request.form.get('batting_team')
    bowling_team = request.form.get('bowling_team')
    city = request.form.get('city')

    target = int(request.form.get('target'))
    score = int(request.form.get('score'))
    overs = float(request.form.get('overs'))
    wickets = int(request.form.get('wickets'))

    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets = 10 - wickets
    crr = score / overs
    rrr = (runs_left * 6) / balls_left

    input_df = pd.DataFrame({
        'batting_team':[batting_team],
        'bowling_team':[bowling_team],
        'city':[city],
        'runs_left':[runs_left],
        'balls_left':[balls_left],
        'wickets':[wickets],
        'total_runs_x':[target],
        'crr':[crr],
        'rrr':[rrr]
    })

    result = pipe.predict_proba(input_df)

    loss = result[0][0]
    win = result[0][1]

    win_prob = round(win * 100)
    loss_prob = round(loss * 100)

    return render_template(
        'index.html',
        teams=sorted(teams),
        cities=sorted(cities),
        win=win_prob,
        loss=loss_prob,
        batting_team=batting_team,
        bowling_team=bowling_team
    )


if __name__ == "__main__":
    app.run(debug=True)
