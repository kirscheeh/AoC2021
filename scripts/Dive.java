import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class Dive{

    public static String[] readFile(){
        
        String[] directions = new String[1000];
        
        try {
            File f = new File("data/day_2.txt");
            Scanner reader = new Scanner(f);
            
            int counter = 0;
            while (reader.hasNextLine()){
                String elem = reader.nextLine();
                String[] helper = elem.split(" ");
                if (helper[0].equals("up"))
                {
                    helper[1] = "-"+helper[1];
                }
                directions[counter] = helper[0]+" "+helper[1];
                counter++;
                
            }
            reader.close();
        }
        catch (FileNotFoundException e){ 
            System.out.println("An error occured.");
            e.printStackTrace();
        }
        return directions;
    }
    
    public static int navigation(String[] data, boolean comp)
    {
        int x = 0;
        int y = 0;
        int aim=0;
        
        for (int i=0; i<data.length; i++)
        {
            String[] step = data[i].split(" ");
            if (step[0].equals("forward"))
                {
                    x+=Integer.parseInt(step[1]);
                    if (comp == true)
                        {
                            y+=aim*Integer.parseInt(step[1]);
                        }
                }
            else
            {
                int val = Integer.parseInt(step[1]);
                if (comp == true)
                {
                    aim += val;
                }
                else
                {
                    y += val;
                }
            }
        }
        return x*y;
    }


    public static void main(String[] args) {
        String[] data = readFile();
        int pos1 = navigation(data, false);
        System.out.println("Part 1: "+pos1);
        int pos2 = navigation(data, true);
        System.out.println("Part 2: "+ pos2);
    }
}