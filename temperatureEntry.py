import csv
from datetime import datetime
import os
from Dataset import Dataset
from graph import line_graph

def read_temperature_data(filepath):
    dates, highs, lows = [], [], []

    with open(filepath) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        date_idx = header_row.index("DATE")
        high_idx = header_row.index("TMAX")
        low_idx = header_row.index("TMIN")

        for row in reader:
            try:
                current_date = datetime.strptime(row[date_idx], "%Y-%m-%d")
                high = int(row[high_idx])
                low = int(row[low_idx])
            except (ValueError, IndexError):
                continue
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows

def plotar_temperaturas(dataset: Dataset, linewidth=3, show_low_temp=False):
    filepath = dataset.value
    dates, highs, lows = read_temperature_data(filepath)

    title = f"Temperaturas - {os.path.basename(filepath).replace('_', ' ').replace('.csv', '')}"

    line_graph(
        x_data=dates,
        y_data1=highs,
        y_data2=lows if show_low_temp else None,
        title=title,
        x_label="Dates",
        y_label="Temperatures",
        with_dates=True,
        linewidth=linewidth
    )

