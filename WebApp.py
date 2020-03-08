from flask import *

from RateCalculator import *

app = Flask(__name__)

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


@app.route('/welcome')
def welcome_page():
    return render_template('index.html')


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


@app.route('/calculatedRates', methods=['GET'])
def calculate_rates():
    calc = RateCalculator(appDict)
    calc.run()


if __name__ == '__main__':
    app.run(debug=True)
