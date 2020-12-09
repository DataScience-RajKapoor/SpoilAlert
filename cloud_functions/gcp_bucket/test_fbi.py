import unittest
import unittest.mock

import main


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
        
        response = main.crime_data_fbi(req)
        print(response)
        assert response.status == 200

    #def test_hello_name_with_name(self):
     #   name = "test"
      #  req = unittest.mock.Mock(args={"name": name})

        # Call tested function
       # assert main.hello_name(req) == "Hello {}!".format(name)
