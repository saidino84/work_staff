import os
from pathlib import Path
import ttkbootstrap as ttk
import tkinter
class HomeController:
    
    
    def __init__(self) -> None:
        # self.list_files()
        self.images={
            'edit':'edit.png',
            'delete_user':'delete.png'
            }
        self.photho_images=[]
        
    def list_files(self,args):
        root_path=Path().parent
        data=os.listdir(f'{root_path}/assets/app_icons')
        print(data,root_path)
    def get_icon(self,icon_name,generic_name):
        '''icon_name: is the name of icon image of asset
            generic_name: is the name that you'll use to call that icon   
        # '''
        self.images[generic_name]=icon_name
        root_path=Path().parent
        _icon_path=os.path.join(root_path,'app/assets','app_icons',icon_name)
        
        _icon=tkinter.PhotoImage(name=generic_name,file=_icon_path,)
        self.photho_images.append(_icon)
        return generic_name