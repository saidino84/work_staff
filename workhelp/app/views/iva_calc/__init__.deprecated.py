from tkinter import *
import tkinter as tk
import tkinter
# import customtkinter as ctk
from tkinter import ttk
import re
from app.constants import Utils

class IvaCalculator(ttk.Frame):
    blue00f="#0D47A1"
    def __init__(self,root) -> None:
        super().__init__(root)
        self.root=root
        # self.bg_color='#1A237E'
        self.bg_color=Utils.bgColor
        self.style=ttk.Style()
        
        # self.bind('<FocusIn>',self.print_em)
        self.root.bind('<Key>',self.make_calculation)
        self.string_find_pattern=re.compile(r'[a-z|A-Z].+',flags=re.DOTALL)
        
        '''variables'''
        self.is_readonly_var=BooleanVar(value=True)
        self.txt_var_res=StringVar()
        
        self.allowed=[1,2,3,4,5,6,7,8,9,0]
        
        ''''TODO  vars '''
        
        # self.bind('<FocusIn>',self.print_em)
        
        # self._style_frame(self.fram_ivas,self.bg_color)
        self.buildwidgets()
    def _style_frame(self,fram:ttk.Frame,color):
        style=ttk.Style()
        style.configure(f'{fram}.TFrame',background=color)
        fram.configure(style=style)
        
    def buildwidgets(self):
        self.rowconfigure(0,weight=2,)
        self.columnconfigure(0,weight=1)
        
        # row 2
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=2)
        
        self.fram_input=ttk.Frame(self,)
        self.fram_input.grid(row=0,column=0,columnspan=2,rowspan=4,sticky='nsew')
        self.fram_input.columnconfigure(0,weight=1)
        
        self.input=ttk.Entry(self.fram_input,font=('Ubunto',40,'bold'))
        
        self.bind('<Return>',self.calc_parcent)
        self.input.grid(row=0,column=0,sticky="nwe",ipady=30)
        
        '''styling frames'''
        
        # self.style.configure("TFrame",background="#0f47c2")
        self.style.configure("ivas_frame.TFrame",background=Utils.bgColor)
        
        
        self.fram_ivas=ttk.Frame(self,style="ivas_frame.TFrame")
        self.fram_ivas.grid(row=1,column=0,pady=10)
        self.input_ivas=ttk.Combobox(self.fram_ivas,values=('17',"15","10","5","1",),state="readonly" if self.is_readonly_var else "normal")
        self.input_ivas.grid(row=0,column=1)
        
        self.check_readonly=ttk.Checkbutton(self.fram_input,
            variable=self.is_readonly_var,
            offvalue="Off",onvalue="On",
            command=self.set_readable,
            )
        self.check_readonly.grid(row=0,column=2)
        
        self.fram_res=ttk.Frame(self,style='TFrame')
        self.fram_res.grid(row=2,column=0,)
        self.lbl_res=ttk.Label(self.fram_res,text='0.0',
                                  font=('Ubunto', 32,'italic')
                                )
        self.lbl_res.configure(justify=tkinter.CENTER)
        self.lbl_res.grid(row=0,column=0,ipadx=50,)
        ...
    def set_readable(self):
        # print(self.is_readonly_var.get())
        #self.is_readonly_var.set(not self.is_readonly_var)
        print(self.is_readonly_var.get())
        if self.is_readonly_var:
            self.input_ivas['state']='readonly'
            self.input_ivas.configure(state='readonly')
        else:
            self.is_readonly_var['state']='normal'
            self.input_ivas.configure(state='normal')
            
    def calc_parcent(self,e):
        print("returned",self.input.get())
        if self.input.get()=='1':
            self.lbl_res['text']=20
            self.lbl_res.configure(foreground='green')
            
        else:
            self.lbl_res['text']='Not Allowed !'
            self.lbl_res.configure(foreground='#ffc2c2')
        ...
    def update_res(self) -> None:
        ...
    def check_data(self):
        value=self.input.get().strip()
        # print(value,"Value [1]")
        findstr=self.string_find_pattern.findall(value)
        # print(findstr,'data found')
        return findstr
    def make_calculation(self,event):
        value=self.check_data()
        if self.string_find_pattern.match(self.input.get()) and self.check_data() ==[]:
            print('\033[31;43mYou typed strings\033[m')
        else:
            print('\033[32mYOU TYPED NUMBER\033[m')
            try:
                
                res=float(self.input.get())
                print(res)
                parcet=(res/100)*int(self.input_ivas.get())+res
                self.lbl_res.configure(foreground='#ffffff')
                self.lbl_res['text']="{:.2f}".format(parcet)
            except Exception as e:
                print('\033[31;43mYou typed strings\033[m')
                self.lbl_res['text']='0.0'
                self.lbl_res.configure(foreground="#ff0000")
        #d=self.input.delete(0,10)
        return 
        
        # if event.widget==self:
        # print(" deleted sucessfully {}".format(d))
        # self.label['text']='None'
        
        self.lbl_res['text']="01.0"
        self.calc_parcent(event)
        
