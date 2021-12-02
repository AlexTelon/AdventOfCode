using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Kattis
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229";
            //input = "3, 4, 1, 5";

            // Input is to be translated to a ascii.
            List<int> inputASCII = input.Select(x => ToASCII(x)).ToList();

            // Addition that we must add to all input
            inputASCII.AddRange(new List<int>() { 17, 31, 73, 47, 23 });

            //List<int> lenghts = input.Split(',').Select(int.Parse).ToList();

            var size = 256;

            // our 255 list with 0,1,2,3,4,5,6.. written to it
            var hashList = new List<int>() { };
            for (int i = 0; i < size; i++)
            {
                hashList.Add(i);
            }

            // skipsize and index is preserved between each run
            var skipsize = 0;
            var index = 0;

            for (int k = 0; k < 64; k++)
            {
                // here we do a round of knot hash

                foreach (var len in inputASCII)
                {
                    var subList = new List<int>();

                    // Are we trying to do stuff out of bounds? Then we need to wrap around
                    if (index + len > hashList.Count())
                    {
                        // first get all on this side
                        subList = hashList.GetRange(index, hashList.Count() - index);

                        // then add the missing ones from the start
                        subList.AddRange(hashList.GetRange(0, len - (hashList.Count() - index)));

                    }
                    else
                    {
                        subList = hashList.GetRange(index, len);
                    }

                    subList.Reverse();

                    for (int i = 0; i < subList.Count(); i++)
                    {
                        var hashI = (index + i) % hashList.Count();
                        hashList[hashI] = subList[i];
                    }

                    //Console.WriteLine(len);

                    //PrintList(hashList);

                    index += (len + skipsize);
                    index %= hashList.Count();
                    skipsize++;
                }
            }

            // we now have a sparse hash (0-255 in each)

            var denseHash = new List<int>();

            for (int i = 0; i < 255; i += 16)
            {
                var hash = 0x0;
                for (int j = 0; j < 16; j++)
                {
                    hash ^= hashList[i + j];
                }
                denseHash.Add(hash);
            }

            // now we need to get it to a hexadecimal format

            Console.WriteLine("-- derp --");
            Console.WriteLine(hashList[0] * hashList[1]); // 161 is too low, 3288 is too low, 29240 is right

        }

        private static int ToASCII(char c)
        {
            if (c == ',') return 44;

            int num = (int)c;

            //is a number
            if (num >= 48 && num <= 57)
            {
                return num;
            }
            throw new Exception("ToASCII not valid input");
        }

        //private static List<int> KnotHashRound(List<int> lengths)
        //{
        //    return hashList;
        //}

        private static void PrintList(List<int> list)
        {
            foreach (var item in list)
            {
                Console.Write(item + " ");
            }
            Console.WriteLine();
        }
    }
}
