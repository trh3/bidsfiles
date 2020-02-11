import json
import os
import re

class DataSchema:
    def __init__(self, schema_json):

        with open(os.path.abspath(schema_json), "r") as config_file:
            self.schema_json = json.load(config_file)
        self.sep = self.schema_json['separator']
        self.tag_keys = schema_json['tags'].keys()
        self.file_keys = schema_json['files'].keys()
        self.files = schema_json['files']

        self.required_regex = re.compile("^{.*?}")
        self.optional_regex = re.compile("^<.*?>")
        self.group_regex = re.compile("^\[.*?\]")
        for f in self.files:
            format_str = f['format']
            f['tag_comp'] = self.parse_format_string(format_str)


    def file_parser(self, file_path):
        base_name = os.path.basename(file_path)
        base_name = ".".split(base_name)[0]
        base_name_sans_ext = base_name[0]
        ext = base_name[1:]
        base_name_components = self.sep.split(base_name)
        file_key = base_name_components[-1]
        if len(base_name_components) > 1:
            file_tags = base_name_components[0:-1]
        else:
            file_tags = None

    def file_ext_validator(self, file_key, file_ext):
        valid = True
        if file_ext not in self.files[file_key]['extensions']:
            valid = False
        return valid

    def file_key_validator(self, file_key):
        valid = True
        if file_key not in self.file_keys:
            valid = False
        return valid

    def file_tag_validator(self, file_tags, file_key):


    def parse_format_string(self, format_str):
        format_comps = self.sep.split(format_str)
        comp_dict = {"required":False, "optional": False, "group": False}
        location_counter = 0
        for comp in format_comps:
           comp_dict = {"required": False, "optional": False, "group": False}
           comp_dict['required'] = self.required_regex.match(comp)
           comp_dict['optional'] = self.optional_regex.match(comp)
           comp_dict['group'] = self.group_regex.match(comp)
           loc = location_counter
           if not comp_dict['group']:
            location_counter += 1
           key = re.sub("{|<|\[|\]|>|}","",comp)
           



