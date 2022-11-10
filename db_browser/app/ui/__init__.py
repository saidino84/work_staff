from tkinter import IntVar, StringVar
from ttkbootstrap.constants import W
from app.db.repository.repository import Repository 

from ttkbootstrap import ttk
from ttkbootstrap.style import Style
from app.controllers.app_controller import HomeController


class Ui():
    def __init__(self,root:ttk.Widget,repository:Repository,controller:HomeController):
        self.root=root
        self.controller=controller
        self.repository=repository
        
        self.selected_item_var_id=IntVar()
        self.name_entry_var=StringVar()
        self.entry_age_var=IntVar()
        self.email_entry_var=StringVar()
        self.entry_msg_var=StringVar()
        
        self.start_widgets()

    def start_widgets(self):
        self.frame=ttk.Frame(self.root,padding=32)
        self.frame.pack(expand=True,fill='both')
        self.frame.columnconfigure(index=1,weight=1)
        # frame.rowconfigure(index=3,weight=1)
        # frame.columnconfigure(index=)


        self.label=ttk.Label(self.frame,text='Name :')
        self.label.grid(row=0,column=0,sticky='nsew')
        self.name_entry=ttk.Entry(self.frame,textvariable=self.name_entry_var)
        self.name_entry.grid(row=0,column=1,padx=10,sticky='ew')

        self.label_ege=ttk.Label(self.frame,text='Idade')
        self.label_ege.grid(row=0,column=2)
        self.entry_age=ttk.Entry(self.frame,textvariable=self.entry_age_var)
        self.entry_age.grid(row=0,column=3,padx=(5,10))

        self.space=ttk.Label(self.frame,padding=3)
        self.space.grid(row=1,column=0)

        self.label_email=ttk.Label(self.frame,text='Email :')
        self.label_email.grid(row=2,column=0,sticky='nsew')
        self.email_entry=ttk.Entry(self.frame,textvariable=self.email_entry_var)
        self.email_entry.grid(row=2,column=1,padx=10,sticky='ew')
        
        self.label_id=ttk.Label(self.frame,text='ID :')
        self.label_id.grid(row=2,column=2,sticky='nsew')
        self.email_id=ttk.Entry(self.frame,textvariable=self.selected_item_var_id,
                                state="readonly")
        self.email_id.grid(row=2,column=3,padx=10,sticky='ew')
        

        self.btn_send=ttk.Button(self.frame,text='Save')
        self.btn_send.grid(row=3,column=1,columnspan=3,sticky='ew',padx=10,pady=15)
        self.btn_send.bind('<Button-1>',self.confirm_send)

        scrollex=ttk.Scrollbar(self.frame)
        self.frame.rowconfigure(index=4,weight=1)
        self.frame.columnconfigure(index=1,weight=1)
        
        self.treeview=ttk.Treeview(self.frame,show='headings',height=5,selectmode='browse')
        self.treeview.grid(row=4,column=1,sticky='nsew',padx=10,ipadx=5,columnspan=5)
        self.treeview.configure(columns=('Id','Name','Age','Email','Password'))
       
        self.treeview.column('Id',width=20,stretch=True)
        self.treeview.column('Name',width=120,stretch=True)
        self.treeview.column('Age',width=20,stretch=True)
        self.treeview.column('Email',width=20,stretch=True)
        self.treeview.column('Password',width=20,stretch=True)
        self.treeview.bind("<ButtonRelease-1>",self.get_selected_item)
        # for treeview show the columns , is needed to call it with headins
        for col in self.treeview['columns']:
            self.treeview.heading(col,text=col.title(),anchor=W)
        
        
        self._update_treeview()
        self.draw_icon_btn()
        
        self.draw_message_form()
    def draw_message_form(self):
   
        
        self.entry_message=ttk.Entry(self.frame,
                                textvariable=self.entry_msg_var,
                                     
                                     )
        self.entry_message.grid(row=5,column=1,columnspan=2,
                                sticky='ew',padx=(10,0),pady=10)
        
        self.frame.rowconfigure(index=5,weight=1)
        
        self.frame_for_msg=ttk.Frame(self.frame)
        self.frame_for_msg.grid(row=5,column=3,sticky='e',ipadx=10,pady=(10,10))
        
        self.frame_for_msg.columnconfigure(index=1,weight=1)
        
        self.entry_user_id=ttk.Combobox(self.frame_for_msg,width=10,values=self.repository.list_of_user_ids())  # type: ignore
        self.entry_user_id.current(0)
        self.entry_user_id.grid(row=1,column=0,sticky='e',padx=5)
        
        self.btn_send_msg=ttk.Button(self.frame_for_msg,text='Save',command=self.save_message)
        self.btn_send_msg.grid(row=1,column=2,sticky='e',)        

        
    def draw_icon_btn(self):
        
        _frame_quick_shortcut=ttk.Frame(self.frame,)
        _frame_quick_shortcut.grid(row=4,column=0)
        btn_delete_user=ttk.Label(_frame_quick_shortcut,text='Delete',
                                #   image=self.controller.get_icon('edit'),
                                  image=self.controller.get_icon('delete.png','deleteuser')
                                )
        btn_delete_user.grid(row=0,column=0,sticky=W,pady=2)
        btn_delete_user.bind('<Button-1>',lambda x:self.delete_record_by_id())
        
        self.btn_edit_user=ttk.Label(_frame_quick_shortcut,
                                      
                                      text='edit',
                                      image=self.controller.get_icon('eedit.png','edit')
                                )
        self.btn_edit_user.grid(row=1,column=0,)
        self.btn_edit_user.bind('<Button-1>',lambda x:self.edit_record_by_id())
    def confirm_send(self,*args):
        from ttkbootstrap.dialogs.dialogs import Messagebox
        try:
            id=self.selected_item_var_id.get()
        except Exception as e:
            self.selected_item_var_id.set(0)
        _name=self.name_entry_var.get()
        _age=self.entry_age_var.get()
        _email=self.email_entry_var.get()
        _id=self.selected_item_var_id.get()
        print(_id,' GOT ID VALUE')
        if _name ==None or len(_name)<4 or _email ==None or len(_email)<5 or _age ==None or _age<10:
            return Messagebox.ok(message='Dados Invalidos',title='Adicoa de Dados')
        assert(_name !=None)
        message=self.repository.create_or_update_pessoa(
            name=_name,
            email=_email,
            idade=int(_age),
            id=_id
            )
                                        
        print(f'{_name},       {_age} ==== {_email}')                       
        d=Messagebox.ok(message=message,title='Adicoa de Dados')
        self.treeview.update()
        self._update_treeview()
        self.entry_user_id.configure(values=self.repository.list_of_user_ids())  # type: ignore
        
        self.clear_entry()
    def save_message(self):
        self.repository.add_message(self.entry_msg_var.get(),int(self.entry_user_id.get()))
        #TODO CREATE FULLL DESIGN
        # self.treeview.insert(parent='fond',index='end',values=('subItem','lost','pradice'))
    def clear_entry(self):
        for i in [self.name_entry_var,self.selected_item_var_id,self.email_entry_var,self.entry_age_var]:
            i.set('')
        ...
    def get_selected_item(self,*kw):
        data=self.treeview.selection()[0]
        record_id=int(self.treeview.item(self.treeview.selection()[0])["values"][0])
        self.selected_item_var_id.set(record_id)
        print('[getting data]')
        self.get_user_message(int(record_id))
        
        self.edit_record_by_id()
    def delete_record_by_id(self):
        
        self.repository.delete_pessoa(int(self.selected_item_var_id.get()))
        self._update_treeview()
        self.entry_user_id.configure(values=self.repository.list_of_user_ids())  # type: ignore
        
        
    
    def edit_record_by_id(self):
        _record_id=self.treeview.item(self.treeview.selection()[0])['values'][0]
        record=self.repository.get_user_by_id(int(_record_id))
        self.name_entry_var.set(str(record.nome))
        self.email_entry_var.set(str(record.email))
        self.entry_age_var.set(int(str(record.idade)))
        print('MESSAGES')
        self.entry_user_id.configure(values=self.repository.list_of_user_ids())  # type: ignore
        
    
    def get_user_message(self,id:int):
        messages=self.repository.get_user_by_id(id)
        all_msg=''.join(messages)
        self.entry_msg_var.set
        
        
        
    def _update_treeview(self):
        
        # filter(lambda x:self.treeview.delete(x),self.treeview.get_children())
        # x for self.treeview.insert('','end',)
        [self.treeview.delete(x) for x in self.treeview.get_children()]
        [self.treeview.insert('','end',values=(i.id,i.nome,i.idade,i.email)) for i in self.repository.get_users()]
        #
        # for i in self.repository.get_users():
        #     self.treeview.insert('','end',values=(i.id,i.nome,i.idade,i.email))
        #     print('updated')


