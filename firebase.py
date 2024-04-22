import firebase_admin
from firebase_admin import credentials, db
import csv

# Initialize Firebase app
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://leakagedetection-3b460-default-rtdb.asia-southeast1.firebasedatabase.app'
})

# Function to retrieve data from Firebase
def retrieve_data():
    alldata = db.reference('data').get()
    print("All Data:", alldata)

    # to get all data seperately
    # ref_flow_rate_1 = db.reference('data/flow_rate_1')
    # ref_flow_rate_2 = db.reference('data/flow_rate_2')
    # ref_tds_value = db.reference('data/tds_value')
    # ref_temperature = db.reference('data/temperature')

    # data_flow_rate_1 = ref_flow_rate_1.get()
    # data_flow_rate_2 = ref_flow_rate_2.get()
    # data_tds_value = ref_tds_value.get()
    # data_temperature = ref_temperature.get()

    # print("Flow Rate 1 Data:", data_flow_rate_1)
    # print("Flow Rate 2 Data:", data_flow_rate_2)
    # print("TDS Value Data:", data_tds_value)
    # print("Temperature Data:", data_temperature)

#call the function
retrieve_data()

def convert_to_csv(data):
    keys = ['is_leakage_detected', 'flow_rate_1', 'flow_rate_2', 'tds_value', 'temperature']
    filename = 'H:\\Major Project\\major\\sensor_data.csv'

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerow(data)

    print("Data converted to CSV successfully.")

# Example usage:
data = {
    'is_leakage_detected': True,
    'flow_rate_1': 0.5,
    'flow_rate_2': 0.6,
    'tds_value': 0.7,
    'temperature': 0.8
}

convert_to_csv(data)

def send_data_to_firebase(is_leakage_detected, flow_rate_1, flow_rate_2, tds_value, temperature):
    data = {
        'is_leakage_detected': is_leakage_detected,
        'flow_rate_1': flow_rate_1,
        'flow_rate_2': flow_rate_2,
        'tds_value': tds_value,
        'temperature': temperature
    }
    # Create a new reference in the database
    new_ref = db.reference('leakage_data')

    # Set the data in the new reference
    new_ref.set(data)

#call the function
send_data_to_firebase(True, 0.5, 0.6, 0.7, 0.8)
