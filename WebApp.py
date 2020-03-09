from flask import *

from App.RateCalculator import *
from env.config import Config
from forms.VendorDetails import VendorDetailsForm

app = Flask(__name__)
app.config.from_object(Config)
keyList = ["vendor_name",
           "languages",
           "project_type",
           "new_words",
           "low_fuzzies",
           "high_fuzzies",
           "reps",
           "hundred_matches",
           "context_matches",
           "pre_flight_hours",
           "dtp_hours"]

appDict = {key: None for key in keyList}


@app.route('/')
@app.route('/vendor_details', methods=['GET', 'POST'])
def vendor_details():
    form = VendorDetailsForm()

    if request.method == "POST":
        print()
    return render_template('vendor_details.html', form=form)


@app.route('/calculatedRates', methods=['GET'])
def calculate_rates():
    calc = RateCalculator(appDict)
    calc.run()


if __name__ == '__main__':
    app.run(debug=True)
