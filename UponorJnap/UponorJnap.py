import requests


class UponorJnap:
    def __init__(self, host):
        self.url = "http://" + host + "/JNAP/"

    def get_data(self):
        r = requests.post(url=self.url, headers={"x-jnap-action": "http://phyn.com/jnap/uponorsky/GetAttributes"},
                          data='{}')
        data = r.json()

        variables = {}
        for var in data['output']['vars']:
            variables[var['waspVarName']] = var['waspVarValue']
        return variables

    def send_data(self, data):
        items = []
        for k, v in data.items():
            items.append('{"waspVarName": "' + k + '","waspVarValue": "' + str(v) + '"}')
        payload = '{"vars": [' + ','.join(items) + ']}'

        r = requests.post(url=self.url, headers={"x-jnap-action": "http://phyn.com/jnap/uponorsky/SetAttributes"},
                          data=payload)
        r_json = r.json()

        if 'result' in r_json and not r_json['result'] == 'OK':
            raise ValueError(r_json)
