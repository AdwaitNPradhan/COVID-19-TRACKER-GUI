import json
import requests
import subprocess as sp





def official_data(CVD):

    url = "https://api.rootnet.in/covid19-in/stats/latest"
    response = requests.get(url)
    parsed=response.text
    data=json.loads(parsed)

    #data printing of official data
    CVD['cc'] = data['data']['summary']['total']

    CVD['cci'] = data['data']['summary']['confirmedCasesIndian']

    CVD['ccf'] = data['data']['summary']['confirmedCasesForeign']

    CVD['recv'] = data['data']['summary']['discharged']

    CVD['dead'] = data['data']['summary']['deaths']

    CVD['active'] = CVD['cc']-(CVD['recv']+CVD['dead'])


def state_data(state, CVD):
    url = "https://api.rootnet.in/covid19-in/stats/latest"
    response = requests.get(url)
    parsed=response.text
    data=json.loads(parsed)
    #data printing of state data
    state_info = data['data']['regional'][state]

    CVD['cc'] = state_info['totalConfirmed']

    CVD['cci'] = state_info['confirmedCasesIndian']

    CVD['ccf'] = state_info['confirmedCasesForeign']

    CVD['recv'] = state_info['discharged']

    CVD['dead'] = state_info['deaths']

    CVD['active'] = CVD['cc']-(CVD['recv']+CVD['dead'])

