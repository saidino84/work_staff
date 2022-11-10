#:__author__: Saide Adamo

import tkinter as tk
from datetime import datetime

from ttkbootstrap import DateEntry, Style, ttk
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.constants import *
from ttkbootstrap.icons import Icon

from app.controllers.home_controller import HomeController

class Componets:
    
    def __init__(self) -> None:
        
        self.input_tnumber_var=tk.StringVar()
        self.input_tdestiny_var=tk.StringVar()
        self.input_tuser_var=tk.StringVar()
        self.entry_tpercents_var=tk.StringVar(value='17,10')
        self.entry_tdate_var=tk.StringVar(value='542')
        self.entry_tsubtotal_var=tk.StringVar(value='10')
        self._entry_ttotal_var=tk.StringVar()
        self.controler=HomeController()
        self.total=tk.StringVar()
        self.entry_parcet_trans_varone=tk.StringVar(value='10%')
        self.entry_parcet_trans_varsecond=tk.StringVar(value='10%')
        self.entry_parcet_trans_varone=tk.StringVar(value='10%')
        
        
    
    @property
    def entry_ttotal_var(self)->tk.StringVar:
        print('GETTING')
        _percents=self.entry_tpercents_var.get()
        if _percents and self.entry_tsubtotal_var.get() ==None:
            print('falling into simple')
            return self.entry_tsubtotal_var.get()
            
        dados=_percents.split(',')
        if len(dados) ==2 and self.entry_tsubtotal_var.get() !=None and self.entry_tsubtotal_var.get().isnumeric:
            _vat,_trans=dados[0],dados[1]
            _subtotal=self.entry_tsubtotal_var.get()
            try:
                perc=(int(_vat)*int(_subtotal)/100)+_subtotal
                transp=(int(_trans)*int(perc)/100)+perc
            except Exception as e:
                self._setup_tooltip(self.first_entry_tpercents,message=f'{e}')
                

        self._entry_ttotal_var= tk.StringVar(value=f'{(17*int(self.entry_tsubtotal_var.get())/100)+int(self.entry_tsubtotal_var.get())}')
        print(f'TOTAL xx:{self._entry_ttotal_var}')
        return self._entry_ttotal_var
    
    def clear_subtotal(self,*kw):
        self.input_tsubtotal.delete(0,20)
    
    def calc_total(self,*args):
        print('GETTING TOTAL')
        print('total Var',self.entry_ttotal_var)
        self.total.set(f"{self.entry_ttotal_var.get():,}")
        print('Total',self.total)
        self.input_ttotal.update()
        # self.input_ttotal.configure(textvariable=self.total)
        
    
        
    def setup_form(self,root:ttk.Frame):
        '''This setups Form View'''
        self.fram_ds=ttk.Frame(root)
        
        self.fram_ds.grid(row=0,column=0)
        
        for i in range(3):
            self.fram_ds.rowconfigure(index=i,weight=1)
            self.fram_ds.columnconfigure(index=i,weight=1)
            # self.co
        
        '''numero'''
        self.label_tnumer=ttk.Label(self.fram_ds,text='Transfer Number',justify='left')
        self.label_tnumer.grid(row=0,column=0,sticky=W,)
        self.input_tnumber=ttk.Entry(self.fram_ds,width=10,)
        self.input_tnumber.grid(row=1,column=0,ipadx=10,sticky='ew',)
        
        '''data'''
        self.label_tdate=ttk.Label(self.fram_ds,text='Transfer Date',)
        self.label_tdate.grid(row=0,column=1,padx=(10,10),sticky=W)
        self.entry_tdate=DateEntry(self.fram_ds,startdate=datetime.today(),)
        self.entry_tdate.grid(row=1,column=1,padx=10,sticky='ew',)
  
        '''descriptions'''
        self.label_tdate=ttk.Label(self.fram_ds,text='Description')
        self.label_tdate.grid(row=2,column=0,pady=5,sticky=W)
        self.input_tnumber=ttk.Entry(self.fram_ds,)
        self.input_tnumber.grid(row=3,column=0,columnspan=3,ipadx=75,sticky='nsew',pady=(5,10))
        
        '''subtotal'''
        valdate_subtotal=self.fram_ds.register(self.controler.validate_subtotal)
        space=ttk.Label(self.fram_ds,text='')
        self.label_tsubtotal=ttk.Label(self.fram_ds,text='Subtotal',justify='left')
        self.label_tsubtotal.grid(row=4,column=0,sticky=W,)
        self.input_tsubtotal=ttk.Entry(self.fram_ds,width=10,textvariable=self.entry_tsubtotal_var)
        self.input_tsubtotal.grid(row=5,column=0,ipadx=10,sticky='ew',)
        self.input_tsubtotal.bind('<FocusIn>',self.clear_subtotal)
        # self.fram_ds.bind('<key>',self.calc_total)
        
        '''percents'''
        self.label_tpercents=ttk.Label(self.fram_ds,text='Vat/Transport')
        self.label_tpercents.grid(row=4,column=1,padx=(10,10),sticky='nesw')
        
        self.vat_frame=ttk.Frame(self.fram_ds)
        self.vat_frame.grid(row=5,column=1,padx=10,sticky='ew')
        
        self.first_entry_tpercents=ttk.Spinbox(self.vat_frame,width=6,values=('17','0',))
        self.first_entry_tpercents.grid(row=0,column=0,sticky='nesw',)
    
        self.second_entry_tpercents=ttk.Spinbox(self.vat_frame,width=6,values=[15,10,7,5,3],textvariable=self.entry_parcet_trans_varone)
        self.second_entry_tpercents.grid(row=0,column=1,sticky='nesw',padx=10)
        
        self.thirty_entry_tpercents=ttk.Spinbox(self.vat_frame,width=6,values=[15,10,7,5,3])
        self.thirty_entry_tpercents.grid(row=0,column=2,padx=(10,10))
    
        
        '''User'''
        
        self.label_tuser=ttk.Label(self.fram_ds,text='User',justify='left',)
        self.label_tuser.grid(row=0,column=3,sticky='nesw',padx=10)
        self.input_tuser=ttk.Combobox(self.fram_ds,width=10, values=['Saide Adamo','Jonas Saidino Faquito','Claudia Saidino','Ancha Adamo'])
        self.input_tuser.current(0)
        self.input_tuser.grid(row=1,column=3,ipadx=10,sticky='ew',padx=10,)
        
        '''destine'''
        self.label_tdestiny=ttk.Label(self.fram_ds,text='Destiny',)
        self.label_tdestiny.grid(row=2,column=3,pady=5,sticky='nsew',padx=10)
        self.input_tdestiny=ttk.Entry(self.fram_ds,textvariable=self.input_tdestiny_var)
        self.input_tdestiny.grid(row=3,column=3,columnspan=3,ipadx=75,sticky='ew',padx=10,pady=(5,10))
        
        
        '''total'''
        self.label_ttotal=ttk.Label(self.fram_ds,text='Total',)
        self.label_ttotal.grid(row=4,column=3,pady=5,sticky='nsew',padx=10)
        self.input_ttotal=ttk.Entry(self.fram_ds,textvariable=self.total,state=DISABLED)
        self.input_ttotal.grid(row=5,column=3,columnspan=3,ipadx=75,sticky='nsew',padx=10,pady=(5,10))
        
        
        """btn save"""
        self.btn_save=ttk.Button(self.fram_ds,text='Salvar',style='TButton.sucess',
                                 command=self.calc_total,#image=self.controler.get_icon('but_new.png','save')
                                 )
        self.btn_save.grid(row=6,column=0,sticky=W,pady=10)
    
    
        
        
    
        
        
            