import pandas as pd
import matplotlib.pyplot as plt


# Open the data file and read the IssuanceDate, CleanBid, CleanAsk, and LastPrice columns from Sheet1
xls = pd.ExcelFile(r'../datafiles/Book1.xlsx')
df = pd.read_excel(xls, sheet_name='Sheet1', usecols='F, H, I, J')

# Issuance Date Data file to only display Issuance Date in Data File
issuance_df = pd.read_excel(xls, sheet_name='Sheet1', usecols='F')


# Issuance Date Data Frame
date_agg = issuance_df[issuance_df['IssuanceDate'].str.contains('DIs', na=False)]
print(date_agg)


# parse through Issuance Date Data Frame to add the dates into the "dates" list.
# dates are of the form: "month/day/year"
dates = []
for index, rows in date_agg.iterrows():
    rows.IssuanceDate = rows.IssuanceDate[3:]

    year = rows.IssuanceDate[:4]
    month = rows.IssuanceDate[4:6]
    day = rows.IssuanceDate[6:]

    rows.IssuanceDate = month + '/' + day + '/' + year

    dates.append(rows.IssuanceDate)


print(" ")

# CleanBid Data Frame
bpr_agg = df[df['CleanBid'].str.contains('BPr', na=False)]
print(bpr_agg[['CleanBid']])
print(" ")


# Parse through CleanBid Data Frame to add CleanBid values into the "bpr" list.
bpr = []
for index, rows in bpr_agg.iterrows():
    rows.CleanBid = rows.CleanBid[3:]
    bpr.append(float(rows.CleanBid))

print(" ")

# CleanAsk data frame
api_agg = df[df['CleanAsk'].str.contains('APl', na=False)]
print(api_agg[['CleanAsk']])
print(" ")

# Parse through CleanAsk Data Frame to add CleanAsk values into the "api" list.
api = []
for index, rows in api_agg.iterrows():
    rows.CleanAsk = rows.CleanAsk[3:]
    api.append(float(rows.CleanAsk))
api.append(-10)
print(" ")

# LastPrice data frame
Pl_agg = df[df['LastPrice'].str.contains('Pl', na=False)]
print(api_agg[['LastPrice']])
print(" ")

# Parse through LastPrice Data Frame to add LastPrice values into the "pl" list.
pl = []
for index, rows in Pl_agg.iterrows():
    rows.LastPrice = rows.LastPrice[2:]
    pl.append(float(rows.LastPrice))
pl.append(-10)
print(" ")

# Consider the corner cases where there are more dates then CleanBid, CleanAsk, or LastPrice values.
# In this case, set the empty values to -10 so they are not displayed on the graph.
for i in range(len(dates)):
    if i > len(api):
        api[i] = -10
    if i > len(bpr):
        bpr[i] = -10
    if i > len(pl):
        pl[i] = -10

# plot the scatter

# Format the "dates" list to display a range of date in the x axis.
date = [pd.to_datetime(d) for d in dates]

fig, ax1 = plt.subplots()

ax1.scatter(date, bpr, label="CleanBid")


ax2 = ax1
ax2.scatter(date, api, label="CleanAsk")

ax3 = ax2
ax3.scatter(date, pl, label="Last Price", c='gray')
plt.gcf().autofmt_xdate()
plt.xlabel("Issuance Date")
plt.ylabel("CleanBid, CleanAsk, Last Price")
plt.title("CleanBid, CleanAsk and Last Price Against Issuance Date")
plt.ylim(0)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.18),
           fancybox=True, shadow=True, ncol=3)

plt.grid()
plt.show()
