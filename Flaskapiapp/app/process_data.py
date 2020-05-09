import http.client
import json
def get_data():
    conn = http.client.HTTPConnection("dummy.restapiexample.com")
    conn.request("GET","/api/v1/employees")
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def process():
    data = get_data()
    return data['data'][0]

def covid_get():
    conn = http.client.HTTPSConnection("covid-19-statistics.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com",
        'x-rapidapi-key': "cab6f7cd99msh3ec93c9b6cc0a04p11df57jsn17d30713b9c3"
    }

    conn.request("GET", "/reports/total?date=2020-04-07", headers=headers)

    res = conn.getresponse()
    cvddata = res.read()
    return json.loads(cvddata.decode("utf-8"))   
    print(data.decode("utf-8"))


    