using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;



class Result
{

    /*
     * Complete the 'arrayChallenge' function below.
     *
     * The function is expected to return a LONG_INTEGER_ARRAY.
     * The function accepts LONG_INTEGER_ARRAY arr as parameter.
     */

    public static List<long> arrayChallenge(List<long> arr)
    {
        List<long> counterList = new List<long>();
        for(int i=0;i<arr.Count;i++){
            if(i==0)
                counterList.Add(0);
            else if(i==1)
            {
                long counter = arr[i] -arr[i-1];
                counterList.Add(counter);
            }            
            else{
                int k = i;
                long counter = 0;
                while(k>0){
                    --k;
                    if(arr[k]>arr[i]){
                        counter =counter - Math.Abs(arr[i] - arr[k]);
                        Console.WriteLine(counter);
                    }
                    else{
                        counter = counter +(arr[i] + arr[k]);
                    }
                
                }
                counterList.Add(counter);
            }
            
        }
        return counterList;
    }

}

class Solution{
     public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int arrCount = Convert.ToInt32(Console.ReadLine().Trim());

        List<long> arr = new List<long>();

        for (int i = 0; i < arrCount; i++)
        {
            long arrItem = Convert.ToInt64(Console.ReadLine().Trim());
            arr.Add(arrItem);
        }

        List<long> result = Result.arrayChallenge(arr);

        textWriter.WriteLine(String.Join("\n", result));

        textWriter.Flush();
        textWriter.Close();
    }
}