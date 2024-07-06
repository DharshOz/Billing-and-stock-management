import java.util.*;
public class hello{
    private String var;
    public void print(){
        System.out.println("ENTER YOUR NAME: ");
        Scanner in = new Scanner(System.in);
        var = in.nextLine();
        System.out.println("HELLO "+var);
    }
    public static void main(String arg[]){
        hello a = new hello();
        a.print();
    }
}
