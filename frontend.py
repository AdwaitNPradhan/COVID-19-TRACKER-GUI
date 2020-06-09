import PySimpleGUI as sg
import backend

CV = {}
FONT = 'Kaushan'
THEME = 'DarkPurple6'
sg.theme(THEME)

sg.SetGlobalIcon('CIRCUITS(1).ico')

def India(CV):
    backend.official_data(CV)
    return CV

def state(state,CV):
    backend.state_data(state,CV)
    return CV

st_list = ['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadar Nagar Haveli','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telengana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal']

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

try:
    CV = India(CV)
except:
    sg.popup_auto_close("Couldn't connect to database, internet connection not detected or some other errors may have occurred.\n Exitting",title = 'COVID - 19 TRACKER',auto_close_duration=5)
    exit(0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def india():
    global CV
    
    CV = India(CV)
    
    COLUMN_1 = [[sg.Text('Number of Confirmed cases',font = FONT),sg.Text(CV['cc'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))],
                [sg.Text('Indian Origin',font = FONT),sg.Text(CV['cci'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))],
                [sg.Text('Patients Recovered',font = FONT),sg.Text(CV['recv'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))]
                ]
    
    COLUMN_2 = [[sg.Text('Active Cases',font = FONT),sg.Text(CV['active'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))],
                [sg.Text('Non - Indian Origin',font = FONT),sg.Text(CV['ccf'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))],
                [sg.Text('Patients Dead',font = FONT),sg.Text(CV['dead'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))]
                ]

    FRAME_LAYOUT = [[sg.Column(COLUMN_1),sg.Column(COLUMN_2)]]

    HOME_WINDOW =  [[sg.Text('COVID - 19 TRACKER',size = (64,0),relief = sg.RELIEF_RAISED,justification = 'center',font = FONT,text_color='Purple',background_color='Yellow')],
                    [sg.Text('Area of Reference: INDIA',size = (64,0),font = FONT,justification='center')],
                    [sg.Frame('Details:',FRAME_LAYOUT)],
                    [sg.Button('Check for Individual\nstates',size = (20,2),font = FONT),sg.Button('Credits',size = (20,2),font = FONT,focus = True),sg.Text('',size = (2,0)),sg.Text('  COVID - 19 TRACKER\n© 2020 BCA DEV CLUB')]
                    ]

    home_window = sg.Window('COVID - 19 TRACKER (AOR: INDIA)',HOME_WINDOW)
    
    while True:             
        event, values = home_window.read()
        CV = India(CV)
        if event in (None, 'Cancel'):
            sg.popup_annoying('Exitting',auto_close=True,auto_close_duration=0.1,button_type=None,grab_anywhere=False,keep_on_top=True)
            home_window.close()
            CV.clear()
            break
        elif event in 'Check for Individual\nstates':
            sg.popup_annoying('Moving',auto_close=True,auto_close_duration=0.1,button_type=None,grab_anywhere=False,keep_on_top=True)
            home_window.close()
            CV = state(34,CV)
            State(34)
        elif event in 'Credits':
            home_window.close()
            credit()
    exit(0)
    
    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def State(st_id):
    global CV
    
    CV = state(st_id,CV)
    
    COLUMN_1_1 = [[sg.Text('Number of Confirmed cases',font = FONT),sg.Text(CV['cc'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))],
                [sg.Text('Indian Origin',font = FONT),sg.Text(CV['cci'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))],
                [sg.Text('Patients Recovered',font = FONT),sg.Text(CV['recv'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))]
                ]
    
    COLUMN_2_1 = [[sg.Text('Active Cases',font = FONT),sg.Text(CV['active'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))],
                [sg.Text('Non - Indian Origin',font = FONT),sg.Text(CV['ccf'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))],
                [sg.Text('Patients Dead',font = FONT),sg.Text(CV['dead'],relief=sg.RELIEF_RAISED,font = FONT,justification = 'center',size = (10,0))]
                ]

    FRAME_LAYOUT1 = [[sg.Column(COLUMN_1_1),sg.Column(COLUMN_2_1)]]

    STATE_WINDOW = [[sg.Text(' COVID - 19 TRACKER',size = (64,0),relief = sg.RELIEF_RAISED,justification = 'center',font = FONT,text_color='Purple',background_color='Yellow')],
                    [sg.Text('Area of Reference: ',size = (34,0),font = FONT,justification='center'),sg.DropDown(st_list,key = 'stateid',background_color='White',text_color='DarkBlack',size = (20,8),default_value=st_list[st_id],readonly=True),sg.Button('Get',font = FONT,size = (10,0))],
                    [sg.Frame('Details:',FRAME_LAYOUT1)],
                    [sg.Button('Back',size = (20,2),font = FONT,focus = True),sg.Button('Credits',size = (20,2),font = FONT,focus = True),sg.Text('',size = (0,1)),sg.Text('  COVID - 19 TRACKER\n© 2020 BCA DEV CLUB')]]

    state_window = sg.Window('COVID - 19 TRACKER (AOR: CUSTOM)',STATE_WINDOW)

    while True:             
        event1, vals = state_window.read()
       
        CV = state(st_id,CV)
        if event1 in (None, 'Cancel'):
            sg.popup_annoying('Exitting',auto_close=True,auto_close_duration=0.1,button_type=None,grab_anywhere=False,keep_on_top=True)
            state_window.close()
            CV.clear()
            break
        elif event1 in 'Get':            
            st_id = st_list.index(vals['stateid'])
            state_window.close()
            State(st_id)
            
        elif event1 in 'Back':
            sg.popup_annoying('Moving',auto_close=True,auto_close_duration=0.1,button_type=None,grab_anywhere=False,keep_on_top=True)
            state_window.close()
            CV.clear()
            CV = India(CV)
            india()
        elif event1 in 'Credits':
            state_window.close()
            credit()
            
    exit(0)
        
        
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
def credit():
    credit_layout = [[sg.Button('←'),sg.Text('COVID - 19 TRACKER',size = (68,0),relief = sg.RELIEF_RAISED,justification = 'center',font = FONT,text_color='Purple',background_color='Yellow')],
                     [sg.Text(' ',size = (0,1)),sg.Text('',size = (25,1)),sg.Text('Support the developppers',relief=sg.RELIEF_RAISED,size = (20,0),justification='center',font = FONT,text_color='Purple',background_color='Yellow')],

                     [sg.Text('''           This Application was developed by the Core members of the BCA Developers Club
            Backend: Avilash Ghosh
                Frontend: Adwait Narayan Pradhan
                 You can support the developers by Donating Some funds.
           Did you like what we did? You can contact us for development of your Application by
                Requesting for service(charges applied).''',justification='center',font = FONT)],
                      [sg.Button('Support Us',size = (20,2),font = FONT,focus = True),sg.Text('',size = (10,1)),sg.Button('Request for service',size = (20,2),font = FONT,focus = True),sg.Text('',size = (0,1)),sg.Text('  COVID - 19 TRACKER\n© 2020 BCA DEV CLUB')]]

    credit_window = sg.Window('COVID - 19 TRACKER (Support the Developpers)',credit_layout)

    while True:
        event2,val = credit_window.read()
        if event2 in (None,'Cancel','Close'): 
            sg.popup_annoying('Exitting',auto_close=True,auto_close_duration=0.1,button_type=None,grab_anywhere=False,keep_on_top=True)
            credit_window.close()
            break
        elif event2 in 'Support Us':
            sg.PopupOK('''Support via Donation:
                    Google Pay: 7001940069          
                         PayTM: 7001940069             ''',font = FONT,title = 'Support the Developers')
        elif event2 in 'Request for service':
            sg.PopupOK("Email us at: 'emailforbcadevclub@gmail.com'\nMail us your plan and request, we will come back to you with further details. ",title = 'Request for Service',font = FONT)
        elif event2 in '←':
            credit_window.close()
            State(34)
    exit(0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():                
    greet = [
            [sg.Text("This is an active COVID - 19 TRACKER.\nCreated by the core members of BCA DEV CLUB. Click on ok to proceed.",font = FONT)],
             [sg.Button('OK',font = FONT,bind_return_key=True),sg.Button('Close',font = FONT)]
             ]
    
    greet_win = sg.Window('COVID - 19 TRACKER',greet)
    
    while True:
        eve,val = greet_win.read()
        if eve in (None,'Cancel','Close'):
            sg.popup_annoying('Exitting',auto_close=True,auto_close_duration=0.1,button_type=None,grab_anywhere=False,keep_on_top=True)
            greet_win.close()
            break
        elif eve in 'OK':
            greet_win.close()
            india()
    exit(0)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


main()
exit(0)