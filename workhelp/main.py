"""
Simple Data save Manager with tkinter ttbootstrap
Author: Saidino
License: GNU GPLv3 license
Source: https://github.com/saidino84/work_staff
"""

from app.app import LogicApp
from app.views.home_page import HomePage
# from PIL import Image, ImageTk

import sv_ttk



if __name__=="__main__":
    app=LogicApp()
    _home_page=HomePage(app)

    # sv_ttk.set_theme('dark')
    # app.attributes('-topmost',True) 
    # app.icon=Image.open('app/assets/impuesto.png')
    # app.photoico=ImageTk.PhotoImage(app.icon)
    # app.wm_iconphoto(False,app.photoico)
    _home_page.pack(fill='both',expand=True)
    
    # _home_page.grid(row=0,column=0,sticky='nesw')

    # # Set a minim size for the window and place it int midle
    # app.update()
    # app.minsize(app.winfo_width(),app.winfo_height())
    # # root.minsize(785,400)
    # x_coord=int((app.winfo_screenwidth()/2)-(785/2))
    # y_coord=int((app.winfo_screenheight()/2)-(400/2))
    # app.geometry("+{}+{}".format(x_coord,y_coord))

    app.mainloop()