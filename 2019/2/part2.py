import computer

computer = computer.Computer(debug=True)

for noun in range(100):
    for verb in range(100):
        
        computer.load_memory('input.txt')
        computer.data[1] = noun
        computer.data[2] = verb

        print(f'{noun} {verb}')
        computer.run()

        if computer.data[0] == 19690720:
            print(computer.data[0])
            print(f"Answer: 100 * {noun} + {verb} == {100 * noun + verb}")
            exit()