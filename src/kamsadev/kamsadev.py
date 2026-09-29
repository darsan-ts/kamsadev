from tkinter.constants import NORMAL


import customtkinter as ctk
import random
def show_kamsa_arguments():
    print("kamsadev(name,size,bg,theme,resizable,fullscreen,transparency,topmost,icon)")

def kamsahelp():
    print("""create window\n
    app=kamsadev()\n
    frame=kamsadev.kamsaframe()
    label=kamsadev.kamsalabel()
    button=kamsadev.kamsabutton()


    """)
def easter_egg(master=None):
    def random_strs():
        lvl = [30, 20, 69, 40, 30, 67, 28, 77, 90, 33]
        num = random.choice(lvl)
        names = [
            "sanus\n komsa level:100",
            f"shiva karthik\n komsa level:{num}",
            f"magizh\nkomsa level:{num}",
            f"darsan\nkomsa level:{num}"
        ]
        choice = random.choice(names)
        eglbl.configure(text=choice)

    # Use Toplevel if attached to an existing app; create CTk window if standalone
    if master:
        popup = ctk.CTkToplevel(master)
    else:
        popup = ctk.CTkToplevel()

    popup.title("KAMSADEV")
    popup.geometry("350x350")
    popup.resizable(False, False)
    popup.config(bg="black")
    popup.overrideredirect(True)

    eglbl = ctk.CTkLabel(popup, text="", bg_color="black", font=("impact", 30))
    egbtn = ctk.CTkButton(
        popup, 
        text="random", 
        hover_color="red", 
        fg_color="black", 
        text_color="white", 
        command=random_strs
    )
    egbtn.pack(pady=20)
    eglbl.pack()

    close = ctk.CTkButton(
        popup, 
        text="close", 
        fg_color="black", 
        hover_color="red", 
        command=popup.destroy
    )
    close.pack(side="bottom", pady=70)

    # Start loop only if running as a standalone window
    if not master:
        popup.mainloop()
    

class kamsadev(ctk.CTk):
    def __init__(self, name="TS", size="1920x1080", bg="#242424", theme="dark", resizable=True, fullscreen=False, transparency=1.0, topmost=False, icon=None, debug=False):
        super().__init__()
        self.title(name)
        self.geometry(size)
        self.config(bg=bg)
        ctk.set_appearance_mode(theme)
        self.resizable(resizable, resizable)
        self.attributes("-fullscreen", fullscreen)
        self.attributes("-alpha", transparency)
        self.attributes("-topmost", topmost)
        if icon:
            self.iconbitmap(icon)
        if debug:
            self.bind("<Button-1>", self.show_coordinates) 
    
    def show_coordinates(self, event):
        print(f"Clicked position -> x={event.x}, y={event.y}")
          
    def run(self):
        self.mainloop()


class kamsaframe(ctk.CTkFrame):
    def __init__(
        self, 
        master=None, 
        width=200, 
        height=200, 
        corner_radius=None, 
        border_width=None, 
        bg_color="transparent", 
        fg_color=None, 
        border_color=None, 
        prop=False,
        # PACK ARGUMENTS
        pack=True,
        side="top",
        fill="none",
        expand=False,
        padx=0,
        pady=10,
        ipadx=0,
        ipady=0,
        pack_anchor="center", 
        # PLACE ARGUMENTS
        place=False,
        x=0,
        y=0,
        relx=0.0,
        rely=0.0,
        # GRID ARGUMENTS
        grid=False,
        row=0,
        column=0,
        columnspan=1,
        rowspan=1,
        sticky="nsew",
        grid_padx=0,
        grid_pady=0,
        **kwargs
    ):
        super().__init__(
            master=master, 
            width=width, 
            height=height, 
            corner_radius=corner_radius, 
            border_width=border_width, 
            bg_color=bg_color, 
            fg_color=fg_color, 
            border_color=border_color, 
            **kwargs
        )
        
        self.pack_propagate(prop)
        
        if grid:
            self.grid(
                row=row,
                column=column,
                columnspan=columnspan,
                rowspan=rowspan,
                sticky=sticky,
                padx=grid_padx,
                pady=grid_pady
            )
        elif place:
            self.place(x=x, y=y, relx=relx, rely=rely)
        elif pack:
            self.pack(
                side=side,
                fill=fill,
                expand=expand,
                padx=padx,
                pady=pady,
                ipadx=ipadx,
                ipady=ipady,
                anchor=pack_anchor
            )


class kamsalabel(ctk.CTkLabel):
    def __init__(
        self,
        master=None,
        width=0,
        height=28,
        corner_radius=None,
        bg_color="transparent",
        fg_color=None,
        text_color=None,
        text_color_disabled=None,
        text="kamsaLabel",
        font=None,
        image=None,
        compound="center",
        anchor="center",
        # PACK ARGUMENTS
        pack=True,
        side="top",
        fill="none",
        expand=False,
        padx=0,
        pady=5,
        ipadx=0,
        ipady=0,
        pack_anchor="center",
        # PLACE ARGUMENTS
        place=False,
        x=0,
        y=0,
        relx=0.0,
        rely=0.0,
        # GRID ARGUMENTS
        grid=False,
        row=0,
        column=0,
        columnspan=1,
        rowspan=1,
        sticky="nsew",
        grid_padx=0,
        grid_pady=0,
        **kwargs
    ):
        super().__init__(
            master=master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            bg_color=bg_color,
            fg_color=fg_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            text=text,
            font=font,
            image=image,
            compound=compound,
            anchor=anchor,
            **kwargs
        )
        if grid:
            self.grid(
                row=row,
                column=column,
                columnspan=columnspan,
                rowspan=rowspan,
                sticky=sticky,
                padx=grid_padx,
                pady=grid_pady
            )
        elif place:
            self.place(x=x, y=y, relx=relx, rely=rely)
        elif pack:
            self.pack(
                side=side,
                fill=fill,
                expand=expand,
                padx=padx,
                pady=pady,
                ipadx=ipadx,
                ipady=ipady,
                anchor=pack_anchor
            )


class kamsabutton(ctk.CTkButton):
    def __init__(
        self, 
        master=None, 
        width=140, 
        height=28, 
        corner_radius=None, 
        border_width=None, 
        border_spacing=2, 
        bg_color="transparent", 
        fg_color=None, 
        hover_color="#F2090D", 
        border_color=None, 
        text_color=None, 
        text_color_disabled=None, 
        text="kamsaButton", 
        font=None, 
        textvariable=None, 
        image=None, 
        state="normal", 
        hover=True, 
        command=None, 
        compound="left", 
        anchor="center",
        # PACK ARGUMENTS
        pack=True,
        side="top",
        fill="none",
        expand=False,
        padx=0,
        pady=10,
        ipadx=0,
        ipady=0,
        pack_anchor="center", 
        # PLACE ARGUMENTS
        place=False,
        x=0,
        y=0,
        relx=0.0,
        rely=0.0,
        # GRID ARGUMENTS
        grid=False,
        row=0,
        column=0,
        columnspan=1,
        rowspan=1,
        sticky="nsew",
        grid_padx=0,
        grid_pady=0,
        **kwargs
    ):
        super().__init__(
            master=master, 
            width=width, 
            height=height, 
            corner_radius=corner_radius, 
            border_width=border_width, 
            border_spacing=border_spacing, 
            bg_color=bg_color, 
            fg_color=fg_color, 
            hover_color=hover_color, 
            border_color=border_color, 
            text_color=text_color, 
            text_color_disabled=text_color_disabled, 
            text=text, 
            font=font, 
            textvariable=textvariable, 
            image=image, 
            state=state, 
            hover=hover, 
            command=command, 
            compound=compound, 
            anchor=anchor, 
            **kwargs
        )
        if grid:
            self.grid(
                row=row,
                column=column,
                columnspan=columnspan,
                rowspan=rowspan,
                sticky=sticky,
                padx=grid_padx,
                pady=grid_pady
            )
        elif place:
            self.place(x=x, y=y, relx=relx, rely=rely)
        elif pack:
            self.pack(
                side=side,
                fill=fill,
                expand=expand,
                padx=padx,
                pady=pady,
                ipadx=ipadx,
                ipady=ipady,
                anchor=pack_anchor
            )

class kamsacheckbox(ctk.CTkCheckBox):
    def __init__(
        self,
        master=None,
        width=100,
        height=24,
        checkbox_width=24,
        checkbox_height=24,
        corner_radius=None,
        border_width=None,
        bg_color="transparent",
        fg_color=None,
        hover_color=None,
        border_color=None,
        checkmark_color=None,
        text_color=None,
        text_color_disabled=None,
        text="Kamsacheckbox",
        font=None,
        variable=None,
        onvalue=1,
        offvalue=0,
        command=None,
        state="normal",
        hover=True,
        # PACK ARGUMENTS
        pack=True,
        side="top",
        fill="none",
        expand=False,
        padx=0,
        pady=5,
        ipadx=0,
        ipady=0,
        pack_anchor="center",
        # PLACE ARGUMENTS
        place=False,
        x=0,
        y=0,
        relx=0.0,
        rely=0.0,
        # GRID ARGUMENTS
        grid=False,
        row=0,
        column=0,
        columnspan=1,
        rowspan=1,
        sticky="nsew",
        grid_padx=0,
        grid_pady=0,
        **kwargs
    ):
        super().__init__(
            master=master,
            width=width,
            height=height,
            checkbox_width=checkbox_width,
            checkbox_height=checkbox_height,
            corner_radius=corner_radius,
            border_width=border_width,
            bg_color=bg_color,
            fg_color=fg_color,
            hover_color=hover_color,
            border_color=border_color,
            checkmark_color=checkmark_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            text=text,
            font=font,
            variable=variable,
            onvalue=onvalue,
            offvalue=offvalue,
            command=command,
            state=state,
            hover=hover,
            **kwargs
        )

        if grid:
            self.grid(
                row=row,
                column=column,
                columnspan=columnspan,
                rowspan=rowspan,
                sticky=sticky,
                padx=grid_padx,
                pady=grid_pady
            )
        elif place:
            self.place(x=x, y=y, relx=relx, rely=rely)
        elif pack:
            self.pack(
                side=side,
                fill=fill,
                expand=expand,
                padx=padx,
                pady=pady,
                ipadx=ipadx,
                ipady=ipady,
                anchor=pack_anchor
            )
class kamsascrollableframe(ctk.CTkScrollableFrame):
    def __init__(
        self, 
        master=None, 
        width=200, 
        height=200, 
        corner_radius=None, 
        border_width=None, 
        bg_color="transparent", 
        fg_color=None, 
        border_color=None, 
        scrollbar_fg_color=None, 
        scrollbar_button_color=None, 
        scrollbar_button_hover_color=None, 
        label_fg_color=None, 
        label_text_color=None, 
        label_text="", 
        label_font=None, 
        label_anchor="center", 
        orientation="vertical",
        # PACK ARGUMENTS
        pack=True,
        side="top",
        fill="none",
        expand=False,
        padx=0,
        pady=10,
        ipadx=0,
        ipady=0,
        pack_anchor="center", 
        # PLACE ARGUMENTS
        place=False,
        x=0,
        y=0,
        relx=0.0,
        rely=0.0,
        # GRID ARGUMENTS
        grid=False,
        row=0,
        column=0,
        columnspan=1,
        rowspan=1,
        sticky="nsew",
        grid_padx=0,
        grid_pady=0,
        **kwargs
    ):
        super().__init__(
            master=master, 
            width=width, 
            height=height, 
            corner_radius=corner_radius, 
            border_width=border_width, 
            bg_color=bg_color, 
            fg_color=fg_color, 
            border_color=border_color, 
            scrollbar_fg_color=scrollbar_fg_color, 
            scrollbar_button_color=scrollbar_button_color, 
            scrollbar_button_hover_color=scrollbar_button_hover_color, 
            label_fg_color=label_fg_color, 
            label_text_color=label_text_color, 
            label_text=label_text, 
            label_font=label_font, 
            label_anchor=label_anchor, 
            orientation=orientation, 
            **kwargs
        )

        # Priority layout handling: grid > place > pack
        if grid:
            self.grid(
                row=row,
                column=column,
                columnspan=columnspan,
                rowspan=rowspan,
                sticky=sticky,
                padx=grid_padx,
                pady=grid_pady
            )
        elif place:
            self.place(x=x, y=y, relx=relx, rely=rely)
        elif pack:
            self.pack(
                side=side,
                fill=fill,
                expand=expand,
                padx=padx,
                pady=pady,
                ipadx=ipadx,
                ipady=ipady,
                anchor=pack_anchor
            )
    def orderlabel(
            self,
            *strings,
            width=0,
            height=28,
            corner_radius=None,
            bg_color="transparent",
            fg_color=None,
            text_color=None,
            text_color_disabled=None,
            text="kamsaLabel",
            font=None,
            image=None,
            compound="center",
            anchor="center",
            # PACK ARGUMENTS
            
    ):
        self.all_items=[]
        for items in strings:
            labels=kamsalabel(master=self,text=f"{items}",
                                   width=width,
                                    height=height,
                                    corner_radius=corner_radius,
                                    bg_color=bg_color,
                                    fg_color=fg_color,
                                    text_color=text_color,
                                    text_color_disabled=text_color_disabled,
                                    font=font,
                                    image=image,
                                    compound=compound,
                                    anchor=anchor,
                                    )
            self.all_items.append(labels)
    def orderbutton(
                self,
                *strings,
                width=140, 
                height=28,
                corner_radius=None,
                bg_color="transparent",
                fg_color=None,
                text_color=None,
                text_color_disabled=None,
                
                font=None,
                image=None,
                compound="left",
                anchor="center",
                # PACK ARGUMENTS
                
        ):
            self.all_buttons=[]
            for items in strings:
                buttons=kamsabutton(master=self,text=f"{items}",
                                       width=width,
                                        height=height,
                                        corner_radius=corner_radius,
                                        bg_color=bg_color,
                                        fg_color=fg_color,
                                        text_color=text_color,
                                        text_color_disabled=text_color_disabled,
                                        font=font,
                                        image=image,
                                        compound=compound,
                                        anchor=anchor,
                                        )
                self.all_buttons.append(buttons)
    def ordercheckbox(
        self,
        *strings,
        width=100,
        height=24,
        checkbox_width=24,
        checkbox_height=24,
        corner_radius=None,
        border_width=None,
        bg_color="transparent",
        fg_color=None,
        hover_color=None,
        border_color=None,
        checkmark_color=None,
        text_color=None,
        text_color_disabled=None,
        font=None,
        command=None,
        state="normal",
        hover=True,
    ):
        self.all_checkboxes = []
        for item in strings:
            chk = kamsacheckbox(
                master=self,
                text=str(item),
                width=width,
                height=height,
                checkbox_width=checkbox_width,
                checkbox_height=checkbox_height,
                corner_radius=corner_radius,
                border_width=border_width,
                bg_color=bg_color,
                fg_color=fg_color,
                hover_color=hover_color,
                border_color=border_color,
                checkmark_color=checkmark_color,
                text_color=text_color,
                text_color_disabled=text_color_disabled,
                font=font,
                command=command,
                state=state,
                hover=hover,
            )
            self.all_checkboxes.append(chk)
if __name__ == "__main__":

    root=kamsadev()
    
    
    root.run()

    
    
    
    
    