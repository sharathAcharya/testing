import json
from datetime import datetime, timedelta


class utility:
    def __init__(self):
        self.data_val = {}

    # reading the   json information
    def extract_json_data(self, filepath):
        with open(filepath, 'r') as fp:
            data = json.load(fp)
            doc_details = data['documents'][0]
            self.data_val['doc_type'] = doc_details['doc_type'].split('.')[-1]
            field_info = doc_details['fields']
            self.data_val['First Name'] = field_info['Firstname']['content']
            self.data_val['Last Name'] = field_info['Lastname']['content']
            self.data_val['Date Of Birth'] = field_info['DateOfBirth']['content']
            self.data_val['Date Of Expiration'] = field_info['DateOfExpiration']['content']

    # validating the expiration date
    def validation_from_json(self):
        dateofexp = datetime.strptime(self.data_val['Date Of Expiration'], '%d.%m.%Y').date()
        current_date = datetime.now().date() + timedelta(days=10)
        if dateofexp < current_date:
            print("Given Document is Expried")
        else:
            print("Given Document is valid")


if __name__ == '__main__':
    obj = utility()
    obj.extract_json_data(r"C:\Users\Downloads\sample.json")
    obj.validation_from_json()
