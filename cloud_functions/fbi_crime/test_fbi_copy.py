import unittest
import unittest.mock
import json
import ori_table


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
        req = unittest.mock.Mock()

        # Call tested function
        #assert ori_table.crime_data_fbi(req) == "https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies"
        print('i am testing the request')
        print(ori_table.crime_data_fbi(req))
        response = ori_table.crime_data_fbi(req)
        #row_json = json.loads(response)
        #print(row_json['HI'])
        #data = json.loads(row_json.data)
        print('\nI am before the response\n')
        #print(data['ori'])
        print(response)

    #def test_hello_name_with_name(self):
     #   name = "test"
      #  req = unittest.mock.Mock(args={"name": name})

        # Call tested function
       # assert main.hello_name(req) == "Hello {}!".format(name)
