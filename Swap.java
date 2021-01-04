import java.util.*;

public class Swap
{
	public static void main(String args[])
	{
		
		Scanner sc = new Scanner(System.in);
		int no1,no2,no3;
		System.out.println("Enter 2 Numbers ->");
		no1 = sc.nextInt();
		no2 = sc.nextInt();
		no1=no2;

		no2=no1;
       		System.out.println("no1->"+no1+"no2->"+no2);
	
	}
}
