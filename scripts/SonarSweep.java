import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class SonarSweep {

    public static int[] readFile(){
        int[] data = new int[2000];
        try {
            File f = new File("../data/day_1.txt");
            Scanner reader = new Scanner(f);
            
            int counter = 0;
            while (reader.hasNextLine()){
                String elem = reader.nextLine();
                data[counter] = Integer.parseInt(elem);
                counter ++;
            }
            reader.close();
        }
        catch (FileNotFoundException e){
            System.out.println("An error occured.");
            e.printStackTrace();
        }
        return data;
    }

    public static int DepthMeasure(int[] data, int SlidingWindow){ 
        int counter = 0;
        
        for (int i = 0; i < data.length-SlidingWindow; i++) 
        {   
            int val1 = 0;
            int val2 = 0;

            for (int j = 0; j < SlidingWindow; j++)
            {
                val1+=data[j+i];
                val2+=data[j+i+1];               
            }
            
            if (val1<val2) 
            {
                counter++;
            }
        }
        return counter;
    }

    public static void main(String[] args) {
        
        int[] data = readFile();
        
        int num1 = DepthMeasure(data, 1);
        System.out.println("Part 1: " +num1);
        
        int num2 = DepthMeasure(data, 3);
        System.out.println("Part 2: "+num2);
    }
}


