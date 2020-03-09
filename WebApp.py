from flask import *
import logging

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
    invalid_input = {}

    if request.method == "POST":
        appDict.update(vendor_name=form.vendor_name.data)
        appDict.update(languages=form.languages.data)
        appDict.update(project_type=form.project_type.data)
        appDict.update(new_words=form.new_words.data)
        appDict.update(low_fuzzies=form.low_fuzzies.data)

        # TODO: Cleanup
        # Remove this for loop when the app is completed
        # This is solely for testing purposes - We should be throwing an error
        # if the appDict is not complete with all values
        for key, value in appDict.items():
            if value is None:
                appDict[key] = 1
        ###############################################

        if any(value is None for value in appDict.values()):
            invalid_input.update(missing_inputs='All fields are required - Make sure you have populated all fields')
            return render_template('vendor_details.html', form=form, invalid_input=invalid_input)
        else:
            calculator = RateCalculator(appDict)
            calculator.validate_input()
            if not calculator.vendor_languages_check:
                invalid_input.update(languages='"{0}" is not in our list of valid languages.'.format(form.languages.data))
                return render_template('vendor_details.html', form=form, invalid_input=invalid_input)
            calculator.run()
            return render_template('vendor_details.html', form=form, calc_results=calculator.language_costs)
    else:
        return render_template('vendor_details.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
