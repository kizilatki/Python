class Flying():
    company = "British Airways"

    def __init__(self, code, start, arrival, time, capacity, passenger):
        self.code = code
        self.start = start
        self.arrival = arrival
        self.time = time
        self.capacity = capacity
        self.passenger = passenger

    def announce(self):
        return "{} code {}-{} flight will take {} times".format(
            self.code,
            self.start,
            self.arrival,
            self.time)

    def update_capacity(self):
        return self.capacity - self.passenger

    def ticket_sale(self, ticket_amount=1):
        if self.passenger + ticket_amount <= self.capacity:  # Bütün özellikleri if kümesine atadım.
            self.passenger += ticket_amount
            self.update_capacity()

            print("{} amount ticket is sold, rest of the amount: {}".format(
                ticket_amount,
                self.update_capacity()))

        else:
            print("Payment failed! Insufficient seats amount")

    def ticket_cancel(self, ticket_amount=1):
        if self.passenger >= ticket_amount:
            self.passenger -= ticket_amount
            self.update_capacity()

            print("{} amount ticket cancelled, current seats number: {}".format(
                ticket_amount,
                self.update_capacity()))

        else:
            print("Payment failed! Please enter a right ticket amount.")
