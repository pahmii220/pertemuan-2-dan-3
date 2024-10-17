import PySimpleGUI as sg
sg.theme('DarkGreen4'),
sg.theme_text_color("#ffff00")
window= sg.Window (title ="Latihan Pertama",
            layout=[[sg.Text("NPM        :2210010231")],
                    [sg.Text("NAMA      :MUHAMMAD PAHMI")],
                    [sg.Text("KELAS     :5M REGULER BANJARMASIN")],
                    [sg.Text("MATKUL    :PEMROGRAMAN VISUAL 3")]],
size=(400,200))
font=("Times", 18)
window()
window.close()