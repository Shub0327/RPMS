import firebase_admin
from firebase_admin import credentials, db

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
