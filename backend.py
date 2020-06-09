import json
import requests
import subprocess as sp

url = "https://api.rootnet.in/covid19-in/stats/latest"
response = requests.get(url)
parsed=response.text
data=json.loads(parsed)

def official_data(CVD):
    #data printing of official data
    CVD['cc'] = data['data']['summary']['total']

    CVD['cci'] = data['data']['summary']['confirmedCasesIndian']

    CVD['ccf'] = data['data']['summary']['confirmedCasesForeign']

    CVD['recv'] = data['data']['summary']['discharged']

    CVD['dead'] = data['data']['summary']['deaths']

    CVD['active'] = CVD['cc']-(CVD['recv']+CVD['dead'])


def state_data(state, CVD):
    state_info = data['data']['regional'][state]

    CVD['cc'] = state_info['totalConfirmed']

    CVD['cci'] = state_info['confirmedCasesIndian']

    CVD['ccf'] = state_info['confirmedCasesForeign']

    CVD['recv'] = state_info['discharged']

    CVD['dead'] = state_info['deaths']

    CVD['active'] = CVD['cc']-(CVD['recv']+CVD['dead'])
#Test code to see the number of states
# for state in range(39):
#     try:
#         print("%s: '%s'" % (state,data['data']['regional'][state]['loc']),end = "\n")  
#     except IndexError:
#         print("\nBREAKING\n-")
#         break