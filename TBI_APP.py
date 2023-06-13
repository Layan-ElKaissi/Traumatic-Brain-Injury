#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 00:16:47 2023

@author: layankaissi
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import hydralit_components as hc
from streamlit_lottie import st_lottie
import json
from PIL import Image
from streamlit_card import card



# Set page configuration
st.set_page_config(
    page_title="TBI Dashboard",
    page_icon="🧠",
    layout='wide'
)

# hide streamlit features
hide_streamlit_style = """
    <style>
        div[data-testid="stToolbar"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
        }
        div[data-testid="stDecoration"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
        }
        div[data-testid="stStatusWidget"] {
            visibility: hidden;
            height: 0%;
            position: fixed;
        }
        #MainMenu {
            visibility: hidden;
            height: 0%;
        }
        header {
            visibility: hidden;
            height: 0%;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Add CSS styles and icon libraries
st.markdown("""
    <style>
    .navigation-bar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #00008B;
        padding: 20px;
        margin-bottom: 20px;
        margin-top: 250px; /* Adjust the margin top value to move the navigation bar lower */
    }
    .navigation-bar {
        display: flex;
        justify-content: space-around;
        align-items: center;
        font-size: 24px;
        color: white;
    }
    .navigation-bar-item {
        display: flex;
        align-items: center;
        cursor: pointer;
        color: white;
        margin-right: 20px;
    }
    .navigation-bar-item i {
        margin-right: 10px;
    }
    .navigation-bar-item.active {
        background-color: #2F4F4F;
        border-radius: 4px;
        padding: 4px 8px;
    }
    </style>
""", unsafe_allow_html=True)



# Add CSS styles and icon libraries
st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/v4-shims.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/v4-shims.min.css">
    """, unsafe_allow_html=True)

# Define menu data with labels and icons
menu_data = [
    {'label': 'Home', 'icon': '<i class="fa-solid fa-key" style="color: #ffffff;"></i>'},
    {'label': 'Overview', 'icon': "fas fa-brain"},
    {'label': 'Statistics', 'icon': "fas fa-chart-bar"},
    {'label': 'Prevention', 'icon': "fas fa-shield-virus"},
    {'label': 'Treatment', 'icon': "fas fa-stethoscope"}
]

# Remove duplicate "Home" tab
menu_data = [item for item in menu_data if item['label'] != 'Home']

over_theme = {'txc_inactive': 'white', 'menu_background': '#00008B'}
menu_label = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    hide_streamlit_markers=False,
    sticky_nav=True,
    sticky_mode='sticky'
)

# Home Page
if menu_label == 'Home':
    st.title("Traumatic Brain Injury Dashboard")
   
    st.write("") 
       
    with open("/Users/apple/Desktop/brain-imaging.json", "r") as f:
            lottie_json = json.load(f)
            st_lottie(lottie_json, height=600, width=800)

if menu_label == "Overview":
        st.title("Traumatic Brain Injury (TBI) Overview")
        st.subheader(" - The Silent Epidemic")
        # Create two columns with custom CSS classes
        col1, col2 = st.columns(2)
        # Add content about TBI overview
        with col1:
         st.markdown("""
<div style="text-align: justify;">
        <p>Traumatic brain injury (TBI) happens when a sudden, external, physical assault damages the brain. It is one of the most common causes of disability and death in adults. TBI is a broad term that describes a vast array of injuries that happen to the brain. The damage can be focal (confined to one area of the brain) or diffuse (happens in more than one area of the brain). The severity of a brain injury can range from a mild concussion to a severe injury that results in coma or even death.</p>
        <p><strong>Brain injury may happen in one of two ways:</strong></p>
        <ul>
            <li>Closed brain injury: Closed brain injuries happen when there is a nonpenetrating injury to the brain with no break in the skull. A closed brain injury is caused by a rapid forward or backward movement and shaking of the brain inside the bony skull that results in bruising and tearing of brain tissue and blood vessels. Closed brain injuries are usually caused by car accidents, falls, and increasingly, in sports. Shaking a baby can also result in this type of injury (called shaken baby syndrome).</li>
            <li>Penetrating brain injury: Penetrating, or open head injuries happen when there is a break in the skull, such as when a bullet pierces the brain.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

         with col2:
           labels = ['Severe TBI', 'Moderate TBI', 'Mild TBI']
           values = [7.95, 11.04, 81.02]

           colors = ['#003366', '#3366CC', '#99CCFF']

           fig = go.Figure(data=[go.Pie(
    labels=labels,
    values=values,
    hole=0.6,
    textposition='outside',
    textinfo='percent',
    textfont_size=14,
    marker=dict(colors=colors)
)])
           
           fig.update_layout(
    title="Distribution of TBI Types",
    title_x=0.3,
    title_font=dict(size=24),
    showlegend=True,
    legend=dict(
        x=0.7,
        y=0.5,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="rgba(0,0,0,0)"
    ),
)
           
           col2.plotly_chart(fig)



# Create two columns with custom CSS classes
        col1, col2 = st.columns(2)

# Define the content for the info cards
        mild_tbi_content = """
    <div style="background-color: #E6F3FF; color: #000; padding: 20px; margin-bottom: 20px; border-radius: 10px; border: 2px solid #6699FF;">
    <h2 style="font-family: 'Arial', sans-serif;">Mild TBI and Concussions</h2>
    
    - Mild traumatic brain injury (TBI), often referred to as a concussion, is the most common form of TBI.
    - It is usually caused by a blow or jolt to the head or body that disrupts the normal functioning of the brain.
    - Symptoms of mild TBI can include headache, confusion, dizziness, memory problems, and sensitivity to light or noise.
    - Most people with mild TBI recover fully within a few weeks or months with appropriate rest and medical management.
    
    <a href="https://www.cdc.gov/traumaticbraininjury/mild.html" style="text-decoration: none; color: #3366CC; font-weight: bold;">Learn more : CDC mTBI & Concussions</a>
    </div>
"""

        moderate_severe_tbi_content = """
    <div style="background-color: #D9E6FF; color: #000; padding: 20px; margin-bottom: 20px; border-radius: 10px; border: 2px solid #3366CC;">
    <h2 style="font-family: 'Arial', sans-serif;">Moderate and Severe TBIs</h2>
    
    - Moderate and severe traumatic brain injuries (TBIs) are more severe forms of brain injury.
    - They can result from falls, motor vehicle accidents, assaults, or other traumatic events that cause significant impact or penetration to the head.
    - Moderate and severe TBIs often lead to more profound and long-lasting effects on cognitive, physical, and emotional functioning.
    - Rehabilitation and ongoing medical support are crucial for individuals with moderate and severe TBIs.
    
    <a href="https://www.cdc.gov/traumaticbraininjury/severe.html" style="text-decoration: none; color: #3366CC; font-weight: bold;">Learn more : CDC Moderat & Severe TBIs</a>
    </div>
"""

# Render the info cards in the respective columns
        col1.markdown(mild_tbi_content, unsafe_allow_html=True)
        col2.markdown(moderate_severe_tbi_content, unsafe_allow_html=True)
          
         # Define the data for the bar graph
        data = {
        "Outcome": ["Died", "Became Worse", "Stayed Home", "Improved"],
        "Number of Cases": [22, 30, 22, 26]
    }

        df = pd.DataFrame(data)
         # Define the colors for the bar graph
        colors = [
    '#3366CC', '#3377B4', '#3388CC', '#3399E6'
]
         # Create the bar graph
        fig = go.Figure(data=go.Bar(
        x=df["Outcome"],
        y=df["Number of Cases"],
        text=df["Number of Cases"],
        textposition="outside",
        texttemplate='%{text}%',
        marker=dict(
        color=colors,
        line=dict(color='rgba(0,0,0,0)', width=0.5)
    ),
    width=0.5
))
         # Set the layout of the bar graph
        fig.update_layout(
       title="Five-year Outcomes of People with Moderate to Severe TBI",
       xaxis=dict(title=""),
       yaxis=dict(
        title="",
        showticklabels=False
    ),
       showlegend=False,
       plot_bgcolor='rgba(0, 0, 0, 0)',
       paper_bgcolor='rgba(0, 0, 0, 0)',
       height=500,
       width=600
   )

   # Remove gridlines
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        
        info_card_expanded = col2.checkbox("Show Statistics", key="checkbox_stats")  
        if info_card_expanded:
            col2.empty()  # Clear the content of the column
            col2.plotly_chart(fig)  # Show the graph in the same column
        
 
        
        st.subheader("Possible Results of Traumatic Brain Injury:")

# Create expandable buttons
        with st.expander("Cognitive deficits"):
           st.write("""
- Coma
- Confusion
- Shortened attention span
- Memory problems and amnesia
- Problem-solving deficits
- Problems with judgment
- Inability to understand abstract concepts
- Loss of sense of time and space
- Decreased awareness of self and others
- Inability to accept more than one- or two-step commands at the same time


""")

        with st.expander("Motor deficits"):
           st.write("""
- Paralysis or weakness
- Spasticity (tightening and shortening of the muscles)
- Poor balance
- Decreased endurance
- Inability to plan motor movements
- Delays in getting started
- Tremors
- Swallowing problems
- Poor coordination

                    """)

        with st.expander("Perceptual or sensory deficits"):
           st.write("""
- Changes in hearing, vision, taste, smell, and touch
- Loss of sensation or heightened sensation of body parts
- Left- or right-sided neglect
- Difficulty understanding where limbs are in relation to the body
- Vision problems, including double vision, lack of visual acuity, or limited range of vision
                    """)

        with st.expander("Communication and language deficits"):
          st.write("""
- Difficulty speaking and understanding speech (aphasia)
- Difficulty choosing the right words to say (aphasia)
- Difficulty reading (alexia) or writing (agraphia)
- Difficulty knowing how to perform certain very common actions, like brushing one's teeth (apraxia)
- Slow, hesitant speech and decreased vocabulary
- Difficulty forming sentences that make sense
- Problems identifying objects and their function
- Problems with reading, writing, and ability to work with numbers
                   """)

        with st.expander("Functional deficits"):
          st.write("""
- Impaired ability with activities of daily living (ADLs), such as dressing, bathing, and eating
- Problems with organization, shopping, or paying bills
- Inability to drive a car or operate machinery
                   """)

        with st.expander("Social difficulties"):
          st.write("""
- Impaired social capacity resulting in difficult interpersonal relationships
- Difficulties in making and keeping friends
- Difficulties understanding and responding to the nuances of social interaction
                   """)

        with st.expander("Regulatory disturbances"):
          st.write("""
- Fatigue
- Changes in sleep patterns and eating habits
- Dizziness
- Headache
- Loss of bowel and bladder control
                   """)

        with st.expander("Personality or psychiatric changes"):
          st.write("""
- Apathy
- Decreased motivation
- Emotional lability
- Irritability
- Anxiety and depression
- Disinhibition, including temper flare-ups, aggression, cursing, lowered frustration tolerance, and inappropriate sexual behavior
                   """)
 
        with st.expander("Traumatic Epilepsy"):
          st.write("""
- Epilepsy can happen with a brain injury, but more commonly with severe or penetrating injuries. While most seizures happen immediately after the injury, or within the first year, it is also possible for epilepsy to surface years later. Epilepsy includes both major or generalized seizures and minor or partial seizures.
                   """)
                   
        st.subheader("Diagnosis")
        col1, col2, col3, col4 = st.columns(4)
    
        with col1: 
           with open("/Users/apple/Desktop/doctor.json", "r") as f:
             lottie_json = json.load(f)
             st_lottie(lottie_json, height=400)
             
        with col2: 
           with open("/Users/apple/Desktop/brain1.json", "r") as f:
             lottie_json = json.load(f)
             st_lottie(lottie_json, height=400)
             
        with col3: 
           with open("/Users/apple/Desktop/brain2.json", "r") as f:
              lottie_json = json.load(f)
              st_lottie(lottie_json, height=400)
              
        with col4: 
           with open("/Users/apple/Desktop/brain3.json", "r") as f:
              lottie_json = json.load(f)
              st_lottie(lottie_json, height=400)
              
        st.write("")
        step1 = """
        <div style="background-color: #E6F3FF; color: #000; padding: 10px; margin-bottom: 10px; border-radius: 10px; border: 2px solid #6699FF;">
    <h2 style="font-family: 'Arial', sans-serif; font-size: 18px;">Healthcare provider will ask about your symptoms and the details of your injury</h2>
             """
             
        step2 = """
        <div style="background-color: #E6F3FF; color: #000; padding: 10px; margin-bottom: 10px; border-radius: 10px; border: 2px solid #6699FF;">
    <h2 style="font-family: 'Arial', sans-serif; font-size: 18px;">Healthcare provider will do a neurologic exam, and may do imaging tests, such as a CT scan or MRI</h2>
             """  
             
        step3 = """
        <div style="background-color: #E6F3FF; color: #000; padding: 10px; margin-bottom: 10px; border-radius: 10px; border: 2px solid #6699FF;">
    <h2 style="font-family: 'Arial', sans-serif; font-size: 18px;">Healthcare provider may do neuropsychological tests to check how your brain is functioning</h2>
             """   
             
        step4 = """
        <div style="background-color: #E6F3FF; color: #000; padding: 10px; margin-bottom: 10px; border-radius: 10px; border: 2px solid #6699FF;">
    <h2 style="font-family: 'Arial', sans-serif; font-size: 18px;">Healthcare provider may use a tool such as the Glasgow coma scale to determine how severe the TBI is. This scale measures your ability to open your eyes, speak, and move.</h2>
             """          
        st.markdown(step1, unsafe_allow_html=True)
        st.markdown(step2, unsafe_allow_html=True)
        st.markdown(step3, unsafe_allow_html=True)
        st.markdown(step4, unsafe_allow_html=True)


if menu_label == "Statistics":
        st.title("TBI Statistics in the United States")
        # Add content about TBI statistics worldwide and in the US
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Annual TBIs reported", "2.8 M")
        col2.metric("Annual Deaths", "52 K")
        col3.metric("Annual hospitalizations", "230 K")
        col4.metric("Annual Economic burden", "> 40.6 B")
        col5.metric("Americans with TBI-related disability", "5.3 M")
        
        
        # Add an empty space to create a gap between the rows
        st.write("")
        # Add an empty space to create a gap between the rows
        st.write("")
        # Load the gender icons
        boy_icon = Image.open("/Users/apple/Desktop/boy-2.png")
        girl_icon = Image.open("/Users/apple/Desktop/girl.png")
        st.write("")
       # Set first 3 sets of visuals
        viz1 = st.columns(2)
        with viz1[0]:
            st.subheader("The rate of TBI-related deaths in males is 3 Times as high as in females")
            icon_size = 50  # Adjust the height as desired
            col1, col2, col3, col4 = st.columns([0.2, 0.2, 0.5, 1])

            with col1:
             st.image(boy_icon, width=icon_size)
            with col2: 
             st.image(boy_icon, width=icon_size)
            with col3:
             st.image(boy_icon, width=icon_size)
         
             # Add the girl icon within the container
            with col4:  
             st.image(girl_icon, width=45)
        st.write("")
        st.write("")
        with viz1[0]:
             st.subheader("The rate of TBI-related hospitalizations in males is 2 Times as high as in females")
             icon_size = 50  # Adjust the height as desired
             col1, col2, col3, col4 = st.columns([0.2, 0.2, 0.5, 1])

             with col1:
              st.image(boy_icon, width=icon_size)
             with col2: 
              st.image(boy_icon, width=icon_size)
             
              # Add the girl icon within the container
             with col4:  
              st.image(girl_icon, width=45)
             
        with viz1[0]:
    # Data
             show_graph = st.button('Number of traumatic brain injury-related deaths per 100,000 in 2019')
             if show_graph:
                data = {
            'Year': [2019],
            'Male Deaths': [44610],
            'Female Deaths': [16001],
            
        }
                df = pd.DataFrame(data)
                df["Male Deaths"] = df["Male Deaths"].apply(lambda x: f"{x:,}")
                df["Female Deaths"] = df["Female Deaths"].apply(lambda x: f"{x:,}")

        # Bar chart
                fig = go.Figure()

                fig.add_trace(go.Bar(x=df['Year'], y=df['Male Deaths'], name='Male', marker_color='#00284C',
                            text=df['Male Deaths'], textposition='auto',textfont=dict(size=16)))
                fig.add_trace(go.Bar(x=df['Year'], y=df['Female Deaths'], name='Female', marker_color='#0178e4',text=df['Female Deaths'], textposition='auto',textfont=dict(size=16)
                             ))

        # Customize layout
                fig.update_layout(
            showlegend=True,
            xaxis=dict(title=None, showgrid=False),
            yaxis=dict(title=None, showgrid=False),
            plot_bgcolor='white',
            width=500,
            height=400
        )

        # Render the chart
                st.plotly_chart(fig)
 
        with viz1[1]:
        # Define the data
           data2 = {
    'Region': ['Northeast', 'Midwest', 'South', 'West'],
    '2018': [8306, 13478, 25179, 13602],
    '2019': [8092, 13335, 25323, 13861]}
           
           df2 = pd.DataFrame(data2)
           
           
           # Define the mapping between region names and state codes
           region_to_state = {
    'Northeast': ['CT', 'ME', 'MA', 'NH', 'RI', 'VT', 'NJ', 'NY', 'PA'],
    'Midwest': ['IN', 'IL', 'MI', 'OH', 'WI', 'IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD'],
    'South': ['DE', 'DC', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA', 'WV', 'AL', 'KY', 'MS', 'TN', 'AR', 'LA', 'OK', 'TX'],
    'West': ['AZ', 'CO', 'ID', 'NM', 'MT', 'UT', 'NV', 'WY', 'AK', 'CA', 'HI', 'OR', 'WA']
}

# Create a color scale for the map
           colorscale = ['lightblue', 'blue']
           
           # Get user's selected year
           selected_year = st.selectbox('', ['2018', '2019'])
           
           # Create the data for the map
           map_data = []
           for region in data2['Region']:
             for i, state in enumerate(region_to_state[region]):
               value = df2.loc[df2['Region'] == region, selected_year].values[0]
               map_data.append({'code': state, 'value': value})
                
         # Filter the map data based on the selected year
           filtered_map_data = [d for d in map_data if d['value']]
           

# Create the choropleth map
           fig2 = go.Figure(data=go.Choropleth(
        locations=[d['code'] for d in filtered_map_data],
        z=[d['value'] for d in filtered_map_data],
        locationmode='USA-states',
        colorscale=colorscale,
        colorbar_title='Number of TBI Deaths',
        zmin=min([d['value'] for d in filtered_map_data]),
        zmax=max([d['value'] for d in filtered_map_data])
    ))
           
           # Add region names as annotations
           for region in region_to_state.keys():
             annotation_data = df2.loc[df2['Region'] == region, selected_year].values[0]
             fig2.add_annotation(
               x=region_to_state[region][0],
               y=-20,
               text=f"{region}: {annotation_data}",
               showarrow=False,
               font=dict(color='black', size=12),
        )


# Add a title and customize the layout
             fig2.update_layout(
    title_text=f'Annual number of traumatic brain injury-related deaths by US Census Region ({selected_year})',
    geo=dict(
        scope='usa',
        showlakes=False,
        lakecolor='rgb(255, 255, 255)'
    )
)

# Render the map
           st.plotly_chart(fig2)
           
           # Set first 3 sets of visuals
        viz2 = st.columns(2)
        with viz2[0]:
               # Define the data
          data = {
    'Emergency Visits': {
        'years': [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
        'male_rates': [494.6, 525.8, 500.8, 582.4, 590.9, 538.1, 491.6, 714.1, 850.9, 800.4],
        'female_rates': [349.3, 345.1, 348.4, 393.2, 421.6, 421.4, 424.3, 521.2, 508.1, 633.7]
    },
    'Hospitalizations': {
        'years': [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
        'male_rates': [104, 107.3, 121.9, 123, 113.7, 124.3, 115.5, 123.1, 105.9, 106.3],
        'female_rates': [62.1, 64.7, 68.2, 72.9, 72.6, 73.8, 68.6, 68.6, 90.4, 77.6]
    },
    'Deaths': {
        'years': [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
        'male_rates': [27.8, 27.4, 27.2, 26.8, 27.8, 27.2, 27, 26.5, 25.5, 25.4],
        'female_rates': [9.6, 9.5, 9.6, 9.8, 9.7, 9.5, 9.5, 9.1, 9.1, 9]
    }
}

# Create the figure
          fig = go.Figure()

# Set the layout
          fig.update_layout(
    xaxis=dict(title='', showgrid=False, showline=True),
    yaxis=dict(title='', showgrid=False, showline=True),
    plot_bgcolor='white',
    width=600,
    height=400,
    showlegend=True,
    legend=dict(x=0.02, y=0.98, bgcolor='rgba(255, 255, 255, 0.5)'),
    paper_bgcolor='white'
)

# Remove gridlines
          fig.update_xaxes(showgrid=False)
          fig.update_yaxes(showgrid=False)

# Create the radio button
          selected_data = st.radio("Select TBI-related Data", list(data.keys()))

# Add the traces based on the selected data type
          years = data[selected_data]['years']
          male_rates = data[selected_data]['male_rates']
          female_rates = data[selected_data]['female_rates']

          fig.add_trace(go.Scatter(
    x=years,
    y=male_rates,
    mode='lines+markers',
    name='Male',
    marker=dict(symbol='circle', size=8, color='#2a4657'),
    line=dict(color='#013667', width=2)
))

          fig.add_trace(go.Scatter(
    x=years,
    y=female_rates,
    mode='lines+markers',
    name='Female',
    marker=dict(symbol='square', size=8, color='#0178e4'),
    line=dict(color='#0165c0', width=2)
))

# Update the title based on the selected data type
          if selected_data == 'Emergency Visits':
            title = 'Rates of TBI-Related Emergency Department Visits by Gender from 2001-2010'
          elif selected_data == 'Hospitalizations':
             title = 'Rates of TBI-Related Hospitalizations by Gender from 2001-2010'
          elif selected_data == 'Deaths':
             title = 'Rates of TBI-Related Deaths by Gender from 2001-2010'

          fig.update_layout(title=title)
               
               # Apply custom CSS for radio button
          st.markdown(
    """
    <style>
    .radio-group .radio-option input[type="radio"] {
        display: none;
    }
    .radio-group .radio-option label {
        display: inline-block;
        cursor: pointer;
        padding: 8px 12px;
        border-radius: 4px;
        font-weight: bold;
        font-family: Arial, sans-serif;
        color: #ffffff;
        background-color: #007bff;
        margin-right: 10px;
    }
    .radio-group .radio-option input[type="radio"]:checked + label {
        background-color: #004aad;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the figure
          st.plotly_chart(fig, use_container_width=True)
        
        
        with viz2[1]:
           # Define the age groups
           age_groups = ['0-4', '5-14', '15-24', '25-44', '45-64', '65+']
           age_data = pd.DataFrame(age_groups)

    
# Define the data for emergency department visits
           ed_data = pd.DataFrame({
    'Year': ['2001–2002', '2003–2004', '2005–2006', '2007–2008', '2009–2010'],
    '0-4': [1112.6, 1272.3, 1268.3, 1374, 2193.8],
    '5-14': [498.8, 529.8, 591.4, 590.2, 888.7],
    '15-24': [576.9, 827.5, 648.3, 811.3, 981.9],
    '25-44': [388.3, 320.3, 373, 366.7, 470],
    '45-64': [164.8, 197.3, 267, 307.4, 328.2],
    '65+': [373.1, 293.3, 485.8, 544.7, 603.3]
})

# Define the data for hospitalizations
           hospitalizations_data = pd.DataFrame({
    'Year': ['2001–2002', '2003–2004', '2005–2006', '2007–2008', '2009–2010'],
    '0-4': [70.3, 78.7, 73.3, 63.4, 57.7],
    '5-14': [54.5, 48.5, 42.5, 40, 23.1],
    '15-24': [104.1, 126.6, 97.1, 106.5, 81.2],
    '25-44': [65.9, 76.4, 74.2, 75.2, 65.3],
    '45-64': [60.1, 67.9, 83.7, 83.9, 79.4],
    '65+': [191.5, 224.2, 237.5, 211.4, 294]
})
          

# Define the data for deaths
           deaths_data = pd.DataFrame({
    'Year': ['2001–2002', '2003–2004', '2005–2006', '2007–2008', '2009–2010'],
    '0-4': [5.2, 5.2, 5, 4.6, 4.3],
    '5-14': [3.2, 3, 2.7, 2.2, 1.9],
    '15-24': [23.4, 22, 21.2, 18.7, 15.6],
    '25-44': [17.6, 16.8, 16.8, 16, 14.6],
    '45-64': [17.5, 17.7, 18.1, 17.9, 17.6],
    '65+': [41.2, 42.1, 43.8, 44.9, 45.2]
})
   

# Create the figure
           fig = go.Figure()

# Set the layout
           fig.update_layout(
    xaxis=dict(title='', showgrid=False, showline=True),
    yaxis=dict(title='', showgrid=False, showline=True),
    plot_bgcolor='white',
    width=800,
    height=400,
    showlegend=True,
    legend=dict(x=4.02, y=0.98, bgcolor='rgba(255, 255, 255, 0.5)'),
    paper_bgcolor='white'
)

# Remove gridlines
           fig.update_xaxes(showgrid=False)
           fig.update_yaxes(showgrid=False)

# Define the color palette
           color_palette = [
    '#2525db', '#3030e1', '#3a3ae8', '#4545ee', '#4f4ff5', '#5959fb'
]
           
           # Function to update the figure based on the selected data type
           def update_figure(data):
               
               fig.data = []  # Clear existing traces
               for i, age_group in enumerate(age_groups):
                  
                  
                  trace = go.Scatter(
                       x=data['Year'],
                       y=data[age_group],
                       mode='lines+markers',
                       name=f'Age Group: {age_group}',
                       marker=dict(size=8),
                       line=dict(width=2),
                   )
                  fig.add_trace(trace)
                  

# Add the radio button for data selection
           data_type = st.radio("Select TBI-related Data:", ('Emergency Visits', 'Hospitalizations', 'Deaths'))

# Update the data and colors based on the selection
           if data_type == 'Emergency Visits':
             data = ed_data
           elif data_type == 'Hospitalizations':
            data = hospitalizations_data
           elif data_type == 'Deaths':
             data = deaths_data
             
 # Update the figure based on the selected data type
           update_figure(data)    
             

# Update the title based on the selected data
           fig.update_layout(title=f"Rates of TBI-Related {data_type} by Age Group from 2001-2010")

# Set the color scale
           fig.update_traces(marker=dict(colorscale='viridis'))

# Add an empty space to create a gap between the rows
           st.write("")
# Display the figure
           st.plotly_chart(fig, use_container_width=True)
        
           
        viz3 = st.columns(4)
        with viz3[0]:
         data = {
    "Year": [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014],
    "Total": [1884195, 1925173, 2019166, 2377868, 2521966, 2653617, 2735909, 2797754, 2877757],
    "ED Visits": [1551107, 1603124, 1698326, 2047886, 2143133, 2332299, 2390167, 2460278, 2532537],
    "Hospitalizations": [278655, 267350, 267015, 277315, 325996, 267480, 290360, 281555, 288420],
    "Deaths": [54433, 54699, 53825, 52667, 52837, 53837, 55382, 55921, 56800]
}

         df = pd.DataFrame(data)

         fig = go.Figure()

         fig.add_trace(go.Scatter(
    x=df["Year"],
    y=df["Total"],
    mode='lines+markers',
    name='Total',
    line=dict(color='#3366CC')
))

         fig.add_trace(go.Scatter(
    x=df["Year"],
    y=df["ED Visits"],
    mode='lines+markers',
    name='Emergency Department Visits',
    line=dict(color='#993399')
))

         fig.add_trace(go.Scatter(
    x=df["Year"],
    y=df["Hospitalizations"],
    mode='lines+markers',
    name='Hospitalizations',
    line=dict(color='#66CCCC')
))

         fig.add_trace(go.Scatter(
    x=df["Year"],
    y=df["Deaths"],
    mode='lines+markers',
    name='Deaths',
    line=dict(color='#006633')
))

         fig.update_layout(
   title={
        'text': "Estimated Number of TBI-Related ED Visits, Hospitalizations, and Deaths<br>from 2006 to 2014",
        'x': 0.5,
        'y': 0.95,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size': 18},
    },
    xaxis=dict(title="", showgrid=False, showline=True),
    yaxis=dict(title="", showgrid=False, showline=True),
    showlegend=False,
    plot_bgcolor='rgba(0, 0, 0, 0)',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    height=400,
    width=600,
    margin=dict(l=50, r=50, t=50, b=50)
    
)
         # Add labels next to each line
         annotations = [
       dict(
        x=df["Year"].iloc[-1],
        y=df[column].iloc[-1] + 100000,
        xanchor='left',
        yanchor='middle',
        text=column,
        font=dict(color=fig["data"][i]["line"]["color"]),  # i+1 to skip the first trace (Total)
        showarrow=False,
    )
    for i, column in enumerate(df.columns[1:])
   ]

         fig.update_layout(annotations=annotations)
         fig.update_xaxes(range=[2006, 2015])
         st.plotly_chart(fig)
         
     
         
         with viz3[2]:
           
           # Data for the pie charts
           hospitalization_percentage = 32  
           fig1 = go.Figure(data=[go.Pie(
        labels=['Hospitalizations', 'Other'],
        values=[hospitalization_percentage, 100 - hospitalization_percentage],
        hole=0.6,
        marker_colors=['#013667', '#0165c0'],
        showlegend=False,
        textinfo='none'
        
    )])
           fig1.update_layout(title="Adults Aged 75+ years account for<br>32% of all TBI-related hospitalizations", width=400, height=400)
           st.plotly_chart(fig1, use_container_width=True)
          
           
         with viz3[3]:
           
           death_percentage = 28
           fig2 = go.Figure(data=[go.Pie(
        labels=['Hospitalizations', 'Other'],
        values=[death_percentage, 100 - death_percentage],
        hole=0.6,
        marker_colors=['#013667', '#0165c0'],
        showlegend=False,
        textinfo='none'
        
    )])
           fig2.update_layout(title="Adults Aged 75+ years account for<br>28% of all TBI-related deaths", width=400, height=400)
           

           st.plotly_chart(fig2)
           

        
        viz4 = st.columns(2)
        with viz4[0]:
            # Create a DataFrame with the data
            data = {
    "Injury Mechanism": [
        "Unintentional motor vehicle crashes",
        "Unintentional falls",
        "Unintentionally struck by/against an object",
        "Other unintentional injury",
        "Suicide",
        "Homicide",
        "Other (no intent or mechanism specified)",
    ],
    "2000–2002": [
        17055, 7734, 393, 4719, 19882, 6049, 559
    ],
    "2003–2005": [
        16516, 9863, 381, 4566, 20168, 5943, 643
    ],
    "2006–2008": [
        14943, 11694, 381, 4290, 20854, 5950, 706
    ],
    "2009–2011": [
        11482, 13301, 360, 3826, 21877, 5297, 726
    ],
    "2012–2014": [
        10916, 15107, 367, 3870, 23227, 5089, 751
    ],
    "2015–2017": [
        11236, 16828, 339, 4144, 25965, 5779, 792
    ]
}

            df = pd.DataFrame(data)

# Create a selectbox to choose the year
            years = df.columns[1:].tolist()
            selected_year = st.selectbox("", years)

# Get the data for the selected year
            year_data = df[selected_year].tolist()

# Calculate the percentages
            total_deaths = sum(year_data)
            percentages = [round((deaths / total_deaths) * 100, 2) for deaths in year_data]

# Define colors for the chart
            colors = [
    'rgb(33, 113, 181)',  # Blue
    'rgb(8, 48, 107)',  # Dark Blue
    'rgb(63, 36, 110)',  # Dark Purple
    'rgb(204, 41, 54)',  # Red
    'rgb(255, 196, 37)',  # Yellow
    'rgb(118, 167, 93)',  # Light Green
    'rgb(0, 75, 54)'  # Dark Green
]

# Create a pie chart using Plotly Go
            fig = go.Figure(data=[go.Pie(
    labels=df["Injury Mechanism"],
    values=percentages,
    hole=0.6,
    sort=False,
    marker=dict(colors=colors),
    textinfo='value'
)])

# Set the title
            fig.update_layout(
    title=f"Percentage of TBI-related Deaths by Injury Mechanism\nYear: {selected_year}",
    title_font=dict(size=16),
    legend=dict(
        title="Injury Mechanism",
        orientation="h",
        yanchor="bottom",
        y=-0.6,
        xanchor="center",
        x=0.5
    )
)

# Display the chart
            st.plotly_chart(fig)
           
        with viz4[1]:
            # Define the data for 2018 and 2019
            data_2018_2019 = {
    'Injury Mechanism': ['Motor Vehicle Traffic Crashes', 'Falls', 'Struck by or Against an Object',
                         'Suicide', 'Assault', 'Other Unspecified'],
    'Male': [7497, 10546, 275, 18684, 4042, 2850],
    'Female': [2794, 7552, 54, 2802, 1561, 1070]
}

# Define the data for 2016 and 2017
            data_2016_2017 = {
    'Injury Mechanism': ['Motor Vehicle Traffic Crashes', 'Falls', 'Struck by or Against an Object',
                         'Suicide', 'Assault', 'Other Unspecified'],
    'Male': [8036, 10180, 291, 17382, 4280, 3011],
    'Female': [3062, 7228, 55, 2789, 1665, 1163]
}

# Create a DataFrame for each year's data
            df_2018_2019 = pd.DataFrame(data_2018_2019)
            df_2016_2017 = pd.DataFrame(data_2016_2017)
            
            # Define the available years for the select box
            years = ['2018-2019', '2016-2017']

# Create the initial bar graph for the selected year
            def create_bar_graph(year):
              if year == '2018-2019':
                 df = df_2018_2019
              else:
                 df = df_2016_2017

              fig = go.Figure(data=[
        go.Bar(name='Male', x=df['Injury Mechanism'], y=df['Male'], marker_color='#013667'),
        go.Bar(name='Female', x=df['Injury Mechanism'], y=df['Female'], marker_color='#0165c0')
    ])

              fig.update_layout(
        title=f"Number of deaths by Injury Mechanism & Gender - {year}",
        xaxis_title="",
        yaxis_title="",
        xaxis=dict(
        tickangle=0, showgrid=False, showline=True),
        yaxis=dict(
        showgrid=False, showline=True),
        barmode='group',
        legend=dict(
            x=0.85,
            y=1,
            traceorder="normal",
            font=dict(
                family="sans-serif",
                size=12,
                color="black"
            ),
            bgcolor="rgba(0,0,0,0)"
            
        )
    )


              return fig
          # Add a select box to choose the year
            selected_year = st.selectbox("", years)
              
              # Create the bar graph based on the selected year
            fig = create_bar_graph(selected_year)

    # Render the graph using Streamlit
            st.plotly_chart(fig)
            
        
            
        viz5 = st.columns(2)
        with viz5[0]:  
              
                # Create the DataFrame for the data
              data = {
    "Year": [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
    "White": [36479, 38054, 38171, 38070, 38720, 39623, 39241, 39852, 40018, 38846, 39626, 40153, 41080, 41706, 42146, 43423, 44742, 45897, 45402, 45160],
    "Black": [6268, 6325, 6213, 6395, 6308, 6588, 6606, 6375, 5923, 5644, 5471, 5657, 5736, 5782, 5743, 6366, 6857, 7050, 6983, 7135],
    "American Indian/Alaska Native": [581, 613, 651, 653, 598, 628, 605, 563, 569, 580, 551, 628, 639, 621, 644, 685, 652, 752, 656, 611],
    "Asian/Pacific Islander": [890, 954, 986, 1009, 970, 1093, 1058, 1125, 1030, 1073, 1076, 1182, 1219, 1265, 1330, 1380, 1528, 1553, 1619, 1649],
    "Hispanic": [4505, 4826, 4881, 5015, 4950, 5329, 5279, 5197, 4778, 4823, 4356, 4518, 4745, 4649, 4877, 5173, 5585, 5717, 5761, 5937],
    "Other": [204, 209, 217, 159, 157, 147, 134, 133, 116, 197, 184, 150, 175, 155, 201, 219, 170, 162, 0, 0]
}
              df = pd.DataFrame(data)
              # Select box for year
              selected_year = st.selectbox("", df["Year"].unique())

# Filter data for the selected year
              filtered_df = df[df["Year"] == selected_year].reset_index(drop=True)
              
              

# Create the bar graph
              fig = go.Figure()

              for i, ethnicity in enumerate(filtered_df.columns[1:-1]):
                 fig.add_trace(go.Bar(
            x=filtered_df[ethnicity],
            y=[ethnicity],
            name=ethnicity,
            orientation="h",
            text=filtered_df[ethnicity],
            textposition="auto",
            marker=dict(
                color="#0165c0",
                line=dict(color="#0165c0", width=0.5))
            
        )
    )
# Update the layout
              fig.update_layout(
    title="Total Number of TBI Deaths by Ethnicity",
    xaxis_title="",
    xaxis=dict(
        visible=False,
        showgrid=False
    ),yaxis=dict(
        showgrid=False
    ),
    yaxis_title="",
    barmode="group",
    showlegend=False,
    height=500,
    width=600
   
)

# Display the bar graph
              st.plotly_chart(fig)
              
              
        with viz5[1]:
           with open("/Users/apple/Desktop/people.json", "r") as f:
              lottie_json = json.load(f)
              st_lottie(lottie_json, height=500)
              
              
              
        viz6 = st.columns(1)
        with viz6[0]:  
             data = {
     "Injury Cause": [
         "Motor Vehicle Traffic Crashes",
         "Falls",
         "Struck by or Against an Object",
         "Suicide",
         "Assault",
         "Other",
     ],
     "Total Hospitalizations": [55730, 109760, 5335, 1460, 14590, 19075],
 }

             df = pd.DataFrame(data)
             # Sort the DataFrame by Total Hospitalizations in descending order
             df = df.sort_values(by="Total Hospitalizations", ascending=False)
             
             # Format the Total Hospitalizations column with commas
             df["Total Hospitalizations"] = df["Total Hospitalizations"].apply(lambda x: f"{x:,}")

             fig = go.Figure(data=go.Bar(
     y=df["Injury Cause"],
     x=df["Total Hospitalizations"],
     orientation="h",
     text=df["Total Hospitalizations"],
     textposition="auto",
     marker=dict(
         color="#0165c0",
         line=dict(color="#0165c0", width=0.5)
     )
 ))

             fig.update_layout(
     title="Causes of Traumatic Brain Injury Hospitalizations in 2017",
     xaxis=dict(
         visible=False,
         showgrid=False
     ),
     yaxis=dict(
         showgrid=False
     ),
     showlegend=False,
     plot_bgcolor='rgba(0, 0, 0, 0)',
     paper_bgcolor='rgba(0, 0, 0, 0)',
     height=500,
     width=600
     
 )

             fig.update_xaxes(showticklabels=False)

             st.plotly_chart(fig)
                  
                         


if menu_label == "Prevention":
    st.title("TBI Prevention")
    # Add content about TBI prevention strategies and tips
    st.markdown("<h3 style='text-align: left; color: blue;'>Prevention methods for those with a high risk of TBI</h1>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.subheader("Children between 0-14 years are at a high risk of falling")
        st.markdown("<br>", unsafe_allow_html=True)  # Add a line break

        st.markdown("""
        <div style="padding-top: 40px;"></div>
        """, unsafe_allow_html=True)
        # Animation1 about children 0-14 years
        with open("/Users/apple/Desktop/student.json", "r") as f:
            lottie_json = json.load(f)
            st_lottie(lottie_json, height=400)
            st.caption(f"""
            <div>
                <div style="vertical-align:left;font-size:16px;padding-left:5px;padding-top:5px;margin-left:0em";>
Make living and play areas safer for children                 

Supervise children playing on or near fall hazards.

Place guards, gates, and screens around windows and stairs. </div>""",unsafe_allow_html = True)
    with col2:
        st.subheader("Teens and young adults are at a high risk of sports and recreational activity injuries that cause TBI")
        # Animation2 about teens and young adults
        with open("/Users/apple/Desktop/soccer.json", "r") as f:
            lottie_json = json.load(f)
            st_lottie(lottie_json, height=400)
            st.caption(f"""
            <div>
                <div style="vertical-align:left;font-size:16px;padding-left:5px;padding-top:5px;margin-left:0em";>
                 
Adhere to safe play, and model a safe sports culture.

Wear well-maintained and properly fitting protective equipment, particularly helmets, for the activity.

Avoid hits to the head to the extent possible.

Implement rule changes (such as those limiting body checking or ball heading). </div>""",unsafe_allow_html = True)

    with col3:
        st.subheader("Teens and young adults are at a high risk of motor vehicle collisions that cause TBI")
        st.markdown("<br>", unsafe_allow_html=True)  # Add a line break

        st.markdown("""
        <div style="padding-top: 0px;"></div>
        """, unsafe_allow_html=True)
        # Animation3 about teens and young adults
        with open("/Users/apple/Desktop/delivery.json", "r") as f:
            lottie_json = json.load(f)
            st_lottie(lottie_json, height=399)
            st.caption(f"""
            <div>
                <div style="vertical-align:left;font-size:16px;padding-left:5px;padding-top:5px;margin-left:0em";>
                 
Wear a seat belt, no matter how short the ride.

Wear a helmet when riding motorcycles, scooters, and bicycles.

Never drive while impaired. 

Obey traffic laws, and exercise caution when driving in bad weather.

Enact and enforce laws related to impaired and distracted driving and other traffic safety issues.

Continue to develop advances in automobile engineering, such as antilock brakes and airbags. </div>""",unsafe_allow_html = True)

    with col4:
        st.subheader("Older adults, aged 65 and up, are at a high risk of falling")
        st.markdown("<br>", unsafe_allow_html=True)  # Add a line break

        st.markdown("""
        <div style="padding-top: 35px;"></div>
        """, unsafe_allow_html=True)
        # Animation4 about older adults
        with open("/Users/apple/Desktop/old-man.json", "r") as f:
            lottie_json = json.load(f)
            st_lottie(lottie_json, height=400)
            st.caption(f"""
            <div>
                <div style="vertical-align:left;font-size:16px;padding-left:5px;padding-top:5px;margin-left:0em";>
                 
Improve home safety to reduce trip hazards, such as by using antislip rugs, in-home lighting, and grab bars along staircases.

Discuss fall risk and prevention with a health care provider: Talk to your doctor to evaluate your risk for falling, and talk with them about specific things you can do to reduce your risk for a fall.

Ask your doctor or pharmacist to review your medicines to see if any might make you dizzy or sleepy. This should include prescription medicines, over-the counter medicines, herbal supplements, and vitamins.

Participate in exercises that improve balance, strength, coordination, and gait (e.g., Tai Chi). </div>""",unsafe_allow_html = True)



if menu_label == "Treatment":
        st.title("TBI Treatment")
        # Add content about TBI treatment options and therapies
        For_mild_tbi = """
    <div style="background-color: #E6F3FF; color: #000; padding: 20px; margin-bottom: 20px; border-radius: 10px; border: 2px solid #6699FF;">
    <h2 style="font-family: 'Arial', sans-serif;font-size: 18px;">Treatment for Mild TBI and Concussions</h2>
    
The main treatment is rest. If you have a headache, you can try taking over-the-counter pain relievers. It is important to follow your health care provider's instructions for complete rest and a gradual return to your normal activities. If you start doing too much too soon, it may take longer to recover. Contact your provider if your symptoms are not getting better or if you have new symptoms.
"""


        For_severe_tbi = """
    <div style="background-color: #D9E6FF; color: #000; padding: 20px; margin-bottom: 20px; border-radius: 10px; border: 2px solid #3366CC;">
    <h2 style="font-family: 'Arial', sans-serif;font-size: 18px;"> Treatment for Moderate and Severe TBIs </h2>

    
The first thing health care providers will do is stabilize you to prevent further injury. They will manage your blood pressure, check the pressure inside your skull, and make sure that there is enough blood and oxygen getting to your brain.

Once you are stable, the treatments may include:
    
Surgery to reduce additional damage to your brain, for example to:
 - Remove hematomas (clotted blood)
 - Get rid of damaged or dead brain tissue
 - Repair skull fractures
 - Relieve pressure in the skull
 
Medicines to treat the symptoms of TBI and to lower some of the risks associated with it, such as:
 - Anti-anxiety medication to lessen feelings of nervousness and fear
 - Anticoagulants to prevent blood clots
 - Anticonvulsants to prevent seizures
 - Antidepressants to treat symptoms of depression and mood instability
 - Muscle relaxants to reduce muscle spasms
 - Stimulants to increase alertness and attention
 
Rehabilitation therapies, which can include therapies for physical, emotional, and cognitive difficulties:
 - Physical therapy, to build physical strength, coordination, and flexibility
 - Occupational therapy, to help you learn or relearn how to perform daily tasks, such as getting dressed, cooking, and bathing
 - Speech therapy, to help you to with speech and other communication skills and treat swallowing disorders
 - Psychological counseling, to help you learn coping skills, work on relationships, and improve your emotional well-being
 - Vocational counseling, which focuses on your ability to return to work and deal with workplace challenges
 - Cognitive therapy, to improve your memory, attention, perception, learning, planning, and judgment
 
Some people with TBI may have permanent disabilities. A TBI can also put you at risk for other health problems such as anxiety, depression, and post-traumatic stress disorder. Treating these problems can improve your quality of life.
"""

        st.markdown(For_mild_tbi, unsafe_allow_html=True)
        st.markdown(For_severe_tbi, unsafe_allow_html=True)
               
        
        card(
    title="Stages of a care journey after TBI",
    text="",
    image="https://nap.nationalacademies.org/openbook/25394/xhtml/images/img-64-1.jpg",
    url="https://nap.nationalacademies.org/read/25394/chapter/5#48")

        
  

# Add custom JavaScript to handle tab selection
script = """
<script>
    function setTab(label) {
        const tabs = document.querySelectorAll('.navigation-bar-item');
        tabs.forEach(tab => tab.style.backgroundColor = '');
        tabs.forEach(tab => {
            if (tab.innerText.includes(label)) {
                tab.style.backgroundColor = 'white';
            }
        });
        Streamlit.setComponentValue(label);
    }
</script>
"""
st.markdown(script, unsafe_allow_html=True)
