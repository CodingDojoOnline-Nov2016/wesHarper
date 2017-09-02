using System;

namespace first_csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine("Yo!");
            int favoriteNum = 42;
            Console.WriteLine(favoriteNum + "hi");
            Console.WriteLine("The {0} cow, jumped over the {1}, {2} times!", "brown", "Moon", 7);

            Random rand = new Random();
            for(int i = 0; i < 10; i++) {
                Console.WriteLine(rand.Next(2,8));
            }
        }
    }
}
