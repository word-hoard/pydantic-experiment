from pydantic.dataclasses import dataclass

@dataclass
class ConsoleDimensions:
    width: int
    height: int

@dataclass
class Test:

    console_size: ConsoleDimensions


test = Test((3,4)) # converts the tuple to ConsoleDimensions nicely
print(test) 
test.console_size = (4, 55) # leaves as tuple
print(test)