/**
 * Car.java
 * date created: 2/12/2021
 * Author: Benjamin M'Sadoques
 *
 * provides a Car, the data items used for making the plot
 */

package carSamplePlot;

public class Car
{
	private String Car;
	private String Manufacturer;
	private double MPG;
	private double Weight;
	
	/**
	 * makes a car
	 * @param car name
	 * @param manufacturer series
	 * @param mPG 
	 * @param weight
	 */
	public Car(String car, String manufacturer, double mPG, double weight)
	{
		Car = car;
		Manufacturer = manufacturer;
		MPG = mPG;
		Weight = weight;
	}

	public String getCar()
	{ 
		return Car;
	}

	public String getManufacturer()
	{
		return Manufacturer;
	}

	public double getMPG()
	{
		return MPG;
	}

	public double getWeight()
	{
		return Weight;
	}
}
