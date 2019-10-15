import java.io.*;
import java.util.*;
class Abundant_num
{
	public static void main(String args[])
	{
		int n,b,sum=0;
		Scanner scan=new Scanner(System.in);
		System.out.println("enter the series number>>");
		n=scan.nextInt();
		for(int i=1;i<=n/2;i++)
		{
			if(n%i==0)
				sum=sum+i;

	    }
	    if(sum>n)
	    System.out.println("it is a abundant number sum "+sum +">"+n);
	    else
	    System.out.println("it is a abundant number sum"+sum+"<"+n);
	    	
    }
}