using System;

namespace Kattis
{
    class Program
    {
        public class Position
        {
            public int X { get; set; }
            public int Y { get; set; }

            public Position(int x, int y)
            {
                X = x;
                Y = y;
            }

            public void MoveRight() { X++; }
            public void MoveUp() { Y++; }
            public void MoveLeft() { X--; }
            public void MoveDown() { Y--; }

            public string ToString()
            {
                return "(" + X + ", " + Y + ")";
            }
        }


        class Square
        {
            public Square(int side, int stepsLeft, int maxStepsInSquare)
            {
                this.Side = side;
                this.Steps = stepsLeft;
                this.MaxStepsInSquare = maxStepsInSquare;
            }

            public Square()
            {
                Side = 1;
                Steps = 1;
                MaxStepsInSquare = 0;
            }

            public int Side { get; set; }
            public int Steps { get; set; }
            public int MaxStepsInSquare { get; set; }


            public void Step(Position position)
            {
                //if (StepsLeft == 0) position.MoveRight();

                // we are along the last side 
                //if (Steps <= Side + 1) position.MoveRight(); //last side (bottom one)
                //else if (Steps <= 2 * Side) position.MoveDown(); // left side
                //else if (Steps < 3 * Side) position.MoveLeft(); // top side
                //else position.MoveUp(); // right side

                // move right if we are anywhere along the bottom side
                //if (Steps == 0) position.MoveRight();

                int BOTTOM_SIDE = MaxStepsInSquare - Side;
                int LEFT_SIDE = BOTTOM_SIDE - (Side - 1);
                int TOP_SIDE = LEFT_SIDE - (Side - 1);

                if (Steps >= BOTTOM_SIDE) position.MoveRight();
                else if (Steps >= LEFT_SIDE) position.MoveDown();
                else if (Steps >= TOP_SIDE) position.MoveLeft();
                else position.MoveUp(); // right side

                Steps++;

                if (Steps >= MaxStepsInSquare)
                {
                    Side += 2;
                    Steps = 0;
                    MaxStepsInSquare = Side * Side - (Side - 2) * (Side - 2);
                }

            }

        }

        static int BOARD_X = 101;
        static int BOARD_Y = 101;
        static int[,] Board = new int[BOARD_X, BOARD_Y];

        public static void SetBoard(Position position, int value)
        {
            Board[BOARD_X / 2 + position.X, BOARD_Y / 2 + position.Y] = value;
        }

        public static int GetBoard(Position position)
        {
            return Board[BOARD_X / 2 + position.X, BOARD_Y / 2 + position.Y];
        }

        static void Main(string[] args)
        {
            
            Square square = new Square();

            int counter = 1;

            Position position = new Position(0, 0);

            var finalValue = 277678;
            //finalValue = 24;

            SetBoard(new Position(0, 0), 1);

            while (true)
            {
                counter++;
                square.Step(position);

                SetBoard(position, GetSurroundingValues(position));

                if (GetBoard(position) > finalValue) break;
                //Console.Clear();
                //Console.WriteLine(counter);
                //Console.WriteLine(position.ToString());
                //Console.ReadKey();
            }
            Console.WriteLine(position.ToString());
            Console.WriteLine(Math.Abs(position.X) + Math.Abs(position.Y) - 1);

            Console.WriteLine("Star 2: " + GetBoard(position));

            //Console.WriteLine(GetBoard(new Position(0,0)));
            //Console.WriteLine(GetBoard(new Position(1,1)));
            //Console.WriteLine(GetBoard(new Position(-1,-1)));
            //Console.WriteLine(GetBoard(new Position(0,2)));
        }

        private static int GetSurroundingValues(Position position)
        {
            var total = 0;
            for(int x = -1; x <= 1; x++)
            {
                for (int y = -1; y <= 1; y++)
                {
                    if (x == 0 && y == 0) continue;
                    total += GetBoard(new Position(position.X + x, position.Y + y));
                    //Console.WriteLine(x + " " + y);
                }
            }
            //Console.WriteLine(total);
            //total += Board[position.X + 1, position.Y];
            return total;

        }
    }
}
