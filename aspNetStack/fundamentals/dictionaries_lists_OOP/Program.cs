using System;
using System.Collections.Generic;
namespace dictionaries_lists_OOP
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string,string> profile = new Dictionary<string, string>();
            profile.Add("Name", "Todd");
            profile.Add("Location", "Seattle");
            foreach (KeyValuePair<string,string> item in profile)
            {
                Console.WriteLine("Key: {0}, Value: {1}", item.Key, item.Value);
            }

            int[] myIntegers = new int[5];

            List<Dictionary<string, string>> people = new List<Dictionary<string,string>>();
            people.Add(profile);
            foreach (Dictionary<string,string> person in people)
            {
                foreach (KeyValuePair<string,string> value in person)
                {
                    Console.WriteLine("Key: {0}, Value: {1}", value.Key, value.Value);
                }
            }
        }
    }
}
