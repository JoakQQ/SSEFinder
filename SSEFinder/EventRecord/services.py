import requests


def get_location_api(name):
    # make the API Call
    r = requests.get('https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=' + name)

    # check response code & handle it
    if r.status_code == 200:
        data = r.json()
        result = []
        result.append(200)
        for key in ['x', 'y', 'nameEN', 'addressEN']:
            result.append(data[0][key])
        return result
    else:
        return r.status_code, None
