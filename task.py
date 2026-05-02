import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

df = pd.read_csv("sales_cleaned.csv")
df.columns = df.columns.str.strip()
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

df = df.dropna(subset=["Date", "Product", "Sales"]).copy()
df.set_index("Date", inplace=True)

weekly_sales = df["Sales"].resample("W").sum()
fig, ax = plt.subplots(figsize=(10, 5))
weekly_sales.plot(ax=ax)
ax.set_title("Weekly Sales Trend")
ax.set_ylabel("Sales")
fig.tight_layout()
fig.savefig("weekly_trend.png")
plt.close(fig)

pivot = df.pivot_table(values="Sales", index="Product", aggfunc=["sum", "mean"])
print("Product sales pivot table:\n", pivot)

numeric_df = df.select_dtypes(include=["number"])
corr = numeric_df.corr()
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap="vlag", ax=ax)
ax.set_title("Correlation Heatmap")
fig.tight_layout()
fig.savefig("heatmap.png")
plt.close(fig)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.barplot(ax=axes[0], x="Product", y="Sales", data=df.reset_index(), estimator=sum, ci=None)
axes[0].set_title("Revenue by Product")
axes[0].tick_params(axis="x", rotation=45)

daily_sales = df["Sales"].resample("D").sum().reset_index()
sns.lineplot(ax=axes[1], x="Date", y="Sales", data=daily_sales)
axes[1].set_title("Daily Sales")
axes[1].set_xlabel("Date")
fig.tight_layout()
fig.savefig("dashboard.png")
plt.close(fig)

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x="Product", y="Sales", data=df.reset_index(), ax=ax)
ax.set_title("Sales Distribution by Product")
ax.tick_params(axis="x", rotation=45)
fig.tight_layout()
fig.savefig("boxplot.png")
plt.close(fig)

if len(numeric_df.columns) > 1:
    sns.pairplot(df.reset_index()[numeric_df.columns])
    plt.savefig("pairplot.png")
    plt.close()
else:
    print("Not enough numeric columns to generate a pairplot.")

top_product = df.groupby("Product")["Sales"].sum().idxmax()
product_df = df[df["Product"] == top_product]
cumsum = product_df["Sales"].cumsum()

fig, ax = plt.subplots(figsize=(10, 5))
cumsum.plot(ax=ax)
ax.set_title(f"Cumulative Sales for Top Product: {top_product}")
ax.set_ylabel("Cumulative Sales")
fig.tight_layout()
fig.savefig("cumsum.png")
plt.close(fig)

summary = df.groupby("Product").agg(Total_Revenue=("Sales", "sum"), Transaction_Count=("Sales", "count"))
print("Product summary:\n", summary)

df["Projected_Revenue"] = df["Sales"] * 1.15

top = df.groupby("Product")["Sales"].sum().nlargest(5)
total = df["Sales"].sum()
top_share = (top.sum() / total) * 100 if total else 0
print(f"Top 5 products contribute {top_share:.2f}% of total sales")
