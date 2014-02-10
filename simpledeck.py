from deckparts import Game,Player

game = Game()
game.Setup(2, 5)
game.deck.Shuffle(10)

p1 = Player()
p1.name = "Adam"

p2 = Player()
p2.name = "Brad"

game.AddPlayer(p1)
game.AddPlayer(p2)

for p in game.GetPlayers():
     print (str.format("Player: {}",p.name))


#for c in game.deck.cards:
     #print(str.format("{} of {}",c.name,c.suit.name))
