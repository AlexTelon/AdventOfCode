First I made [solve.py](solve.py) which is only a slightly cleaner version of what I originaly wrote.

Then I spent some time experimenting. version 1, 2 is more about what I order I wrote them than it being about later versions being "better".

The text is basically copy paster from my reddit [post for the day](https://www.reddit.com/r/adventofcode/comments/zgnice/2022_day_9_solutions/izi1gbw/).

**[v1.py](v1.py)**

A mix of trying to have a readable yet short solution. No complex numbers, just ordinary tuples.

The way I move is readable too me but I can see it being a bit obscure. Same with the walrus operator..

**[v2.py](v2.py) improved(?) move knot logic**

The new code is this:
```python
    def move_knot(Hx,Hy, Tx,Ty):
        # The basic idea is if they are not touching then move the tail towards head.
        touching = math.dist((Hx,Hy),(Tx,Ty)) < 2
        if not touching:
            # Move tail towards head.
            Ty += [-1, 1][Ty < Hy] if Ty != Hy else 0
            Tx += [-1, 1][Tx < Hx] if Tx != Hx else 0
        return (Tx, Ty)
```
I tried to make the logic above clearer and something felt of until I realised that I should flip the logic. Instead of checking that the distance in 3 different cases is larger than something I instead check if this one distance is less than something.

This is something I considered but no, only for codegolf.

```python
            Tx += [-1, 1, 0][(Tx < Hx) + 2*(Tx==Hy)]
```

**[v3.py](v3.py) Moving toward a goal**

Refactored a bit more and using the concept of touching in two places now. We set the new goal position of head right away and then let the tail move towards it.

```python
    Hx, Hy = Hx+(dx*d), Hy+(dy*d)
    while not touching(Hx, Hy, *tail[0]):
        prev = Hx, Hy
        tail = [prev := move_knot(*prev, *t) for t in tail]

        seen.add(tail[-1])
```

**[v4.py](v4.py) created Point class**

I wrote a solution with complex numbers but did not like the look of it. Here we are not using the Point class much however.  Next up, some nifty tricks with the mutable Point class!

**[v5.py](v5.py) Point class magic**
I got rid of the walrus operator and I am simply asking all the knots in the tail to move towards the previous one. And since we mutate the points themselves we don't have to use the walrus operator anymore.


**[v6.py](v6.py) snake**

head and tail merged to a snake of length 10.

**[v7.py](v7.py) snake + goal**

This is what I wanted to get to in v6. We now only keep track of an external goal and move the snake towards it.

Next, I will separate the parsing of goals and the moving of the snake to separate loops. To separate concerns.

**[v8.py](v8.py) seperated gathering goals and moving**

Now we gather the goals independently of moving the snake. Not that its important here or anything. But now we have some separation from the input format and solving of the task.

Mostly just an exercise for myself.