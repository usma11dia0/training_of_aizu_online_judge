class simple_dictionary:
    def __init__(self):
        self.data = set()

    def insert(self, s: str) -> None:
        self.data.add(s)

    def find(self, s: str) -> None:
        if s in self.data:
            return print("yes")
        else:
            return print("no")


n = int(input())
command_list = [list(map(str, input().split())) for _ in range(0, n)]

d = simple_dictionary()

for command, target in command_list:
    if command == "insert":
        d.insert(target)
    elif command == "find":
        d.find(target)
