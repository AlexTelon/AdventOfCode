lines = open(0).read().splitlines()
# lines = open("sample.txt").read().splitlines()
busses = lines[1].split(',')
busses = [(int(x),i) for i,x in enumerate(busses) if x != "x"]

# OK i got it now! I have solved a similar  problem in an earlier year I now realise!

# basically start with 2 busses and solve for them. The two of them together will have a common cycle for which they fulfil the requirement.
# This common cycle will be our new step size. (Tough we technically do begin with 1 bus and its own cycle as step.)
# ...
# Then add a new bus. Use the stepsize from before until you find a time for which this new bus is also valid.
# Now continue until you have found another time for which all 3 are valid. The difference between this and the previous is the new step.

# So note that for each number of busses n.We have to find a match _twice_ and compare the diff between them to get the cycle time for those n busses.

# then add up more and more busses til done. But for the last bus we dont want the cycle time so we exit early to get the first time all busses matched the requirement.

# This way we always increase the stepsize while also always consider cases where all previous busses are always valid.

offsets =  [b for a,b in busses]

step = busses[0][0]
time = 0
prev = time
for i, (bus, offset) in enumerate(busses[1:]):
    first = True

    while True:
        time += step
        # print(time, [(time + offset) / t for t, offset in busses])
        if (time + offset) % bus == 0:
            if first:
                first = False
                prev = time
                if i == len(busses) - 2:
                    print([(time + offset) / t for t, offset in busses])
                    print('part2 ans:', time)
                    exit()
                continue

            # new timestamp is a multiple of this bus number and all previous ones as well!
            step = time - prev
            break