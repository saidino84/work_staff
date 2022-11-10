from datetime import datetime
from pathlib import Path
import os
import tkinter as tk
from ttkbootstrap import ttk,DateEntry,Style
from ttkbootstrap.constants import *

class TransfereceRegistForm():
    def __init__(self, root:ttk.Frame) -> None:
        """_regis form_
            root (ttk.Frame): _receives root to for those widgets be placed in that root_
        """
        self.root=root
        self.delivered_var=tk.BooleanVar()
    def buid_widgets(self):
        '''trans number'''
        entry_style=Style().configure('stack.TEntry',bordercolor='#900B73',fieldbackground='#4609AF8C')
        for i in [0,1,2]:
            self.root.rowconfigure(index=i,weight=1)
            self.root.columnconfigure(index=i,weight=1)
        # self.root.rowconfigure(index=2,weight=1,minsize=20)
        self.config_label=ttk.LabelFrame(self.root,text='Controls')
        self.config_label.grid(row=0,column=0,sticky='nsew',padx=10,pady=2)
        
        self.switch_delivered=ttk.Radiobutton(self.config_label,text='Devolvido',variable=self.delivered_var,value=1)
        self.switch_delivered.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')
        
        self.switch_delivered=ttk.Radiobutton(self.config_label,text='Pendente',variable=self.delivered_var,value=2)
        self.switch_delivered.grid(row=1,column=0,padx=5,pady=5,sticky='nsew')
        
        # self.switch_delivered=ttk.Radiobutton(self.root,text='Pendente',variable=self.deliverd_var,value=2)
        # self.switch_delivered.grid(row=0,column=0,padx=5,pady=5,sticky='nsew')
        '''Frame for input fields'''
        self.input_fileds_frame=ttk.Frame(self.root,padding=10)
        self.input_fileds_frame.grid(row=0,column=1,padx=10,pady=10,sticky='nsew')
        
        self.label_tnumber=ttk.Label(self.input_fileds_frame,text='Transference Number',padding=0,anchor='w',justify='left',style='info')
        self.label_tnumber.grid(row=0,column=1,padx=10,pady=(10,0),sticky='w')
        
        self.input_tnumber=ttk.Entry(self.input_fileds_frame,)
        self.input_tnumber.grid(row=1,column=1,padx=10,pady=(0,10),sticky='w')
        
        '''trans date'''
        self.label_tdate=ttk.Label(self.root,text="Data da Transferencia",padding=0,anchor='w',justify='left',style='info')
        self.label_tdate.grid(row=0,column=2,padx=10,pady=(10,0),sticky='w')
        
        self.label_tdate=DateEntry(self.root,startdate=datetime.today(),)
        self.label_tdate.grid(row=1,column=2,padx=10,pady=(0,10),sticky='w')
        """subtotal"""
        self.label_tsubtotal=ttk.Label(self.input_fileds_frame,text='User',padding=0,anchor='w',justify='left',style='info')
        self.label_tsubtotal.grid(row=2,column=1,padx=10,pady=(10,0),sticky='w')
        
        self.input_tsubtotal=ttk.Entry(self.input_fileds_frame,)
        self.input_tsubtotal.grid(row=3,column=1,sticky='ew',padx=10,pady=10)
        
        """user"""
        self.label_tnumber=ttk.Label(self.input_fileds_frame,text='User',padding=0,anchor='w',justify='left',style='info')
        self.label_tnumber.grid(row=4,column=1,padx=10,pady=(10,0),sticky='w')
        
        self.input_tnumber=ttk.Entry(self.input_fileds_frame,style='info',)
        self.input_tnumber.grid(row=5,column=1,sticky='nsew',padx=10,pady=(0,10),)
        
        
        '''descriptions'''
        self.label_tdescription=ttk.Label(self.input_fileds_frame,text='User',padding=0,anchor='w',justify='left',style='info')
        self.label_tdescription.grid(row=7,column=1,padx=10,pady=(10,0),sticky='w')
        # self.trans_descriptions=ScrolledText(self.root,
        #                     highlightcolor=self.root.master.master.master.master.master.style.colors.danger,
        #                     highlightbackground=self.root.master.master.master.master.master.style.colors.border,
        #                     highlightthickness=1,height=20,
        #                     )
        # self.trans_descriptions.grid(row=8,column=1,sticky='nsw',padx=(10,0),pady=10,rowspan=2)
        
        """btn save"""
        self.btn_save=ttk.Button(self.input_fileds_frame,text='Salvar',style='Link.TButton',width=40,
                                 command=self.list_files,image=self.get_icon('but_new.png','save'))
        self.btn_save.grid(row=12,column=1,sticky='w',padx=10,pady=10)
        
    
    def list_files(self):
        root_path=Path().parent
        data=os.listdir(f'{root_path}/assets/')
        print(data,root_path)
    def get_icon(self,icon_name,generic_name):
        root_path=Path().parent
        _icon_path=os.path.join(root_path,'assets','icons',icon_name)
        self._icon=tk.PhotoImage(name=generic_name,file=_icon_path,)
        
        return generic_name
        
        
        
        
        
        
        
        
