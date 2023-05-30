#!/usr/bin/python

import json
import xmltodict
from collections import defaultdict

class FilterModule(object):

    def filters(self):
        return {
            'xml2json': self.xml2json,
        }

    def xml2json(self, value):
        import xmltodict, json
        return json.dumps(xmltodict.parse(value))
