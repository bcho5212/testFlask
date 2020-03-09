from App.ConfigLoader import ConfigLoader
from App.Validator import Validator


class RateCalculator(Validator):
    def __init__(self, appDict):
        Validator.__init__(self)
        self.appDict = appDict
        self.vendor_name = appDict["vendor_name"]
        self.languages = appDict["languages"].split(',')
        self.project_type = appDict["project_type"]
        self.new_words = int(appDict["new_words"])
        self.low_fuzzies = int(appDict["low_fuzzies"])
        self.high_fuzzies = int(appDict["high_fuzzies"])
        self.reps = int(appDict["reps"])
        self.hundred_matches = int(appDict["hundred_matches"])
        self.context_matches = int(appDict["context_matches"])
        self.pre_flight_hours = int(appDict["pre_flight_hours"])
        self.dtp_hours = int(appDict["dtp_hours"])
        self.language_costs = {}
        self.rates = {}

    def run(self):
        config = ConfigLoader('rates')
        vendor = config.generate_vendor(self.vendor_name)
        totalWC = (
                self.new_words +
                self.low_fuzzies +
                self.high_fuzzies +
                self.reps +
                self.hundred_matches +
                self.context_matches
        )
        for language in self.languages:
            self.get_language_cost(language, vendor, totalWC)

    def get_language_cost(self, language, vendor, totalWC):
        i = 0
        while i < len(vendor.rates):
            try:
                self.rates = vendor.rates[i][language]
                break
            except:
                i += 1
        if not self.rates:
            raise ValueError(
                "Language={0} is not set up for this vendor={1} in the rates.yml config file.".format(language, vendor))

        newWordsCost = float(self.rates["new_words"]) * self.new_words
        lowFuzziesCost = float(self.rates["low_fuzzies"]) * self.low_fuzzies
        highFuzziesCost = float(self.rates["high_fuzzies"]) * self.high_fuzzies
        repsCost = float(self.rates["reps"]) * self.reps
        hundredMatchesCost = float(self.rates["hundred_matches"]) * self.hundred_matches
        contextMatchesCost = float(self.rates["context_matches"]) * self.context_matches
        reviewCost = float(self.rates["review"]) * totalWC
        preflightCost = float(self.rates["preflight"]) * self.pre_flight_hours
        DTPCost = float(self.rates["dtp"]) * self.dtp_hours
        if totalWC <= 250:
            LSOCost = float(self.rates["lso"]) / 2
        if totalWC >= 250:
            LSOCost = float(self.rates["lso"]) * totalWC / 500
        self.language_costs["newWordCost"] = newWordsCost
        self.language_costs["lowFuzziesCost"] = lowFuzziesCost
        self.language_costs["highFuzziesCost"] = highFuzziesCost
        self.language_costs["repsCost"] = repsCost
        self.language_costs["hundredMatchesCost"] = hundredMatchesCost
        self.language_costs["contextMatchesCost"] = contextMatchesCost
        self.language_costs["reviewCost"] = reviewCost
        self.language_costs["preflightCost"] = preflightCost
        self.language_costs["DTPCost"] = DTPCost
        self.language_costs["LSOCost"] = LSOCost

    def validate_input(self):
        self.validate_self(self.appDict)


if __name__ == '__main__':
    testDict = {}
    testDict["vendor_name"] = "LB"
    testDict["languages"] = "ARAR"
    testDict["project_type"] = "test"
    testDict["new_words"] = 2
    testDict["low_fuzzies"] = 0
    testDict["high_fuzzies"] = 0
    testDict["reps"] = 0
    testDict["hundred_matches"] = 0
    testDict["context_matches"] = 0
    testDict["pre_flight_hours"] = 0
    testDict["dtp_hours"] = 0
    testCalc = RateCalculator(testDict)
    testCalc.run()
    for type_cost in testCalc.language_costs:
        print(type_cost + ": " + str(testCalc.language_costs[type_cost]))
