using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Kattis
{
    class Program
    {
        public enum Instruction
        {
            snd, set, add, mul, mod, rcv, jgz
        }

        class Command
        {
            public Instruction Instruction { get; set; }
            public char A { get; set; } // only one letter char
            public string B { get; set; } // string or value
        }



        static async Task Main(string[] args)
        {

            var testInput = @"set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2";

            var sendTest = @"snd a
snd p
rcv a
rcv b
rcv c
rcv d";

            var input = @"set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 680
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19";

            Dictionary<char, long> RegistersA = new Dictionary<char, long>();
            Dictionary<char, long> RegistersB = new Dictionary<char, long>();

            var BufferA = new ConcurrentQueue<long>();
            var BufferB = new ConcurrentQueue<long>();

            //Semaphore sem = new Semaphore(0, 1);
            //Mutex mutex = new Mutex();
            bool mutexA = true;
            bool mutexB = true;

            Object obj = new Object();

            Task.Run(() => Solver(sendTest, 0, RegistersA, BufferA, BufferB, ref mutexA, ref mutexB));
            await Task.Run(() => Solver(sendTest, 1, RegistersB, BufferB, BufferA, ref mutexB, ref mutexA));

            //Task[] tasks = new Task[2];

            //tasks[0] = Task.Run(() => Solver(input, 0, RegistersA, BufferA, BufferB, ref mutexA, ref mutexB));
            //tasks[1] = Task.Run(() => Solver(input, 1, RegistersB, BufferB, BufferA, ref mutexB, ref mutexA));

            //Task.WaitAll(tasks);
            // 253 is too low!


        }

        private static void Solver(string input, int id,
            Dictionary<char, long> registers,
            ConcurrentQueue<long> bufferIn,
            ConcurrentQueue<long> bufferOut,
            ref bool mutexThis,
            ref bool mutexOther)
        {
            long pc = 0; // program counter
            long currentFreq = 1337;
            bool done = false;

            long sendCount = 0;

            //var registers = new Dictionary<char, long>();
            registers.Add('p', id);

            List<string> rawInst = input.Split(new[] { Environment.NewLine }, StringSplitOptions.None).ToList();
            var instructions = rawInst.Select(ToInstruction).ToList();

            while (!done)
            {
                //Console.WriteLine();
                //Console.WriteLine("Pc: " + pc + "\nnext instruction: " + rawInst[(int)pc]);
                //Console.WriteLine(string.Join(" ", registers.Keys));
                //Console.WriteLine(string.Join(" ", registers.Values));
                //Console.WriteLine();
                //Console.ReadKey();



                var instruction = instructions[(int)pc];
                char x = instruction.A;
                string tmp = instruction.B;
                long y;
                if (!long.TryParse(tmp, out y))
                {
                    if (tmp.Count() == 1)
                    {

                        // if its not a numer then its an address
                        y = registers[tmp[0]];
                    }
                    else
                    {
                        //throw new Exception("Something wrong with Y");
                    }
                }

                // make sure register[x] exists
                if (!registers.ContainsKey(x))
                {
                    registers.Add(x, 0);
                }


                switch (instruction.Instruction)
                {
                    case Instruction.snd:
                        //snd X plays a sound with a frequency equal to the value of X.
                        //currentFreq = registers[x];
                        bufferOut.Enqueue(registers[x]);
                        sendCount++;
                        //Console.WriteLine("id: " + id + " sendcount: " + sendCount);
                        break;
                    case Instruction.set:
                        //set X Y sets register X to the value of Y.
                        registers[x] = y;
                        break;
                    case Instruction.add:
                        //add X Y increases register X by the value of Y.
                        registers[x] += y;
                        break;
                    case Instruction.mul:
                        //mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
                        registers[x] = registers[x] * y;
                        break;
                    case Instruction.mod:
                        //mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y(that is, it sets X to the result of X modulo Y).
                        registers[x] = registers[x] % y;
                        break;
                    case Instruction.rcv:
                        //rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
                        //if (registers[x] != 0)
                        //{
                        //    Console.WriteLine(currentFreq);
                        //    done = true;
                        //}
                        //Console.WriteLine("id " + id + " recving");

                        //lock (obj)
                        //{
                        long num;
                        //bufferIn.TryDequeue   
                        //Console.WriteLine("waiting.. ID: " + id + " SENDCOUNT: " + sendCount);
                        //while (!bufferIn.TryDequeue(out num))
                        //{
                        //    mutexThis = false;
                        //    // if the other thread is waiting and we have not sent anything then we are deadlocked
                        //    if (!mutexOther && bufferOut.LongCount() == 0 && bufferIn.LongCount() == 0)
                        //    {
                        //        // the other side is also waiting! 
                        //        // Deadlock found (probably)
                        //        Console.WriteLine("deadlock.. ID: " + id + " SENDCOUNT: " + sendCount);
                        //        return;
                        //    }
                        //}
                        while (bufferIn.TryDequeue(out num)) registers[x] += num;
                        //registers[x] = bufferIn.TryDequeue(out num);
                      
                        break;
                    //}

                    case Instruction.jgz:
                        //jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
                        if (registers[x] > 0) pc += (y - 1);
                        break;
                    default:
                        throw new Exception("unkown instruction");
                }
                pc++;
            }

            Console.WriteLine("id " + id + " done!");
        }

        private static Command ToInstruction(string arg)
        {
            var tokens = arg.Split(' ');

            //snd, set, add, mul, mod, rcv, jgz
            Instruction instruction;

            switch (tokens[0])
            {
                case "snd":
                    instruction = Instruction.snd;
                    break;
                case "set":
                    instruction = Instruction.set;
                    break;
                case "add":
                    instruction = Instruction.add;
                    break;
                case "mul":
                    instruction = Instruction.mul;
                    break;
                case "mod":
                    instruction = Instruction.mod;
                    break;
                case "rcv":
                    instruction = Instruction.rcv;
                    break;
                case "jgz":
                    instruction = Instruction.jgz;
                    break;
                default:
                    throw new Exception("unknown instruciton");
            }

            char a = tokens[1][0];
            string b = "";
            if (tokens.Count() > 2) b = tokens[2];

            var command = new Command() { Instruction = instruction, A = a, B = b };
            return command;
        }
    }
}
