import tkinter as tk



class Graphic_thingy:
    def __init__(self):
        self.root=tk.Tk()
        self.oldxp:int=None
        self.oldyp:int=None
        self.isDrawing=False
        self.isEraesing=False
        self.window_w=1500
        self.window_h=1400
        self.line_width=10
        self.window_geomerty=f"{self.window_w}x{self.window_h}"
        self.main_canvas=tk.Canvas(self.root,width=self.window_w-100,height=self.window_h-100)
        self.main_canvas.create_rectangle(0,0,self.window_w-100,self.window_h-100,fill="#ffffff")
        self.Color="#00ff00"
        self.main_canvas.bind("<Motion>",self.Motion)
        self.main_canvas.bind("<ButtonPress-1>", self.Button_draw)
        self.main_canvas.bind("<ButtonPress-3>", self.Button_ereas)
        self.main_canvas.bind("<ButtonRelease-1>", self.BUp)
        self.main_canvas.bind("<ButtonRelease-3>", self.BUp)
        self.root.geometry(self.window_geomerty)
        self.root.title("graphic_thingy")
        self.main_canvas.pack()
        self.root.mainloop()


    def BUp(self,event):
        print("te")
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
        self.main_canvas.create_line(x1,y1,x2,y2,width=self.line_width,fill=self.Color,capstyle=tk.ROUND, smooth=tk.TRUE)


    def Motion(self,e):
        if self.isDrawing or self.isEraesing:
            oldx=self.oldxp
            oldy=self.oldyp
            newxp=e.x
            newyp=e.y
            self.Draw(oldx,oldy,newxp,newyp)
            self.oldxp=newxp
            self.oldyp=newyp





if __name__=="__main__":
    app=Graphic_thingy()