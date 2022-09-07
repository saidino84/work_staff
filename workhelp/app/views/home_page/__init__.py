from cProfile import label
import tkinter as tk
from tkinter.tix import Tree
from ttkbootstrap import ttk as bttk,Meter
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from turtle import width
from app.app import LogicApp
from ttkbootstrap.tooltip import ToolTip
from random import choice
from app.constants import Utils
# from app.views.iva_calc import IvaCalculator
class HomePage(bttk.Frame):
    
    def __init__(self,root:LogicApp):
        bttk.Frame.__init__(self)
        self.root=root
        # Making the app responsive
        self.style=bttk.Style()
        # self.style.configure("main.TFrame",background=Utils.primary_color)
        
        self.configure(style="main.TFrame")
        for index in [0,1]:
            # if index==1:
            self.columnconfigure(index=index,weight=1)
            self.rowconfigure(index=index,weight=1)
        
        # SETTINGS VARIABLES '''''''
        self.use_dark_var=tk.BooleanVar(value=True)
        self.setup_widgets()
        
    def setup_widgets(self):
        self.left_frame_views()
        self.center_frame_views()
        self.right_frame_views()
        # ...
    
    
    
    def left_frame_views(self):
        '''configuration frame'''
        self.config_frame=bttk.LabelFrame(self,text="Configurations",padding=(20,10))
        self.config_frame.grid(
            row=0,column=0,padx=(20,20),pady=(20,10),sticky='ew'
        )
        self.check_1=bttk.Checkbutton(
            self.config_frame,text='Unchecked',style='success.TCheckbutton',
        )
        self.check_1.grid(row=0,column=0,padx=5,pady=10,sticky='nsew')
        
        self.check_2=bttk.Checkbutton(
            self.config_frame,text="Use Lowercase",style='warning.TCheckbutton',
        )
        self.check_2.grid(row=1,column=0,padx=5,pady=10,sticky='nsew')
        
        
        self.check_3=bttk.Checkbutton(self.config_frame,text='Log In as Root')
        self.check_3.grid(row=2,column=0,padx=5,pady=10,sticky='nsew')
        
        self.check_4=bttk.Checkbutton(self.config_frame,text="Programer",state='Disabled',
                                     style='danger.TCheckbutton')
        self.check_4.grid(row=3,column=0,padx=5,pady=5,sticky='nsew')
        # METER
       
        
        # SEPARADOR
        self.separator=bttk.Separator(self)
        self.separator.grid(row=1,column=0,padx=(20,10),pady=10,sticky='ew')
        
        
        self.user_configs=bttk.LabelFrame(self,text='User rules',padding=(20,10))
        self.user_configs.grid(row=3,column=0,sticky='nsew',padx=(20,10),pady=(10,20))
        
        
        self.use_dark=bttk.Radiobutton(self.user_configs,text='Use dark',
                                      padding=(20,10),variable=self.use_dark_var,value=1)
        self.use_dark.grid(row=0,column=0,)
        
        self.use_light=bttk.Radiobutton(self.user_configs,text='Use Light',padding=(20,10),variable=self.use_dark_var,value=2)
        self.use_light.grid(row=1,column=0,)
        
        self.separator_1=bttk.Separator(self.user_configs)
        self.separator_1.grid(row=2,column=0,padx=(10,10),pady=10,sticky='ew')
        self.data_calc=Meter(master=self.user_configs,bootstyle="success", subtextstyle="warning",amounttotal=100,amountused=45)
        self.data_calc.grid(row=3,column=0)
        
        

        

    def center_frame_views(self):
        
        """configure center frame"""
        
        paddings=(10,20)
        self.commands_frame=bttk.Frame(self,padding=(0,0,0,10))
        
        self.commands_frame.grid(row=0,column=1,padx=10,pady=(20,10),sticky='ew',rowspan=3)
        self.commands_frame.columnconfigure(0,weight=1)
        # self.rowconfigure(index=1,minsize=120)
        """adding components"""
        spacer=bttk.Label(self.commands_frame,text="-DB  B R O W S E R-  ")
        spacer.grid(row=0,column=0)
        
        self.search_input=bttk.Entry(self.commands_frame,)
        self.search_input.grid(row=1,column=0,padx=5,pady=(0,10),sticky='ew')
        
        self.maxim_list_data_display=bttk.Spinbox(self.commands_frame,values=("one","two","three",'four'))
        self.maxim_list_data_display.insert(2,"Spin")
        self.maxim_list_data_display.grid(row=2,column=0,padx=5,pady=10,sticky='ew')
        
        self.menu=tk.Menu(self)
        self.menu.add_command(label="Fechar App")
        self.menu.add_command(label="Comando Proximo")
        self.menu.add_command(label="Comando Ultimo")
        self.menu.add_separator()
        self.menu.add_checkbutton(label="Root",state='disabled',)
        self.menu.add_command(label="Show calc",command=self.root.show_calc)
        
        self.menu_btn=bttk.Menubutton(self.commands_frame,text='Options',menu=self.menu,direction='right')
        self.menu_btn.grid(row=3,column=0)
        
        self.btn_lauch_calc=bttk.Button(self.commands_frame,text="Calc Help",padding=(20,10),
                                        style='info.outline.TButton',command=self._launch_calc)
        self.btn_lauch_calc.grid(row=3,column=0)
        
        
   
        
    def right_frame_views(self):
        
        # PanedView
        self.panned=bttk.PanedWindow(self) 
        self.panned.grid(row=0,column=1, pady=(25,2),sticky='nsew',rowspan=3)
        
        #pane 1
        self.pane_1=bttk.Frame(self.panned,padding=5)
        self.panned.add(self.pane_1,weight=1)
        
        self.add_search_input()
        self.add_tableview()
        
       
    def add_search_input(self):
        self.search_container=bttk.Frame(self.pane_1,padding=10)
        self.search_container.pack(side='top',expand=True,fill='x')
        self.search_container.columnconfigure(index=0,weight=2)
        self.inpt_search=bttk.Entry(self.search_container)
        self.inpt_search.grid(row=0,column=0,sticky='ew',padx=10,pady=5)
        self.btnsearch=bttk.Button(self.search_container,text="LookUp",style='TButton')
        self.btnsearch.grid(row=0,column=1)
        
    def add_triview(self):
         # Scrollbar
        self.treev_scroller_y=bttk.Scrollbar(self.pane_1)
        # self.treev_scroller_y.pack(side='right',fill='y')
        
        self.treev_scroller_x=bttk.Scrollbar(self.pane_1,orient='horizontal')
        # self.treev_scroller_x.pack(side='bottom',fill='x')
        # TreeView
        
        self.treeview = bttk.Treeview(self.pane_1,
                                      selectmode='browse',
                                      yscrollcommand=self.treev_scroller_y.set,
                                      xscrollcommand=self.treev_scroller_x.set,
                                      columns=(1,2),
                                      height=10,
                                      style='sucess.Treeview',
                                      )

        self.treeview.pack(expand=True,fill='both')
        self.treev_scroller_y.config(command=self.treeview.yview)
        self.treev_scroller_x.config(command=self.treeview.xview)
        
        # Treeview columns 
        self.treeview.column("#0",anchor='w',width=120)
        self.treeview.column(1,anchor='w',width=120)
        self.treeview.column(2,anchor='w',width=120)
        
    def add_tableview(self):
        self.tbview_container=bttk.Frame(self.pane_1,padding=2,style='danger.TFrame')
        self.tbview_container.pack(expand=True,fill='x')
        self.tableview=Tableview(
            self.tbview_container,
            coldata=[{'text':'id',"stretch":True,"minwidth":20,"width":60,"command":lambda :print('id')} ,
                     {'text':'Data',"stretch":True,"minwidth":20,"width":60,"anchor":E,"command":lambda :print('Data')},
                     {'text':'Numero',"stretch":True,"minwidth":20,"width":60,"anchor":CENTER,"command":lambda :print('Numero da Factura')},
                     {'text':'Subtotal',"stretch":True,"minwidth":20,"width":85,"anchor":W,"command":lambda :print('Subtotal')},
                     {'text':'Percentos',"stretch":True,"minwidth":20,"width":60,"anchor":E,"command":lambda :print('Percentagens')},
                     {'text':'Total',"stretch":True,"minwidth":20,"width":80,"anchor":W,"command":lambda :print('O Total da Factura')},
                     {'text':'Destino',"stretch":True,"minwidth":20,"width":80,"anchor":CENTER,"command":lambda :print('Destino da Transferencia')},
                     {'text':'User',"stretch":True,"minwidth":20,"width":60,"command":lambda :print('Apessoa que Fez a transferencia')},
                     {'text':'Description',"stretch":True,"minwidth":20,"width":100,"anchor":CENTER,"command":lambda :print('Descreve os produtos que enviaste')},],
            rowdata=
                # (1,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (2,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (3,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (4,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (5,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (6,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (7,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (8,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (9,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (10,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (11,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (12,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                # (13,'05/09/2022',6425,7854.24,[17,10],29801,'Armazem Muxara','Saidino','Carne Nacional , Vorse, Babalaze '),
                
                list((x,
                      '05/09/2022',
                      6425+x,
                      7854.24,
                      [choice([0,17]),choice([15,10,7,5,1])],
                      29801+x
                      ,choice(['Armazem Muxara',"Vip Montepuez","Maputo Armazem"]),
                      choice(['Saidino',"silvestre"]),
                      choice(['Carne Nacional , Vorse, Babalaze ',"congelados","Agua","Arroz","Electrodomesticos","Frutas","Secos"]))for x in range(160))
                
                ,
            bootstyle=DANGER,
             paginated=True,
             searchable=True,
            #  stripecolor=('#c98860',None),
             autofit=True,
             height=30,pagesize=40
            )
        self.tableview.pack(expand=True,fill=BOTH)
        
    
    def load_demodatas(self):
        from app.db.repository import treeview_data
        for item in treeview_data:
            self.treeview.insert(
                parent=item[0],index='end',iid=item[1],values=item[3]
            )
            if item[0]=='' or item[1] in {8,21}:
                self.treeview.item(item[1], open=True) #open parents
        
        self.treeview.selection_set(10)
        self.treeview.see(7)
    
    def _launch_calc(self):
        self.root.show_calc()
        ...
    def _setup_tooltip(self,widget,message="especify message to your widget"):
        ToolTip(widget=widget,text=message,bootstyle=(DANGER,INVERSE))