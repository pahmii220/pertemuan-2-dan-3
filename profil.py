import PySimpleGUI as sg
sg.theme('DarkGreen4'),
sg.theme_text_color("#ffff00")
window= sg.Window (title ="Profile",
            layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                        font=("Arial",25,"italic","bold","underline"))],
                    [sg.Text("NPM        :2210010231")],
                    [sg.Text("NAMA      :MUHAMMAD PAHMI")],
                    [sg.Text("KELAS     :5M REGULER BANJARMASIN")]],
size=(510,200))
font=("Times", 18)
window()
window.close()