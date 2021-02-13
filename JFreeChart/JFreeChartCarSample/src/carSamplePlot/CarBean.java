/**
 * CarBean.java
 * date created: 2/12/2021
 * Author: Benjamin M'Sadoques
 *
 * Provides the car bean, used by open CSV to read the CSV directly into the file
 */

package carSamplePlot;

import com.opencsv.bean.CsvBindByPosition;

public class CarBean
{
	@CsvBindByPosition(position = 1)
	private String Car;
	
	@CsvBindByPosition(position = 2)
	private String Manufacturer;
	
	@CsvBindByPosition(position = 3)
	private String MPG;
	
	@CsvBindByPosition(position = 7)
	private String Weight;
	
	public String getCar()
	{
		return Car;
	}

	public String getManufacturer()
	{
		return Manufacturer;
	}

	public String getMPG()
	{
		return MPG;
	}

	public String getWeight()
	{
		return Weight;
	}
}
