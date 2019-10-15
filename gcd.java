import java.io.*;
import java.util.*;
class gcd
{
	public static void main(String args[])
	{
		int a=15,b=20,hcf,lcm,sum=0;
		Scanner scan=new Scanner(System.in);
		System.out.println("enter the series number>>");
		while(b!=0)
		{		
			int temp=b;
			b=a%b;
			a=temp;
	    }
	    hcf=a;
	    System.out.println("gcd of two numbers>>>"+a);

	    System.out.println("lcm of two numbers>>>"+(10*b)/hcf);   
	 }
}