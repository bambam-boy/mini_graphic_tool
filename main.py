import tkinter as tk



class Main:
    def __init__(self):
        self.root=tk.Tk()
        self.window_w=2300
        self.window_h=1400
        self.window_geomerty=f"{self.window_w}x{self.window_h}"
        self.main_canvas=tk.Canvas(self.root,width=self.window_w,height=self.window_h)
        self.main_canvas.create_rectangle(0,0,self.window_w,self.window_h,fill="#0b68ea")
        self.root.geometry(self.window_geomerty)
        self.root.title("graphic_thingy")
        # self.root.bind("<Configure>",self.resize_window)
        self.main_canvas.place(x=0,y=0)
        self.draw_parts()
        self.root.mainloop()



    # def resize_window(self,e):
    #     self.window_w=e.width
    #     self.window_h=e.height
    #     self.canvas.resize(self.window_w,self.window_h)



    def draw_parts(self):
        self.canvas=MainCnavas(self.root,self.window_w,self.window_h)



class MainCnavas:
    def __init__(self,root,w,h):
        self.root=root
        self.w=w
        self.h=h
        self.padding=700
        self.oldxp:int=None
        self.oldyp:int=None
        self.isDrawing=False
        self.isEraesing=False
        self.line_width=10
        self.editing_canvas=tk.Canvas(self.root,width=self.w-self.padding,height=self.h-50)
        self.editing_canvas.create_rectangle(0,0,self.w-self.padding,self.h-50,fill="#ffffff")
        self.Color="#00ff00"
        self.editing_canvas.bind("<Motion>",self.Motion)
        self.editing_canvas.bind("<ButtonPress-1>", self.Button_draw)
        self.editing_canvas.bind("<ButtonPress-3>", self.Button_ereas)
        self.editing_canvas.bind("<ButtonRelease-1>", self.BUp)
        self.editing_canvas.bind("<ButtonRelease-3>", self.BUp)
        self.editing_canvas.place(x=30*(self.padding/100),y=25)
        self.root.tkraise(self.editing_canvas)


    # def resize(self,w,h):
    #     self.w=w
    #     self.h=h
    #     self.editing_canvas.config(width=w-100,height=h-100)



    def BUp(self,event):
        self.isDrawing=False
        self.isEraesing=False


    def Button_draw(self,e):
        self.isDrawing=True
        self.isEraesing=False
        self.Color="#00ff00"
        self.oldxp=e.x
        self.oldyp=e.y
        self.line_width=10



    def Button_ereas(self,e):
        self.isDrawing=False
        self.isEraesing=True
        self.Color="#ffffff"
        self.oldxp=e.x
        self.oldyp=e.y
        self.line_width=30


    def Draw(self,x1,y1,x2,y2):
        self.editing_canvas.create_line(
            x1,
            y1,
            x2,
            y2,
            width=self.line_width,
            fill=self.Color,
            capstyle=tk.ROUND, 
            smooth=tk.TRUE
        )


    def Motion(self,e):
        if self.isDrawing or self.isEraesing:
            oldx=self.oldxp
            oldy=self.oldyp
            newxp=e.x
            newyp=e.y
            self.Draw(
                oldx,
                oldy,
                newxp,
                newyp
            )
            self.oldxp=newxp
            self.oldyp=newyp


        





if __name__=="__main__":
    app=Main()