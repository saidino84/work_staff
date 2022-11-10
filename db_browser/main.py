from ttkbootstrap import Style
from app.controllers.app_controller import HomeController
from app.db.repository.repository import Repository
from app.ui import Ui
from app.ui import ttk
from tkinter import *
class App:
    def __init__(self) -> None:
        self.LGRAY='#545454'
        self.DGRAY='#242424'
        self.RGBGRAY='#2e2e2e'
        
        self.controller=HomeController()
        self.repository=Repository()
        self.style=Style(theme='darkly')
        self.root=self.style.master
        self.root.overrideredirect(True)
        self.root.geometry('700x450+500+500')
        
        self.setup_windows_bar()
        
        # self.start_plantforms()
    def setup_windows_bar(self):
        # self.title_bar=ttk.Frame(self.root,bg='#ffffff',relief='raised',bd=1,highlightthickness=1)
        self.title_bar=ttk.Frame(self.root,style='dangerous')
        self.title_bar.bind('<Button-1>',self.get_windows_pos)
        
        # put a close button on the title bar
        self.close_btn=ttk.Button(self.title_bar,text='   x  ',
            command=self.root.destroy,)
        self.expand_btn=ttk.Button(self.title_bar,text='[]',
                     
                    )
        self.minimize_btn=ttk.Button(self.title_bar,text='  -  ',
                                     )
        self.title_bar_title=ttk.Label(self.title_bar,text='Mini Db Browser',
                                       style='light'
                                   )
        
        
        
        # PACKING THE WIDGETS
        self.title_bar.pack(expand=1,fill=X)
        self.close_btn.pack(side=RIGHT)
        self.close_btn.pack(side=RIGHT)
        self.expand_btn.pack(side=RIGHT)
        self.minimize_btn.pack(side=RIGHT)
        self.title_bar_title.pack(side=LEFT, padx=10)
        
        # Ui the main area of the windows , this is where the actual app will go
        self.ui=Ui(self.root,repository=self.repository,controller=self.controller)
        
        
        # self.ui.pack(expand=1,fill=BOTH)
         
    def get_windows_pos(self,event):
        xwin=self.root.winfo_x()
        ywin=self.root.winfo_y()
        
        startx=event.x_root
        starty=event.y_root
        
        ywin =ywin -starty
        xwin=xwin-startx
        
        def move_windows(event):
            self.root.geometry('+{0}+{1}'.format(event.x_root+xwin,event.y_root+ywin))
        
        startx=event.x_root
        starty=event.y_root
        
        self.title_bar.bind('<B1-Motion>',move_windows)
        
            
            
        
        
    @DeprecationWarning            
    def start_plantforms(self):
        self.controller=HomeController()
        self.repository=Repository()
        self.style=Style(theme='darkly')
        self.root=Tk()#self.style.master
        self.root.overrideredirect(True)
        self.root.geometry('700x450+500+500')
        self.root.title('DB BROWSER')
    def start_app(self):
        self.root.mainloop()
        

if __name__=='__main__':
    app=App().start_app()