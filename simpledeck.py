from deckparts import Game,Player

game = Game()
game.Setup(2, )
game.deck.Shuffle(10)

p1 = Player()
p1.name = "Adam"

p2 = Player()
p2.name = "Brad"

game.AddPlayer(p1)
game.AddPlayer(p2)

game.Deal()

for p in game.GetPlayers():
     print(str.format("Player {}'s hand:",p.name))
     for c in p.hand.GetCardsInHand():
          print(str.format("     {} of {}",c.name,c.suit.name))