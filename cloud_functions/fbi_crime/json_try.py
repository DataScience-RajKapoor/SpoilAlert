import json
import pandas as pd

row = {
    "state":"HI", "state_details":[{
    "agency":"HI0010000", "agency_details":[{
      "ori": "HI0010000",
      "agency_name": "Hawaii Police Department County Sheriff's Office",
      "agency_type_name": "County",
      "state_name": "Hawaii",
      "state_abbr": "HI",
      "division_name": "Pacific",
      "region_name": "West",
      "region_desc": "Region IV",
      "county_name": "HAWAII",
      "nibrs": False,
      "latitude": 19.716698,
      "longitude": -155.08688,
      "nibrs_start_date": ""
    },
    "HI0050000": {
      "ori": "HI0050000",
      "agency_name": "Maui Police Department County Sheriff's Office",
      "agency_type_name": "County",
      "state_name": "Hawaii",
      "state_abbr": "HI",
      "division_name": "Pacific",
      "region_name": "West",
      "region_desc": "Region IV",
      "county_name": "MAUI",
      "nibrs": False,
      "latitude": 20.887321,
      "longitude": -156.48763,
      "nibrs_start_date": ""
    },
    "HI0020000": {
      "ori": "HI0020000",
      "agency_name": "Honolulu Police Department",
      "agency_type_name": "City",
      "state_name": "Hawaii",
      "state_abbr": "HI",
      "division_name": "Pacific",
      "region_name": "West",
      "region_desc": "Region IV",
      "county_name": "HONOLULU",
      "nibrs": True,
      "latitude": 21.304317,
      "longitude": -157.85077,
      "nibrs_start_date": "01/01/2018"
    },
    "HI0040000": {
      "ori": "HI0040000",
      "agency_name": "Kauai Police Department County Sheriff's Office",
      "agency_type_name": "County",
      "state_name": "Hawaii",
      "state_abbr": "HI",
      "division_name": "Pacific",
      "region_name": "West",
      "region_desc": "Region IV",
      "county_name": "KAUAI",
      "nibrs": False,
      "latitude": 22.012038,
      "longitude": -159.705965,
      "nibrs_start_date": ""
    }
  },
  "DE": {
    "DE0030500": {
      "ori": "DE0030500",
      "agency_name": "Milford Police Department",
      "agency_type_name": "City",
      "state_name": "Delaware",
      "state_abbr": "DE",
      "division_name": "South Atlantic",
      "region_name": "South",
      "region_desc": "Region III",
      "county_name": "KENT; SUSSEX",
      "nibrs": True,
      "latitude": 38.91612,
      "longitude": -75.42161,
      "nibrs_start_date": "01/01/2001"
    },
    "DE0030300": {
      "ori": "DE0030300",
      "agency_name": "Laurel Police Department",
      "agency_type_name": "City",
      "state_name": "Delaware",
      "state_abbr": "DE",
      "division_name": "South Atlantic",
      "region_name": "South",
      "region_desc": "Region III",
      "county_name": "SUSSEX",
      "nibrs": True,
      "latitude": 38.677511,
      "longitude": -75.335495,
      "nibrs_start_date": "01/01/2001"
    },
    "DE0011900": {
      "ori": "DE0011900",
      "agency_name": "Dover Fire Marshal",
      "agency_type_name": "Other",
      "state_name": "Delaware",
      "state_abbr": "DE",
      "division_name": "South Atlantic",
      "region_name": "South",
      "region_desc": "Region III",
      "county_name": "KENT",
      "nibrs": True,
      "latitude": "",
      "longitude": "",
      "nibrs_start_date": "01/01/2013"
    },
    "DE0030100": {
      "ori": "DE0030100",
      "agency_name": "Bridgeville Police Department",
      "agency_type_name": "City",
      "state_name": "Delaware",
      "state_abbr": "DE",
      "division_name": "South Atlantic",
      "region_name": "South",
      "region_desc": "Region III",
      "county_name": "SUSSEX",
      "nibrs": True,
      "latitude": 38.744175,
      "longitude": -75.599144,
      "nibrs_start_date": "01/01/2001"
    }
  }
    }

print(type(row))
row_json = json.dumps(row)

def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v

#print(row_json)
print(row_json)
print('I am going to normalize it\n')
print(pd.json_normalize(row))