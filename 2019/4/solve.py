import computer

computer = computer.Computer(debug=True)

computer.load_memory('input.txt')

# computer.data = list(map(int, f.read().split(',')))

# print("-----------")
# print(computer.data)

computer.run()
