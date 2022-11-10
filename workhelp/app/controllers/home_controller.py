import os
from pathlib import Path
import tkinter


class HomeController:
    
    def __init__(self) -> None:
        ...
    
    def list_files(self):
        root_path=Path().parent
        data=os.listdir(f'{root_path}/assets/')
        print(data,root_path)
    def get_icon(self,icon_name:str,generic_name:str):
        '''icon_name: is the name of icon image of asset
            generic_name: is the name that you'll use to call that icon   
        '''
        root_path=Path().parent
        _icon_path=os.path.join(root_path,'assets','icons',icon_name)
        self._icon=tkinter.PhotoImage(name=generic_name,file=_icon_path,)
        
        return generic_name
    
    def validate_subtotal(value:str):
        if value.isnumeric or value=='':
            return True
        return False

        