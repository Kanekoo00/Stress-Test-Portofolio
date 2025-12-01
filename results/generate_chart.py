import pandas as pd
import matplotlib.pyplot as plt

# Load data
file = "reports/aggregate report-23000Samples.csv"
df = pd.read_csv(file)

print(df.head())
print(df.columns)

# Exclude TOTAL row if exists
df = df[df["Label"] != "TOTAL"]

row = df.iloc[0]

# Convert numeric columns safely
def clean_number(val):
    if isinstance(val, str):
        val = val.replace('%','').strip()
    return float(val)

avg = clean_number(row["Average"])
p90 = clean_number(row["90% Line"])
p95 = clean_number(row["95% Line"])
maxv = clean_number(row["Max"])
throughput = clean_number(row["Throughput"])
error = clean_number(row["Error %"])

# Plot response time
plt.figure()
plt.plot(["Average", "90%", "95%", "Max"], [avg, p90, p95, maxv], marker='o')
plt.title("Response Time Analysis")
plt.ylabel("Milliseconds")
plt.xlabel("Metric")
plt.savefig("results/response_time_chart2.png")
plt.close()

# Plot throughput & error
plt.figure()
plt.bar(["Throughput", "Error Rate"], [throughput, error])
plt.title("Throughput & Error Rate")
plt.ylabel("Value")
plt.savefig("results/throughput_error_chart2.png")
plt.close()

print("Charts successfully generated in /results folder ✅")
