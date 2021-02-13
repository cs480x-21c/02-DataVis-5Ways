import java.awt.*;
import java.awt.geom.Point2D;

public class Car {

    private String Manufacturer;
    private double MPG;
    private double Weight;
    private Point2D point;
    private boolean init;
    private Color color;
    private double size;

    public boolean isInit() {
        return init;
    }

    public Car (String [] arr ){
        double x;
        double y;
        try {
            x =  Double.parseDouble(arr[7]);
            y = Double.parseDouble(arr[3]);
            Manufacturer = arr[2];
            MPG = y;
            Weight =x;
            point = new Point2D.Double(x,y);
            init = true;
        } catch (NumberFormatException e) {
        return;
        }
    }

    public String getManufacturer() {
        return Manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        Manufacturer = manufacturer;
    }

    public Double getMPG() {
        return MPG;
    }

    public void setMPG(Double MPG) {
        this.MPG = MPG;
    }

    public Double getWeight() {
        return Weight;
    }

    public void setWeight(Double weight) {
        Weight = weight;
    }

    public Point2D getPoint() {
        return point;
    }

    public void setPoint(Point2D point) {
        this.point = point;
    }

    public Color getColor(){
        //System.out.println(Manufacturer.toLowerCase());
        switch (Manufacturer.toLowerCase()){
            case "\"ford\"":
                return new Color(163, 165, 0, 50);
            case "\"mercedes\"":
                return new Color(0, 176, 246, 50);
            case "\"honda\"":
                return  new Color(0, 191, 125, 50);
            case "\"toyota\"":
                return  new Color(231, 107, 243, 50);
            case "\"bmw\"":
                return new Color(248, 118, 109, 50);

        }
        return Color.magenta;
    }

    public double getSize(){

        if(Weight<= 2000) {
            size = 10;
        }
        else if(Weight<4000){
            size = 15;
        } else size =20;

        return size;
    }
}
