#scrape data from airbnb
import requests,sys
from bs4 import BeautifulSoup
import pandas as pd
url='https://www.airbnb.co.in/s/Manali--Himachal-Pradesh/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&query=Manali%2C%20Himachal%20Pradesh&date_picker_type=calendar&place_id=ChIJP9A_FgiHBDkRzXZQvg6oKYE&checkin=2022-11-25&checkout=2022-11-30&source=structured_search_input_header&search_type=user_map_move&adults=2&ne_lat=32.28992221531866&ne_lng=77.29836740296662&sw_lat=32.151958294584254&sw_lng=77.0750359515506&zoom=12&search_by_map=true'

page=requests.get(url)
print(page)
soup=BeautifulSoup(page.text,'lxml')
print(type(soup))
#print(soup)
df=pd.DataFrame(columns =['links', 'title', 'desc', 'beds','cost per night'])



while True:
    postings=soup.find_all('a',class_='ln2bl2p dir dir-ltr')
    links_row=[]
    for post in postings:
        link=post.get('href')
        full_link='https://www.airbnb.co.in'+link
        links_row.append(full_link)
        print(full_link)

    titles_row=[]  
    title=soup.find_all('div',class_='t1jojoys dir dir-ltr') 
    for t in title:
        tit=t.text
        titles_row.append(tit)
        
    des_row=[]
    desc=soup.find_all('span',class_='t6mzqp7 dir dir-ltr')
    for d in desc:
        desc=d.text
        des_row.append(desc)
        
    beds_row=[]
    beds=soup.find_all('div',class_='f15liw5s s1cjsi4j dir dir-ltr')
    for b in beds:
        bed_text=b.text.strip()
        print(bed_text)
        if bed_text=='':
            pass
        else:
            beds_row.append(bed_text)

    cost_row=[]
    costs=soup.find_all('span',class_='_tyxjp1')
    for c in costs:
        cost_row.append(c.text.replace('\xa0','').replace('₹',''))
    print(beds_row)   
    print(len(links_row))
    print(len(titles_row))
    print(len(des_row))
    print(len(beds_row))
    print(len(cost_row))
    details_list=[]
    
    for i in range(len(links_row)):
        list1=[]
        list1.append(links_row[i]) 
        list1.append(titles_row[i])
        list1.append(des_row[i])
        try:
            list1.append(beds_row[i])
        except:
            list1.append('none')
        list1.append(cost_row[i])
        details_list.append(list1)
        
       
        
    print(details_list)
    for i in details_list:
        df.loc[len(df)] = i
        print(df)
    try:    
        next_page=soup.find('a',{'aria-label':'Next'}).get('href')
    except:
        df.to_excel(r"C:\Users\AMacharla\Documents\file_airbnb.xlsx")
        break
    #print(next_page)
    next_page_full='https://www.airbnb.co.in'+next_page
    print(next_page_full)
    url=next_page_full
    page=requests.get(url)
    print(page)
    soup=BeautifulSoup(page.text,'lxml')
    print(type(soup))

