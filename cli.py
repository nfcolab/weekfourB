import random
import math

command_freqs = {
    "ls": 0.13,
    "cd": 0.12,
    "mkdir": 0.11,
    "chmod": 0.08,
    "rmdir": 0.04,
    "cp": 0.09,
    "mv": 0.07,
    "rm": 0.07,
    "history": 0.05,
    "more": 0.03,
    "man": 0.03,
    "lp": 0.01,
    "pwd": 0.02,
    "who": 0.01,
    "grep": 0.04,
    "cat": 0.06    
    }

def get_random_command(command_freqs):
    return random.choices(list(command_freqs.keys()), weights = command_freqs.values(), k = 1)[0]


class cli():
    def __init__(self):
        self.clear()

    def clear(self):
        self.touched = {}
        self.current_time = 0

    def activation(self, item):
        s = 0
        for i in self.touched[item]:
            if i < self.current_time:
                s += math.pow(self.current_time - i, -0.5)
        return math.log(s)

    def rt(self, item):        
        return 1.06*math.exp(-1.53*self.activation(item))
    

    def train(self, training_time, cmd):
        training_time += self.current_time
        while self.current_time < training_time:
            c = get_random_command(cmd)
            if c not in self.touched:
                self.touched[c] = []
                rt = 10
            else:
                rt = self.rt(c)
                if rt > 10:
                    rt = 10
            self.current_time += rt
            self.touched[c].append(self.current_time)
            self.current_time += 5

# rts = []
# for i in range(10):
#     print(i)
#     c = cli()
#     c.train(5000, command_freqs)
#     # command_freqs["new"] = 0.02
#     # c.train(7200, command_freqs)
#     rts.append(c.rt("who"))

c = cli()
c.train(60*60*12, command_freqs)
