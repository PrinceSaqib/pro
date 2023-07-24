import pandas as pd
t={
    'courses':["Python","java","DBMS","MM"],
    'Fee':[300,500,450,100],
    'Complexity':[100,52,10,36]
}
fd=pd.DataFrame(t)
print(fd)
print("\n",fd.pivot(columns='courses',values='Fee'))
