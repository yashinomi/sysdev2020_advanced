import java.util.Scanner;

public class Challange_three {
	
	public static int numberOfcycles = 0;
	
    public static void main(String[] args) {
		//hunk change
		//hunk change
		//hunk change
		//hunk change
		//hunk change
    	System.out.println("Enter your desired number: ");
    	Scanner scanner = new Scanner(System.in);
    	int number = scanner.nextInt();  
    	
    	long recursiveStart = System.nanoTime();
    	recursiveCollatz(number);      
        long recursiveEnd = System.nanoTime();
        
        //this separates the two run's results 
        numberOfcycles = 0;
        
    	long iterativeStart = System.nanoTime();
    	iterativeCollatz(number);      
        long iterativeEnd = System.nanoTime();
             
        System.out.println("Recursive run took " + 
        (recursiveEnd - recursiveStart)/1000 + " microseconds"); 
        System.out.println("Iterative run took " + 
        (iterativeEnd - iterativeStart)/1000 + " microseconds"); 

        scanner.close();
    }

    public static void recursiveCollatz(int n) {
		//don't change
		//don't change
		//don't change
		//don't change
    	//Prints 5 results each line
    	if(numberOfcycles%8 == 0) {
    		System.out.println();
    		System.out.print(n + " ");
    	} else System.out.print(n + " ");
    	
    	numberOfcycles++;
    	
        if (n == 1) return;
        else if (n % 2 == 0) recursiveCollatz(n / 2);
        else recursiveCollatz(3*n + 1);
    }
	
    public static void iterativeCollatz(int n) {
		//conflict change main side 
		//conflict change branch side 
    	StringBuilder result = new StringBuilder();
        while (n != 1) {        
        	//Prints 5 results each line
            if(numberOfcycles%8 == 0) {               
                result.append("\n");
        	}
            result.append(n + " ");
            numberOfcycles++;
            
            if (n % 2 == 0) {
                n /= 2;
            }  else {
                n = (n * 3) + 1;
            }
        }
        result.append(1);
        System.out.println(result);
    }
	
	
}
