#!/bin/bash

time ./bin/debug/Kattis.exe < sample.in > sample.out
diff sample.out sample.ans --strip-trailing-cr -b
