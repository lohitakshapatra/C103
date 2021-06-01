import plotly.express as px
import pandas as pd

df=pd.read_csv("data.csv")
fig=px.scatter(df,x="Population",y="Per capita",title="population",size="Percentage",color="Country",size_max=25)
fig.show()