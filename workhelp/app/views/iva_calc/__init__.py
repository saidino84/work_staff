from tkinter import *
import tkinter as tk
import tkinter
from tkinter import ttk
import re,os
from PIL import Image, ImageTk


class IvaCalculator(ttk.Frame):
    blue00f="#0D47A1"

    def __init__(self,root,ic_close='',) -> None:
        super().__init__(root)
        self.background="#ffcccc"
        self.root=root
        self.ic_close=ic_close
        self.bg_color='#1A237E'
        self.style=ttk.Style()
        # self._style_frame(self,"#ff0000")
        # self.configure(background="#ffd600")

        # self.bind('<FocusIn>',self.print_em)
        self.root.bind('<Key>',self.make_calculation)
        self.root.bind("<FocusIn>",self.clear_all)
        self.string_find_pattern=re.compile(r'[a-z|A-Z].+',flags=re.DOTALL)

        '''variables'''
        self.is_readonly_var=BooleanVar(value=True)
        self.txt_var_res=StringVar()

        self.allowed=[1,2,3,4,5,6,7,8,9,0]

        ''''TODO  *vars '''
        # self.bind('<FocusIn>',self.print_em)

        # self._style_frame(self.fram_ivas,self.bg_color)
        self.buildwidgets()
    def clear_all(self,event):
        self.input.delete(0,10)
    def _style_frame(self,fram:ttk.Frame,color):
        style=ttk.Style()
        style.configure(f'{fram}.TFrame',background=color)
        fram.configure(style=style)

    def buildwidgets(self):
        self.rowconfigure(0,weight=2,)
        self.columnconfigure(0,weight=1)

        # row 2
        self.rowconfigure(1,weight=3)
        # row 3
        self.rowconfigure(2,weight=2)

        self.fram_input=ttk.Frame(self,height=44)
        self.fram_input.grid(row=0,column=0,columnspan=2,rowspan=4,sticky='nsew')
        self.fram_input.columnconfigure(0,weight=1)

        self.input=ttk.Entry(self.fram_input,font=('Ubunto',28,'bold'))

        self.bind('<Return>',self.calc_parcent)
        self.input.grid(row=0,column=0,rowspan=2,sticky="n",pady=5)

        '''styling frames'''

        # self.style.configure("TFrame",background="#0f47c2")

        '''FRAME SPACE'''
        self.fram_fram_space=ttk.Frame(self,height=20)
        self.fram_fram_space.grid(row=1,column=0)
        self.lbl_top_info=ttk.Label(self.fram_fram_space,font=("ubunto",12,"normal"))
        self.lbl_top_info.grid(row=1,column=0)







        self.fram_ivas=ttk.Frame(self,style="TFrame")
        self.fram_ivas.grid(row=2,column=0,pady=30,ipady=20)
        self.input_ivas=ttk.Combobox(self.fram_ivas,values=('17',"15","10","5","1",),state="readonly" if self.is_readonly_var else "normal")
        self.input_ivas.grid(row=0,column=0)

        self.check_readonly=ttk.Checkbutton(self.fram_ivas,
            variable=self.is_readonly_var,
            offvalue="Off",onvalue="On",
            command=self.set_readable,
            )
        self.check_readonly.grid(row=0,column=1)

        self.operador_fram=ttk.Frame(self.fram_ivas,height=32)
        self.operador_fram.grid(row=1,column=0,columnspan=2)
        self.lbl_operador=ttk.Label(self.operador_fram,text="  +  ")
        self.lbl_operador.grid(row=0,column=0)
        self.input_ivas_2=ttk.Combobox(self.fram_ivas,values=("17","15","10","5","1"),state="readonly" if self.is_readonly_var else "normal")
        self.input_ivas_2.grid(row=2,column=0)




        self.check_readonly_2=ttk.Checkbutton(self.fram_ivas,
            variable=self.is_readonly_var,
            offvalue="Off",onvalue="On",
            command=self.set_readable,
            )
        self.check_readonly_2.grid(row=2,column=1)

        self.fram_res=ttk.Frame(self,
                    #style='TFrame',
                     )
        self.fram_res.grid(row=3,column=0,)
        self.lbl_res=ttk.Label(self.fram_res,text='0.0',
                                  font=('Ubunto', 26,'bold'),
                                )
        self.lbl_res.configure(justify=tkinter.LEFT)
        self.lbl_res.grid(row=0,column=0,ipadx=50,)

        self.lbl_res_last=ttk.Label(self.fram_res,text='0.0',
                                  font=('Ubunto', 10,'bold'), 
                                )
        self.lbl_res_last.configure(justify=tkinter.RIGHT,)
        self.lbl_res_last.grid(row=1,column=0,ipadx=50,)

        var=StringVar(value="System")
        # self.optionmenu_1 = ttk.OptionMenu(master=self.fram_res,
        #                     values=["Light", "Dark", "System"],
        #                     variable=var,
        #                     command=self.change_appearance_mode,
        #                     )
        # self.optionmenu_1.grid(row=1,column=0)
        ...
    def change_appearance_mode(self,event):
        # self.lbl_res.configure(foreground='#1565C0')
        ...
        ...
    def set_readable(self):
        # print(self.is_readonly_var.get())
        #self.is_readonly_var.set(not self.is_readonly_var)
        self.lbl_res.configure(foreground='#1565C0')
        print(self.is_readonly_var.get())
        if self.is_readonly_var.get():
            self.input_ivas['state']='readonly'
            self.input_ivas.configure(state='readonly')
        else:
            self.input_ivas['state']='normal'
            self.input_ivas.configure(state='normal')

    def calc_parcent(self,e):
         
        ...
    def evaluate_input(self) -> None:

        try:
            # self.lbl_res.configure(foreground='#ffd600')
            res=eval(self.input.get().strip())

            print(f'{res}  : RES')
            self.lbl_res['text']=res
            # self.lbl_res.configure(foreground='#ffd600')
        except Exception as e:
            # self.lbl_res.configure(foreground='#ffcccc')T

            ...
    def check_data(self):
        # self.lbl_res.configure(foreground='#1565C0')
        value=self.input.get().strip()
        # print(value,"Value [1]")
        findstr=self.string_find_pattern.findall(value)
        # print(findstr,'data found')
        return findstr
    def make_calculation(self,event):
        # self.lbl_res.configure(foreground='#1565C0')
        value=self.check_data()
        # self.lbl_res.configure(foreground='#1565C0')
        if self.string_find_pattern.match(self.input.get()) and self.check_data() ==[]:
            print('\033[31;43mYou typed strings\033[m')
        else:
            print('\033[32mYOU TYPED NUMBER\033[m')
            try:

                res=float(self.input.get())
                print(res)
                parcent=(res/100)*int(self.input_ivas.get())+res
                parcet_second=(parcent/100)*int(self.input_ivas_2.get())+parcent
                # self.lbl_res.configure(style="warning.Inverse.TLabel")
                # self.lbl_res['text']="{:,.2f}".format(parcet)

                # self.lbl_res_last.configure(foreground='#FFDE03')
                self.lbl_res_last["text"]="{:,.2f}".format(parcet_second)
            except Exception as e:
                print('\033[31;43mYou typed strings\033[m')
                # self.lbl_res['text']='0.0'
                # self.lbl_res.configure(style="danger.Inverse.TLabel")
                self.evaluate_input()
        #d=self.input.delete(0,10)
        # self.lbl_res.configure(foreground='#1565C0')
        # return self.lbl_res.configure(foreground='#1565C0')

        # if event.widget==self:
        # print(" deleted sucessfully {}".format(d))
        # self.label['text']='None'

        self.calc_parcent(event)
        self.lbl_res.configure(foreground='#ffc2c2')
    def on_closing(self,event=0):
        print('DESTROYED....')
        self.destroy()
