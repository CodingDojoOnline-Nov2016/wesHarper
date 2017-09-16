using System;

namespace oop
{
    class Program
    {
        static void Main(string[] args)
        {
            LandVehicle LV = new LandVehicle(4, "Land");
            Console.WriteLine(LV.ToString());
            Console.WriteLine(LV.Wheels);
            LV.PrintHello();
        }
    }

    public class LandVehicle
    {
        public int Wheels;
        public string Medium;
        public LandVehicle(int wheels, string medium)
        {
            Wheels = wheels;
            Medium = medium;
        }

        public string ToString()
        {
            return this.Wheels.ToString();
        }

        public void PrintHello()
        {
            Console.WriteLine("Hello");
        }
    }

}
