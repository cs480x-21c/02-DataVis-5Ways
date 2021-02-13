/**
 * PlotMaker.java
 * date created: 2/12/2021
 * Author: Benjamin M'Sadoques
 *
 * Provides the plot maker, used to transform the car data into a bubble plot
 */

package carSamplePlot;

import java.awt.Color;
import java.util.List;

import javax.swing.JFrame;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.XYPlot;
import org.jfree.data.xy.DefaultXYZDataset;

public class PlotMaker extends JFrame
{
	/**
	 * serial
	 */
	private static final long serialVersionUID = -8761329308471591946L;
	private List<Car> carData;
	private DefaultXYZDataset dataSet;
	private final double CIRCLE_SCALE = 2300.0;

	/**
	 * Creates the plot maker for the car data set
	 * @param carData
	 */
	public PlotMaker(List<Car> carData)
	{
		this.carData = carData;
		this.dataSet = new DefaultXYZDataset();
	}
	
	/**
	 * Adds a series 
	 * @param seriesName one of the car manufactures
	 * @return
	 */
	public PlotMaker addSeries(String seriesName)
	{
		// The bubble charts require an array of doubles for the XYZ series
		double[] x = new double[carData.size()];
		double[] y = new double[carData.size()];
		double[] r = new double[carData.size()];
		int i = 0;
		
		for(Car car: carData)
		{
			if (car.getManufacturer().equals(seriesName))
			{
				x[i] = car.getWeight();
				y[i] = car.getMPG();
				// I am not sure what the circle size is, but scaling it down works well
				r[i] = car.getWeight()/CIRCLE_SCALE;          
			    i++;
			}
		}
		
		// Formats and adds the new series
		double data[][] = {x, y, r};
		dataSet.addSeries(seriesName, data);
		
		return this;
	}
	
	/**
	 * makes the plot
	 * this is where the magic happens
	 */
	public void make()
	{
	    // Creates the chart as a bubble chart  
	    JFreeChart chart = ChartFactory.createBubbleChart("", "Weight", "MPG", this.dataSet);  
	    
	   // Sets the colors for each manufacturer (sadly I could not set this earlier)
	   chart.getXYPlot().getRenderer().setSeriesPaint(0, Color.decode("0xF77973"));
	   chart.getXYPlot().getRenderer().setSeriesPaint(1, Color.decode("0xB0B24B"));
	   chart.getXYPlot().getRenderer().setSeriesPaint(2, Color.decode("0x31BC80"));
	   chart.getXYPlot().getRenderer().setSeriesPaint(3, Color.decode("0x2FB1F6"));
	   chart.getXYPlot().getRenderer().setSeriesPaint(4, Color.decode("0xE86DF1"));
	   	   
	   // Sets the bubble alpha to 0.5
	   chart.getXYPlot().setForegroundAlpha(0.5f);
	   
	   // Sets the axis ranges
	   chart.getXYPlot().getDomainAxis().setRange(1500, 5100);
	   chart.getXYPlot().getRangeAxis().setRange(8, 48);
	  
	   //Changes the background color  
	   XYPlot plot = (XYPlot)chart.getPlot();  
	   plot.setBackgroundPaint(Color.decode("0xEBEBEB"));  
	   
	   // Create Panel  
	   ChartPanel panel = new ChartPanel(chart);  
	   setContentPane(panel);  
	}
}
