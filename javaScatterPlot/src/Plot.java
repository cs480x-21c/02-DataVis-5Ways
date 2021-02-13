import javax.swing.*;
import java.awt.*;
import java.awt.geom.AffineTransform;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Point2D;
import java.io.*;
import java.util.ArrayList;

public class Plot extends JFrame{
    private static ArrayList content = new ArrayList<Car>();
    private int width = 900;
    private int height = 600;
    private int plotWidth = 700;
    private int plotHeight = 480;
    private int boundLeft = 50;
    private int boundRight = 150;
    private int boundTop = 10;
    private int boundBottom = 100;
    private int xStart =1500;
    private int xEnd =5110;
    private int yStart = 7;
    private int yEnd = 47;

    public Point2D fitPoint(Point2D pt){
        //System.out.println(pt + "   ");
        Double x = ((pt.getX()-xStart)/(xEnd-xStart))*plotWidth + boundLeft;
        Double y = height - ((pt.getY()-yStart)/(yEnd-yStart))*plotHeight - boundBottom -boundTop;
        return new Point2D.Double(x,y);
    }
    public Plot(){
        setSize(width,height);
        setVisible(true);
        setTitle("Plot by Elene");
        JPanel panel = new JPanel() {
            @Override
            public void paintComponent(Graphics g) {
                //g.translate(0, 0);
                super.paintComponent(g);
                Graphics2D g2 = (Graphics2D) g.create();
                //g2.drawRect(boundLeft,boundTop,plotWidth,plotHeight); // drawRect(x-position, y-position, width, height)
                g2.drawLine(boundLeft, boundTop, boundLeft, height-boundBottom);
                //Y-axis
                g2.drawLine(boundLeft, height-boundBottom, (width-boundRight), height-boundBottom);
                for (int i=0; i< content.size(); i++ ) {
                    Car car = (Car) content.get(i);
                    Point2D pt =  fitPoint(car.getPoint());
                    Ellipse2D dot = new Ellipse2D.Double(pt.getX(), pt.getY(), car.getSize(), car.getSize());
                    g2.setPaint(car.getColor());
                    g2.fill(dot);
                }

                g.drawString("Weight",(width-boundRight)/2, height-boundBottom+40);
                int[] xScale = new int[]{2000, 3000, 4000, 5000};
                for (int i = 0; i < 4; i++)
                {
                    g.drawString("|", boundLeft+80+200 *i, height-boundBottom+10);
                    g.drawString(String.valueOf(xScale[i]), boundLeft+70+200 *i, height-boundBottom+25);
                }

                int[] yScale = new int[]{40, 30, 20, 10};
                for (int i = 0; i < 4; i++)
                {
                    String tick = yScale[i] + "-";
                    g.drawString(tick, boundLeft-20, boundTop+50 + 130*i);
                }
                g2.setPaint(Color.black);
                g2.drawString("MPG",boundLeft-30, height/2 -30);
                AffineTransform old = g2.getTransform();
                g2.rotate(90);
                g2.drawString("MPG",width/2, height/2);
                g2.drawString("MPG",boundLeft-20, height/2);

                g2.setTransform(old);
            }
        };
        setContentPane(panel);
        getContentPane().setBackground(Color.WHITE);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public static void main(String[] args) throws FileNotFoundException {

        System.out.println("HelloWorld");
        String line = "";

        try(BufferedReader br = new BufferedReader(new FileReader(new File("../cars-sample.csv")))) {

            while ((line = br.readLine()) != null) {
                Car car = new Car(line.split(","));
                if(car.isInit())
                 content.add(car); // Manuf, MPG, Weight
            }
        } catch (FileNotFoundException e) {
            //Some error logging
        } catch (IOException e) {
            e.printStackTrace();
        }
        //content.remove(0); //headers
        System.out.println(content.size());

        Plot plot = new Plot();

    }
}
