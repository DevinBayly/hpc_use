import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import json
import sys
import random
import streamlit.elements.image as st_image
import requests as rq
import seaborn as sb
from PIL import Image
# get the custom component
from streamlit_component_x.src.streamlit_component_x import example

# code that helps us gather an instutions data per a year
import requests as rq
# https://github.com/DevinBayly/vis-sieve/raw/1b09d0bcc7851eeb63524c4e730499eba59cb7ef/openalex_code/hear_me_ROR.ipynb
# TODO add a progress bar to the tool

headers = {"mailto":"baylyd@arizona.edu"}

@st.cache_data
def get_researcher_id(first,last,ror):
    res = rq.get(f"https://api.openalex.org/authors?filter=display_name.search:{first.lower()} {last.lower()},affiliations.institution.ror:{ror}",headers=headers)
    data = res.json()["results"]
    # assume the first hit is the best id
    # TODO put in test for making sure that the system can announce which name failed or broke

    if len(data)> 0:
        return Path(data[0]["id"]).stem
    else:
        return -1

@st.cache_data
def results_per_year(author_id,ror,year,qlim=2):
    # progress bar
    pubs_per_year_prog = st.progress(0,text=f"Starting query for year {year}, {qlim} in progress")
    all_res = []
    url =f"https://api.openalex.org/works?filter=authorships.author.id:{author_id},publication_year:{year},institutions.ror:{ror}&cursor=*&per-page=200"
    print(url)
    res = rq.get(url,headers=headers)
    data = res.json()
    print(data["meta"])
    all_res.extend(data["results"])
    cursor = data["meta"]["next_cursor"]
    query =1
    pubs_per_year_prog.progress(1/qlim, text=f'Works total {data["meta"]["count"]}, {qlim} in progress')


    while query < qlim:
        res = rq.get(f"https://api.openalex.org/works?filter=authorships.author.id:{author_id},publication_year:{year},institutions.ror:{ror}&cursor={cursor}&per-page=200")
        data = res.json()
        all_res.extend(data["results"])
        cursor = data["meta"].get("next_cursor",None)
        query+=1
        print(query)
        pubs_per_year_prog.progress(query/qlim)
    print("done",year,ror)
    pubs_per_year_prog.empty()
    return all_res


# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit
# app: `$ streamlit run my_component/example.py`


labels= ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
parents= ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ]


#concept_names, concept_counts, concept_parents = json.load(open('found_concepts.json', "r"))
#
## Sort by 
#for _ in range(3):
#    for i, concept_name in enumerate(concept_parents):
#        if concept_name != "" and concept_name not in concept_names:
#            concept_names.pop(i)
#            concept_counts.pop(i)
#            concept_parents.pop(i)
#            # print(concept_name)
#            # print("Removed " + concept_name)
#
#    print("Leftovers")
#    for i, concept_name in enumerate(concept_parents):
#        if concept_name != "" and concept_name not in concept_names:
#            # print(concept_name)
#            pass
#
#
#"""
## Publications by Users of University of Arizona HPC
#
#This app presents an interactive data visualization allowing a user to explore the scientific fields that our HPC users published to in the time range 2016-2022. 
#
#Interaction instructions:
#* Clicking on an individual square will expand the view and present the sub-fields for the selected square, this allows you to "go down" the tree
#* To "go back up" the tree, click on the ribbon at the top 
#* Now please click fullscreen to explore further
#You are encouraged to full screen the tree map below. 
#"""
##fig.update_traces(marker_cornerradius=5)
## st.plotly_chart(fig)
#
#print("running example from test_custom")


# Here's the main application view 


res = example([list(labels),list(parents)],key="fixed")

# standard metrics calculated 
# although they are defined later this is just to make sure they are able to update the metrics shown
# TODO think about how to maek the bar charts interactions also update things like the tree map

# bar chart section
# show the trend of the publication submissions over years

# making a sidebar
# "with" notation
with st.sidebar:
    st.write("""## Fill in the following elements to submit an publication impact query for a set of users""")
    #uploaded_file = st.file_uploader("Upload a list of Cluster User Names")
    #if uploaded_file is not None:
    #    text = open(uploaded_file).read_lines()
    #    st.write(text)
    names = st.text_area("First name, Last name, **One per line**",
    """Chris, Reidy
Devin, Bayly
Ben, Kruse
Jeremy, Frumkin
Nirav, Merchant
Tyson, Swetnam
Joshua, Levine""")

    name = st.text_input("Enter the Institution Name", "University of Arizona")
    res = rq.get(f"https://api.ror.org/organizations?query={name}").json()
    if res:
        items = res.get("items")
        if items:
            best_res = items[0]
            st.write(best_res["id"])
            ror_id = Path(best_res["id"]).stem
            print(ror_id)

    
    #specifying the range in time that we want to inspect
    start_date, end_date = st.select_slider(
        "Select a range of years to survey user publications",
        options=list(range(2016,2023)),
        value=(2016, 2017))
    st.write("You selected years between", start_date, "and", end_date)
    # limiting the queries to a number
    queries_per_year = st.select_slider(
        "Select the number of queries per year",
        options=list(range(1,100)),
        value=(1))
    st.write("You selected ", queries_per_year," per year")


    # go get the information, save it to disk so that it's cached though 
    # set a button here so that it doesn't try this each time we reload page 

    btn = st.button("Submit", type="primary")
    if btn:
        print(ror_id)
        # TODO set up checking for all the dependent inputs
        # TODO add a parameter that will tell us how many pages of results we want to gather from each year, for demo we can set it to 1 or 2
        # TODO set up the progress bars for this section
        year = start_date
        # go through the list of the researchers
        for name in names.strip().split("\n"):
            first,last = name.split(",")
            print(first,last)
            author_id = get_researcher_id(first,last,ror_id)
            if author_id ==-1:
                print("no id for ",first,last)
                continue
            qres = results_per_year(author_id,ror_id,year,qlim= queries_per_year)
            # st.write(qres)
            #print(qres)
            Path(f"{author_id}_{year}_{ror_id}.json").write_text(json.dumps(qres))
    # this code is from the vis sieve project 

#if res and 'finished' not in res:
#    st.markdown(res)
#    df = pd.read_csv("works.csv")
#    print(df.shape,res)
#    inds = df.concepts.str.contains(str(res),na=False)
#    # print(inds)
#    sub = df[inds].head(n=20)
#    print(sub)
#    st.table(sub)
