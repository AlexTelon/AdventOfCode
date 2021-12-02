using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Kattis
{
    class Program
    {

        class Board
        {
            public List<int> Data { get; set; } = new List<int>();
            public int Step { get; set; }
            public int Pos { get; set; } = 0;
            private int counter = 0;

            public int Size = 1;

            public void Next()
            {
                Pos = (Pos + Step) % Size++;

                ++counter;

                // only add data to position 1
                if (Pos == 0)
                {
                    Data.Insert(Pos + 1, counter);
                }
                //Pos = (Pos + 1) % Data.Count();
                Pos++;
            }
        }

        static void Main(string[] args)
        {

            var input = 3;
            input = 369;
            Board board = new Board() { Step = input };
            board.Data.Add(0);

            while(true)
            {
                board.Next();
                if (board.Size == 50000001) break;
                //Console.WriteLine(string.Join(" ", board.Data));
            }
            Console.WriteLine("-----");



            //Console.WriteLine("----");
            //Console.WriteLine(string.Join(" ", board.Data));
            ////Console.WriteLine(board.Pos);
            ////Console.WriteLine(board.Data[board.Pos]);
            ////Console.WriteLine(board.Data[board.Pos+1]);
            Console.WriteLine("0: " + board.Data[0]);
            Console.WriteLine("1: " + board.Data[1]);
            //Console.WriteLine("2: " + board.Data[2]);
            //// 1222153 is too low

        }
    }
}
