import streamlit as st
import requests, json
from bs4 import BeautifulSoup
import pandas as pd
import re
from PIL import Image
from io import BytesIO
# import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
#@st.cache(persist=True)



#st.image('par.png' ,width=400)
#st.markdown("<h1 style='text-align: center;'>INDIAN PARLIAMENT 🏛</h1>", unsafe_allow_html=True)



colm1, colm2 = st.columns([1, 4])

with colm1:

    st.image("Lio.jpg", width=40)
    st.write("Data from https://www.india.gov.in/")



with colm2:
    #st.write(" ")
    st.image('par.png', width=800)
    #T="      INDIAN PARLIAMENT 🏛"
    #T = '<p style="font-family:sans-serif; color:dark grey; font-size: 45px;">' + T + '</p>'
    #st.write(T,unsafe_allow_html=True)


#st.sidebar.markdown(f"<span style='color: black;font-size: 30px;font-weight: bold;'>Indian Parliament </span>", unsafe_allow_html=True)
#st.sidebar.write("Data BY india.gov.in ")

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
#     animation_symbol='❅'
# st.markdown(f"""<div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>
#                 <div class="snowflake">{animation_symbol}</div>""",unsafe_allow_html=True)
#
#





###############################################################################################################################################################

tab1, tab2, tab3,tab4,tab5,tab6,tab7= st.tabs(["President", "Vice President", "Prime Minister","Council of Ministers","Lok Sabha","Rajya Sabha","Chief Ministers"])

with tab1:
    limk = "https://www.india.gov.in/my-government/whos-who/president"
    htmldata = requests.get(limk).text
    soup = BeautifulSoup(htmldata, 'html.parser')
    president = soup.find_all("div", class_="field-content")
    #president[0]
    image = president[0].find_all('img')
    for item in image:
        link = item['src']
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
    st.image(img, width=300)
    for i in president[1]('p'):
        t=i.text
        t = '<p style="font-family:sans-serif; color: black; font-size: 15px;">' + t + '</p>'
        st.write(t,unsafe_allow_html=True)
        #print(i.text)
    for i in president[1]('a'):
        st.write(i['href'])
        #print(i['href'])



with tab2:
    limk = "https://www.india.gov.in/my-government/whos-who/vice-president"
    htmldata = requests.get(limk).text
    soup = BeautifulSoup(htmldata, 'html.parser')
    president = soup.find_all("div", class_="field-content")
    # president[0]
    image = president[0].find_all('img')
    for item in image:
        link = item['src']
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
    st.image(img, width=300)
    for i in president[1]('p'):
        st.write(i.text)
        # print(i.text)
    for i in president[1]('a'):
        st.write(i['href'])
        # print(i['href'])


with tab3:
    limk = "https://www.india.gov.in/my-government/whos-who/prime-minister"
    htmldata = requests.get(limk).text
    soup = BeautifulSoup(htmldata, 'html.parser')
    president = soup.find_all("div", class_="field-content")
    # president[0]
    image = president[0].find_all('img')
    for item in image:
        link = item['src']
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
    st.image(img, width=300)
    for i in president[1]('p'):
        st.write(i.text)
        # print(i.text)
    for i in president[1]('a'):
        st.write(i['href'])
        #print(i['href'])

with tab4:
    url = "https://www.india.gov.in/my-government/whos-who/council-ministers"
    htmldata = requests.get(url).text
    soup = BeautifulSoup(htmldata, 'html.parser')
    img = soup.find_all('table', class_="views-view-grid cols-2")

    data = img[1].find_all("tr")

    cabinet_ministers_images_links = []
    for i in range(len(data)):
        # print(i)
        # print(i.text)
        images = data[i].find_all('img')
        for j in images:
            cabinet_ministers_images_links.append(j['src'])

    cabinet_ministers_names = []
    for i in range(len(data)):
        names = data[i].find_all("span", class_="field-content")
        for j in names:
            cabinet_ministers_names.append(j.text.strip())

    ministry_list = []
    for i in range(len(data)):
        ministry = data[i].find_all('ul')
        for j in ministry:
            lst = []
            for k in j:
                lst.append(k.text)
                #print(k.text)
            ministry_list.append(lst)

    co1, co2 = st.columns(2)
    with co1:
        with st.expander("Cabinet Ministers"):
            #st.subheader("Cabinet Ministers")
            for i in range(len(cabinet_ministers_names)):

                st.image(cabinet_ministers_images_links[i])
                st.write("**"+cabinet_ministers_names[i]+"**")
                for j in ministry_list[i]:
                    j= '<p style="font-family:sans-serif; color:Green; font-size: 15px;">'+j+'</p>'
                    st.write(j, unsafe_allow_html=True)
                st.write("---------------------------------------------------------------------------")

            #st.write(ministry_list[i])
    data = img[3].find_all("tr")
    cabinet_ministers_images_links = []
    for i in range(len(data)):
        # print(i)
        # print(i.text)
        images = data[i].find_all('img')
        for j in images:
            cabinet_ministers_images_links.append(j['src'])
            # print(j['src'])
        # print("#####################")
    cabinet_ministers_names = []
    for i in range(len(data)):
        names = data[i].find_all("span", class_="field-content")
        for j in range(len(names)):
            if j % 2 == 0:
                cabinet_ministers_names.append(names[j].text.strip())
                # print(j)
    ministry_list = []
    for i in range(len(data)):
        ministry = data[i].find_all('ul')
        for j in ministry:
            lst = []
            for k in j:
                lst.append(k.text)
                # print(k.text)
            ministry_list.append(lst)
    ministry_list.insert(42, ' ')


    with co2:
        with st.expander("Ministers of State"):
            #st.subheader("Cabinet Ministers")
            for i in range(len(cabinet_ministers_names)):

                st.image(cabinet_ministers_images_links[i])
                st.write("**"+cabinet_ministers_names[i]+"**")
                for j in ministry_list[i]:
                    j= '<p style="font-family:sans-serif; color:Green; font-size: 15px;">'+j+'</p>'
                    st.write(j, unsafe_allow_html=True)
                st.write("---------------------------------------------------------------------------")

        #st.image("https://static.streamlit.io/examples/dog.jpg")








with tab5:


    df = pd.read_csv('loksabhadf.csv')
    option = st.selectbox(
        'Search Member of Parliament',
        (df["0"]))


    p = option
    p = p.lower()
    p = re.sub(" ", "-", p)
    p = p.replace(".", "")
    p = p.replace("--", "-")
    p = p[1:-1]

    url = "https://www.india.gov.in/my-government/indian-parliament/" + str(p)
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html')
    datas = soup.find_all("p", class_="view-field")
    Details = {}

    for data in datas[1:-2]:
        label = data.find(class_="view-label").text
        output = data.find(class_="view-output").text
        label = label.lower()
        label = re.sub(" ", "-", label)
        label = label.replace(".", "")
        label = label.replace("--", "-")

        if output is None:
            output = "."
        Details[label] = output
    dataframe = pd.DataFrame.from_dict(Details.items())
    htmldata = requests.get(url).text
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    for item in images:

        if item['alt'] == "":
            url_image = item['src']

    response = requests.get(url_image)
    img = Image.open(BytesIO(response.content))
    col1, col2 = st.columns([3, 1])
    #col1.subheader(option)
    option = '<p style="font-family:sans-serif; color:Green; font-size: 15px;">' + option+ '</p>'
    col1.table(dataframe)
    # col2.subheader("A narrow column with the data")
    col2.image(img, width=100)
    col2.write(option,unsafe_allow_html=True)


with tab6:
    df = pd.read_csv('rajsabhadf.csv')
    option = st.selectbox(
        'Search Member of Parliament',
        (df["0"]))

    p = option
    p = p.lower()
    p = re.sub(" ", "-", p)
    p = p.replace(".", "")
    p = p.replace("--", "-")
    p = p[1:-1]

    url = "https://www.india.gov.in/my-government/indian-parliament/" + str(p)
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html')
    datas = soup.find_all("p", class_="view-field")
    Details = {}

    for data in datas[1:-2]:
        label = data.find(class_="view-label").text
        output = data.find(class_="view-output").text
        label = label.lower()
        label = re.sub(" ", "-", label)
        label = label.replace(".", "")
        label = label.replace("--", "-")

        if output is None:
            output = "."
        Details[label] = output
    dataframe = pd.DataFrame.from_dict(Details.items())
    htmldata = requests.get(url).text
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    for item in images:

        if item['alt'] == "":
            url_image = item['src']

    response = requests.get(url_image)
    img = Image.open(BytesIO(response.content))
    colu1, colu2 = st.columns([3, 1])
    # col1.subheader(option)
    option = '<p style="font-family:sans-serif; color:Green; font-size: 15px;">' + option + '</p>'
    colu1.table(dataframe)
    # col2.subheader("A narrow column with the data")
    colu2.image(img, width=100)
    colu2.write(option, unsafe_allow_html=True)


with tab7:
    #st.header("Chief Ministers")

    url = "https://www.india.gov.in/my-government/whos-who/chief-ministers"
    # print(url)
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html')
    states = soup.find_all("td", class_="views-field views-field-php")
    links = soup.find_all("td", class_="views-field views-field-title")
    STATES = []
    for state in states:
        state = state.text
        state = state.strip()

        STATES.append(state)

    CM = []
    for link in links:
        CM.append(link.text.strip())
        # print(link.text)

    LINKS = []
    for link in links:
        LINKS.append("(" + link.find('a').get('href') + ")")
    # print(link.find('a').get('href'))

    cm_image_links = []
    cm_image_url = "https://en.wikipedia.org/wiki/List_of_current_Indian_chief_ministers"
    htmldata = requests.get(cm_image_url).text
    soup = BeautifulSoup(htmldata, 'html.parser')
    images = soup.find_all('img')
    for item in images:
        url = item['src']
        # print("https:"+url)
        cm_image_links.append("https:" + url)

    cm_image_links.pop(0)
    cm_image_links.pop(0)
    cm_image_links.pop(0)

    state_list = st.selectbox(
        'select a state',
        (STATES))
    st.write('You selected:', state_list)

    i = STATES.index(state_list)
    # st.write(STATES[i]+" : "+"["+CM[i]+"]" +  LINKS[i])
    photu = requests.get(cm_image_links[i])
    # imge = Image.open(BytesIO(photu.content))
    c1, c2 = st.columns([3, 1])
    c1.subheader("[" + CM[i] + "]" + LINKS[i])
    # col1.write(STATES[i]+" : "+"["+CM[i]+"]" +  LINKS[i])
    c2.caption("**Hon’ble Chief Minister of** " + "**" + STATES[i] + "**")
    # c2.image(imge, caption=CM[i], width=100)





Dict = {'madhya-pradesh':'https://www.findeasy.in/constituencies-in-madhya-pradesh-legislative-assembly/',
        #'assam':"https://www.findeasy.in/constituencies-in-assam-legislative-assembly-assam-mla-list/",
        'telangana':"https://www.findeasy.in/constituencies-in-telangana-legislative-assembly/",
        'rajasthan':"https://www.findeasy.in/constituencies-in-rajasthan-legislative-assembly/",
        'gujrat':"https://www.findeasy.in/constituencies-in-gujarat-legislative-assembly/",
        'odisha':"https://www.findeasy.in/constituencies-in-odisha-legislative-assembly/",
        'kerala':"https://www.findeasy.in/constituencies-in-kerala-legislative-assembly/",
        'jharkhand':"https://www.findeasy.in/constituencies-in-jharkhand-legislative-assembly/",
        #'chhattisgarh':"https://www.findeasy.in/constituencies-in-chhattisgarh-legislative-assembly/",
        #'haryana':"https://www.findeasy.in/constituencies-in-haryana-legislative-assembly/",
        'delhi':"https://www.findeasy.in/constituencies-in-delhi-legislative-assembly/",
        'uttarakhand':"https://www.findeasy.in/constituencies-in-uttarakhand-legislative-assembly/",
        'himachal-pradesh':"https://www.findeasy.in/constituencies-in-himachal-pradesh/",
        'tripura': "https://www.findeasy.in/constituencies-in-tripura-legislative-assembly/",
        'arunachal-pradesh':"https://www.findeasy.in/constituencies-in-arunachal-pradesh-legislative-assembly/",
        'meghalaya':"https://www.findeasy.in/meghalaya-constituencies-in-meghalaya-legislative-assembly/",
        'manipur':"https://www.findeasy.in/constituencies-in-manipur-legislative-assembly/",
        'nagaland':"https://www.findeasy.in/constituencies-in-nagaland-legislative-assembly/",
        'goa':"https://www.findeasy.in/constituencies-in-goa-legislative-assembly/",
        'mizoram':"https://www.findeasy.in/constituencies-in-mizoram-legislative-assembly/",
        #'jammu-kashmir':"https://www.findeasy.in/constituencies-in-jammu-and-kashmir-legislative-assembly/",
        'sikkim':"https://www.findeasy.in/constituencies-in-sikkim-legislative-assembly/",
        'puducherry': "https://www.findeasy.in/constituencies-in-puducherry-legislative-assembly/"
        }

st.write("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

statesls=["madhya-pradesh","telangana","rajasthan","gujrat","odisha","kerala","jharkhand","delhi","uttarakhand","himachal-pradesh","tripura","arunachal-pradesh","meghalaya","manipur","nagaland","goa","mizoram","sikkim","puducherry"]
op = st.selectbox(
    'select a state',
    (statesls))

t="List of constituencies of the " + op + " Legislative Assembly"
st.markdown("<h1 style='text-align: center;'>"+t+"</h1>", unsafe_allow_html=True)
#st.write('You selected:', Dict[op])








l=Dict[op]
htmldata=requests.get(l).text
soup = BeautifulSoup(htmldata, 'html.parser')
img=soup.find_all('table')
rows=img[1].find_all('tr')
LST = []
for tr in range(len(rows)):
    lst = []
    for td in rows[tr]:
        lst.append(td.text.strip())
        # print(td.text)
        # party.append(td.text.strip())
        # seats.append(td[2].text)
    LST.append(lst)
    # print("###################")
# print(LST)
df = pd.DataFrame(LST)
df = pd.DataFrame(df.values[1:], columns=df.iloc[0])
#df=df.drop(['#'], axis=1)
colum1,colum2 =st.columns([3,1])
colum2.table(df)

# for i in range(len(df)):
#     if df['MLA Seats'][i]==0 :
#         df['MLA Seats'][i]=0
#     else:
#         df['MLA Seats'][i]=float(df['MLA Seats'][i])
#     #type(df['Seats'][1])


# labels = df['Party']
# sizes =  [float(x) for x in df['MLA Seats']]
# #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes,labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# colum2.pyplot(fig1)

#
#
rows2=img[0].find_all('tr')
LST = []
for tr in range(len(rows2)):
    lst = []
    for td in rows2[tr]:
        lst.append(td.text.strip())
        # print(td.text)
        # party.append(td.text.strip())
        # seats.append(td[2].text)
    LST.append(lst)
    print("###################")

df = pd.DataFrame(LST)
df = pd.DataFrame(df.values[1:], columns=df.iloc[0])
#df=df.drop(['No.'], axis=1)
colum1.table(df)


#
#

rows3=img[2].find_all('tr')
LST = []
for tr in range(len(rows3)):
    lst = []
    for td in rows3[tr]:
        lst.append(td.text.strip())
        # print(td.text)
        # party.append(td.text.strip())
        # seats.append(td[2].text)
    LST.append(lst)
    print("###################")

df = pd.DataFrame(LST)
df = pd.DataFrame(df.values[1:], columns=df.iloc[0])
#df=df.drop(['#'], axis=1)
colum2.table(df)
