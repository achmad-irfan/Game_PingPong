import pandas as pd

# Import List Pemain
list_players= pd.read_csv("player.csv",delimiter=";")

class Players():
    def __init__(self, name, serve, return_serve ,power, backhand, forehand, slice, dropshot, voley,stamina,country):
        self.name=name
        self.serve=serve
        self.returnServe=return_serve
        self.power=power
        self.bh=backhand
        self.fh=forehand
        self.slice=slice
        self.dropshot=dropshot
        self.voley=voley
        self.stamina=stamina
        self.country=country
        
    def serve(self):
        self.stamina -= 2
        
players_objects = {}           
for row in list_players.itertuples(index=False):
    name = row.Player       
    data = row[1:]          
    p = Players(*data)       
    players_objects[name] = p  
    

