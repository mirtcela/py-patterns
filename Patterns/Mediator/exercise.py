class Mediator:
    def __init__(self):
        self.participants = []
        
    def broadcast(self, source, value):
        for p in self.participants:
            if p != source:
                p.value += value
                
    def join(self, person):
        self.participants.append(person)
        
class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        mediator.join(self)

    def say(self, value):
        # todo
        self.mediator.broadcast(self, value)