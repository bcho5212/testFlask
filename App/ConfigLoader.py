import logging
import pathlib

import yaml

from vendors.BaseVendor import BaseVendor


class ConfigLoader:
    def __init__(self, file_name):
        self.configs = {}
        str_path = [str(pathlib.Path().absolute()), 'config', file_name + '.yml']
        self.yml_path = '/'.join(str_path)
        with open(self.yml_path, 'r') as stream:
            yml_config = yaml.load(stream, Loader=yaml.BaseLoader)
            self.configs[file_name] = yml_config

    def check_vendor_config_loaded(self, vendor_name):
        loaded_vendors = []
        for config in self.configs.get('rates'):
            loaded_vendors.append(config.get("vendor").get("name"))
        if vendor_name in loaded_vendors:
            return True
        else:
            return False

    def generate_vendor(self, vendor_name):
        if not self.check_vendor_config_loaded(vendor_name):
            logging.error("The vendor {0} is not loaded".format(vendor_name))
            raise ValueError("Failed to generate vendor as associated configuration was not loaded")

        for rates_config in self.configs.get("rates"):
            if vendor_name == rates_config["vendor"]["name"]:
                return BaseVendor(vendor_name, rates_config["vendor"]["language_rates"])


if __name__ == '__main__':
    configLoader = ConfigLoader('rates')
    test_vendor = configLoader.generate_vendor('LB')
    print(test_vendor.name)
    print(test_vendor.rates)
    print(type(test_vendor.rates[0]["ARAR"]))
