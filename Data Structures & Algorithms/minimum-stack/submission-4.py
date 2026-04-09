from dataclasses import dataclass

@dataclass
class Item:
    val: int
    min_val: int | None

class MinStack:

    def __init__(self):
        self.stack: list[Item] = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(Item(val=val, min_val=val))
            return
        current_min = self.stack[-1].min_val
        min_val = val if val < current_min else current_min
        self.stack.append(Item(val=val, min_val=min_val))
        
    def pop(self):
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val
        

    def getMin(self) -> int:
        return self.stack[-1].min_val
        
