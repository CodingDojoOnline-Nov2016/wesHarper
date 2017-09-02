using System;

namespace fundamentals1
{
    class Program
    {
        static void Main(string[] args)
        {
            for(int i = 1; i <= 255; i++) {
                Console.WriteLine(i);
            }

            for(int j = 1; j <= 100; j++) {
                if((j % 3 == 0 || j % 5 == 0) && !(j % 3 == 0 && j % 5 == 0)) {
                    Console.WriteLine(j);
                }
            }
        }
    }
}
