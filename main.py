from bs4 import BeautifulSoup as bs
import requests
import html5lib
import pandas as pd
url = "https://en.wikipedia.org/wiki/2023_Karnataka_Legislative_Assembly_election"
d1 = requests.get(url)
bs1 = bs(d1.text, 'html5lib')
const_tab = bs1.findAll('table', attrs={"class": "wikitable sortable"})
row_no = 0
const_result = {}
for tr in const_tab[0].findAll("tr"):
    row_no += 1
    dist_check = 0
    if row_no < 3:
        continue

    td = [x.text for x in tr.findAll("td")]
    if len(td) == 0:
        continue

    const_no, const_name = '', ''
    if len(td) == 12:
        const_no, const_name = td[1].strip(), td[2].strip()
    else:
        const_no, const_name = td[0].strip(), td[1].strip()
    const_result[const_no] = const_name

# print(const_result)

def get_top_count(data):
    count_dt = list(data.keys())
    count_dt.sort(reverse=True)
    return {x:data[x] for x in count_dt[:5]}

count_per_party = {}
sl_no = 1
with open("data-content.csv","w") as fl:
    fl.write("slno,const no,const name,fp,fpc,sp,spc,tp,tpc,frp,frpc,fvp,fvpc,total votes, winning party")
    for const_no,const_name in const_result.items():
        url = f"https://results.eci.gov.in/ResultAcGenMay2023/ConstituencywiseS10{const_no}.htm?ac={const_no}"
        if int(const_no) == 10:
            break

        dt = requests.get(url)
        bs_dt = bs(dt.text, "html5lib")

        data_table = bs_dt.findAll("table",attrs={"style":"margin: auto; width: 100%; font-family: Verdana; border: solid 1px black;font-weight:lighter"})
        if len(data_table) == 0:
            continue

        row_content = data_table[0].findAll("tr", attrs={"style":"font-size:12px;"})
        if len(row_content) == 0:
            continue

        count_per_party = {}
        for t in row_content:
            td = [x.text for x in t.findAll("td")]
            count = int(td[-2])
            party = td[2]
            if count not in count_per_party:
                count_per_party[count] = party
            else:
                count_per_party[count] += f"##{party}"
        #print (count_per_party)
        result_data = get_top_count(count_per_party)
        #print (result_data)
        rst_lst = f'{sl_no},{const_no},{const_name},'+','.join([f"{result_data[x]},{x}" for x in result_data]) + f",{sum(list(result_data.keys()))},{list(result_data.values())[0]}"
        # print (rst_lst)  _ to print ht eweb scap list
        fl.write("\n%s"%(rst_lst))
        sl_no += 1

        #if sl_no > 11:
        #    break



data_df = pd.read_csv("data-content.csv")
data_df

inp = ''
try:
    inp = int(input("Enter the const number: "))

    if inp > len(data_df):
        print("Please enter a valid const number")
    else:
        print("success")
except:
    print("Please enter a valid number")

d = data_df[data_df["const no"] == inp].reset_index(inplace=False).drop(['index'], axis=1)
d = [d[x][0] for x in d.columns][3:-2]

x = [d[i] for i in range(0, len(d), 2)]
y = [d[i] for i in range(1, len(d), 2)]
print(x)
print(y)
import matplotlib.pyplot as plt
plt.pie(y, labels=x)
plt.show()