class Validator:
    validVendors = ["LB", "LB+MOR", "TDC+MOR", "LB+LQS", "TDC+LQS", "MOR-only"]
    validLanguages = ["ARAR", "ZHCN", "ZHTW", "FRFR", "DEDE", "ITIT", "JAJP", "KOKR", "PTBR", "ESLA", "arar", "zhcn",
                      "zhtw", "frfr", "dede", "itit", "jajp", "kokr", "ptbr", "esla"]
    validAnswer = ["Y", "N", "y", "n"]
    validProjectTypes = ["M", "P", "m", "p"]

    def __init__(self):
        self.vendor_name_check = True
        self.vendor_languages_check = True
        self.vendor_project_type_check = True

    def validate_self(self, appDict):
        self.validate_vendor_name(appDict["vendor_name"])
        self.validate_languages(appDict["languages"])
        self.validate_project_type(appDict["project_type"])

    def validate_vendor_name(self, vendor_name_input):
        if vendor_name_input in self.validVendors:
            pass
        else:
            self.vendor_name_check = False

    def validate_languages(self, language_input):
        languages = language_input.split(',')
        if any(language in languages for language in self.validLanguages):
            pass
        else:
            self.vendor_languages_check = False

    def validate_project_type(self, project_type_input):
        if project_type_input in self.validProjectTypes:
            pass
        else:
            self.vendor_project_type_check = False
