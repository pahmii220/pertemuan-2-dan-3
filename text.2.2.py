import PySimpleGUI as sg
sg.theme('DarkGreen4')
sg.theme_text_color("#FFFF00")
window= sg.Window (title ="Profile",
            layout=[[sg.Text("FAKULTAS INFORMASI ",size=(25,1),justification="center")],
                    [sg.Text("FAKULTAS INFORMASI ",size=(25,1),justification="left")],
                    [sg.Text("FAKULTAS INFORMASI ",size=(25,1),justification="right")],
                    [sg.Text(("FAKULTAS INFORMASI "+" ")* 2,size=(25,2),justification="center")],
                    [sg.Text("UNISKA MAB BANJARMASIN",text_color="#FFCC00")]],
        size=(400,250),
        font=("Times", 18))
window()
window.close()