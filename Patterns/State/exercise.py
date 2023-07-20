class CombinationLock:
    def __init__(self, combination):
        self.status = 'LOCKED'
        # todo
        self.cb = combination
        self.input_cb = []
        
    def reset(self):
        # todo - reset lock to LOCKED state
        self.status = 'LOCKED'
        self.input_cb = []

    def enter_digit(self, digit):
        # todo
        if len(self.input_cb) == 0:
            self.status = ''
        self.status += str(digit)
        self.input_cb.append(digit)
        if len(self.input_cb) == len(self.cb):
            if self.input_cb == self.cb:
                self.status = 'OPEN'
            else:
                self.status = 'ERROR'