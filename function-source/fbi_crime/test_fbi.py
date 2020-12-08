import unittest
import unittest.mock
import json
import main
import final_test


class TestFbiApi(unittest.TestCase):
    
    # commenting as I have arguments
    #def test_crime_data_fbi(self):
     #   req = unittest.mock.Mock()

        # Call tested function
       # assert main.hcrime_data_fbi(req) == "Hello World!"
        

    def test_crime_data(self):

        data = {'ori': 'HI0010000',
                'start_date':'2018',
                'end_date':2019,
                'distance':'10'}
        req = unittest.mock.Mock(args=data)

        # Call tested function
        #assert main.crime_data_fbi(req) == "https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/HI0010000/offenses/2018/2019"
        
        response = final_test.crime_data_fbi(req)
        #row = '{ "results" : [ { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "violent-crime", "state_abbr" : "IL", "cleared" : 0, "actual" : 27420 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "rape-legacy", "state_abbr" : "IL", "cleared" : 0, "actual" : 0 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "rape", "state_abbr" : "IL", "cleared" : 0, "actual" : 1857 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "property-crime", "state_abbr" : "IL", "cleared" : 0, "actual" : 86822 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "motor-vehicle-theft", "state_abbr" : "IL", "cleared" : 0, "actual" : 10115 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "larceny", "state_abbr" : "IL", "cleared" : 0, "actual" : 64982 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "human-trafficing", "state_abbr" : "IL", "cleared" : 0, "actual" : 0 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "homicide", "state_abbr" : "IL", "cleared" : 0, "actual" : 567 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "burglary", "state_abbr" : "IL", "cleared" : 0, "actual" : 11725 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "arson", "state_abbr" : "IL", "cleared" : 0, "actual" : 0 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "aggravated-assault", "state_abbr" : "IL", "cleared" : 0, "actual" : 15315 }, { "ori" : "ILCPD0000", "data_year" : 2018, "offense" : "robbery", "state_abbr" : "IL", "cleared" : 0, "actual" : 9681 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "rape", "state_abbr" : "IL", "cleared" : 0, "actual" : 1761 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "arson", "state_abbr" : "IL", "cleared" : 0, "actual" : 0 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "aggravated-assault", "state_abbr" : "IL", "cleared" : 0, "actual" : 15296 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "violent-crime", "state_abbr" : "IL", "cleared" : 0, "actual" : 25532 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "robbery", "state_abbr" : "IL", "cleared" : 0, "actual" : 7983 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "burglary", "state_abbr" : "IL", "cleared" : 0, "actual" : 9578 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "homicide", "state_abbr" : "IL", "cleared" : 0, "actual" : 492 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "human-trafficing", "state_abbr" : "IL", "cleared" : 0, "actual" : 0 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "larceny", "state_abbr" : "IL", "cleared" : 0, "actual" : 62083 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "motor-vehicle-theft", "state_abbr" : "IL", "cleared" : 0, "actual" : 9081 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "property-crime", "state_abbr" : "IL", "cleared" : 0, "actual" : 80742 }, { "ori" : "ILCPD0000", "data_year" : 2019, "offense" : "rape-legacy", "state_abbr" : "IL", "cleared" : 0, "actual" : 0 } ], "pagination" : { "count" : 24, "page" : 0, "pages" : 1, "per_page" : 0 } }'
        #row_json = json.loads(row)
        #print(response.data)
        #data = json.loads(response.data)
        print('I am before the response')
        #print(data['results'])
        print(response)

    #def test_hello_name_with_name(self):
     #   name = "test"
      #  req = unittest.mock.Mock(args={"name": name})

        # Call tested function
       # assert main.hello_name(req) == "Hello {}!".format(name)
