from pydantic.dataclasses import dataclass

@dataclass
class ConsoleDimensions:
    width: int
    height: int

@dataclass
class Test:

    console_size: ConsoleDimensions


test = Test((3,4))
print(test)
test.console_size = (4, 55)
print(test)