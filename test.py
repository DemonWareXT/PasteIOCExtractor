#!/usr/bin/env python3


from pprint import pprint
from refinery import xtp, Unit
from refinery.lib.patterns import indicators
from ioc_finder import find_iocs
import itertools

data = "192.168.1.1"
pprint(find_iocs(data))

quit()

# pprint(xtp().process(data, pattern=indicators.ipv4))
class b64custom(Unit):
    _pattern = (
        indicators.hostname.name,
        indicators.url.name,
        indicators.email.name,
    )

    def __init__(self, pattern=_pattern):
        super().__init__(pattern=pattern)

    def process(self, data):
        return data | map(self.args.pattern, self._pattern) | xtp

    def reverse(self, data):
        return data | -xtp | map(self._pattern, self.args.pattern)


pprint(b64custom.process(data))
