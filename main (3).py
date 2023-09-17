#Define the base class player
class player:
  def play(self):
    print("The player is playing cricket.")

#Define the deriver class Batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")

#Define the deriver class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bolwing.")

#Crete objects of Batsamn and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()
