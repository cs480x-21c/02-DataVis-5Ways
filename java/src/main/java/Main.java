import tech.tablesaw.api.IntColumn;
import tech.tablesaw.api.NumberColumn;
import tech.tablesaw.api.NumericColumn;
import tech.tablesaw.api.Table;
import tech.tablesaw.columns.Column;
import tech.tablesaw.plotly.Plot;
import tech.tablesaw.plotly.api.BubblePlot;
import tech.tablesaw.plotly.components.Marker;
import tech.tablesaw.selection.Selection;

public class Main {

    public static void main(String[] args) {

        Table table = null;
        try {
            table = Table.read().csv("cars-sample.csv");
        } catch(Exception e) {
            System.out.println("Could not find table");
            System.exit(1);
        }

        NumericColumn col = table.numberColumn("MPG");
        Selection sel = col.isNotMissing();
        table = table.where(sel);

        IntColumn sizes = IntColumn.create("sizes");
        IntColumn weights = table.intColumn("Weight");

        for(Integer weight : weights) {

            int newValue = (weight / 1000) * 10;
            sizes.append(newValue);

        }

        table.addColumns(sizes);

        Plot.show(
                BubblePlot.create("",
                        table,
                        "Weight",
                        "MPG",
                        "sizes",
                        "Manufacturer")
        );

        /*Plot.show(
                BubblePlot.create("",
                        table.column("Weight"),
                        table.column("MPG"),
                        table.intColumn("sizes"),
        new double[] {30, 30, 30},
        Marker.SizeMode.DIAMETER,
        0.5)
        );*/

    }

}
