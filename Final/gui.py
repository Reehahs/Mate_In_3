# import chessBoard
import tkinter as tk

class GUI:
    foc = None
    images = {}
    lightColour = "#DDB88C"
    darkColour = "#A66D4F"
    rows = 8
    cols = 8
    size = 64
    hColour = "khaki"

    def __init__(self, parent, chessboard):
        self.chessboard = chessboard
        self.parent = parent
        canvWidth, canvHeight = self.cols * self.size,self.rows * self.size
        self.canvas = tk.Canvas(parent, height = canvHeight, width = canvWidth)
        self.canvas.pack(padx = 7, pady = 7)
        self.drawBoard()
    # A function that will draw and colour the chess board
    def drawBoard(self):
        colour = self.darkColour
        for r in range(self.rows):
            
            if colour == self.darkColour:
                colour = self.lightColour
            else:
                colour = self.darkColour
            for c in range(self.cols):
                x1, y1 = (c * self.size) , ((7 - r) * self.size)
                x2, y2 = x1 + self.size , y1 + self.size
                if (self.foc is not None and (r, c) in self.foc):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill = self.hColour,
                    tags="area")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill= colour, tags="area")
                if colour == self.darkColour:
                    colour = self.lightColour
                else:
                    colour = self.darkColour
            self.canvas.tag_raise("occupied")
            self.canvas.tag_lower("area")
    def draw_pieces(self):
        self.canvas.delete("occupied")

        for crd, pce in self.chessboard.items():
            coor_x, coor_y = self.chessboard.num_notation(crd)
            if pce is not None:
                img = "pieceImages/%s%s.png" % (pce.shortname.lower(), pce.colour)
                piecename = "%s%s%s" % (pce.shortname, coor_x, coor_y)
            if img not in self.images:
                self.images[img] = tk.PhotoImage(file=img)
                self.canvas.create_image(0, 0, image=self.images[img], tags=(piecename, "occupied"), anchor="c")
                
                x_ = (coor_y * self.size) + int(self.size / 2)
                y_ = ((7 - coor_x) * self.size) + int(self.size / 2)
                self.canvas.coords(piecename, x_, y_)

    def main(chessboard):
        tkin = tk.Tk()
        tkin.title("CP 468: Term Project")
        gui = GUI(tkin, chessboard)
        gui.drawBoard()
        gui.draw_pieces()
        tkin.mainloop()

    if __name__ == "__main__":
        game = chessBoard.Board()
        main(game)  