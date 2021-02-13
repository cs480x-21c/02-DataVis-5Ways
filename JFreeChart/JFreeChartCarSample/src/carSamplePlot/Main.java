/**
 * Main.java
 * date created: 2/12/2021
 * Author: Benjamin M'Sadoques
 *
 * Provides main, the program starting point
 */

package carSamplePlot;

import java.util.List;

import javax.swing.WindowConstants;

public class Main
{
	/**
	 * program starting point
	 * @param args
	 */
	public static void main(String[] args)
	{
		// Gets the data from the csv into Car Beans
		CarBeanReader reader = new CarBeanReader("..//..//cars-sample.csv");
		// filters out NA and converts to a list of Cars (with Doubles)
		reader.filterNA();

		// finally a usable data set
		List<Car> dataSet = reader.getDataSet();
		
		// Creates the object used to make plots with the data
		PlotMaker plot = new PlotMaker(dataSet);
		
		// adds the series, one for each manufacturer
		// and makes the plot (adds the other details)
		plot.addSeries("bmw")
			.addSeries("ford")
			.addSeries("honda")
			.addSeries("mercedes")
			.addSeries("toyota")
			.make();
		
		// Makes the plot window using swing (plot is a JFrame)
		plot.setSize(616, 439);  
	    plot.setLocationRelativeTo(null);  
	    plot.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);  
	    plot.setVisible(true);  
	}
}
