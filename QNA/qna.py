class QNA_BOT():
    def __init__(self, ask) -> None:
        self.messages = []
        self.ask = ask
    def start_loop(self):
        while True:
            q = input("Q: ")
            a  = self.ask(self.messages, q)
            self.messages.append({"role": "assistant", "data": a})
            self.messages.append({"role": "user", "data": q})
            print("A: " + a)
        