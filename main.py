# MIT License
#
# Copyright (c) 2024 Tofi_Toffee
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import cv2
import FreeSimpleGUI as sg
import sys

sg.theme('Reddit')

version = [0,1,0,"b"]
#Format of version: [major, minor, patch, revision]

credits = """Developed by TofiToffee 2024. Based on the MIT license.

I'm not affliated with The Indie Stone.

""" + "Current version: " + ".".join(str(x) for x in version)

help = """Due to a Bug in the game's engine, the cursor renders with Red and Blue Channels flipped 
I've developed this tool to provide a temporary fix.

How to use:

1. Select an image to convert (32x32 preferably).
2. Select an output name.
3. Press convert.
4. The cursor will be saved in the same directory as the image.
5. Go to Steam and go to Project Zomboid.
6. Open the local folder and go to media/ui.
7. Replace the cursor_white.png with your custom one."""

layout = [[sg.Text('Select image')],
            [sg.Input(), sg.FileBrowse(file_types=(('PNG Files', '*.png'),))],
            [sg.Text('Output name')],
            [sg.Input("cursor_white.png")],
            [sg.Button('Convert'), sg.Button('Exit'), sg.Button('About'), sg.Button('Help')]]

window = sg.Window('Project Zomboid - Cursor Converter ' + "v" + ".".join(str(x) for x in version), layout, icon="icon.ico", font=("Tahoma",12))

def convert_image(img,final_name):
    if img == "":
        sg.popup('Please select an image', title="Error", font=("Tahoma",12))
        return
    #Import the image
    img1 = cv2.imread(str(img), cv2.IMREAD_UNCHANGED)

    #Convert the image to RGBA
    img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGBA, cv2.IMREAD_UNCHANGED)

    #Save the image acording to the name
    cv2.imwrite(str(final_name), img2)
    sg.popup('Conversion complete', title="Success", font=("Tahoma",12))


while True:
    event, values = window.read()
    #Check for button presses

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    #Check for About
    if event == 'About':
        #Popup with credits
        sg.popup(credits, title="About",font=("Tahoma",12 ))

    #Check for Convert
    if event == 'Convert':
        convert_image(values[0],values[1])
    if event == 'Help':
        sg.popup(help, title="About",font=("Tahoma",12))