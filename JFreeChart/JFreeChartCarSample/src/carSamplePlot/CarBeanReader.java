/**
 * CarBeanReader.java
 * date created: 2/12/2021
 * Author: Benjamin M'Sadoques
 *
 * Provides the capability to read the file into CarBeans
 * Filters the car beans into an easier to use Car data set
 */

package carSamplePlot;

import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.List;

import com.opencsv.bean.CsvToBeanBuilder;

public class CarBeanReader
{
	private List<CarBean> beans;
	private ArrayList<Car> dataSet;
	
	/**
	 * serial
	 */
	private static final long serialVersionUID = -1353373314658748249L;
	
	/**
	 * Reads the CSV into the internal list of Car Beans
	 * @param filePath csv file path
	 */
	public CarBeanReader(String filePath)
	{
		try 
		{
			// The CSV reader for JFreeChart is very minimal, needed a better library
			Reader fileReader = new FileReader(filePath);

			// Reads the data set into the Car Beans (they have the data we need)
			this.beans = new CsvToBeanBuilder<CarBean>(fileReader)
					.withType(CarBean.class)
					.withSkipLines(1)
					.build()
					.parse();
			
			// Used for filtering and re-interpreting
			dataSet = new ArrayList<Car>();
		} 
		catch (IOException e)
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	/**
	 * Filters the current Car bean list to a data set of cars
	 * any entry with "NA" is removed
	 */
	public void filterNA()
	{
		// Dataset needs to be filtered for NA, and needs to be integers
		for(CarBean bean: this.beans)
		{
			// filters out NA
			if (!bean.getMPG().equals("NA"))
			{
				// Adds a new car to the data set
				this.dataSet.add(new Car(bean.getCar(), 
						bean.getManufacturer(),
						Double.parseDouble(bean.getMPG()),
						Double.parseDouble(bean.getWeight())));
			}
		}
	}

	public List<Car> getDataSet()
	{
		return this.dataSet;
	}

	public static long getSerialversionuid()
	{
		return serialVersionUID;
	}
}
