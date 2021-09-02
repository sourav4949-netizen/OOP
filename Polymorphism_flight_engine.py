class Flight:
    def __init__(self,engine):
        self.engine=engine
    def startEngine(self):
        self.engine.start()

class BoeingEngine:
    def start(self):
        print("Starting Boeing Engine")


class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")
ae=AirbusEngine()
f1=Flight(ae)
f1.startEngine()

be=BoeingEngine()
f2=Flight(be)
f2.startEngine()