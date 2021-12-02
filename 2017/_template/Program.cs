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

            List<int> tokens = Console.ReadLine().Split().Select(int.Parse).ToList();
            int sum = 0;

            int n = int.Parse(Console.ReadLine());
            var results = new List<string>();

            for (int i = 0; i < n; i++)
            {

            }


            Console.WriteLine(String.Join("\n", results));

            Console.WriteLine(sum);
        }
    }
}
