from flask import *

from RateCalculator import *
from env.config import Config
from forms.VendorDetails import VendorDetailsForm

app = Flask(__name__)
app.config.from_object(Config)

validVendors = ["LB", "LB+MOR", "TDC+MOR", "LB+LQS", "TDC+LQS", "MOR-only"]
validLanguages = ["ARAR", "ZHCN", "ZHTW", "FRFR", "DEDE", "ITIT", "JAJP", "KOKR", "PTBR", "ESLA", "arar", "zhcn",
                  "zhtw", "frfr", "dede", "itit", "jajp", "kokr", "ptbr", "esla"]
validAnswer = ["Y", "N", "y", "n"]
validProjectTypes = ["M", "P", "m", "p"]

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


@app.route('/vendor_details')
def vendor_details():
    form = VendorDetailsForm()
    return render_template('vendor_details.html', form=form)


@app.route('/requestValidVendor')
def request_valid_vendor():
    return render_template('requestValidVendor.html')


@app.route('/requestLanguage')
def request_language():
    return render_template('requestLanguage.html', appDict=appDict)


@app.route('/requestValidLanguage')
def request_valid_language():
    return render_template('requestValidLanguage.html', appDict=appDict)


@app.route('/requestProjectType')
def request_project_type():
    return render_template('requestProjectType.html', appDict=appDict)


@app.route('/requestValidProjectType')
def request_valid_project_type():
    return render_template('requestValidProjectType.html', appDict=appDict)


@app.route('/requestNumberOfNewWords')
def request_number_of_new_words():
    return render_template('requestNumberOfNewWords.html', appDict=appDict)


# @app.route('/vendorInput', methods=['POST'])
# def vendor_check():
#     input_vendor = request.form['vendor']
#     if check_vendor(input_vendor, validVendors):
#         appDict.update(vendor_name=input_vendor)
#         return redirect(url_for('request_language', appDict=appDict))
#     else:
#         return redirect(url_for('request_valid_vendor'))
#
#
# @app.route('/languageInput', methods=['POST'])
# def language_check():
#     input_languages = request.form['languages']
#     if check_vendor(input_languages, validLanguages):
#         appDict.update(languages=input_languages)
#         return redirect(url_for('request_project_type', appDict=appDict))
#     else:
#         return redirect(url_for('request_valid_language', appDict=appDict))
#
#
# @app.route('/projectTypeInput', methods=['POST'])
# def project_type_check():
#     input_project_types = request.form['projectTypes']
#     if check_project_type(input_project_types, validProjectTypes):
#         appDict.update(project_type=input_project_types)
#         return redirect(url_for('request_number_of_new_words', appDict=appDict))
#     else:
#         return redirect(url_for('request_valid_project_type', appDict=appDict))


@app.route('/calculatedRates', methods=['GET'])
def calculate_rates():
    calc = RateCalculator(appDict)
    calc.run()


if __name__ == '__main__':
    app.run(debug=True)
