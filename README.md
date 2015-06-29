# mongodb-udacity-
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "jeju_south-korea.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons","Ro","ro"]

# UPDATE THIS VARIABLE
mapping = { "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Ave.": "Avenue",
            "Rd": "Road",
            "Rd.": "Road",
            "dong":"dong",
            "Dong":"Dong"
            }


def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types


def update_name(name, mapping):
    m = street_type_re.search(name).group()
    #print m
    #print mapping.keys()
    if m in mapping.keys():
        name = street_type_re.sub(mapping[m], name)
        
    return name


def test():
    st_types = audit(OSMFILE)
    #assert len(st_types) == 3
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name
            if name == "dong":
                assert better_name == "dong"
            if name == "Dong":
                assert better_name == "Dong"
""" In korea, there are different Address Notations which is quite distinguished with western style.
    Dong(Subdivision ) , ro -> road but we do not use abbreviation for ro or Dong, actually do not use abbreviation like St, Rd, Ave"""

if __name__ == '__main__':
    test()
