

# import tkinter as tk
from PIL import Image, ImageTk
from ttkbootstrap import Style
import ttkbootstrap as tk
import tkinter as tk
from ttkbootstrap import Style

from app.views.iva_calc import IvaCalculator


class LogicApp(tk.Tk):
    def __init__(self,title='Utility',themename='darkly',**kw):
        super().__init__(*kw)
        self.title=title
        self.themename=themename
        self.style=Style('darkly')
        # self.attributes('-topmost',True) 
        # self.themename='darkly'
        self.icon=Image.open('app/assets/impuesto.png')
        self.photoico=ImageTk.PhotoImage(self.icon)
        self.wm_iconphoto(False,self.photoico)
        
    # Set a minim size for the window and place it int midle
        self.update()
        self.minsize(self.winfo_width(),self.winfo_height())
        # root.minsize(785,400)
        x_coord=int((self.winfo_screenwidth()/2)-(785/2))
        y_coord=int((self.winfo_screenheight()/2)-(400/2))
        self.geometry("+{}+{}".format(x_coord,y_coord))

        # self.mainloop()
    
    def show_calc(self):
        self.top_level=tk.Toplevel(self,container=False)
        self.top_level.attributes('-topmost',True)
        self.top_level.wm_transient(self)
        self.iva_calc=IvaCalculator(self.top_level)
        self.iva_calc.pack(expand=True,fill="both")
        
        
        