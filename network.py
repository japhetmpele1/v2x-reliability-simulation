import random

class Network:
    def __init__(self, packet_loss=0.1, latency=0.05):
        self.packet_loss = packet_loss
        self.latency = latency

    def transmit(self, message):
        if random.random() < self.packet_loss:
            return None  # packet lost
        return message
