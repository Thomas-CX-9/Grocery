import threading
from random import randint
from os import _exit,system
from time import sleep
playerBloc=round(randint(0,1)) # 0:Black | 1:White
gameTime=int(input('Time Limit:   '))
stop=0
term=1 # 0:Black | 1:White

'''
Intro:
    Define a class about the board:
        It check is the + statement legal in checks() by traceback()
            findKing() use itering to find the king position
            traceback() use itering to find the attacker
        It check is # statement legal in checkmated() by check() and traceback()
        It check is stalemate happen in the game in stalemated() by pos_move()
        It give all possible moves in pos_moves() by itering the list in __init__()
        It check is the move legal by validate()
            It use traceback() to see is the King under attack after the move
        It show the visible board by showboard()
            It change the visible board by itering the text board in __init__()
        It use timer to count down
            It use num60() to change the time(integer) to time(mm:ss)
            It use sleep() to find the time interval
            It use \r to print
        It use movePiece() to request player input 
            moving() is use to change the text board and call validate() and checks()
'''

class board:
    #########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

    # initialize
    def __init__(self):
        self.board = [
        ['♜ ', '♞ ' , '♝ ', '♛ ', '♚ ', '♝ ', '♞ ', '♜'],  # Black back rank
        ['♟️ ', '♟️ ', '♟️ ', '♟️ ', '♟️ ', '♟️ ', '♟️ ', '♟️'],  # Black pawns
        ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],  # Empty squares (black/white pattern)
        ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],  # Empty squares (white/black pattern)
        ['⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜'],  # Empty squares (black/white pattern)
        ['⬜', '⬛', '⬜', '⬛', '⬜', '⬛', '⬜', '⬛'],  # Empty squares (white/black pattern)
        ['♟️ ', '♟️ ', '♟️ ', '♟️ ', '♟️ ', '♟️ ', '♟️ ', '♟️'],  # White pawns
        ['♜ ', '♞ ' , '♝ ', '♛ ', '♚ ', '♝ ', '♞ ', '♜'],  # WHite back rank
        ]
        self.board_color=[
        ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],#Black back rank
        ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],#Black pawns
        ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],#Emptys quares (black/whitepattern)
        ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],#Empty squares (white/blackpattern)
        ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],#Empty squares (black/whitepattern)
        ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],#Empty squares (white/blackpattern)
        ['⬛','⬜','⬛','⬜','⬛','⬜','⬛','⬜'],#White pawns
        ['⬜','⬛','⬜','⬛','⬜','⬛','⬜','⬛'],#WHite back rank
        ]
        # For calculation
        self.text_board=list(
        list({'name':'Ra','bloc':0,'moved':False}, {'name':'N','bloc':0,'moved':False}, {'name':'B','bloc':0,'moved':False}, {'name':'Q','bloc':0,'moved':False}, {'name':'K','bloc':0,'moved':False,'checked':False}, {'name':'B','bloc':0,'moved':False}, {'name':'N','bloc':0,'moved':False}, {'name':'Rh','bloc':0,'moved':False}),  # Black back rank
        list({'name':'a','bloc':0,'moved':False,'double':False}, {'name':'b','bloc':0,'moved':False,'double':False}, {'name':'c','bloc':0,'moved':False,'double':False}, {'name':'d','bloc':0,'moved':False,'double':False}, {'name':'e','bloc':0,'moved':False,'double':False}, {'name':'f','bloc':0,'moved':False,'double':False}, {'name':'g','bloc':0,'moved':False,'double':False}, {'name':'h','bloc':0,'moved':False,'double':False}),  # Black pawns 
        list(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '),  # Empty squares (black/white pattern)
        list(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '),  # Empty squares (white/black pattern)
        list(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '),  # Empty squares (black/white pattern)
        list(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '),  # Empty squares (white/black pattern)
        list({'name':'a','bloc':1,'moved':False,'double':False}, {'name':'b','bloc':1,'moved':False,'double':False}, {'name':'c','bloc':1,'moved':False,'double':False}, {'name':'d','bloc':1,'moved':False,'double':False}, {'name':'e','bloc':1,'moved':False,'double':False}, {'name':'f','bloc':1,'moved':False,'double':False}, {'name':'g','bloc':1,'moved':False,'double':False}, {'name':'h','bloc':1,'moved':False,'double':False}),  # White pawns
        list({'name':'Ra','bloc':1,'moved':False}, {'name':'N','bloc':1,'moved':False}, {'name':'B','bloc':1,'moved':False}, {'name':'Q','bloc':1,'moved':False}, {'name':'K','bloc':1,'moved':False,'checked':False}, {'name':'B','bloc':1,'moved':False}, {'name':'N','bloc':1,'moved':False}, {'name':'Rh','bloc':1,'moved':False})  # White back rank
        )
        self.copiedBoard=self.text_board
        self.pawnList=('a','b','c','d','e','f','g','h')
        self.changeable=('Ra','Rb','Rc','Rd','Re','Rf','Rg','Rh','N','B','Q')
        self.allPosibleMove=(
    #                     PAWNS                     #
        # a pawn move
        'a2','a3','a4','a5','a6','a7','a2+','a3+','a4+','a5+','a6+','a7+','a2#','a3#','a4#','a5#','a6#','a7#',
        # a pawn take
        'axb2','axb3','axb4','axb5','axb6','axb7','axb2+','axb3+','axb4+','axb5+','axb6+','axb7+','axb2#','axb3#','axb4#','axb5#','axb6#','axb7#',
        # a pawn promote
        'a8=Ra','a8=N','a8=B','a8=Q','a8=Ra+','a8=N+','a8=B+','a8=Q+','a8=Ra#','a8=N#','a8=B#','a8=Q#',
        'a1=Ra','a1=N','a1=B','a1=Q','a1=Ra+','a1=N+','a1=B+','a1=Q+','a1=Ra#','a1=N#','a1=B#','a1=Q#',
        'axb8=Rb','axb8=N','axb8=B','axb8=Q','axb8=Rb+','axb8=N+','axb8=B+','axb8=Q+','axb8=Rb#','axb8=N#','axb8=B#','axb8=Q#',
        'axb1=Rb','axb1=N','axb1=B','axb1=Q','axb1=Rb+','axb1=N+','axb1=B+','axb1=Q+','axb1=Rb#','axb1=N#','axb1=B#','axb1=Q#',
        # b pawn move
        'b2','b3','b4','b5','b6','b7','b2+','b3+','b4+','b5+','b6+','b7+','b2#','b3#','b4#','b5#','b6#','b7#',
        # b pawn take
        'bxc2','bxc3','bxc4','bxc5','bxc6','bxc7','bxc2+','bxc3+','bxc4+','bxc5+','bxc6+','bxc7+','bxc2#','bxc3#','bxc4#','bxc5#','bxc6#','bxc7#',
        'bxa2','bxa3','bxa4','bxa5','bxa6','bxa7','bxa2+','bxa3+','bxa4+','bxa5+','bxa6+','bxa7+','bxa2#','bxa3#','bxa4#','bxa5#','bxa6#','bxa7#',
        # b pawn promote
        'b8=Rb','b8=N','b8=B','b8=Q','b8=Rb+','b8=N+','b8=B+','b8=Q+','b8=Rb#','b8=N#','b8=B#','b8=Q#',
        'b1=Rb','b1=N','b1=B','b1=Q','b1=Rb+','b1=N+','b1=B+','b1=Q+','b1=Rb#','b1=N#','b1=B#','b1=Q#',
        'bxc8=Rc','bxc8=N','bxc8=B','bxc8=Q','bxc8=Rc+','bxc8=N+','bxc8=B+','bxc8=Q+','bxc8=Rc#','bxc8=N#','bxc8=B#','bxc8=Q#',
        'bxa8=Ra','bxa8=N','bxa8=B','bxa8=Q','bxa8=Ra+','bxa8=N+','bxa8=B+','bxa8=Q+','bxa8=Ra#','bxa8=N#','bxa8=B#','bxa8=Q#',
        'bxc1=Rc','bxc1=N','bxc1=B','bxc1=Q','bxc1=Rc+','bxc1=N+','bxc1=B+','bxc1=Q+','bxc1=Rc#','bxc1=N#','bxc1=B#','bxc1=Q#',
        'bxa1=Ra','bxa1=N','bxa1=B','bxa1=Q','bxa1=Ra+','bxa1=N+','bxa1=B+','bxa1=Q+','bxa1=Ra#','bxa1=N#','bxa1=B#','bxa1=Q#',
        # c pawn move
        'c2','c3','c4','c5','c6','c7','c2+','c3+','c4+','c5+','c6+','c7+','c2#','c3#','c4#','c5#','c6#','c7#',
        # c pawn take
        'cxd2','cxd3','cxd4','cxd5','cxd6','cxd7','cxd2+','cxd3+','cxd4+','cxd5+','cxd6+','cxd7+','cxd2#','cxd3#','cxd4#','cxd5#','cxd6#','cxd7#',
        'cxb2','cxb3','cxb4','cxb5','cxb6','cxb7','cxb2+','cxb3+','cxb4+','cxb5+','cxb6+','cxb7+','cxb2#','cxb3#','cxb4#','cxb5#','cxb6#','cxb7#',
        # c pawn promote
        'c8=Rb','c8=N','c8=B','c8=Q','c8=Rb+','c8=N+','c8=B+','c8=Q+','c8=Rb#','c8=N#','c8=B#','c8=Q#',
        'c1=Rb','c1=N','c1=B','c1=Q','c1=Rb+','c1=N+','c1=B+','c1=Q+','c1=Rb#','c1=N#','c1=B#','c1=Q#',
        'cxd8=Rd','cxd8=N','cxd8=B','cxd8=Q','cxd8=Rd+','cxd8=N+','cxd8=B+','cxd8=Q+','cxd8=Rd#','cxd8=N#','cxd8=B#','cxd8=Q#',
        'cxb8=Rd','cxb8=N','cxb8=B','cxb8=Q','cxb8=Rd+','cxb8=N+','cxb8=B+','cxb8=Q+','cxb8=Rd#','cxb8=N#','cxb8=B#','cxb8=Q#',
        'cxd1=Rd','cxd1=N','cxd1=B','cxd1=Q','cxd1=Rd+','cxd1=N+','cxd1=B+','cxd1=Q+','cxd1=Rd#','cxd1=N#','cxd1=B#','cxd1=Q#',
        'cxb1=Rb','cxb1=N','cxb1=B','cxb1=Q','cxb1=Rb+','cxb1=N+','cxb1=B+','cxb1=Q+','cxb1=Rb#','cxb1=N#','cxb1=B#','cxb1=Q#',
        # d pawn move
        'd2','d3','d4','d5','d6','d7','d2+','d3+','d4+','d5+','d6+','d7+','d2#','d3#','d4#','d5#','d6#','d7#',
        # d pawn take
        'dxe2','dxe3','dxe4','dxe5','dxe6','dxe7','dxe2+','dxe3+','dxe4+','dxe5+','dxe6+','dxe7+','dxe2#','dxe3#','dxe4#','dxe5#','dxe6#','dxe7#',
        'dxc2','dxc3','dxc4','dxc5','dxc6','dxc7','dxc2+','dxc3+','dxc4+','dxc5+','dxc6+','dxc7+','dxc2#','dxc3#','dxc4#','dxc5#','dxc6#','dxc7#',
        # d pawn promote
        'd8=Rd','d8=N','d8=B','d8=Q','d8=Rd+','d8=N+','d8=B+','d8=Q+','d8=Rd#','d8=N#','d8=B#','d8=Q#',
        'd1=Rd','d1=N','d1=B','d1=Q','d1=Rd+','d1=N+','d1=B+','d1=Q+','d1=Rd#','d1=N#','d1=B#','d1=Q#',
        'dxe8=Re','dxe8=N','dxe8=B','dxe8=Q','dxe8=Re+','dxe8=N+','dxe8=B+','dxe8=Q+','dxe8=Re#','dxe8=N#','dxe8=B#','dxe8=Q#',
        'dxc8=Rc','dxc8=N','dxc8=B','dxc8=Q','dxc8=Rc+','dxc8=N+','dxc8=B+','dxc8=Q+','dxc8=Rc#','dxc8=N#','dxc8=B#','dxc8=Q#',
        'dxe1=Re','dxe1=N','dxe1=B','dxe1=Q','dxe1=Re+','dxe1=N+','dxe1=B+','dxe1=Q+','dxe1=Re#','dxe1=N#','dxe1=B#','dxe1=Q#',
        'dxc1=Rc','dxc1=N','dxc1=B','dxc1=Q','dxc1=Rc+','dxc1=N+','dxc1=B+','dxc1=Q+','dxc1=Rc#','dxc1=N#','dxc1=B#','dxc1=Q#',
        # e pawn move
        'e2','e3','e4','e5','e6','e7','e2+','e3+','e4+','e5+','e6+','e7+','e2#','e3#','e4#','e5#','e6#','e7#',
        # e pawn take
        'exf2','exf3','exf4','exf5','exf6','exf7','exf2+','exf3+','exf4+','exf5+','exf6+','exf7+','exf2#','exf3#','exf4#','exf5#','exf6#','exf7#',
        'exd2','exd3','exd4','exd5','exd6','exd7','exd2+','exd3+','exd4+','exd5+','exd6+','exd7+','exd2#','exd3#','exd4#','exd5#','exd6#','exd7#',
        # e pawn promote
        'e8=Re','e8=N','e8=B','e8=Q','e8=Re+','e8=N+','e8=B+','e8=Q+','e8=Re#','e8=N#','e8=B#','e8=Q#',
        'e1=Re','e1=N','e1=B','e1=Q','e1=Re+','e1=N+','e1=B+','e1=Q+','e1=Re#','e1=N#','e1=B#','e1=Q#',
        'exf8=Rf','exf8=N','exf8=B','exf8=Q','exf8=Rf+','exf8=N+','exf8=B+','exf8=Q+','exf8=Rf#','exf8=N#','exf8=B#','exf8=Q#',
        'exd8=Rd','exd8=N','exd8=B','exd8=Q','exd8=Rd+','exd8=N+','exd8=B+','exd8=Q+','exd8=Rd#','exd8=N#','exd8=B#','exd8=Q#',
        'exf1=Rf','exf1=N','exf1=B','exf1=Q','exf1=Rf+','exf1=N+','exf1=B+','exf1=Q+','exf1=Rf#','exf1=N#','exf1=B#','exf1=Q#',
        'exd1=Rd','exd1=N','exd1=B','exd1=Q','exd1=Rd+','exd1=N+','exd1=B+','exd1=Q+','exd1=Rd#','exd1=N#','exd1=B#','exd1=Q#',
        # f pawn move
        'f2','f3','f4','f5','f6','f7','f2+','f3+','f4+','f5+','f6+','f7+','f2#','f3#','f4#','f5#','f6#','f7#',
        # f pawn take
        'fxg2','fxg3','fxg4','fxg5','fxg6','fxg7','fxg2+','fxg3+','fxg4+','fxg5+','fxg6+','fxg7+','fxg2#','fxg3#','fxg4#','fxg5#','fxg6#','fxg7#',
        'fxe2','fxe3','fxe4','fxe5','fxe6','fxe7','fxe2+','fxe3+','fxe4+','fxe5+','fxe6+','fxe7+','fxe2#','fxe3#','fxe4#','fxe5#','fxe6#','fxe7#',
        # f pawn promote
        'f8=Rf','f8=N','f8=B','f8=Q','f8=Rf+','f8=N+','f8=B+','f8=Q+','f8=Rf#','f8=N#','f8=B#','f8=Q#',
        'f1=Rf','f1=N','f1=B','f1=Q','f1=Rf+','f1=N+','f1=B+','f1=Q+','f1=Rf#','f1=N#','f1=B#','f1=Q#',
        'fxg8=Rg','fxg8=N','fxg8=B','fxg8=Q','fxg8=Rg+','fxg8=N+','fxg8=B+','fxg8=Q+','fxg8=Rg#','fxg8=N#','fxg8=B#','fxg8=Q#',
        'fxe8=Re','fxe8=N','fxe8=B','fxe8=Q','fxe8=Re+','fxe8=N+','fxe8=B+','fxe8=Q+','fxe8=Re#','fxe8=N#','fxe8=B#','fxe8=Q#',
        'fxg1=Rg','fxg1=N','fxg1=B','fxg1=Q','fxg1=Rg+','fxg1=N+','fxg1=B+','fxg1=Q+','fxg1=Rg#','fxg1=N#','fxg1=B#','fxg1=Q#',
        'fxe1=Re','fxe1=N','fxe1=B','fxe1=Q','fxe1=Re+','fxe1=N+','fxe1=B+','fxe1=Q+','fxe1=Re#','fxe1=N#','fxe1=B#','fxe1=Q#',
        # g pawn move
        'g2','g3','g4','g5','g6','g7','g2+','g3+','g4+','g5+','g6+','g7+','g2#','g3#','g4#','g5#','g6#','g7#',
        # g pawn take
        'gxh2','gxh3','gxh4','gxh5','gxh6','gxh7','gxh2+','gxh3+','gxh4+','gxh5+','gxh6+','gxh7+','gxh2#','gxh3#','gxh4#','gxh5#','gxh6#','gxh7#',
        'gxf2','gxf3','gxf4','gxf5','gxf6','gxf7','gxf2+','gxf3+','gxf4+','gxf5+','gxf6+','gxf7+','gxf2#','gxf3#','gxf4#','gxf5#','gxf6#','gxf7#',
        # g pawn promote
        'g8=Rg','g8=N','g8=B','g8=Q','g8=Rg+','g8=N+','g8=B+','g8=Q+','g8=Rg#','g8=N#','g8=B#','g8=Q#',
        'g1=Rg','g1=N','g1=B','g1=Q','g1=Rg+','g1=N+','g1=B+','g1=Q+','g1=Rg#','g1=N#','g1=B#','g1=Q#',
        'gxh8=Rh','gxh8=N','gxh8=B','gxh8=Q','gxh8=Rh+','gxh8=N+','gxh8=B+','gxh8=Q+','gxh8=Rh#','gxh8=N#','gxh8=B#','gxh8=Q#',
        'gxf8=Rf','gxf8=N','gxf8=B','gxf8=Q','gxf8=Rf+','gxf8=N+','gxf8=B+','gxf8=Q+','gxf8=Rf#','gxf8=N#','gxf8=B#','gxf8=Q#',
        'gxh1=Rh','gxh1=N','gxh1=B','gxh1=Q','gxh1=Rh+','gxh1=N+','gxh1=B+','gxh1=Q+','gxh1=Rh#','gxh1=N#','gxh1=B#','gxh1=Q#',
        'gxf1=Rf','gxf1=N','gxf1=B','gxf1=Q','gxf1=Rf+','gxf1=N+','gxf1=B+','gxf1=Q+','gxf1=Rf#','gxf1=N#','gxf1=B#','gxf1=Q#',
        # h pawn move
        'h2','h3','h4','h5','h6','h7','h2+','h3+','h4+','h5+','h6+','h7+','h2#','h3#','h4#','h5#','h6#','h7#',
        # h pawn take
        'hxg2','hxg3','hxg4','hxg5','hxg6','hxg7','hxg2+','hxg3+','hxg4+','hxg5+','hxg6+','hxg7+','hxg2#','hxg3#','hxg4#','hxg5#','hxg6#','hxg7#',
        # h pawn promote
        'h8=Rh','h8=N','h8=B','h8=Q','h8=Rh+','h8=N+','h8=B+','h8=Q+','h8=Rh#','h8=N#','h8=B#','h8=Q#',
        'h1=Rh','h1=N','h1=B','h1=Q','h1=Rh+','h1=N+','h1=B+','h1=Q+','h1=Rh#','h1=N#','h1=B#','h1=Q#',
        'hxg8=Rd','hxg8=N','hxg8=B','hxg8=Q','hxg8=Rd+','hxg8=N+','hxg8=B+','hxg8=Q+','hxg8=Rd#','hxg8=N#','hxg8=B#','hxg8=Q#',
        'hxg1=Rd','hxg1=N','hxg1=B','hxg1=Q','hxg1=Rd+','hxg1=N+','hxg1=B+','hxg1=Q+','hxg1=Rd#','hxg1=N#','hxg1=B#','hxg1=Q#',
    #                     BISHOPS                     #
        # moves
        'Ba1','Ba2','Ba3','Ba4','Ba5','Ba6','Ba7','Ba8',
        'Bb1','Bb2','Bb3','Bb4','Bb5','Bb6','Bb7','Bb8',
        'Bc1','Bc2','Bc3','Bc4','Bc5','Bc6','Bc7','Bc8',
        'Bd1','Bd2','Bd3','Bd4','Bd5','Bd6','Bd7','Bd8',
        'Be1','Be2','Be3','Be4','Be5','Be6','Be7','Be8',
        'Bf1','Bf2','Bf3','Bf4','Bf5','Bf6','Bf7','Bf8',
        'Bg1','Bg2','Bg3','Bg4','Bg5','Bg6','Bg7','Bg8',
        'Bh1','Bh2','Bh3','Bh4','Bh5','Bh6','Bh7','Bh8',
        # take
        'Bxa1','Bxa2','Bxa3','Bxa4','Bxa5','Bxa6','Bxa7','Bxa8',
        'Bxb1','Bxb2','Bxb3','Bxb4','Bxb5','Bxb6','Bxb7','Bxb8',
        'Bxc1','Bxc2','Bxc3','Bxc4','Bxc5','Bxc6','Bxc7','Bxc8',
        'Bxd1','Bxd2','Bxd3','Bxd4','Bxd5','Bxd6','Bxd7','Bxd8',
        'Bxe1','Bxe2','Bxe3','Bxe4','Bxe5','Bxe6','Bxe7','Bxe8',
        'Bxf1','Bxf2','Bxf3','Bxf4','Bxf5','Bxf6','Bxf7','Bxf8',
        'Bxg1','Bxg2','Bxg3','Bxg4','Bxg5','Bxg6','Bxg7','Bxg8',
        'Bxh1','Bxh2','Bxh3','Bxh4','Bxh5','Bxh6','Bxh7','Bxh8',
        # check
        'Ba1+','Ba2+','Ba3+','Ba4+','Ba5+','Ba6+','Ba7+','Ba8+',
        'Bb1+','Bb2+','Bb3+','Bb4+','Bb5+','Bb6+','Bb7+','Bb8+',
        'Bc1+','Bc2+','Bc3+','Bc4+','Bc5+','Bc6+','Bc7+','Bc8+',
        'Bd1+','Bd2+','Bd3+','Bd4+','Bd5+','Bd6+','Bd7+','Bd8+',
        'Be1+','Be2+','Be3+','Be4+','Be5+','Be6+','Be7+','Be8+',
        'Bf1+','Bf2+','Bf3+','Bf4+','Bf5+','Bf6+','Bf7+','Bf8+',
        'Bg1+','Bg2+','Bg3+','Bg4+','Bg5+','Bg6+','Bg7+','Bg8+',
        'Bh1+','Bh2+','Bh3+','Bh4+','Bh5+','Bh6+','Bh7+','Bh8+',
        'Bxa1+','Bxa2+','Bxa3+','Bxa4+','Bxa5+','Bxa6+','Bxa7+','Bxa8+',
        'Bxb1+','Bxb2+','Bxb3+','Bxb4+','Bxb5+','Bxb6+','Bxb7+','Bxb8+',
        'Bxc1+','Bxc2+','Bxc3+','Bxc4+','Bxc5+','Bxc6+','Bxc7+','Bxc8+',
        'Bxd1+','Bxd2+','Bxd3+','Bxd4+','Bxd5+','Bxd6+','Bxd7+','Bxd8+',
        'Bxe1+','Bxe2+','Bxe3+','Bxe4+','Bxe5+','Bxe6+','Bxe7+','Bxe8+',
        'Bxf1+','Bxf2+','Bxf3+','Bxf4+','Bxf5+','Bxf6+','Bxf7+','Bxf8+',
        'Bxg1+','Bxg2+','Bxg3+','Bxg4+','Bxg5+','Bxg6+','Bxg7+','Bxg8+',
        'Bxh1+','Bxh2+','Bxh3+','Bxh4+','Bxh5+','Bxh6+','Bxh7+','Bxh8+',
        # mate
        'Ba1#','Ba2#','Ba3#','Ba4#','Ba5#','Ba6#','Ba7#','Ba8#',
        'Bb1#','Bb2#','Bb3#','Bb4#','Bb5#','Bb6#','Bb7#','Bb8#',
        'Bc1#','Bc2#','Bc3#','Bc4#','Bc5#','Bc6#','Bc7#','Bc8#',
        'Bd1#','Bd2#','Bd3#','Bd4#','Bd5#','Bd6#','Bd7#','Bd8#',
        'Be1#','Be2#','Be3#','Be4#','Be5#','Be6#','Be7#','Be8#',
        'Bf1#','Bf2#','Bf3#','Bf4#','Bf5#','Bf6#','Bf7#','Bf8#',
        'Bg1#','Bg2#','Bg3#','Bg4#','Bg5#','Bg6#','Bg7#','Bg8#',
        'Bh1#','Bh2#','Bh3#','Bh4#','Bh5#','Bh6#','Bh7#','Bh8#',
        'Bxa1#','Bxa2#','Bxa3#','Bxa4#','Bxa5#','Bxa6#','Bxa7#','Bxa8#',
        'Bxb1#','Bxb2#','Bxb3#','Bxb4#','Bxb5#','Bxb6#','Bxb7#','Bxb8#',
        'Bxc1#','Bxc2#','Bxc3#','Bxc4#','Bxc5#','Bxc6#','Bxc7#','Bxc8#',
        'Bxd1#','Bxd2#','Bxd3#','Bxd4#','Bxd5#','Bxd6#','Bxd7#','Bxd8#',
        'Bxe1#','Bxe2#','Bxe3#','Bxe4#','Bxe5#','Bxe6#','Bxe7#','Bxe8#',
        'Bxf1#','Bxf2#','Bxf3#','Bxf4#','Bxf5#','Bxf6#','Bxf7#','Bxf8#',
        'Bxg1#','Bxg2#','Bxg3#','Bxg4#','Bxg5#','Bxg6#','Bxg7#','Bxg8#',
        'Bxh1#','Bxh2#','Bxh3#','Bxh4#','Bxh5#','Bxh6#','Bxh7#','Bxh8#',
    #                     KNIGHT                     #
        # moves
        'Na1','Na2','Na3','Na4','Na5','Na6','Na7','Na8',
        'Nb1','Nb2','Nb3','Nb4','Nb5','Nb6','Nb7','Nb8',
        'Nc1','Nc2','Nc3','Nc4','Nc5','Nc6','Nc7','Nc8',
        'Nd1','Nd2','Nd3','Nd4','Nd5','Nd6','Nd7','Nd8',
        'Ne1','Ne2','Ne3','Ne4','Ne5','Ne6','Ne7','Ne8',
        'Nf1','Nf2','Nf3','Nf4','Nf5','Nf6','Nf7','Nf8',
        'Ng1','Ng2','Ng3','Ng4','Ng5','Ng6','Ng7','Ng8',
        'Nh1','Nh2','Nh3','Nh4','Nh5','Nh6','Nh7','Nh8',
        # take
        'Nxa1','Nxa2','Nxa3','Nxa4','Nxa5','Nxa6','Nxa7','Nxa8',
        'Nxb1','Nxb2','Nxb3','Nxb4','Nxb5','Nxb6','Nxb7','Nxb8',
        'Nxc1','Nxc2','Nxc3','Nxc4','Nxc5','Nxc6','Nxc7','Nxc8',
        'Nxd1','Nxd2','Nxd3','Nxd4','Nxd5','Nxd6','Nxd7','Nxd8',
        'Nxe1','Nxe2','Nxe3','Nxe4','Nxe5','Nxe6','Nxe7','Nxe8',
        'Nxf1','Nxf2','Nxf3','Nxf4','Nxf5','Nxf6','Nxf7','Nxf8',
        'Nxg1','Nxg2','Nxg3','Nxg4','Nxg5','Nxg6','Nxg7','Nxg8',
        'Nxh1','Nxh2','Nxh3','Nxh4','Nxh5','Nxh6','Nxh7','Nxh8',
        # check
        'Na1+','Na2+','Na3+','Na4+','Na5+','Na6+','Na7+','Na8+',
        'Nb1+','Nb2+','Nb3+','Nb4+','Nb5+','Nb6+','Nb7+','Nb8+',
        'Nc1+','Nc2+','Nc3+','Nc4+','Nc5+','Nc6+','Nc7+','Nc8+',
        'Nd1+','Nd2+','Nd3+','Nd4+','Nd5+','Nd6+','Nd7+','Nd8+',
        'Ne1+','Ne2+','Ne3+','Ne4+','Ne5+','Ne6+','Ne7+','Ne8+',
        'Nf1+','Nf2+','Nf3+','Nf4+','Nf5+','Nf6+','Nf7+','Nf8+',
        'Ng1+','Ng2+','Ng3+','Ng4+','Ng5+','Ng6+','Ng7+','Ng8+',
        'Nh1+','Nh2+','Nh3+','Nh4+','Nh5+','Nh6+','Nh7+','Nh8+',
        'Nxa1+','Nxa2+','Nxa3+','Nxa4+','Nxa5+','Nxa6+','Nxa7+','Nxa8+',
        'Nxb1+','Nxb2+','Nxb3+','Nxb4+','Nxb5+','Nxb6+','Nxb7+','Nxb8+',
        'Nxc1+','Nxc2+','Nxc3+','Nxc4+','Nxc5+','Nxc6+','Nxc7+','Nxc8+',
        'Nxd1+','Nxd2+','Nxd3+','Nxd4+','Nxd5+','Nxd6+','Nxd7+','Nxd8+',
        'Nxe1+','Nxe2+','Nxe3+','Nxe4+','Nxe5+','Nxe6+','Nxe7+','Nxe8+',
        'Nxf1+','Nxf2+','Nxf3+','Nxf4+','Nxf5+','Nxf6+','Nxf7+','Nxf8+',
        'Nxg1+','Nxg2+','Nxg3+','Nxg4+','Nxg5+','Nxg6+','Nxg7+','Nxg8+',
        'Nxh1+','Nxh2+','Nxh3+','Nxh4+','Nxh5+','Nxh6+','Nxh7+','Nxh8+',
        # mate
        'Na1#','Na2#','Na3#','Na4#','Na5#','Na6#','Na7#','Na8#',
        'Nb1#','Nb2#','Nb3#','Nb4#','Nb5#','Nb6#','Nb7#','Nb8#',
        'Nc1#','Nc2#','Nc3#','Nc4#','Nc5#','Nc6#','Nc7#','Nc8#',
        'Nd1#','Nd2#','Nd3#','Nd4#','Nd5#','Nd6#','Nd7#','Nd8#',
        'Ne1#','Ne2#','Ne3#','Ne4#','Ne5#','Ne6#','Ne7#','Ne8#',
        'Nf1#','Nf2#','Nf3#','Nf4#','Nf5#','Nf6#','Nf7#','Nf8#',
        'Ng1#','Ng2#','Ng3#','Ng4#','Ng5#','Ng6#','Ng7#','Ng8#',
        'Nh1#','Nh2#','Nh3#','Nh4#','Nh5#','Nh6#','Nh7#','Nh8#',
        'Nxa1#','Nxa2#','Nxa3#','Nxa4#','Nxa5#','Nxa6#','Nxa7#','Nxa8#',
        'Nxb1#','Nxb2#','Nxb3#','Nxb4#','Nxb5#','Nxb6#','Nxb7#','Nxb8#',
        'Nxc1#','Nxc2#','Nxc3#','Nxc4#','Nxc5#','Nxc6#','Nxc7#','Nxc8#',
        'Nxd1#','Nxd2#','Nxd3#','Nxd4#','Nxd5#','Nxd6#','Nxd7#','Nxd8#',
        'Nxe1#','Nxe2#','Nxe3#','Nxe4#','Nxe5#','Nxe6#','Nxe7#','Nxe8#',
        'Nxf1#','Nxf2#','Nxf3#','Nxf4#','Nxf5#','Nxf6#','Nxf7#','Nxf8#',
        'Nxg1#','Nxg2#','Nxg3#','Nxg4#','Nxg5#','Nxg6#','Nxg7#','Nxg8#',
        'Nxh1#','Nxh2#','Nxh3#','Nxh4#','Nxh5#','Nxh6#','Nxh7#','Nxh8#',
    #                     QUEEN                     #
        # moves
        'Qa1','Qa2','Qa3','Qa4','Qa5','Qa6','Qa7','Qa8',
        'Qb1','Qb2','Qb3','Qb4','Qb5','Qb6','Qb7','Qb8',
        'Qc1','Qc2','Qc3','Qc4','Qc5','Qc6','Qc7','Qc8',
        'Qd1','Qd2','Qd3','Qd4','Qd5','Qd6','Qd7','Qd8',
        'Qe1','Qe2','Qe3','Qe4','Qe5','Qe6','Qe7','Qe8',
        'Qf1','Qf2','Qf3','Qf4','Qf5','Qf6','Qf7','Qf8',
        'Qg1','Qg2','Qg3','Qg4','Qg5','Qg6','Qg7','Qg8',
        'Qh1','Qh2','Qh3','Qh4','Qh5','Qh6','Qh7','Qh8',
        # take
        'Qxa1','Qxa2','Qxa3','Qxa4','Qxa5','Qxa6','Qxa7','Qxa8',
        'Qxb1','Qxb2','Qxb3','Qxb4','Qxb5','Qxb6','Qxb7','Qxb8',
        'Qxc1','Qxc2','Qxc3','Qxc4','Qxc5','Qxc6','Qxc7','Qxc8',
        'Qxd1','Qxd2','Qxd3','Qxd4','Qxd5','Qxd6','Qxd7','Qxd8',
        'Qxe1','Qxe2','Qxe3','Qxe4','Qxe5','Qxe6','Qxe7','Qxe8',
        'Qxf1','Qxf2','Qxf3','Qxf4','Qxf5','Qxf6','Qxf7','Qxf8',
        'Qxg1','Qxg2','Qxg3','Qxg4','Qxg5','Qxg6','Qxg7','Qxg8',
        'Qxh1','Qxh2','Qxh3','Qxh4','Qxh5','Qxh6','Qxh7','Qxh8',
        # check
        'Qa1+','Qa2+','Qa3+','Qa4+','Qa5+','Qa6+','Qa7+','Qa8+',
        'Qb1+','Qb2+','Qb3+','Qb4+','Qb5+','Qb6+','Qb7+','Qb8+',
        'Qc1+','Qc2+','Qc3+','Qc4+','Qc5+','Qc6+','Qc7+','Qc8+',
        'Qd1+','Qd2+','Qd3+','Qd4+','Qd5+','Qd6+','Qd7+','Qd8+',
        'Qe1+','Qe2+','Qe3+','Qe4+','Qe5+','Qe6+','Qe7+','Qe8+',
        'Qf1+','Qf2+','Qf3+','Qf4+','Qf5+','Qf6+','Qf7+','Qf8+',
        'Qg1+','Qg2+','Qg3+','Qg4+','Qg5+','Qg6+','Qg7+','Qg8+',
        'Qh1+','Qh2+','Qh3+','Qh4+','Qh5+','Qh6+','Qh7+','Qh8+',
        'Qxa1+','Qxa2+','Qxa3+','Qxa4+','Qxa5+','Qxa6+','Qxa7+','Qxa8+',
        'Qxb1+','Qxb2+','Qxb3+','Qxb4+','Qxb5+','Qxb6+','Qxb7+','Qxb8+',
        'Qxc1+','Qxc2+','Qxc3+','Qxc4+','Qxc5+','Qxc6+','Qxc7+','Qxc8+',
        'Qxd1+','Qxd2+','Qxd3+','Qxd4+','Qxd5+','Qxd6+','Qxd7+','Qxd8+',
        'Qxe1+','Qxe2+','Qxe3+','Qxe4+','Qxe5+','Qxe6+','Qxe7+','Qxe8+',
        'Qxf1+','Qxf2+','Qxf3+','Qxf4+','Qxf5+','Qxf6+','Qxf7+','Qxf8+',
        'Qxg1+','Qxg2+','Qxg3+','Qxg4+','Qxg5+','Qxg6+','Qxg7+','Qxg8+',
        'Qxh1+','Qxh2+','Qxh3+','Qxh4+','Qxh5+','Qxh6+','Qxh7+','Qxh8+',
        # mate
        'Qa1#','Qa2#','Qa3#','Qa4#','Qa5#','Qa6#','Qa7#','Qa8#',
        'Qb1#','Qb2#','Qb3#','Qb4#','Qb5#','Qb6#','Qb7#','Qb8#',
        'Qc1#','Qc2#','Qc3#','Qc4#','Qc5#','Qc6#','Qc7#','Qc8#',
        'Qd1#','Qd2#','Qd3#','Qd4#','Qd5#','Qd6#','Qd7#','Qd8#',
        'Qe1#','Qe2#','Qe3#','Qe4#','Qe5#','Qe6#','Qe7#','Qe8#',
        'Qf1#','Qf2#','Qf3#','Qf4#','Qf5#','Qf6#','Qf7#','Qf8#',
        'Qg1#','Qg2#','Qg3#','Qg4#','Qg5#','Qg6#','Qg7#','Qg8#',
        'Qh1#','Qh2#','Qh3#','Qh4#','Qh5#','Qh6#','Qh7#','Qh8#',
        'Qxa1#','Qxa2#','Qxa3#','Qxa4#','Qxa5#','Qxa6#','Qxa7#','Qxa8#',
        'Qxb1#','Qxb2#','Qxb3#','Qxb4#','Qxb5#','Qxb6#','Qxb7#','Qxb8#',
        'Qxc1#','Qxc2#','Qxc3#','Qxc4#','Qxc5#','Qxc6#','Qxc7#','Qxc8#',
        'Qxd1#','Qxd2#','Qxd3#','Qxd4#','Qxd5#','Qxd6#','Qxd7#','Qxd8#',
        'Qxe1#','Qxe2#','Qxe3#','Qxe4#','Qxe5#','Qxe6#','Qxe7#','Qxe8#',
        'Qxf1#','Qxf2#','Qxf3#','Qxf4#','Qxf5#','Qxf6#','Qxf7#','Qxf8#',
        'Qxg1#','Qxg2#','Qxg3#','Qxg4#','Qxg5#','Qxg6#','Qxg7#','Qxg8#',
        'Qxh1#','Qxh2#','Qxh3#','Qxh4#','Qxh5#','Qxh6#','Qxh7#','Qxh8#',
    #                     ROOK                     #
        # moves (|)
        'Ra1','Ra2','Ra3','Ra4','Ra5','Ra6','Ra7','Ra8',
        'Rb1','Rb2','Rb3','Rb4','Rb5','Rb6','Rb7','Rb8',
        'Rc1','Rc2','Rc3','Rc4','Rc5','Rc6','Rc7','Rc8',
        'Rd1','Rd2','Rd3','Rd4','Rd5','Rd6','Rd7','Rd8',
        'Re1','Re2','Re3','Re4','Re5','Re6','Re7','Re8',
        'Rf1','Rf2','Rf3','Rf4','Rf5','Rf6','Rf7','Rf8',
        'Rg1','Rg2','Rg3','Rg4','Rg5','Rg6','Rg7','Rg8',
        'Rh1','Rh2','Rh3','Rh4','Rh5','Rh6','Rh7','Rh8',
        # moves(<>) (1)
        'Rba1','Rca1','Rda1','Rea1','Rfa1','Rga1','Rha1',
        'Rab1','Rcb1','Rdb1','Reb1','Rfb1','Rgb1','Rhb1',
        'Rac1','Rbc1','Rdc1','Rec1','Rfc1','Rgc1','Rhc1',
        'Rad1','Rbd1','Rcd1','Red1','Rfd1','Rgd1','Rhd1',
        'Rae1','Rbe1','Rce1','Rde1','Rfe1','Rge1','Rhe1',
        'Raf1','Rbf1','Rcf1','Rdf1','Ref1','Rgf1','Rhf1',
        'Rag1','Rbg1','Rcg1','Rdg1','Reg1','Rfg1','Rhg1',
        'Rah1','Rbh1','Rch1','Rdh1','Reh1','Rfh1','Rgh1',
        # moves(<>) (2)
        'Rba2','Rca2','Rda2','Rea2','Rfa2','Rga2','Rha2',
        'Rab2','Rcb2','Rdb2','Reb2','Rfb2','Rgb2','Rhb2',
        'Rac2','Rbc2','Rdc2','Rec2','Rfc2','Rgc2','Rhc2',
        'Rad2','Rbd2','Rcd2','Red2','Rfd2','Rgd2','Rhd2',
        'Rae2','Rbe2','Rce2','Rde2','Rfe2','Rge2','Rhe2',
        'Raf2','Rbf2','Rcf2','Rdf2','Ref2','Rgf2','Rhf2',
        'Rag2','Rbg2','Rcg2','Rdg2','Reg2','Rfg2','Rhg2',
        'Rah2','Rbh2','Rch2','Rdh2','Reh2','Rfh2','Rgh2',
        # moves (<>) (3)
        'Rba3','Rca3','Rda3','Rea3','Rfa3','Rga3','Rha3',
        'Rab3','Rcb3','Rdb3','Reb3','Rfb3','Rgb3','Rhb3',
        'Rac3','Rbc3','Rdc3','Rec3','Rfc3','Rgc3','Rhc3',
        'Rad3','Rbd3','Rcd3','Red3','Rfd3','Rgd3','Rhd3',
        'Rae3','Rbe3','Rce3','Rde3','Rfe3','Rge3','Rhe3',
        'Raf3','Rbf3','Rcf3','Rdf3','Ref3','Rgf3','Rhf3',
        'Rag3','Rbg3','Rcg3','Rdg3','Reg3','Rfg3','Rhg3',
        'Rah3','Rbh3','Rch3','Rdh3','Reh3','Rfh3','Rgh3',
        # moves (<>) (4)
        'Rba4','Rca4','Rda4','Rea4','Rfa4','Rga4','Rha4',
        'Rab4','Rcb4','Rdb4','Reb4','Rfb4','Rgb4','Rhb4',
        'Rac4','Rbc4','Rdc4','Rec4','Rfc4','Rgc4','Rhc4',
        'Rad4','Rbd4','Rcd4','Red4','Rfd4','Rgd4','Rhd4',
        'Rae4','Rbe4','Rce4','Rde4','Rfe4','Rge4','Rhe4',
        'Raf4','Rbf4','Rcf4','Rdf4','Ref4','Rgf4','Rhf4',
        'Rag4','Rbg4','Rcg4','Rdg4','Reg4','Rfg4','Rhg4',
        'Rah4','Rbh4','Rch4','Rdh4','Reh4','Rfh4','Rgh4',
        # moves (<>) (5)
        'Rba5','Rca5','Rda5','Rea5','Rfa5','Rga5','Rha5',
        'Rab5','Rcb5','Rdb5','Reb5','Rfb5','Rgb5','Rhb5',
        'Rac5','Rbc5','Rdc5','Rec5','Rfc5','Rgc5','Rhc5',
        'Rad5','Rbd5','Rcd5','Red5','Rfd5','Rgd5','Rhd5',
        'Rae5','Rbe5','Rce5','Rde5','Rfe5','Rge5','Rhe5',
        'Raf5','Rbf5','Rcf5','Rdf5','Ref5','Rgf5','Rhf5',
        'Rag5','Rbg5','Rcg5','Rdg5','Reg5','Rfg5','Rhg5',
        'Rah5','Rbh5','Rch5','Rdh5','Reh5','Rfh5','Rgh5',
        # moves (<>) (6)
        'Rba6','Rca6','Rda6','Rea6','Rfa6','Rga6','Rha6',
        'Rab6','Rcb6','Rdb6','Reb6','Rfb6','Rgb6','Rhb6',
        'Rac6','Rbc6','Rdc6','Rec6','Rfc6','Rgc6','Rhc6',
        'Rad6','Rbd6','Rcd6','Red6','Rfd6','Rgd6','Rhd6',
        'Rae6','Rbe6','Rce6','Rde6','Rfe6','Rge6','Rhe6',
        'Raf6','Rbf6','Rcf6','Rdf6','Ref6','Rgf6','Rhf6',
        'Rag6','Rbg6','Rcg6','Rdg6','Reg6','Rfg6','Rhg6',
        'Rah6','Rbh6','Rch6','Rdh6','Reh6','Rfh6','Rgh6',
        # moves (<>) (7)
        'Rba7','Rca7','Rda7','Rea7','Rfa7','Rga7','Rha7',
        'Rab7','Rcb7','Rdb7','Reb7','Rfb7','Rgb7','Rhb7',
        'Rac7','Rbc7','Rdc7','Rec7','Rfc7','Rgc7','Rhc7',
        'Rad7','Rbd7','Rcd7','Red7','Rfd7','Rgd7','Rhd7',
        'Rae7','Rbe7','Rce7','Rde7','Rfe7','Rge7','Rhe7',
        'Raf7','Rbf7','Rcf7','Rdf7','Ref7','Rgf7','Rhf7',
        'Rag7','Rbg7','Rcg7','Rdg7','Reg7','Rfg7','Rhg7',
        'Rah7','Rbh7','Rch7','Rdh7','Reh7','Rfh7','Rgh7',
        # moves (<>) (8)
        'Rba8','Rca8','Rda8','Rea8','Rfa8','Rga8','Rha8',
        'Rab8','Rcb8','Rdb8','Reb8','Rfb8','Rgb8','Rhb8',
        'Rac8','Rbc8','Rdc8','Rec8','Rfc8','Rgc8','Rhc8',
        'Rad8','Rbd8','Rcd8','Red8','Rfd8','Rgd8','Rhd8',
        'Rae8','Rbe8','Rce8','Rde8','Rfe8','Rge8','Rhe8',
        'Raf8','Rbf8','Rcf8','Rdf8','Ref8','Rgf8','Rhf8',
        'Rag8','Rbg8','Rcg8','Rdg8','Reg8','Rfg8','Rhg8',
        'Rah8','Rbh8','Rch8','Rdh8','Reh8','Rfh8','Rgh8',
        # take
        # |
        'Rxa1','Rxa2','Rxa3','Rxa4','Rxa5','Rxa6','Rxa7','Rxa8',
        'Rxb1','Rxb2','Rxb3','Rxb4','Rxb5','Rxb6','Rxb7','Rxb8',
        'Rxc1','Rxc2','Rxc3','Rxc4','Rxc5','Rxc6','Rxc7','Rxc8',
        'Rxd1','Rxd2','Rxd3','Rxd4','Rxd5','Rxd6','Rxd7','Rxd8',
        'Rxe1','Rxe2','Rxe3','Rxe4','Rxe5','Rxe6','Rxe7','Rxe8',
        'Rxf1','Rxf2','Rxf3','Rxf4','Rxf5','Rxf6','Rxf7','Rxf8',
        'Rxg1','Rxg2','Rxg3','Rxg4','Rxg5','Rxg6','Rxg7','Rxg8',
        'Rxh1','Rxh2','Rxh3','Rxh4','Rxh5','Rxh6','Rxh7','Rxh8',
        # <> (1)
        'Rbxa1','Rcxa1','Rdxa1','Rexa1','Rfxa1','Rgxa1','Rhxa1',
        'Raxb1','Rcxb1','Rdxb1','Rexb1','Rfxb1','Rgxb1','Rhxb1',
        'Raxc1','Rbxc1','Rdxc1','Rexc1','Rfxc1','Rgxc1','Rhxc1',
        'Raxd1','Rbxd1','Rcxd1','Rexd1','Rfxd1','Rgxd1','Rhxd1',
        'Raxe1','Rbxe1','Rcxe1','Rdxe1','Rfxe1','Rgxe1','Rhxe1',
        'Raxf1','Rbxf1','Rcxf1','Rdxf1','Rexf1','Rgxf1','Rhxf1',
        'Raxg1','Rbxg1','Rcxg1','Rdxg1','Rexg1','Rfxg1','Rhxg1',
        'Raxh1','Rbxh1','Rcxh1','Rdxh1','Rexh1','Rfxh1','Rgxh1',
        # <> (2)
        'Rbxa2','Rcxa2','Rdxa2','Rexa2','Rfxa2','Rgxa2','Rhxa2',
        'Raxb2','Rcxb2','Rdxb2','Rexb2','Rfxb2','Rgxb2','Rhxb2',
        'Raxc2','Rbxc2','Rdxc2','Rexc2','Rfxc2','Rgxc2','Rhxc2',
        'Raxd2','Rbxd2','Rcxd2','Rexd2','Rfxd2','Rgxd2','Rhxd2',
        'Raxe2','Rbxe2','Rcxe2','Rdxe2','Rfxe2','Rgxe2','Rhxe2',
        'Raxf2','Rbxf2','Rcxf2','Rdxf2','Rexf2','Rgxf2','Rhxf2',
        'Raxg2','Rbxg2','Rcxg2','Rdxg2','Rexg2','Rfxg2','Rhxg2',
        'Raxh2','Rbxh2','Rcxh2','Rdxh2','Rexh2','Rfxh2','Rgxh2',
        # <> (3)
        'Rbxa3','Rcxa3','Rdxa3','Rexa3','Rfxa3','Rgxa3','Rhxa3',
        'Raxb3','Rcxb3','Rdxb3','Rexb3','Rfxb3','Rgxb3','Rhxb3',
        'Raxc3','Rbxc3','Rdxc3','Rexc3','Rfxc3','Rgxc3','Rhxc3',
        'Raxd3','Rbxd3','Rcxd3','Rexd3','Rfxd3','Rgxd3','Rhxd3',
        'Raxe3','Rbxe3','Rcxe3','Rdxe3','Rfxe3','Rgxe3','Rhxe3',
        'Raxf3','Rbxf3','Rcxf3','Rdxf3','Rexf3','Rgxf3','Rhxf3',
        'Raxg3','Rbxg3','Rcxg3','Rdxg3','Rexg3','Rfxg3','Rhxg3',
        'Raxh3','Rbxh3','Rcxh3','Rdxh3','Rexh3','Rfxh3','Rgxh3',
        # <> (4)
        'Rbxa4','Rcxa4','Rdxa4','Rexa4','Rfxa4','Rgxa4','Rhxa4',
        'Raxb4','Rcxb4','Rdxb4','Rexb4','Rfxb4','Rgxb4','Rhxb4',
        'Raxc4','Rbxc4','Rdxc4','Rexc4','Rfxc4','Rgxc4','Rhxc4',
        'Raxd4','Rbxd4','Rcxd4','Rexd4','Rfxd4','Rgxd4','Rhxd4',
        'Raxe4','Rbxe4','Rcxe4','Rdxe4','Rfxe4','Rgxe4','Rhxe4',
        'Raxf4','Rbxf4','Rcxf4','Rdxf4','Rexf4','Rgxf4','Rhxf4',
        'Raxg4','Rbxg4','Rcxg4','Rdxg4','Rexg4','Rfxg4','Rhxg4',
        'Raxh4','Rbxh4','Rcxh4','Rdxh4','Rexh4','Rfxh4','Rgxh4',
        # <> (5)
        'Rbxa5','Rcxa5','Rdxa5','Rexa5','Rfxa5','Rgxa5','Rhxa5',
        'Raxb5','Rcxb5','Rdxb5','Rexb5','Rfxb5','Rgxb5','Rhxb5',
        'Raxc5','Rbxc5','Rdxc5','Rexc5','Rfxc5','Rgxc5','Rhxc5',
        'Raxd5','Rbxd5','Rcxd5','Rexd5','Rfxd5','Rgxd5','Rhxd5',
        'Raxe5','Rbxe5','Rcxe5','Rdxe5','Rfxe5','Rgxe5','Rhxe5',
        'Raxf5','Rbxf5','Rcxf5','Rdxf5','Rexf5','Rgxf5','Rhxf5',
        'Raxg5','Rbxg5','Rcxg5','Rdxg5','Rexg5','Rfxg5','Rhxg5',
        'Raxh5','Rbxh5','Rcxh5','Rdxh5','Rexh5','Rfxh5','Rgxh5',
        # <> (6)
        'Rbxa6','Rcxa6','Rdxa6','Rexa6','Rfxa6','Rgxa6','Rhxa6',
        'Raxb6','Rcxb6','Rdxb6','Rexb6','Rfxb6','Rgxb6','Rhxb6',
        'Raxc6','Rbxc6','Rdxc6','Rexc6','Rfxc6','Rgxc6','Rhxc6',
        'Raxd6','Rbxd6','Rcxd6','Rexd6','Rfxd6','Rgxd6','Rhxd6',
        'Raxe6','Rbxe6','Rcxe6','Rdxe6','Rfxe6','Rgxe6','Rhxe6',
        'Raxf6','Rbxf6','Rcxf6','Rdxf6','Rexf6','Rgxf6','Rhxf6',
        'Raxg6','Rbxg6','Rcxg6','Rdxg6','Rexg6','Rfxg6','Rhxg6',
        'Raxh6','Rbxh6','Rcxh6','Rdxh6','Rexh6','Rfxh6','Rgxh6',
        # <> (7)
        'Rbxa7','Rcxa7','Rdxa7','Rexa7','Rfxa7','Rgxa7','Rhxa7',
        'Raxb7','Rcxb7','Rdxb7','Rexb7','Rfxb7','Rgxb7','Rhxb7',
        'Raxc7','Rbxc7','Rdxc7','Rexc7','Rfxc7','Rgxc7','Rhxc7',
        'Raxd7','Rbxd7','Rcxd7','Rexd7','Rfxd7','Rgxd7','Rhxd7',
        'Raxe7','Rbxe7','Rcxe7','Rdxe7','Rfxe7','Rgxe7','Rhxe7',
        'Raxf7','Rbxf7','Rcxf7','Rdxf7','Rexf7','Rgxf7','Rhxf7',
        'Raxg7','Rbxg7','Rcxg7','Rdxg7','Rexg7','Rfxg7','Rhxg7',
        'Raxh7','Rbxh7','Rcxh7','Rdxh7','Rexh7','Rfxh7','Rgxh7',
        # <> (8)
        'Rbxa8','Rcxa8','Rdxa8','Rexa8','Rfxa8','Rgxa8','Rhxa8',
        'Raxb8','Rcxb8','Rdxb8','Rexb8','Rfxb8','Rgxb8','Rhxb8',
        'Raxc8','Rbxc8','Rdxc8','Rexc8','Rfxc8','Rgxc8','Rhxc8',
        'Raxd8','Rbxd8','Rcxd8','Rexd8','Rfxd8','Rgxd8','Rhxd8',
        'Raxe8','Rbxe8','Rcxe8','Rdxe8','Rfxe8','Rgxe8','Rhxe8',
        'Raxf8','Rbxf8','Rcxf8','Rdxf8','Rexf8','Rgxf8','Rhxf8',
        'Raxg8','Rbxg8','Rcxg8','Rdxg8','Rexg8','Rfxg8','Rhxg8',
        'Raxh8','Rbxh8','Rcxh8','Rdxh8','Rexh8','Rfxh8','Rgxh8',
        # check
        # moves (|)
        'Ra1+','Ra2+','Ra3+','Ra4+','Ra5+','Ra6+','Ra7+','Ra8+',
        'Rb1+','Rb2+','Rb3+','Rb4+','Rb5+','Rb6+','Rb7+','Rb8+',
        'Rc1+','Rc2+','Rc3+','Rc4+','Rc5+','Rc6+','Rc7+','Rc8+',
        'Rd1+','Rd2+','Rd3+','Rd4+','Rd5+','Rd6+','Rd7+','Rd8+',
        'Re1+','Re2+','Re3+','Re4+','Re5+','Re6+','Re7+','Re8+',
        'Rf1+','Rf2+','Rf3+','Rf4+','Rf5+','Rf6+','Rf7+','Rf8+',
        'Rg1+','Rg2+','Rg3+','Rg4+','Rg5+','Rg6+','Rg7+','Rg8+',
        'Rh1+','Rh2+','Rh3+','Rh4+','Rh5+','Rh6+','Rh7+','Rh8+',
        # moves(<>) (1)
        'Rba1+','Rca1+','Rda1+','Rea1+','Rfa1+','Rga1+','Rha1+',
        'Rab1+','Rcb1+','Rdb1+','Reb1+','Rfb1+','Rgb1+','Rhb1+',
        'Rac1+','Rbc1+','Rdc1+','Rec1+','Rfc1+','Rgc1+','Rhc1+',
        'Rad1+','Rbd1+','Rcd1+','Red1+','Rfd1+','Rgd1+','Rhd1+',
        'Rae1+','Rbe1+','Rce1+','Rde1+','Rfe1+','Rge1+','Rhe1+',
        'Raf1+','Rbf1+','Rcf1+','Rdf1+','Ref1+','Rgf1+','Rhf1+',
        'Rag1+','Rbg1+','Rcg1+','Rdg1+','Reg1+','Rfg1+','Rhg1+',
        'Rah1+','Rbh1+','Rch1+','Rdh1+','Reh1+','Rfh1+','Rgh1+',
        # moves(<>) (2)
        'Rba2+','Rca2+','Rda2+','Rea2+','Rfa2+','Rga2+','Rha2+',
        'Rab2+','Rcb2+','Rdb2+','Reb2+','Rfb2+','Rgb2+','Rhb2+',
        'Rac2+','Rbc2+','Rdc2+','Rec2+','Rfc2+','Rgc2+','Rhc2+',
        'Rad2+','Rbd2+','Rcd2+','Red2+','Rfd2+','Rgd2+','Rhd2+',
        'Rae2+','Rbe2+','Rce2+','Rde2+','Rfe2+','Rge2+','Rhe2+',
        'Raf2+','Rbf2+','Rcf2+','Rdf2+','Ref2+','Rgf2+','Rhf2+',
        'Rag2+','Rbg2+','Rcg2+','Rdg2+','Reg2+','Rfg2+','Rhg2+',
        'Rah2+','Rbh2+','Rch2+','Rdh2+','Reh2+','Rfh2+','Rgh2+',
        # moves (<>) (3)
        'Rba3+','Rca3+','Rda3+','Rea3+','Rfa3+','Rga3+','Rha3+',
        'Rab3+','Rcb3+','Rdb3+','Reb3+','Rfb3+','Rgb3+','Rhb3+',
        'Rac3+','Rbc3+','Rdc3+','Rec3+','Rfc3+','Rgc3+','Rhc3+',
        'Rad3+','Rbd3+','Rcd3+','Red3+','Rfd3+','Rgd3+','Rhd3+',
        'Rae3+','Rbe3+','Rce3+','Rde3+','Rfe3+','Rge3+','Rhe3+',
        'Raf3+','Rbf3+','Rcf3+','Rdf3+','Ref3+','Rgf3+','Rhf3+',
        'Rag3+','Rbg3+','Rcg3+','Rdg3+','Reg3+','Rfg3+','Rhg3+',
        'Rah3+','Rbh3+','Rch3+','Rdh3+','Reh3+','Rfh3+','Rgh3+',
        # moves (<>) (4)
        'Rba4+','Rca4+','Rda4+','Rea4+','Rfa4+','Rga4+','Rha4+',
        'Rab4+','Rcb4+','Rdb4+','Reb4+','Rfb4+','Rgb4+','Rhb4+',
        'Rac4+','Rbc4+','Rdc4+','Rec4+','Rfc4+','Rgc4+','Rhc4+',
        'Rad4+','Rbd4+','Rcd4+','Red4+','Rfd4+','Rgd4+','Rhd4+',
        'Rae4+','Rbe4+','Rce4+','Rde4+','Rfe4+','Rge4+','Rhe4+',
        'Raf4+','Rbf4+','Rcf4+','Rdf4+','Ref4+','Rgf4+','Rhf4+',
        'Rag4+','Rbg4+','Rcg4+','Rdg4+','Reg4+','Rfg4+','Rhg4+',
        'Rah4+','Rbh4+','Rch4+','Rdh4+','Reh4+','Rfh4+','Rgh4+',
        # moves (<>) (5)
        'Rba5+','Rca5+','Rda5+','Rea5+','Rfa5+','Rga5+','Rha5+',
        'Rab5+','Rcb5+','Rdb5+','Reb5+','Rfb5+','Rgb5+','Rhb5+',
        'Rac5+','Rbc5+','Rdc5+','Rec5+','Rfc5+','Rgc5+','Rhc5+',
        'Rad5+','Rbd5+','Rcd5+','Red5+','Rfd5+','Rgd5+','Rhd5+',
        'Rae5+','Rbe5+','Rce5+','Rde5+','Rfe5+','Rge5+','Rhe5+',
        'Raf5+','Rbf5+','Rcf5+','Rdf5+','Ref5+','Rgf5+','Rhf5+',
        'Rag5+','Rbg5+','Rcg5+','Rdg5+','Reg5+','Rfg5+','Rhg5+',
        'Rah5+','Rbh5+','Rch5+','Rdh5+','Reh5+','Rfh5+','Rgh5+',
        # moves (<>) (6)
        'Rba6+','Rca6+','Rda6+','Rea6+','Rfa6+','Rga6+','Rha6+',
        'Rab6+','Rcb6+','Rdb6+','Reb6+','Rfb6+','Rgb6+','Rhb6+',
        'Rac6+','Rbc6+','Rdc6+','Rec6+','Rfc6+','Rgc6+','Rhc6+',
        'Rad6+','Rbd6+','Rcd6+','Red6+','Rfd6+','Rgd6+','Rhd6+',
        'Rae6+','Rbe6+','Rce6+','Rde6+','Rfe6+','Rge6+','Rhe6+',
        'Raf6+','Rbf6+','Rcf6+','Rdf6+','Ref6+','Rgf6+','Rhf6+',
        'Rag6+','Rbg6+','Rcg6+','Rdg6+','Reg6+','Rfg6+','Rhg6+',
        'Rah6+','Rbh6+','Rch6+','Rdh6+','Reh6+','Rfh6+','Rgh6+',
        # moves (<>) (7)
        'Rba7+','Rca7+','Rda7+','Rea7+','Rfa7+','Rga7+','Rha7+',
        'Rab7+','Rcb7+','Rdb7+','Reb7+','Rfb7+','Rgb7+','Rhb7+',
        'Rac7+','Rbc7+','Rdc7+','Rec7+','Rfc7+','Rgc7+','Rhc7+',
        'Rad7+','Rbd7+','Rcd7+','Red7+','Rfd7+','Rgd7+','Rhd7+',
        'Rae7+','Rbe7+','Rce7+','Rde7+','Rfe7+','Rge7+','Rhe7+',
        'Raf7+','Rbf7+','Rcf7+','Rdf7+','Ref7+','Rgf7+','Rhf7+',
        'Rag7+','Rbg7+','Rcg7+','Rdg7+','Reg7+','Rfg7+','Rhg7+',
        'Rah7+','Rbh7+','Rch7+','Rdh7+','Reh7+','Rfh7+','Rgh7+',
        # moves (<>) (8)
        'Rba8+','Rca8+','Rda8+','Rea8+','Rfa8+','Rga8+','Rha8+',
        'Rab8+','Rcb8+','Rdb8+','Reb8+','Rfb8+','Rgb8+','Rhb8+',
        'Rac8+','Rbc8+','Rdc8+','Rec8+','Rfc8+','Rgc8+','Rhc8+',
        'Rad8+','Rbd8+','Rcd8+','Red8+','Rfd8+','Rgd8+','Rhd8+',
        'Rae8+','Rbe8+','Rce8+','Rde8+','Rfe8+','Rge8+','Rhe8+',
        'Raf8+','Rbf8+','Rcf8+','Rdf8+','Ref8+','Rgf8+','Rhf8+',
        'Rag8+','Rbg8+','Rcg8+','Rdg8+','Reg8+','Rfg8+','Rhg8+',
        'Rah8+','Rbh8+','Rch8+','Rdh8+','Reh8+','Rfh8+','Rgh8+',
        # take
        # |
        'Rxa1+','Rxa2+','Rxa3+','Rxa4+','Rxa5+','Rxa6+','Rxa7+','Rxa8+',
        'Rxb1+','Rxb2+','Rxb3+','Rxb4+','Rxb5+','Rxb6+','Rxb7+','Rxb8+',
        'Rxc1+','Rxc2+','Rxc3+','Rxc4+','Rxc5+','Rxc6+','Rxc7+','Rxc8+',
        'Rxd1+','Rxd2+','Rxd3+','Rxd4+','Rxd5+','Rxd6+','Rxd7+','Rxd8+',
        'Rxe1+','Rxe2+','Rxe3+','Rxe4+','Rxe5+','Rxe6+','Rxe7+','Rxe8+',
        'Rxf1+','Rxf2+','Rxf3+','Rxf4+','Rxf5+','Rxf6+','Rxf7+','Rxf8+',
        'Rxg1+','Rxg2+','Rxg3+','Rxg4+','Rxg5+','Rxg6+','Rxg7+','Rxg8+',
        'Rxh1+','Rxh2+','Rxh3+','Rxh4+','Rxh5+','Rxh6+','Rxh7+','Rxh8+',
        # <> (1)
        'Rbxa1+','Rcxa1+','Rdxa1+','Rexa1+','Rfxa1+','Rgxa1+','Rhxa1+',
        'Raxb1+','Rcxb1+','Rdxb1+','Rexb1+','Rfxb1+','Rgxb1+','Rhxb1+',
        'Raxc1+','Rbxc1+','Rdxc1+','Rexc1+','Rfxc1+','Rgxc1+','Rhxc1+',
        'Raxd1+','Rbxd1+','Rcxd1+','Rexd1+','Rfxd1+','Rgxd1+','Rhxd1+',
        'Raxe1+','Rbxe1+','Rcxe1+','Rdxe1+','Rfxe1+','Rgxe1+','Rhxe1+',
        'Raxf1+','Rbxf1+','Rcxf1+','Rdxf1+','Rexf1+','Rgxf1+','Rhxf1+',
        'Raxg1+','Rbxg1+','Rcxg1+','Rdxg1+','Rexg1+','Rfxg1+','Rhxg1+',
        'Raxh1+','Rbxh1+','Rcxh1+','Rdxh1+','Rexh1+','Rfxh1+','Rgxh1+',
        # <> (2)
        'Rbxa2+','Rcxa2+','Rdxa2+','Rexa2+','Rfxa2+','Rgxa2+','Rhxa2+',
        'Raxb2+','Rcxb2+','Rdxb2+','Rexb2+','Rfxb2+','Rgxb2+','Rhxb2+',
        'Raxc2+','Rbxc2+','Rdxc2+','Rexc2+','Rfxc2+','Rgxc2+','Rhxc2+',
        'Raxd2+','Rbxd2+','Rcxd2+','Rexd2+','Rfxd2+','Rgxd2+','Rhxd2+',
        'Raxe2+','Rbxe2+','Rcxe2+','Rdxe2+','Rfxe2+','Rgxe2+','Rhxe2+',
        'Raxf2+','Rbxf2+','Rcxf2+','Rdxf2+','Rexf2+','Rgxf2+','Rhxf2+',
        'Raxg2+','Rbxg2+','Rcxg2+','Rdxg2+','Rexg2+','Rfxg2+','Rhxg2+',
        'Raxh2+','Rbxh2+','Rcxh2+','Rdxh2+','Rexh2+','Rfxh2+','Rgxh2+',
        # <> (3)
        'Rbxa3+','Rcxa3+','Rdxa3+','Rexa3+','Rfxa3+','Rgxa3+','Rhxa3+',
        'Raxb3+','Rcxb3+','Rdxb3+','Rexb3+','Rfxb3+','Rgxb3+','Rhxb3+',
        'Raxc3+','Rbxc3+','Rdxc3+','Rexc3+','Rfxc3+','Rgxc3+','Rhxc3+',
        'Raxd3+','Rbxd3+','Rcxd3+','Rexd3+','Rfxd3+','Rgxd3+','Rhxd3+',
        'Raxe3+','Rbxe3+','Rcxe3+','Rdxe3+','Rfxe3+','Rgxe3+','Rhxe3+',
        'Raxf3+','Rbxf3+','Rcxf3+','Rdxf3+','Rexf3+','Rgxf3+','Rhxf3+',
        'Raxg3+','Rbxg3+','Rcxg3+','Rdxg3+','Rexg3+','Rfxg3+','Rhxg3+',
        'Raxh3+','Rbxh3+','Rcxh3+','Rdxh3+','Rexh3+','Rfxh3+','Rgxh3+',
        # <> (4)
        'Rbxa4+','Rcxa4+','Rdxa4+','Rexa4+','Rfxa4+','Rgxa4+','Rhxa4+',
        'Raxb4+','Rcxb4+','Rdxb4+','Rexb4+','Rfxb4+','Rgxb4+','Rhxb4+',
        'Raxc4+','Rbxc4+','Rdxc4+','Rexc4+','Rfxc4+','Rgxc4+','Rhxc4+',
        'Raxd4+','Rbxd4+','Rcxd4+','Rexd4+','Rfxd4+','Rgxd4+','Rhxd4+',
        'Raxe4+','Rbxe4+','Rcxe4+','Rdxe4+','Rfxe4+','Rgxe4+','Rhxe4+',
        'Raxf4+','Rbxf4+','Rcxf4+','Rdxf4+','Rexf4+','Rgxf4+','Rhxf4+',
        'Raxg4+','Rbxg4+','Rcxg4+','Rdxg4+','Rexg4+','Rfxg4+','Rhxg4+',
        'Raxh4+','Rbxh4+','Rcxh4+','Rdxh4+','Rexh4+','Rfxh4+','Rgxh4+',
        # <> (5)
        'Rbxa5+','Rcxa5+','Rdxa5+','Rexa5+','Rfxa5+','Rgxa5+','Rhxa5+',
        'Raxb5+','Rcxb5+','Rdxb5+','Rexb5+','Rfxb5+','Rgxb5+','Rhxb5+',
        'Raxc5+','Rbxc5+','Rdxc5+','Rexc5+','Rfxc5+','Rgxc5+','Rhxc5+',
        'Raxd5+','Rbxd5+','Rcxd5+','Rexd5+','Rfxd5+','Rgxd5+','Rhxd5+',
        'Raxe5+','Rbxe5+','Rcxe5+','Rdxe5+','Rfxe5+','Rgxe5+','Rhxe5+',
        'Raxf5+','Rbxf5+','Rcxf5+','Rdxf5+','Rexf5+','Rgxf5+','Rhxf5+',
        'Raxg5+','Rbxg5+','Rcxg5+','Rdxg5+','Rexg5+','Rfxg5+','Rhxg5+',
        'Raxh5+','Rbxh5+','Rcxh5+','Rdxh5+','Rexh5+','Rfxh5+','Rgxh5+',
        # <> (6)
        'Rbxa6+','Rcxa6+','Rdxa6+','Rexa6+','Rfxa6+','Rgxa6+','Rhxa6+',
        'Raxb6+','Rcxb6+','Rdxb6+','Rexb6+','Rfxb6+','Rgxb6+','Rhxb6+',
        'Raxc6+','Rbxc6+','Rdxc6+','Rexc6+','Rfxc6+','Rgxc6+','Rhxc6+',
        'Raxd6+','Rbxd6+','Rcxd6+','Rexd6+','Rfxd6+','Rgxd6+','Rhxd6+',
        'Raxe6+','Rbxe6+','Rcxe6+','Rdxe6+','Rfxe6+','Rgxe6+','Rhxe6+',
        'Raxf6+','Rbxf6+','Rcxf6+','Rdxf6+','Rexf6+','Rgxf6+','Rhxf6+',
        'Raxg6+','Rbxg6+','Rcxg6+','Rdxg6+','Rexg6+','Rfxg6+','Rhxg6+',
        'Raxh6+','Rbxh6+','Rcxh6+','Rdxh6+','Rexh6+','Rfxh6+','Rgxh6+',
        # <> (7)
        'Rbxa7+','Rcxa7+','Rdxa7+','Rexa7+','Rfxa7+','Rgxa7+','Rhxa7+',
        'Raxb7+','Rcxb7+','Rdxb7+','Rexb7+','Rfxb7+','Rgxb7+','Rhxb7+',
        'Raxc7+','Rbxc7+','Rdxc7+','Rexc7+','Rfxc7+','Rgxc7+','Rhxc7+',
        'Raxd7+','Rbxd7+','Rcxd7+','Rexd7+','Rfxd7+','Rgxd7+','Rhxd7+',
        'Raxe7+','Rbxe7+','Rcxe7+','Rdxe7+','Rfxe7+','Rgxe7+','Rhxe7+',
        'Raxf7+','Rbxf7+','Rcxf7+','Rdxf7+','Rexf7+','Rgxf7+','Rhxf7+',
        'Raxg7+','Rbxg7+','Rcxg7+','Rdxg7+','Rexg7+','Rfxg7+','Rhxg7+',
        'Raxh7+','Rbxh7+','Rcxh7+','Rdxh7+','Rexh7+','Rfxh7+','Rgxh7+',
        # <> (8)
        'Rbxa8+','Rcxa8+','Rdxa8+','Rexa8+','Rfxa8+','Rgxa8+','Rhxa8+',
        'Raxb8+','Rcxb8+','Rdxb8+','Rexb8+','Rfxb8+','Rgxb8+','Rhxb8+',
        'Raxc8+','Rbxc8+','Rdxc8+','Rexc8+','Rfxc8+','Rgxc8+','Rhxc8+',
        'Raxd8+','Rbxd8+','Rcxd8+','Rexd8+','Rfxd8+','Rgxd8+','Rhxd8+',
        'Raxe8+','Rbxe8+','Rcxe8+','Rdxe8+','Rfxe8+','Rgxe8+','Rhxe8+',
        'Raxf8+','Rbxf8+','Rcxf8+','Rdxf8+','Rexf8+','Rgxf8+','Rhxf8+',
        'Raxg8+','Rbxg8+','Rcxg8+','Rdxg8+','Rexg8+','Rfxg8+','Rhxg8+',
        'Raxh8+','Rbxh8+','Rcxh8+','Rdxh8+','Rexh8+','Rfxh8+','Rgxh8+',
        # mate
        # moves (|)
        'Ra1#','Ra2#','Ra3#','Ra4#','Ra5#','Ra6#','Ra7#','Ra8#',
        'Rb1#','Rb2#','Rb3#','Rb4#','Rb5#','Rb6#','Rb7#','Rb8#',
        'Rc1#','Rc2#','Rc3#','Rc4#','Rc5#','Rc6#','Rc7#','Rc8#',
        'Rd1#','Rd2#','Rd3#','Rd4#','Rd5#','Rd6#','Rd7#','Rd8#',
        'Re1#','Re2#','Re3#','Re4#','Re5#','Re6#','Re7#','Re8#',
        'Rf1#','Rf2#','Rf3#','Rf4#','Rf5#','Rf6#','Rf7#','Rf8#',
        'Rg1#','Rg2#','Rg3#','Rg4#','Rg5#','Rg6#','Rg7#','Rg8#',
        'Rh1#','Rh2#','Rh3#','Rh4#','Rh5#','Rh6#','Rh7#','Rh8#',
        # moves(<>) (1)
        'Rba1#','Rca1#','Rda1#','Rea1#','Rfa1#','Rga1#','Rha1#',
        'Rab1#','Rcb1#','Rdb1#','Reb1#','Rfb1#','Rgb1#','Rhb1#',
        'Rac1#','Rbc1#','Rdc1#','Rec1#','Rfc1#','Rgc1#','Rhc1#',
        'Rad1#','Rbd1#','Rcd1#','Red1#','Rfd1#','Rgd1#','Rhd1#',
        'Rae1#','Rbe1#','Rce1#','Rde1#','Rfe1#','Rge1#','Rhe1#',
        'Raf1#','Rbf1#','Rcf1#','Rdf1#','Ref1#','Rgf1#','Rhf1#',
        'Rag1#','Rbg1#','Rcg1#','Rdg1#','Reg1#','Rfg1#','Rhg1#',
        'Rah1#','Rbh1#','Rch1#','Rdh1#','Reh1#','Rfh1#','Rgh1#',
        # moves(<>) (2)
        'Rba2#','Rca2#','Rda2#','Rea2#','Rfa2#','Rga2#','Rha2#',
        'Rab2#','Rcb2#','Rdb2#','Reb2#','Rfb2#','Rgb2#','Rhb2#',
        'Rac2#','Rbc2#','Rdc2#','Rec2#','Rfc2#','Rgc2#','Rhc2#',
        'Rad2#','Rbd2#','Rcd2#','Red2#','Rfd2#','Rgd2#','Rhd2#',
        'Rae2#','Rbe2#','Rce2#','Rde2#','Rfe2#','Rge2#','Rhe2#',
        'Raf2#','Rbf2#','Rcf2#','Rdf2#','Ref2#','Rgf2#','Rhf2#',
        'Rag2#','Rbg2#','Rcg2#','Rdg2#','Reg2#','Rfg2#','Rhg2#',
        'Rah2#','Rbh2#','Rch2#','Rdh2#','Reh2#','Rfh2#','Rgh2#',
        # moves (<>) (3)
        'Rba3#','Rca3#','Rda3#','Rea3#','Rfa3#','Rga3#','Rha3#',
        'Rab3#','Rcb3#','Rdb3#','Reb3#','Rfb3#','Rgb3#','Rhb3#',
        'Rac3#','Rbc3#','Rdc3#','Rec3#','Rfc3#','Rgc3#','Rhc3#',
        'Rad3#','Rbd3#','Rcd3#','Red3#','Rfd3#','Rgd3#','Rhd3#',
        'Rae3#','Rbe3#','Rce3#','Rde3#','Rfe3#','Rge3#','Rhe3#',
        'Raf3#','Rbf3#','Rcf3#','Rdf3#','Ref3#','Rgf3#','Rhf3#',
        'Rag3#','Rbg3#','Rcg3#','Rdg3#','Reg3#','Rfg3#','Rhg3#',
        'Rah3#','Rbh3#','Rch3#','Rdh3#','Reh3#','Rfh3#','Rgh3#',
        # moves (<>) (4)
        'Rba4#','Rca4#','Rda4#','Rea4#','Rfa4#','Rga4#','Rha4#',
        'Rab4#','Rcb4#','Rdb4#','Reb4#','Rfb4#','Rgb4#','Rhb4#',
        'Rac4#','Rbc4#','Rdc4#','Rec4#','Rfc4#','Rgc4#','Rhc4#',
        'Rad4#','Rbd4#','Rcd4#','Red4#','Rfd4#','Rgd4#','Rhd4#',
        'Rae4#','Rbe4#','Rce4#','Rde4#','Rfe4#','Rge4#','Rhe4#',
        'Raf4#','Rbf4#','Rcf4#','Rdf4#','Ref4#','Rgf4#','Rhf4#',
        'Rag4#','Rbg4#','Rcg4#','Rdg4#','Reg4#','Rfg4#','Rhg4#',
        'Rah4#','Rbh4#','Rch4#','Rdh4#','Reh4#','Rfh4#','Rgh4#',
        # moves (<>) (5)
        'Rba5#','Rca5#','Rda5#','Rea5#','Rfa5#','Rga5#','Rha5#',
        'Rab5#','Rcb5#','Rdb5#','Reb5#','Rfb5#','Rgb5#','Rhb5#',
        'Rac5#','Rbc5#','Rdc5#','Rec5#','Rfc5#','Rgc5#','Rhc5#',
        'Rad5#','Rbd5#','Rcd5#','Red5#','Rfd5#','Rgd5#','Rhd5#',
        'Rae5#','Rbe5#','Rce5#','Rde5#','Rfe5#','Rge5#','Rhe5#',
        'Raf5#','Rbf5#','Rcf5#','Rdf5#','Ref5#','Rgf5#','Rhf5#',
        'Rag5#','Rbg5#','Rcg5#','Rdg5#','Reg5#','Rfg5#','Rhg5#',
        'Rah5#','Rbh5#','Rch5#','Rdh5#','Reh5#','Rfh5#','Rgh5#',
        # moves (<>) (6)
        'Rba6#','Rca6#','Rda6#','Rea6#','Rfa6#','Rga6#','Rha6#',
        'Rab6#','Rcb6#','Rdb6#','Reb6#','Rfb6#','Rgb6#','Rhb6#',
        'Rac6#','Rbc6#','Rdc6#','Rec6#','Rfc6#','Rgc6#','Rhc6#',
        'Rad6#','Rbd6#','Rcd6#','Red6#','Rfd6#','Rgd6#','Rhd6#',
        'Rae6#','Rbe6#','Rce6#','Rde6#','Rfe6#','Rge6#','Rhe6#',
        'Raf6#','Rbf6#','Rcf6#','Rdf6#','Ref6#','Rgf6#','Rhf6#',
        'Rag6#','Rbg6#','Rcg6#','Rdg6#','Reg6#','Rfg6#','Rhg6#',
        'Rah6#','Rbh6#','Rch6#','Rdh6#','Reh6#','Rfh6#','Rgh6#',
        # moves (<>) (7)
        'Rba7#','Rca7#','Rda7#','Rea7#','Rfa7#','Rga7#','Rha7#',
        'Rab7#','Rcb7#','Rdb7#','Reb7#','Rfb7#','Rgb7#','Rhb7#',
        'Rac7#','Rbc7#','Rdc7#','Rec7#','Rfc7#','Rgc7#','Rhc7#',
        'Rad7#','Rbd7#','Rcd7#','Red7#','Rfd7#','Rgd7#','Rhd7#',
        'Rae7#','Rbe7#','Rce7#','Rde7#','Rfe7#','Rge7#','Rhe7#',
        'Raf7#','Rbf7#','Rcf7#','Rdf7#','Ref7#','Rgf7#','Rhf7#',
        'Rag7#','Rbg7#','Rcg7#','Rdg7#','Reg7#','Rfg7#','Rhg7#',
        'Rah7#','Rbh7#','Rch7#','Rdh7#','Reh7#','Rfh7#','Rgh7#',
        # moves (<>) (8)
        'Rba8#','Rca8#','Rda8#','Rea8#','Rfa8#','Rga8#','Rha8#',
        'Rab8#','Rcb8#','Rdb8#','Reb8#','Rfb8#','Rgb8#','Rhb8#',
        'Rac8#','Rbc8#','Rdc8#','Rec8#','Rfc8#','Rgc8#','Rhc8#',
        'Rad8#','Rbd8#','Rcd8#','Red8#','Rfd8#','Rgd8#','Rhd8#',
        'Rae8#','Rbe8#','Rce8#','Rde8#','Rfe8#','Rge8#','Rhe8#',
        'Raf8#','Rbf8#','Rcf8#','Rdf8#','Ref8#','Rgf8#','Rhf8#',
        'Rag8#','Rbg8#','Rcg8#','Rdg8#','Reg8#','Rfg8#','Rhg8#',
        'Rah8#','Rbh8#','Rch8#','Rdh8#','Reh8#','Rfh8#','Rgh8#',
        # take
        # |
        'Rxa1#','Rxa2#','Rxa3#','Rxa4#','Rxa5#','Rxa6#','Rxa7#','Rxa8#',
        'Rxb1#','Rxb2#','Rxb3#','Rxb4#','Rxb5#','Rxb6#','Rxb7#','Rxb8#',
        'Rxc1#','Rxc2#','Rxc3#','Rxc4#','Rxc5#','Rxc6#','Rxc7#','Rxc8#',
        'Rxd1#','Rxd2#','Rxd3#','Rxd4#','Rxd5#','Rxd6#','Rxd7#','Rxd8#',
        'Rxe1#','Rxe2#','Rxe3#','Rxe4#','Rxe5#','Rxe6#','Rxe7#','Rxe8#',
        'Rxf1#','Rxf2#','Rxf3#','Rxf4#','Rxf5#','Rxf6#','Rxf7#','Rxf8#',
        'Rxg1#','Rxg2#','Rxg3#','Rxg4#','Rxg5#','Rxg6#','Rxg7#','Rxg8#',
        'Rxh1#','Rxh2#','Rxh3#','Rxh4#','Rxh5#','Rxh6#','Rxh7#','Rxh8#',
        # <> (1)
        'Rbxa1#','Rcxa1#','Rdxa1#','Rexa1#','Rfxa1#','Rgxa1#','Rhxa1#',
        'Raxb1#','Rcxb1#','Rdxb1#','Rexb1#','Rfxb1#','Rgxb1#','Rhxb1#',
        'Raxc1#','Rbxc1#','Rdxc1#','Rexc1#','Rfxc1#','Rgxc1#','Rhxc1#',
        'Raxd1#','Rbxd1#','Rcxd1#','Rexd1#','Rfxd1#','Rgxd1#','Rhxd1#',
        'Raxe1#','Rbxe1#','Rcxe1#','Rdxe1#','Rfxe1#','Rgxe1#','Rhxe1#',
        'Raxf1#','Rbxf1#','Rcxf1#','Rdxf1#','Rexf1#','Rgxf1#','Rhxf1#',
        'Raxg1#','Rbxg1#','Rcxg1#','Rdxg1#','Rexg1#','Rfxg1#','Rhxg1#',
        'Raxh1#','Rbxh1#','Rcxh1#','Rdxh1#','Rexh1#','Rfxh1#','Rgxh1#',
        # <> (2)
        'Rbxa2#','Rcxa2#','Rdxa2#','Rexa2#','Rfxa2#','Rgxa2#','Rhxa2#',
        'Raxb2#','Rcxb2#','Rdxb2#','Rexb2#','Rfxb2#','Rgxb2#','Rhxb2#',
        'Raxc2#','Rbxc2#','Rdxc2#','Rexc2#','Rfxc2#','Rgxc2#','Rhxc2#',
        'Raxd2#','Rbxd2#','Rcxd2#','Rexd2#','Rfxd2#','Rgxd2#','Rhxd2#',
        'Raxe2#','Rbxe2#','Rcxe2#','Rdxe2#','Rfxe2#','Rgxe2#','Rhxe2#',
        'Raxf2#','Rbxf2#','Rcxf2#','Rdxf2#','Rexf2#','Rgxf2#','Rhxf2#',
        'Raxg2#','Rbxg2#','Rcxg2#','Rdxg2#','Rexg2#','Rfxg2#','Rhxg2#',
        'Raxh2#','Rbxh2#','Rcxh2#','Rdxh2#','Rexh2#','Rfxh2#','Rgxh2#',
        # <> (3)
        'Rbxa3#','Rcxa3#','Rdxa3#','Rexa3#','Rfxa3#','Rgxa3#','Rhxa3#',
        'Raxb3#','Rcxb3#','Rdxb3#','Rexb3#','Rfxb3#','Rgxb3#','Rhxb3#',
        'Raxc3#','Rbxc3#','Rdxc3#','Rexc3#','Rfxc3#','Rgxc3#','Rhxc3#',
        'Raxd3#','Rbxd3#','Rcxd3#','Rexd3#','Rfxd3#','Rgxd3#','Rhxd3#',
        'Raxe3#','Rbxe3#','Rcxe3#','Rdxe3#','Rfxe3#','Rgxe3#','Rhxe3#',
        'Raxf3#','Rbxf3#','Rcxf3#','Rdxf3#','Rexf3#','Rgxf3#','Rhxf3#',
        'Raxg3#','Rbxg3#','Rcxg3#','Rdxg3#','Rexg3#','Rfxg3#','Rhxg3#',
        'Raxh3#','Rbxh3#','Rcxh3#','Rdxh3#','Rexh3#','Rfxh3#','Rgxh3#',
        # <> (4)
        'Rbxa4#','Rcxa4#','Rdxa4#','Rexa4#','Rfxa4#','Rgxa4#','Rhxa4#',
        'Raxb4#','Rcxb4#','Rdxb4#','Rexb4#','Rfxb4#','Rgxb4#','Rhxb4#',
        'Raxc4#','Rbxc4#','Rdxc4#','Rexc4#','Rfxc4#','Rgxc4#','Rhxc4#',
        'Raxd4#','Rbxd4#','Rcxd4#','Rexd4#','Rfxd4#','Rgxd4#','Rhxd4#',
        'Raxe4#','Rbxe4#','Rcxe4#','Rdxe4#','Rfxe4#','Rgxe4#','Rhxe4#',
        'Raxf4#','Rbxf4#','Rcxf4#','Rdxf4#','Rexf4#','Rgxf4#','Rhxf4#',
        'Raxg4#','Rbxg4#','Rcxg4#','Rdxg4#','Rexg4#','Rfxg4#','Rhxg4#',
        'Raxh4#','Rbxh4#','Rcxh4#','Rdxh4#','Rexh4#','Rfxh4#','Rgxh4#',
        # <> (5)
        'Rbxa5#','Rcxa5#','Rdxa5#','Rexa5#','Rfxa5#','Rgxa5#','Rhxa5#',
        'Raxb5#','Rcxb5#','Rdxb5#','Rexb5#','Rfxb5#','Rgxb5#','Rhxb5#',
        'Raxc5#','Rbxc5#','Rdxc5#','Rexc5#','Rfxc5#','Rgxc5#','Rhxc5#',
        'Raxd5#','Rbxd5#','Rcxd5#','Rexd5#','Rfxd5#','Rgxd5#','Rhxd5#',
        'Raxe5#','Rbxe5#','Rcxe5#','Rdxe5#','Rfxe5#','Rgxe5#','Rhxe5#',
        'Raxf5#','Rbxf5#','Rcxf5#','Rdxf5#','Rexf5#','Rgxf5#','Rhxf5#',
        'Raxg5#','Rbxg5#','Rcxg5#','Rdxg5#','Rexg5#','Rfxg5#','Rhxg5#',
        'Raxh5#','Rbxh5#','Rcxh5#','Rdxh5#','Rexh5#','Rfxh5#','Rgxh5#',
        # <> (6)
        'Rbxa6#','Rcxa6#','Rdxa6#','Rexa6#','Rfxa6#','Rgxa6#','Rhxa6#',
        'Raxb6#','Rcxb6#','Rdxb6#','Rexb6#','Rfxb6#','Rgxb6#','Rhxb6#',
        'Raxc6#','Rbxc6#','Rdxc6#','Rexc6#','Rfxc6#','Rgxc6#','Rhxc6#',
        'Raxd6#','Rbxd6#','Rcxd6#','Rexd6#','Rfxd6#','Rgxd6#','Rhxd6#',
        'Raxe6#','Rbxe6#','Rcxe6#','Rdxe6#','Rfxe6#','Rgxe6#','Rhxe6#',
        'Raxf6#','Rbxf6#','Rcxf6#','Rdxf6#','Rexf6#','Rgxf6#','Rhxf6#',
        'Raxg6#','Rbxg6#','Rcxg6#','Rdxg6#','Rexg6#','Rfxg6#','Rhxg6#',
        'Raxh6#','Rbxh6#','Rcxh6#','Rdxh6#','Rexh6#','Rfxh6#','Rgxh6#',
        # <> (7)
        'Rbxa7#','Rcxa7#','Rdxa7#','Rexa7#','Rfxa7#','Rgxa7#','Rhxa7#',
        'Raxb7#','Rcxb7#','Rdxb7#','Rexb7#','Rfxb7#','Rgxb7#','Rhxb7#',
        'Raxc7#','Rbxc7#','Rdxc7#','Rexc7#','Rfxc7#','Rgxc7#','Rhxc7#',
        'Raxd7#','Rbxd7#','Rcxd7#','Rexd7#','Rfxd7#','Rgxd7#','Rhxd7#',
        'Raxe7#','Rbxe7#','Rcxe7#','Rdxe7#','Rfxe7#','Rgxe7#','Rhxe7#',
        'Raxf7#','Rbxf7#','Rcxf7#','Rdxf7#','Rexf7#','Rgxf7#','Rhxf7#',
        'Raxg7#','Rbxg7#','Rcxg7#','Rdxg7#','Rexg7#','Rfxg7#','Rhxg7#',
        'Raxh7#','Rbxh7#','Rcxh7#','Rdxh7#','Rexh7#','Rfxh7#','Rgxh7#',
        # <> (8)
        'Rbxa8#','Rcxa8#','Rdxa8#','Rexa8#','Rfxa8#','Rgxa8#','Rhxa8#',
        'Raxb8#','Rcxb8#','Rdxb8#','Rexb8#','Rfxb8#','Rgxb8#','Rhxb8#',
        'Raxc8#','Rbxc8#','Rdxc8#','Rexc8#','Rfxc8#','Rgxc8#','Rhxc8#',
        'Raxd8#','Rbxd8#','Rcxd8#','Rexd8#','Rfxd8#','Rgxd8#','Rhxd8#',
        'Raxe8#','Rbxe8#','Rcxe8#','Rdxe8#','Rfxe8#','Rgxe8#','Rhxe8#',
        'Raxf8#','Rbxf8#','Rcxf8#','Rdxf8#','Rexf8#','Rgxf8#','Rhxf8#',
        'Raxg8#','Rbxg8#','Rcxg8#','Rdxg8#','Rexg8#','Rfxg8#','Rhxg8#',
        'Raxh8#','Rbxh8#','Rcxh8#','Rdxh8#','Rexh8#','Rfxh8#','Rgxh8#',
    #                      KING                     #
        # moves
        'Ka1','Ka2','Ka3','Ka4','Ka5','Ka6','Ka7','Ka8',
        'Kb1','Kb2','Kb3','Kb4','Kb5','Kb6','Kb7','Kb8',
        'Kc1','Kc2','Kc3','Kc4','Kc5','Kc6','Kc7','Kc8',
        'Kd1','Kd2','Kd3','Kd4','Kd5','Kd6','Kd7','Kd8',
        'Ke1','Ke2','Ke3','Ke4','Ke5','Ke6','Ke7','Ke8',
        'Kf1','Kf2','Kf3','Kf4','Kf5','Kf6','Kf7','Kf8',
        'Kg1','Kg2','Kg3','Kg4','Kg5','Kg6','Kg7','Kg8',
        'Kh1','Kh2','Kh3','Kh4','Kh5','Kh6','Kh7','Kh8',
        # check
        'Ka1+','Ka2+','Ka3+','Ka4+','Ka5+','Ka6+','Ka7+','Ka8+',
        'Kb1+','Kb2+','Kb3+','Kb4+','Kb5+','Kb6+','Kb7+','Kb8+',
        'Kc1+','Kc2+','Kc3+','Kc4+','Kc5+','Kc6+','Kc7+','Kc8+',
        'Kd1+','Kd2+','Kd3+','Kd4+','Kd5+','Kd6+','Kd7+','Kd8+',
        'Ke1+','Ke2+','Ke3+','Ke4+','Ke5+','Ke6+','Ke7+','Ke8+',
        'Kf1+','Kf2+','Kf3+','Kf4+','Kf5+','Kf6+','Kf7+','Kf8+',
        'Kg1+','Kg2+','Kg3+','Kg4+','Kg5+','Kg6+','Kg7+','Kg8+',
        'Kh1+','Kh2+','Kh3+','Kh4+','Kh5+','Kh6+','Kh7+','Kh8+',
        # mate
        'Ka1#','Ka2#','Ka3#','Ka4#','Ka5#','Ka6#','Ka7#','Ka8#',
        'Kb1#','Kb2#','Kb3#','Kb4#','Kb5#','Kb6#','Kb7#','Kb8#',
        'Kc1#','Kc2#','Kc3#','Kc4#','Kc5#','Kc6#','Kc7#','Kc8#',
        'Kd1#','Kd2#','Kd3#','Kd4#','Kd5#','Kd6#','Kd7#','Kd8#',
        'Ke1#','Ke2#','Ke3#','Ke4#','Ke5#','Ke6#','Ke7#','Ke8#',
        'Kf1#','Kf2#','Kf3#','Kf4#','Kf5#','Kf6#','Kf7#','Kf8#',
        'Kg1#','Kg2#','Kg3#','Kg4#','Kg5#','Kg6#','Kg7#','Kg8#',
        'Kh1#','Kh2#','Kh3#','Kh4#','Kh5#','Kh6#','Kh7#','Kh8#',
        #     castle     #
        'O-O','O-O-O',
        # check
        'O-O+','O-O-O+',
        # mate
        'O-O#','O-O-O#',
        )
    
    #########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

    # find all posible moves
    def pos_moves(self,terms: int) -> list: 
        self.pos_move=[]
        for i in self.allPosibleMove:
            if len(i)>=3 and 'R' in i and i[1] in self.pawnList and not i[2] in self.pawnList:
                piece,x,y=i[0]+i[1],i[1],int(i[2])
            elif len(i)>=4 and 'x' in i:
                piece,x,y=i[0],i[2],int(i[3])
            elif len(i)>=4 and 'R' in i and i[1] in self.pawnList and i[2] in self.pawnList:
                piece,x,y=i[0]+i[1],i[2],int(i[3])
            elif len(i)>=5 and 'R' in i and 'x' in i and i[1] in self.pawnList and i[3] in self.pawnList:
                piece,x,y=i[0]+i[1],i[3],int(i[4])
            elif len(i)>=3:
                piece,x,y=i[0],i[1],int(i[2])
            elif '=' in i and not 'x' in i and not( 'R' in i or '+' in i or '#' in i):
                piece,x,y,self.change=i[0],i[0],int(i[1]),i[-1]
            elif '=' in i and 'x' in i and not( 'R' in i or '+' in i or '#' in i):
                piece,x,y,self.change=i[0],i[2],int(i[3]),i[-1]
            elif '=' in i and 'x' in i and 'R' in i and not ('+' in i or '#' in i):
                piece,x,y,self.change=i[0],i[2],int(i[3]),i[-2]+i[-1]
            elif '=' in i and not'x' in i and 'R' in i and not ('+' in i or '#' in i):
                piece,x,y,self.change=i[0],i[0],int(i[1]),i[-2]+i[-1]
            elif '=' in i and 'x' in i and not 'R' in i and ('+' in i or '#' in i):
                piece,x,y,self.change=i[0],i[2],int(i[3]),i[-2]
            elif '=' in i and not 'x' in i and not 'R' in i and ('+' in i or '#' in i):
                piece,x,y,self.change=i[0],i[0],int(i[2]),i[-2]
            elif '=' in i and 'x' in i and 'R' in i and ('+' in i or '#' in i):
                piece,x,y,self.change=i[0],i[2],int(i[3]),i[-3]+i[-2]
            elif '=' in i and not 'x' in i and 'R' in i and ('+' in i or '#' in i):
                piece,x,y,self.change=i[0],i[0],int(i[1]),i[-3]+i[-2]
            elif len(i)>=2:
                piece,x,y=i[0],i[0],int(i[1])
            if self.validate(piece,x,y,terms) and not self.traceback(self.findKing(terms)):
                for k in self.copiedBoard:
                    for j in k:
                        if j!=' ':
                            if j['name']==piece:
                                _,=j
                                k.replace(j,' ')
                                self.copiedBoard[-y][self.pawnList.index(x)]=_
                                self.pos_move.append(i)
                                if not self.checks(1-playerBloc):
                                    self.copiedBoard=self.text_board
                                    self.pos_move.remove(i)
                                for k in self.copiedBoard:
                                    for j in k:
                                        if j!=' ':
                                            if j['name'] in self.pawnList:
                                                j['double']=False
                                    if self.copiedBoard.index(i)==6:
                                        break 
            self.copiedBoard=self.text_board
        return self.pos_move
    # finding the King
    def findKing(self,blocs=playerBloc):
        for i in self.text_board:
            for j in i:
                if j!=' ':
                    if j['name']=='K' and j['bloc']==blocs:
                        self.kx,self.ky=i.index(j),self.text_board.index(i)
                        return self.kx,self.ky,blocs
        return self.kx,self.ky,blocs
    # tracing back
    def traceback(self,*arg):
        x_coor,y_coor,blocs=arg[0],arg[1],arg[2]
        x_coor,y_coor=self.pawnList.index(x_coor),8-y_coor
        # tracing pawn
        if y_coor+1<=7 or x_coor+1<=7:
            if self.text_board[y_coor+1][x_coor+1]!=' ': 
                if self.text_board[y_coor+1][x_coor+1]['name'] in self.pawnList and self.text_board[y_coor+1][x_coor+1]['bloc']==0:   
                    return True
        if y_coor+1<=7 or x_coor-1>=0:
            if self.text_board[y_coor+1][x_coor-1]!=' ':
                if self.text_board[y_coor+1][x_coor-1]['name'] in self.pawnList and self.text_board[y_coor+1][x_coor-1]['bloc']==0:
                    return True
        if y_coor-1>=0 or x_coor-1>=0:
            if self.text_board[y_coor-1][x_coor-1]!=' ':
                if self.text_board[y_coor-1][x_coor-1]['name'] in self.pawnList and self.text_board[y_coor-1][x_coor-1]['bloc']==1:                       
                    return True
        if y_coor-1>=0 or x_coor+1<=7:
            if self.text_board[y_coor-1][x_coor+1]!=' ':
                if self.text_board[y_coor-1][x_coor+1]['name'] in self.pawnList and self.text_board[y_coor-1][x_coor+1]['bloc']==1:
                    return True
        # tracing bishop
        for b in range(1,8): # Quater I
            if y_coor+b>7 or x_coor+b>7:
                break
            if self.text_board[y_coor+b][x_coor+b]!=' ':
                if (self.text_board[y_coor+b][x_coor+b]['name']=='B' or self.text_board[y_coor+b][x_coor+b]['name']=='Q') and self.text_board[y_coor+b][x_coor+b]['bloc']!=blocs:
                    return True
                else:
                    break
        for b in range(1,8): # Quater II
            if y_coor+b>7 or x_coor-b<0:
                break
            if self.text_board[y_coor+b][x_coor-b]!=' ':
                if (self.text_board[y_coor+b][x_coor-b]['name']=='B' or self.text_board[y_coor+b][x_coor-b]['name']=='Q') and self.text_board[y_coor+b][x_coor-b]['bloc']!=blocs:
                    return True
                else:
                    break
        for b in range(1,8): # Quater III
            if y_coor-b<0 or x_coor-b<0:
                break
            if self.text_board[y_coor-b][x_coor-b]!=' ':
                if (self.text_board[y_coor-b][x_coor-b]['name']=='B' or self.text_board[y_coor-b][x_coor-b]['name']=='Q') and self.text_board[y_coor-b][x_coor-b]['bloc']!=blocs:
                    return True
                else:
                    break
        for b in range(1,8): # Quater IV
            if  y_coor-b<0 or x_coor+b>7:
                break
            if self.text_board[y_coor-b][x_coor+b]==' ':
                if (self.text_board[y_coor-b][x_coor+b]=='B' or self.text_board[y_coor-b][x_coor+b]['name']=='Q') and self.text_board[y_coor-b][x_coor+b]['bloc']!=blocs:
                    return True
            else:
                break
        # tracing knight
        if y_coor+2<8 and x_coor+1<8:
            if self.text_board[y_coor+2][x_coor+1]!=' ':
                if self.text_board[y_coor+2][x_coor+1]['bloc']!=blocs and self.text_board[y_coor+2][x_coor+1]['name']=='N':
                    return True
        if y_coor+2<8 and x_coor-1>=0:
            if self.text_board[y_coor+2][x_coor-1]!=' ':
                if self.text_board[y_coor+2][x_coor-1]['bloc']!=blocs and self.text_board[y_coor+2][x_coor-1]['name']=='N':
                    return True
        if y_coor-2>=0 and x_coor+1<8:
            if self.text_board[y_coor-2][x_coor+1]!=' ':
                if self.text_board[y_coor-2][x_coor+1]['bloc']!=blocs and self.text_board[y_coor-2][x_coor+1]['name']=='N':
                    return True
        if  y_coor-2>=0 and x_coor-1>=0:
            if self.text_board[y_coor-2][x_coor-1]!=' ':
                if self.text_board[y_coor-2][x_coor-1]['bloc']!=blocs and self.text_board[y_coor-2][x_coor-1]['name']=='N':
                    return True
        if  y_coor-2>=0 and x_coor-1>=0:
            if self.text_board[y_coor+1][x_coor+2]!=' ':
                if self.text_board[y_coor+1][x_coor+2]['bloc']!=blocs and self.text_board[y_coor+1][x_coor+2]['name']=='N':
                    return True
        if  y_coor+1<8 and x_coor-2>=0:
            if self.text_board[y_coor+1][x_coor-2]!=' ':
                if self.text_board[y_coor+1][x_coor-2]['bloc']!=blocs and self.text_board[y_coor+1][x_coor-2]['name']=='N':
                    return True
        if y_coor-1>=0 and x_coor-2>=0:
            if self.text_board[y_coor-1][x_coor-2]!=' ':
                if self.text_board[y_coor-1][x_coor-2]['bloc']!=blocs and self.text_board[y_coor-2][x_coor-1]['name']=='N':
                    return True
        if y_coor-1>=0 and x_coor+2<8:
            if self.text_board[y_coor-1][x_coor+2]!=' ':
                if self.text_board[y_coor-1][x_coor+2]['bloc']!=blocs and self.text_board[y_coor-2][x_coor-1]['name']=='N':
                    return True
        # tracing rook
        # |
        for r in range(1,8):
            if y_coor+r<8:
                if self.text_board[y_coor+r][x_coor]!=' ':
                    if self.text_board[y_coor+r][x_coor]['bloc']!=blocs and ('R' in self.text_board[y_coor+r][x_coor]['name'] or 'Q'==self.text_board[y_coor+r][x_coor]['name']):
                        return True
                    elif self.text_board[y_coor+r][x_coor]['bloc']==blocs or (not 'R' in self.text_board[y_coor+r][x_coor]['name'] and 'Q'!=self.text_board[y_coor+r][x_coor]['name']):
                        break
            else:
                break
        #^
        for r in range(1,8):
            if y_coor-r>=0:
                if self.text_board[y_coor-r][x_coor]!=' ':
                    if self.text_board[y_coor-r][x_coor]['bloc']!=blocs and ('R' in self.text_board[y_coor-r][x_coor]['name'] or 'Q'==self.text_board[y_coor-r][x_coor]['name']):
                        return True
                    elif self.text_board[y_coor-r][x_coor]['bloc']==blocs or (not 'R' in self.text_board[y_coor-r][x_coor]['name'] and 'Q'!=self.text_board[y_coor-r][x_coor]['name']):
                        break
            else:
                break
        # >
        for r in range(1,8):
            if x_coor+r<8:
                if self.text_board[y_coor][x_coor+r]!=' ':
                    if self.text_board[y_coor][x_coor+r]['bloc']!=blocs and ('R' in self.text_board[y_coor][x_coor+r]['name'] or 'Q'==self.text_board[y_coor][x_coor+r]['name']):
                        return True
                    elif self.text_board[y_coor][x_coor+r]['bloc']==blocs or (not 'R' in self.text_board[y_coor][x_coor+r]['name'] and 'Q'!=self.text_board[y_coor][x_coor+r]['name']):
                        break
            else:
                break
        #<
        for r in range(1,8):
            if x_coor-r>=0:
                if self.text_board[y_coor][x_coor-r]!=' ':
                    if self.text_board[y_coor][x_coor-r]['bloc']!=blocs and ('R' in self.text_board[y_coor][x_coor-r]['name'] or 'Q'==self.text_board[y_coor][x_coor-r]['name']):
                        return True
                    elif self.text_board[y_coor][x_coor-r]['bloc']==blocs or (not 'R' in self.text_board[y_coor][x_coor-r]['name'] and 'Q'!=self.text_board[y_coor][x_coor-r]['name']):
                        break
            else:
                break
        # tracing king
        for k in range(1):
            if y_coor+k>7 or y_coor-k<0 or x_coor+k>7 or x_coor-k<0:
                break
            if self.text_board[y_coor+k][x_coor]!=' ':
                if self.text_board[y_coor+k][x_coor]['name']=='K':
                    return True
            if self.text_board[y_coor-k][x_coor]!=' ':
                if self.text_board[y_coor-k][x_coor]['name']=='K':
                    return True
            if self.text_board[y_coor][x_coor+k]!=' ':
                if self.text_board[y_coor][x_coor+k]['name']=='K':
                    return True
            if self.text_board[y_coor][x_coor-k]!=' ':
                if self.text_board[y_coor][x_coor-k]['name']=='K': 
                    return True
            if self.text_board[y_coor+k][x_coor+k]!=' ':
                if self.text_board[y_coor+k][x_coor+k]['name']=='K':
                    return True
            if self.text_board[y_coor+k][x_coor-k]!=' ':
                if self.text_board[y_coor+k][x_coor-k]['name']=='K': 
                    return True
            if self.text_board[y_coor-k][x_coor+k]!=' ':       
                if self.text_board[y_coor-k][x_coor+k]['name']=='K':
                    return True
            if self.text_board[y_coor-k][x_coor-k]['name']!=' ':
                if self.text_board[y_coor-k][x_coor-k]['name']=='K':
                    return True
        # safe:
        return False
    # check checkmated
    def checkmated(self,blocs=playerBloc):
        self.findKing(blocs)
        if self.traceback(self.findKing(blocs)) and self.traceback(self.kx+1,self.ky,blocs) and self.traceback(self.kx+1,self.ky+1,blocs) and self.traceback(self.kx+1,self.ky-1,blocs) and self.traceback(self.kx-1,self.ky,blocs) and self.traceback(self.kx-1,self.ky+1,blocs) and self.traceback(self.kx-1,self.ky-1,blocs) and self.traceback(self.kx,self.ky+1,blocs) and self.traceback(self.kx,self.ky-1,blocs):
            return True
        return False
    # check 'checked'
    def checks(self,blocs=playerBloc):
        if blocs==0:
            if self.move[-1]=='+' and not self.traceback(self.findKing(1)):
                print('illegal move')
                return False
            elif self.move[-1]=='+' and self.traceback(self.findKing(1)):
                self.findKing(1)
                self.text_board[self.ky][self.kx]['checked']=True
                return True
            elif self.traceback(self.findKing(1)):
                print('illegal move')
                return False
            elif self.move[-1]=='#' and self.checkmated(1):
                print('0-1')
                sleep(1)
                system('cls')
                if blocs==playerBloc:
                    print('You win the game')
                else:
                    print('you lose the game')
                _exit(0)
            elif self.checkmated(1) and not self.move[-1]=='#':
                print("illegal move")
                return False
            elif self.move[-1]=='#':
                print("illegal move")
                return False
        if blocs==1:
            if self.move[-1]=='+' and not self.traceback(self.findKing(0)):
                print('illegal move')
            elif self.traceback(self.findKing(0)):
                self.findKing(0)
                self.text_board[self.ky][self.kx]['checked']=True
            elif self.move[-1]=='#' and self.checkmated(0):
                print('1-0')
                sleep(2)
                system('cls')
                if blocs==playerBloc:
                    print('You win the game')
                else:
                    print('you lose the game')
                _exit(0)
            elif self.move[-1]=='#':
                print("illega; move")
                return False
        return False
    # Stalemated
    def stalemated(self):
        self.pos_moves(term)
        if self.pos_move==[]:
            print('stalemate') 
            print('1/2 - 1/2')
            _exit(0)   
        return 0
    # validation
    def validate(self,pieces,x_coor,y_coor, blocs):
        # a pawn move 2 square
        if pieces in self.pawnList:
            # find pieces
            for i in self.text_board:
                for j in i:
                    vertical=self.text_board.index(i)
                    horizontal=i.index(j)
                    # path validation
                    if j!=' ':
                        if not 'x' in self.move and not '=' in self.move and j['name']==pieces and j['bloc']==blocs and not j['moved'] and (8-y_coor==vertical+2 or 8-y_coor==vertical-2) and self.pawnList.index(x_coor)==horizontal and y_coor<8 and y_coor>0:
                            # path checking
                            if playerBloc==0:
                                for k in range(1,3):
                                    if self.text_board[vertical+k][self.pawnList.index(x_coor)]!=' ':
                                        return False
                            if playerBloc==1:
                                for k in range(-1,-3,-1):
                                    if self.text_board[vertical+k][self.pawnList.index(x_coor)]!=' ':
                                        return False
                            j['double']=True
                            j['moved']=True
                            return True
                        # a pawn move only one square
                        if not 'x' in self.move and not '=' in self.move and j['bloc']==blocs and j['name']==pieces and (8-y_coor==vertical+1 or 8-y_coor==vertical-1) and self.pawnList.index(x_coor)==horizontal and x_coor in self.pawnList and y_coor<8 and y_coor>0:
                            # path checking
                            if y_coor>7 or y_coor<2:
                                return False
                            if self.text_board[-y_coor][horizontal]!=' ':
                                return False
                            j['moved']=True
                            return True
                        # pawn take
                        if not x_coor in self.pawnList:
                            return False
                        if 'x' in self.move and not '=' in self.move and j['name']==pieces  and j['bloc']==blocs and (8-y_coor==vertical+1 or 8-y_coor==vertical-1) and (self.pawnList.index(x_coor)==horizontal+1 or self.pawnList.index(x_coor)==horizontal-1) and x_coor in self.pawnList and y_coor<8 and y_coor>0:
                            # path checking
                            if y_coor>7 or y_coor<2:
                                return False
                            if blocs==0:
                                if 8-y_coor==vertical+1 and self.pawnList.index(x_coor)==horizontal+1:
                                    if self.text_board[vertical+1][horizontal+1]!=' ':
                                        if self.text_board[vertical+1][horizontal+1]['bloc']==1:
                                            j['moved']=True
                                            j['name']=x_coor
                                            return True
                                # En Pass
                                elif vertical==4 and 8-y_coor==vertical+1 and self.text_board[vertical][horizontal+1]!=' ':
                                    if self.text_board[vertical][horizontal+1]['name'] in self.pawnList:
                                        if self.text_board[vertical][horizontal+1]['double']:
                                            j['name']=x_coor
                                            return True
                                if 8-y_coor==vertical+1 and self.pawnList.index(x_coor)==horizontal-1:
                                    if self.text_board[vertical+1][horizontal-1]!=' ':
                                        if self.text_board[vertical+1][horizontal-1]['bloc']==1:
                                            j['moved']=True
                                            j['name']=x_coor
                                            return True
                                # En Pass
                                elif vertical==4 and 8-y_coor==vertical+1 and self.text_board[vertical][horizontal-1]!=' ':
                                    if self.text_board[vertical][horizontal-1]['name'] in self.pawnList:
                                        if self.text_board[vertical][horizontal-1]['double']:
                                            j['name']=x_coor
                                            return True
                            if blocs==1:
                                if 8-y_coor==vertical-1 and self.pawnList.index(x_coor)==horizontal+1:
                                    if self.text_board[vertical-1][horizontal+1]!=' ':
                                        if self.text_board[vertical-1][horizontal+1]['bloc']==0:
                                            j['moved']=True
                                            j['name']=x_coor
                                            return True
                                # En Pass
                                elif vertical==3 and 8-y_coor==vertical-1 and self.text_board[vertical][horizontal+1]!=' ':
                                    if self.text_board[vertical][horizontal+1]['name'] in self.pawnList:
                                        if self.text_board[vertical][horizontal+1]['double']:
                                            j['name']=x_coor
                                            return True
                                if 8-y_coor==vertical-1 and self.pawnList.index(x_coor)==horizontal-1:
                                    if self.text_board[vertical-1][horizontal-1]!=' ':
                                        if self.text_board[vertical-1][horizontal-1]['bloc']==0:
                                            j['moved']=True
                                            j['name']=x_coor
                                            return True
                                # En Pass
                                elif vertical==3 and 8-y_coor==vertical-1 and self.text_board[vertical][horizontal-1]!=' ':
                                    if self.text_board[vertical][horizontal-1]['name'] in self.pawnList:
                                        if self.text_board[vertical][horizontal-1]['double']:
                                            j['name']=x_coor
                                            return True
                        # promotion
                        # check changing
                        if not self.change in self.changeable:
                            return False
                        # normal
                        if not 'x' in self.move and '=' in self.move and j['bloc']==blocs and j['name']==pieces and (8-y_coor==vertical+1 or 8-y_coor==vertical-1) and self.pawnList.index(x_coor)==horizontal and y_coor<8 and y_coor>0:
                            # path checking
                            if y_coor>7 or y_coor<2:
                                return False
                            if self.text_board[-y_coor][horizontal]!=' ':
                                return False
                            if '=' in self.move and j['name']==pieces and (horizontal==7 or horizontal==0):
                                if 'R' in self.change:
                                    if self.change!='R'+x_coor:
                                        return False
                                self.text_board[vertical][horizontal]['name']=self.change
                                return True
                        # take then promote
                        if not x_coor in self.pawnList:
                            return False
                        if 'x' in self.move and '=' in self.move and j['bloc']==blocs and j['name']==pieces and (8-y_coor==vertical+1 or 8-y_coor==vertical-1) and (self.pawnList.index(x_coor)==horizontal+1 or self.pawnList.index(x_coor)==horizontal-1) and x_coor in self.pawnList and y_coor<8 and y_coor>0:
                            # path checking
                            if y_coor>7 or y_coor<2:
                                return False
                            if blocs==0:
                                if 8-y_coor==vertical+1 and self.pawnList.index(x_coor)==horizontal+1:
                                    if self.text_board[vertical+1][horizontal+1]!=' ':
                                        if self.text_board[vertical+1][horizontal+1]['bloc']==1:
                                            if '=' in self.move and j['name']==pieces and horizontal==7:
                                                if self.change!='R'+x_coor:
                                                    return False
                                                self.text_board[vertical+1][horizontal+1]['name']=self.change
                                                return True
                                if 8-y_coor==vertical+1 and self.pawnList.index(x_coor)==horizontal-1:
                                    if self.text_board[vertical+1][horizontal-1]!=' ':
                                        if self.text_board[vertical+1][horizontal-1]['bloc']==1:
                                            if '=' in self.move and j['name']==pieces and horizontal==7:
                                                if self.change!='R'+x_coor:
                                                    return False
                                                self.text_board[vertical+1][horizontal-1]['name']=self.change
                                                return True
                            if blocs==1:
                                if 8-y_coor==vertical-1 and self.pawnList.index(x_coor)==horizontal+1:
                                    if self.text_board[vertical-1][horizontal+1]!=' ':
                                        if self.text_board[vertical-1][horizontal+1]['bloc']==0:
                                            if '=' in self.move and j['name']==pieces and horizontal==0:
                                                if self.change!='R'+x_coor:
                                                    return False
                                                self.text_board[vertical-1][horizontal+1]['name']=self.change
                                                return True
                                if 8-y_coor==vertical-1 and self.pawnList.index(x_coor)==horizontal-1:
                                    if self.text_board[vertical-1][horizontal-1]!=' ':
                                        if self.text_board[vertical-1][horizontal-1]['bloc']==0:
                                            if '=' in self.move and j['name']==pieces and horizontal==0:
                                                if self.change!='R'+x_coor:
                                                    return False
                                                self.text_board[vertical-1][horizontal-1]['name']=self.change
                                                return True
            return False
        # knight moves
        if pieces=='N':
              # find pieces
            for i in self.text_board:
                for j in i:
                    vertical=self.text_board.index(i)
                    horizontal=i.index(j)
                    # path validation
                    if j!=' ':
                        if not 'x' in self.move and j['bloc']==blocs and j['name']==pieces and y_coor>0 and y_coor<9 and x_coor in self.pawnList:
                            # coor vcalidation
                            if vertical-2>=0 and horizontal+1<8:
                                if 8-y_coor==vertical-2 and self.pawnList.index(x_coor)==horizontal+1:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ':
                                        return False
                            if vertical+2<8 and horizontal-1>=0:
                                if 8-y_coor==vertical+2 and self.pawnList.index(x_coor)==horizontal-1:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ':
                                        return False
                            if vertical+2<8 and horizontal+1<8:
                                if self.pawnList.index(x_coor)==horizontal+1 and 8-y_coor==vertical+2:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ':
                                        return False
                            if vertical-2>=0 and horizontal-1>=0:
                                if self.pawnList.index(x_coor)==horizontal-1 and 8-y_coor==vertical-2:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ':
                                        return False
                            if vertical+1<8 and horizontal-2>=0:
                                if self.pawnList.index(x_coor)==horizontal-2 and 8-y_coor==vertical+1:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ':
                                        return False
                            if vertical-1>=0 and horizontal+2<8:
                                if self.pawnList.index(x_coor)==horizontal+2 and 8-y_coor==vertical-1:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ':
                                        return False
                            if vertical+1<8 and horizontal+2<8:
                                if 8-y_coor==vertical+1 and self.pawnList.index(x_coor)==horizontal+2:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ':
                                        return False
                            if vertical-1>=0 and horizontal-2>=0:
                                if 8-y_coor==vertical-1 and self.pawnList.index(x_coor)==horizontal-2:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ':
                                        return False
                        # knight take
                        if 'x' in self.move and j['name']==pieces and j['bloc']==blocs and  x_coor in self.pawnList and y_coor>0 and y_coor<9:
                            if vertical-2>=0 and horizontal+1<8:
                                if 8-y_coor==vertical-2 and self.pawnList.index(x_coor)==horizontal+1:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ' and self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']!=blocs:
                                        return True
                            if vertical+2<8 and horizontal-1>=0:
                                if 8-y_coor==vertical+2 and self.pawnList.index(x_coor)==horizontal-1:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ' and self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']!=blocs:
                                        return True
                            if vertical+2<8 and horizontal+1<8:
                                if self.pawnList.index(x_coor)==horizontal+1 and 8-y_coor==vertical+2:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ' and self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']!=blocs:
                                        return True
                            if vertical-2>=0 and horizontal-1>=0:
                                if self.pawnList.index(x_coor)==horizontal-1 and 8-y_coor==vertical-2:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ' and self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']!=blocs:
                                        return True
                            if vertical+1<8 and horizontal-2>=0:
                                if self.pawnList.index(x_coor)==horizontal-2 and 8-y_coor==vertical+1:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ' and self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']!=blocs:
                                        return True
                            if vertical-1>=0 and horizontal+2<8:
                                if self.pawnList.index(x_coor)==horizontal+2 and 8-y_coor==vertical-1:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ' and self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']!=blocs:
                                        return True
                            if vertical+1<8 and horizontal+2<8:
                                if 8-y_coor==vertical+1 and self.pawnList.index(x_coor)==horizontal+2:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ' and self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']!=blocs:
                                        return True
                            if vertical-1>=0 and horizontal-2>=0:
                                if 8-y_coor==vertical-1 and self.pawnList.index(x_coor)==horizontal-2:
                                    if self.text_board[8-y_coor][self.pawnList.index(x_coor)]!=' ' and self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']!=blocs:
                                        return True
            return False
        # Bishop move
        if pieces=='B':
            # find pieces
            for i in self.text_board:
                for j in i:
                    vertical=self.text_board.index(i)
                    horizontal=i.index(j)
                    if j!=' ':
                        # path validation
                        if j['name']==pieces and j['bloc']==blocs and  (8-y_coor-vertical==self.pawnList.index(x_coor)-horizontal or 8-y_coor-vertical==horizontal-self.pawnList.index(x_coor)) and not 'x' in self.move and y_coor<9 and y_coor>0 and x_coor in self.pawnList:
                            # path checking
                            for k,h in range(horizontal+1,self.pawnList.index(x_coor)+1),range(vertical+1,8-y_coor+1):
                                if self.text_board[h][k]!=' ':
                                    return False
                            for k,h in range(horizontal-1,self.pawnList.index(x_coor)-1,-1),range(vertical+1,8-y_coor+1):
                                if self.text_board[h][k]!=' ':
                                    return False
                            for k,h in range(horizontal+1,self.pawnList.index(x_coor)+1),range(vertical-1,8-y_coor-1,-1):
                                if self.text_board[h][k]!=' ':
                                    return False
                            for k,h in range(horizontal-1,self.pawnList.index(x_coor)-1,-1),range(vertical-1,8-y_coor-1,-1):
                                if self.text_board[h][k]!=' ':
                                    return False
                            return True
                        # bishop take
                        if 'x' in self.move and x_coor in self.pawnList and y_coor<9 and y_coor>0:
                            if 8-y_coor-vertical==self.pawnList.index(x_coor)-horizontal:
                                for k,h in range(horizontal-1,self.pawnList.index(x_coor)-1,-1),range(vertical-1,8-y_coor,-1):
                                    if self.text_board[h][k]!=' ' and self.text_board[h][k]['bloc']!=blocs:
                                        return True
                                for k,h in range(horizontal+1,self.pawnList.index(x_coor)+1),range(vertical+1,9-y_coor):
                                    if self.text_board[h][k]!=' ' and self.text_board[h][k]['bloc']!=blocs:
                                        return True
                            if 8-y_coor-vertical==horizontal-self.pawnList.index(x_coor):
                                for k,h in range(horizontal-1,self.pawnList.index(x_coor)-1,-1),range(vertical+1,8-y_coor+1):
                                    if self.text_board[h][k]!=' ' and self.text_board[h][k]['bloc']!=blocs:
                                        return True
                                for k,h in range(horizontal+1,self.pawnList.index(x_coor)+1),range(vertical-1,8-y_coor-1,-1):
                                    if self.text_board[h][k]!=' ' and self.text_board[h][k]['bloc']!=blocs:
                                        return True
            return False
        # rook move
        if 'R' in self.move:
             # find pieces
            for i in self.text_board:
                for j in i:
                    vertical=self.text_board.index(i)
                    horizontal=i.index(j)
                    if j!=' ':
                        # horizontally
                        # path validation
                        if not 'x' in self.move and j['bloc']==blocs and j['name']==pieces and x_coor in self.pawnList and y_coor==vertical+1:
                            # path check
                            for k in range(horizontal+1,self.pawnList.index(x_coor)+1):
                                if self.text_board[vertical][k]!=' ':
                                    return False
                            for k in range(horizontal-1,self.pawnList.index(x_coor)-1,-1):
                                if self.text_board[vertical][k]!=' ':
                                    return False
                            j['name']='R'+ x_coor
                            return True
                        # vertically
                        # path validation
                        if x_coor in self.pawnList:
                            if not 'x' in self.move and j['bloc']==blocs and j['name']==pieces and self.pawnList.index(x_coor)==horizontal and y_coor<9 and y_coor>0:
                                # path check
                                for k in range(vertical+1,8-y_coor+1):
                                    if self.text_board[k][horizontal]!=' ':
                                        return False
                                for k in range(vertical-1,8-y_coor-1,-1):
                                    if self.text_board[k][horizontal]!=' ':
                                        return False
                                return True
                        # Rook take  
                        if 'x' in self.move and j['bloc']==blocs and x_coor in self.pawnList and y_coor<9 and y_coor>0 and (self.pawnList.index(x_coor)==horizontal or y_coor==vertical+1):
                            if 8-y_coor>vertical and self.pawnList.index(x_coor)==horizontal:
                                for k in range(vertical+1,8-y_coor): # |
                                    if self.text_board[k][horizontal]!=' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                return True
                            if 8-y_coor<vertical and self.pawnList.index(x_coor)==horizontal: # ^
                                for k in range(vertical-1,8-y_coor,-1):
                                    if self.text_board[k][horizontal]!=' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                return True
                            if self.pawnList.index(x_coor)>horizontal and 8-y_coor==vertical: # >
                                for k in range(horizontal+1,self.pawnList.index(x_coor)):
                                    if self.text_board[vertical][k]!=' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                self.text_board[vertical][horizontal]['name']='R'+x_coor
                                return True
                            if self.pawnList.index(x_coor)<horizontal and 8-y_coor==vertical: # <
                                for k in range(horizontal-1,self.pawnList.index(x_coor),-1):
                                    if self.text_board[vertical][k]!=' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                self.text_board[vertical][horizontal]['name']='R'+x_coor 
                                return True
                            return False
            return False
        # Queen move
        if pieces=='Q':
            # find pieces
            for i in self.text_board:
                for j in i:
                    vertical=self.text_board.index(i)
                    horizontal=i.index(j)
                    # moving
                    # path validation
                    if j!=' ':                                                            # vertically                               # horizontally         # inclinedly (/)                                                 # inclinedly (\)
                        if not 'x' in self.move and j['bloc']==blocs and j['name']==pieces and x_coor in self.pawnList and (self.pawnList.index(x_coor)==horizontal or y_coor==vertical+1 or 8-y_coor-vertical==self.pawnList.index(x_coor)-horizontal or 8-y_coor-vertical==horizontal-self.pawnList.index(x_coor)) and y_coor<9 and y_coor>0:
                            # path check
                            # inclinedly
                            for k,h in range(horizontal+1,self.pawnList.index(x_coor)+1),range(vertical+1,8-y_coor+1): # /
                                if self.text_board[h][k]!=' ':
                                    return False
                            for k,h in range(horizontal-1,self.pawnList.index(x_coor)-1,-1),range(vertical+1,8-y_coor+1): # \
                                if self.text_board[h][k]!=' ':
                                    return False
                            for k,h in range(horizontal+1,self.pawnList.index(x_coor)+1),range(vertical-1,8-y_coor-1,-1): # \
                                if self.text_board[h][k]!=' ':
                                    return False
                            for k,h in range(horizontal-1,self.pawnList.index(x_coor)-1,-1),range(vertical-1,8-y_coor-1,-1): # /
                                if self.text_board[h][k]!=' ':
                                    return False
                            # horizontally
                            for k in range(horizontal+1,self.pawnList.index(x_coor)+1): # >
                                if self.text_board[vertical][k]!=' ':
                                    return False
                            for k in range(horizontal-1,self.pawnList.index(x_coor)-1,-1): # <
                                if self.text_board[vertical][k]!=' ':
                                    return False
                            # vertically
                            for k in range(vertical+1,y_coor+1):
                                if self.text_board[k][horizontal]!=' ': # |
                                    return False
                            for k in range(vertical-1,8-y_coor-1,-1):
                                if self.text_board[k][horizontal]!=' ': # ^
                                    return False
                            return True
                    # Queen take 
                        if 'x' in self.move and j['name']==pieces and j['bloc']==blocs and x_coor in self.pawnList and (self.pawnList.index(x_coor)==horizontal or y_coor==vertical+1 or (y_coor-1-vertical)/(self.pawnList.index(x_coor)-horizontal)==1 or (y_coor-1-vertical)/(self.pawnList.index(x_coor)-horizontal)==-1) and y_coor<9 and y_coor>0:
                            # inclinedly
                            if self.pawnList.index(x_coor)>horizontal and 8-y_coor>vertical:
                                for k,h in range(horizontal+1,self.pawnList.index(x_coor)),range(vertical+1,8-y_coor): # /
                                    if self.text_board[h][k]==' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                return True
                            if self.pawnList.index(x_coor)<horizontal and 8-y_coor>vertical:
                                for k,h in range(horizontal-1,self.pawnList.index(x_coor),-1),range(vertical+1,8-y_coor): # \
                                    if self.text_board[h][k]==' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                return True
                            if self.pawnList.index(x_coor)>horizontal and 8-y_coor<vertical:
                                for k,h in range(horizontal+1,self.pawnList.index(x_coor)),range(vertical-1,8-y_coor,-1): # \
                                    if self.text_board[h][k]==' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                return True
                            if self.pawnList.index(x_coor)<horizontal and 8-y_coor<vertical:
                                for k,h in range(horizontal-1,self.pawnList.index(x_coor),-1),range(vertical-1,8-y_coor,-1): #/
                                    if self.text_board[h][k]==' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                return True
                            # horizontally
                            if self.pawnList.index(x_coor)>horizontal and 8-y_coor==vertical:
                                for k in range(horizontal+1,self.pawnList.index(x_coor)): # >
                                    if self.text_board[vertical][k]==' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                return True
                            if self.pawnList.index(x_coor)<horizontal and 8-y_coor==vertical:
                                for k in range(horizontal-1,self.pawnList.index(x_coor),-1): # <
                                    if self.text_board[vertical][k]==' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                return True
                            # vertically
                            if self.pawnList.index(x_coor)==horizontal and 8-y_coor>vertical:
                                for k in range(vertical+1,8-y_coor): # |
                                    if self.text_board[k][horizontal]==' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                return True
                            if self.pawnList.index(x_coor)==horizontal and 8-y_coor<vertical:
                                for k in range(vertical-1,8-y_coor,-1): # ^
                                    if self.text_board[k][horizontal]==' ' or self.text_board[8-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.text_board[8-y_coor][self.pawnList.index(x_coor)]==' ':
                                        return False
                                    return True
                            return False
        # King move
        if pieces=='K':
            for i in self.text_board:
                for j in i:
                    vertical=self.text_board.index(i)
                    horizontal=i.index(j)
                    # path validation
                    if not 'x' in self.move and j['bloc']==blocs and 8-y_coor-vertical>=-1 and 8-y_coor-vertical<=1 and self.pawnList.index(x_coor)-horizontal>=-1 and self.pawnList.index(x_coor)-horizontal<=1: 
                        # path check (stuck)
                        if self.text_board[-y_coor][self.pawnList.index(x_coor)]!=' ':
                            return False
                        # path check (treatening) 
                        if self.traceback(x_coor,y_coor,blocs):
                            return False
                        self.text_board[vertical][horizontal]['moved']=True
                        return True 
                    # path validation
                    if 'x' in self.move and j['name']==pieces and j['bloc']==blocs and 8-y_coor-vertical>=-1 and 8-y_coor-vertical<=1 and self.pawnList.index(x_coor)-horizontal>=-1 and self.pawnList.index(x_coor)-horizontal<=1:          
                        # path check (stuck)
                        if self.text_board[-y_coor][self.pawnList.index(x_coor)]==' ' or self.text_board[-y_coor][self.pawnList.index(x_coor)]['bloc']==blocs or self.traceback(x_coor,y_coor,blocs):
                            return False 
                        self.text_board[vertical][horizontal]['moved']=True
                        return True
        #O-O-O
        if self.move=='O-O-O':
            self.findKing(blocs)
            for k in range(1,4):
                if not self.traceback(self.kx-k,self.ky,blocs) and self.text_board[self.ky][self.kx-k]==' ' and self.text_board[self.ky][self.kx]['moved']==False and self.text_board[self.ky][0]['moved']==False:
                    self.text_board[self.ky][self.kx-3]['moved']=True
                    return True
                else: 
                    return False
        # O-O
        if self.move=='O-O':
            self.findKing(blocs)
            for k in range(1,3):
                if self.text_board[self.ky][self.kx]['moved']!=False or self.text_board[self.ky][7]==' ':
                    break
                if not self.traceback(self.kx+k,self.ky, blocs) and self.text_board[self.ky][self.kx-k]==' ' and self.text_board[self.ky][8]['moved']==False:
                    self.text_board[self.ky][self.kx+2]['moved']=True
                    return True
            return False
        return False
    # change the visual board
    def changeBoard(self):
        for i in self.text_board:
            for j in i:
                if j==' ':
                    if self.text_board.index(i)%2==i.index(j)%2:
                        self.board[self.text_board.index(i)][i.index(j)]='⬛'
                    else:
                        self.board[self.text_board.index(i)][i.index(j)]='⬜'
                elif j['name'] in self.pawnList:
                    self.board[self.text_board.index(i)][i.index(j)]='♟️'
                elif 'R' in j['name']:
                    self.board[self.text_board.index(i)][i.index(j)]='♜'
                elif j['name']=='N':
                    self.board[self.text_board.index(i)][i.index(j)]='♞'
                elif j['name']=='B':
                    self.board[self.text_board.index(i)][i.index(j)]='♝'
                elif j['name']=='Q':
                    self.board[self.text_board.index(i)][i.index(j)]='♛'
                elif j['name']=='K':
                    self.board[self.text_board.index(i)][i.index(j)]='♚'
                else:
                    system('cls')
                    print('error')
                    _exit(0)
    # show board
    def showboard(self):
        self.changeBoard()
        system('cls')
        for i in self.board:
            print(self.board.index(i)+1,end=' ')
            for j in i:
                print(j,end=' ')
            print('')
        print(' a b c d e f g h')

    #########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

    # timer 
    def num60(self,num):
        self.mins=num//60
        self.secs=num%60
    def timer(self):
        global stop,gameTime
        while gameTime!=0:
            stop=0
            self.num60(gameTime)
            print(f'\rtime left:  {self.mins}:{self.secs}',end='',flush=True)
            if stop:
                break
            sleep(1)
            gameTime-=1
        if gameTime==0:
            print(f'Time Left:   {gameTime}\nTime is up, you lose the game')
            _exit(0)
    # moving pieces
    def moving(self,piece,x_coor,y_coor,blocs=playerBloc):
        global stop,term
        if self.validate(piece,x_coor,y_coor, playerBloc) and not self.traceback(self.findKing(blocs)):
            for i in self.text_board:
                for j in i:
                    if j!=' ':
                        if j['name']==piece:
                            _,=j
                            i.replace(j,' ')
                            self.text_board[-y_coor][self.pawnList.index(x_coor)]=_
                            term=1-term
                            if not self.checks(blocs):
                                print('illegal move')
                                self.text_board=self.copiedBoard
                                term=1-term
                                self.movePieces()
                            stop=1
                            for i in self.text_board:
                                for j in i:
                                    if j!=' ':
                                        if j['name'] in self.pawnList:
                                            j['double']=False
                                if self.text_board.index(i)==6:
                                    break
        else:
            print('illegal move')
            self.movePieces()
        self.copiedBoard=self.text_board
        self.stalemated()
    # request
    def movePieces(self):
        global stop
        self.showboard()
        t=threading.Thread(target=self.timer)
        t.start()
        self.move=input('Move:')
        if len(self.move)>=3 and 'R' in self.move and self.move[1] in self.pawnList and not self.move[2] in self.pawnList:
            piece,x,y=self.move[0]+self.move[1],self.move[1],int(self.move[2]) 
            self.moving(piece,x,y)  
        elif len(self.move)>=4 and 'x' in self.move:
            piece,x,y=self.move[0],self.move[2],int(self.move[3])
            self.moving(piece,x,y)
        elif len(self.move)>=4 and 'R' in self.move and self.move[1] in self.pawnList and self.move[2] in self.pawnList:
            piece,x,y=self.move[0]+self.move[1],self.move[2],int(self.move[3])
            self.moving(piece,x,y) 
        elif len(self.move)>=5 and 'R' in self.move and 'x' in self.move and self.move[1] in self.pawnList and self.move[3] in self.pawnList:
            piece,x,y=self.move[0]+self.move[1],self.move[3],int(self.move[4])
            self.moving(piece,x,y)
        elif len(self.move)>=3:
            piece,x,y=self.move[0],self.move[1],int(self.move[2])
            self.moving(piece,x,y)
        elif '=' in self.move and not 'x' in self.move and not( 'R' in self.move or '+' in self.move or '#' in self.move):
            piece,x,y,self.change=self.move[0],self.move[0],int(self.move[1]),self.move[-1]
            self.moving(piece,x,y)
        elif '=' in self.move and 'x' in self.move and not( 'R' in self.move or '+' in self.move or '#' in self.move):
            piece,x,y,self.change=self.move[0],self.move[2],int(self.move[3]),self.move[-1]
            self.moving(piece,x,y)
        elif '=' in self.move and 'x' in self.move and 'R' in self.move and not ('+' in self.move or '#' in self.move):
            piece,x,y,self.change=self.move[0],self.move[2],int(self.move[3]),self.move[-2]+self.move[-1]
            self.moving(piece,x,y)
        elif '=' in self.move and not'x' in self.move and 'R' in self.move and not ('+' in self.move or '#' in self.move):
            piece,x,y,self.change=self.move[0],self.move[0],int(self.move[1]),self.move[-2]+self.move[-1]
            self.moving(piece,x,y)
        elif '=' in self.move and 'x' in self.move and not 'R' in self.move and ('+' in self.move or '#' in self.move):
            piece,x,y,self.change=self.move[0],self.move[2],int(self.move[3]),self.move[-2]
            self.moving(piece,x,y)
        elif '=' in self.move and not 'x' in self.move and not 'R' in self.move and ('+' in self.move or '#' in self.move):
            piece,x,y,self.change=self.move[0],self.move[0],int(self.move[2]),self.move[-2]
            self.moving(piece,x,y)
        elif '=' in self.move and 'x' in self.move and 'R' in self.move and ('+' in self.move or '#' in self.move):
            piece,x,y,self.change=self.move[0],self.move[2],int(self.move[3]),self.move[-3]+self.move[-2]
            self.moving(piece,x,y)
        elif '=' in self.move and not 'x' in self.move and 'R' in self.move and ('+' in self.move or '#' in self.move):
            piece,x,y,self.change=self.move[0],self.move[0],int(self.move[1]),self.move[-3]+self.move[-2]
            self.moving(piece,x,y)
        elif len(self.move)>=2:
            piece,x,y=self.move[0],self.move[0],int(self.move[1])
            self.moving(piece,x,y)
        else:
            print('illegal move')
            stop=1
            self.movePieces()

#########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
a=board
def main():
    if __name__=='__main__':
        while True:
            a.changeBoard()
            a.showboard()
            if term==playerBloc:
                a.movePieces()
                '''MISSING BOT MOVE'''
            else:
                '''MISSING BOT MOVE'''
                a.movePieces()