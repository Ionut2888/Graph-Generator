# Graph Generator

Generate graphs from CSV files using a simple YAML config.

## 📦 Features

- Generate multiple graphs from one CSV file.
- Supported chart types:
  - `line`: Simple line chart
  - `plot`: Line chart with markers
  - `scatter`: Scatter plot
  - `bar`: Bar chart
- Custom titles, labels, and output file names.
- Easy configuration via `config.yaml`.

## 📁 File Structure

```
graphGenerator/
├── data/
│   └── example.csv     # Your input CSV data
├── output/             # Where graphs are saved
│   └── *.png           # You can change the output format
├── main.py            # Main script to generate graphs
├── config.yaml        # Configuration file for graphs
├── requirements.txt   # Python dependencies
└── README.md
```

## 🚀 Installation

1. Clone the repository:

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Usage

1. Edit your input data in `data/examples.csv` or prepare your own CSV file.

2. Modify `config.yaml` to define the graphs you want to generate. Example:
   ```yaml
   graphs:
     - title: "Line Chart"
       x_column: "Date"
       y_columns: ["Sales"]
       kind: "line"
       output_file: "output/line.png"

     - title: "Bar Chart"
       x_column: "Date"
       y_columns: ["Revenue"]
       kind: "bar"
       output_file: "output/bar.png"
   ```

3. Run the script using one of these methods:
   ```bash
   # Using default files in data/ directory
   python main.py

   # Using a custom input file
   python main.py --input your_data.csv
   # or short version:
   python main.py -i your_data.csv

   # Using custom input and config files
   python main.py -i your_data.csv -c your_config.yaml
   ```

4. View your graphs in the `output/` folder.

## Command Line Arguments

The script supports the following command line arguments:
- `--input` or `-i`: Path to your input CSV file (optional)
- `--config` or `-c`: Path to your config file (default: config.yaml)

## ✅ Example example.csv

```csv
Date,Sales,Profit,Revenue
2024-01,100,30,130
2024-02,150,50,200
2024-03,200,70,270
2024-04,170,65,235
2024-05,180,80,260
```

## 🛠 Supported Graph Types

| Type    | Description         |
|---------|-------------------|
| line    | Simple line plot  |
| plot    | Line with markers |
| scatter | Scatter plot      |
| bar     | Vertical bar chart|

## 🎨 Creating Custom Graphs

To create your own custom graph:

1. Prepare your CSV file with the required data columns and place it in the `data/` directory.

2. Add a new graph configuration in `config.yaml`. Example:
   ```yaml
   graphs:
     - title: "My Custom Graph"
       x_column: "MyXColumn"      # The column name for X-axis data
       y_columns: ["Series1", "Series2"]  # One or more columns for Y-axis data
       kind: "plot"              # Choose from: line, plot, scatter, bar
       output_file: "output/my_custom_graph.png"  # Can use .png or .eps format
   ```

3. Make sure your CSV contains all the columns referenced in the configuration.

4. Run the script to generate your custom graph.

### Main Script Implementation

The `main.py` script handles all the graph generation logic. Here's how it works:

1. Place your CSV file in the `data/` directory.
2. The script will:
   - Load your configuration from `config.yaml`
   - Read your CSV using pandas
   - Generate graphs based on your specifications
   - Save them in the output directory

Key features supported in `main.py`:
- Automatic handling of multiple data series
- Support for custom figure sizes via `figure_size` parameter
- Custom axis labels using `x_label` and `y_label`
- Automatic grid lines and legends
- Error handling for missing files and invalid data

Example config with additional options:
```yaml
graphs:
  - title: "My Custom Graph"
    x_column: "MyXColumn"
    y_columns: ["Series1", "Series2"]
    kind: "plot"
    output_file: "output/my_custom_graph.png"
    figure_size: [10, 6]  # Width: 10 inches, Height: 6 inches
    x_label: "Custom X Axis Label"
    y_label: "Custom Y Axis Label"
```

## 📌 Notes

- You can specify multiple y_columns for the same graph to compare multiple series.
- The script will automatically create the `output/` directory if it doesn't exist.
