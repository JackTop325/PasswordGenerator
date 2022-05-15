import java.util.ArrayList;
import java.util.Scanner;
import java.util.Random;

public class Generator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rand = new Random();

        String upperChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String lowerChars = "abcdefghijklmnopqrstuvwxyz";
        String digits = "1234567890";
        String symbols = "!@#$%^&*()-=+,./<>?";

        String possibleChars = upperChars + lowerChars + digits + symbols;

        System.out.println("Please enter how long you want the password to be: ");
        int length = Integer.parseInt(input.nextLine());

        String password = "";
        while(0!=length){
            password += possibleChars.charAt(rand.nextInt(possibleChars.length()));
            length--;
        }
        
        System.out.println("Generated Password is: "+password);
        input.close();
    }
}
