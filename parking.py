class Garage():
  def __init__(self):
  #these are the attributes:
    self.currentTicket = {} #dictionary where we will determine if user has paid 
    self.tickets = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #List of tickets
    self.availableTickets = self.parkingSpaces = len(self.tickets) #spaces still available
    self.takenTicket = 0


  def takeTicket(self):
    takenTicket = self.tickets.pop(0)
    self.availableTickets = self.parkingSpaces = len(self.tickets)
    self.currentTicket[self.takenTicket] = "unpaid"
    print ("You took ticket number: "+ str(takenTicket))
 
  def payForParking(self):
    payment = input ("Please enter your payment:\n")
    while (int(payment) < 5 ):
      payment = input ("The minimum payment is $5.00 for greater amounts we will take them as tip!\n Please enter your payment:\n")
    if(int(payment) > 5):
      print("Thank you for your payment and tip. Have a great day!")
    elif(int(payment) == 5):
      print("Wow, not even a penny for tip...? Enjoy your day...")
    self.currentTicket[self.takenTicket] = "paid"

  def leaveGarage(self):
    if(self.currentTicket[self.takenTicket] == "paid"):
      print("Thank You, have a nice day")
    while(self.currentTicket[self.takenTicket] == "unpaid"):
      self.payForParking();
    self.tickets.insert(self.tickets[len(self.tickets)-1], self.tickets[len(self.tickets)-1] + 1)
    self.availableTickets = self.parkingSpaces = len(self.tickets)

      
# - - - - - - - - - - - - - - - Main- - - - - - - - - - - - - - - - 
class Main():
    def showInstructions():
        print("""
________________________________________________        
|Welcome to Raul's Parking Garage               |
|Please select one of the following options:    |
|_______________________________________________|
|   [1] Take parking ticket                     |
|   [2] Pay for parking                         |
|   [3] Leave Garage                            |
|   [4] Close program                           |
|_______________________________________________|
        """)
    def run():
        Main.showInstructions()
        self = Garage()
        while True:
            choice = input("What service would you like? ")
            if choice.lower() == "1":
                self.takeTicket()
            elif choice.lower() == "2":
                self.payForParking()    
            elif choice.lower() == "3":
                self.leaveGarage()
            elif choice.lower() == "4":
                print("Goodbye!")
                exit()
            else:
                print("That is not one of the choices, read carefully!")
Main.run()

