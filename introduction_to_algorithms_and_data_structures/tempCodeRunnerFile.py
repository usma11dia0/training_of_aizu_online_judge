while True:
    command_list = list(sys.stdin.readline().split())
    if command_list[0] == "insert":
        T.insert_heap(int(command_list[1]))
    elif command_list[0] == "extract":
        T.extract_max()
    elif command_list[0] == "end":
        break