
from turtle import title
import streamlit as st
import os
from gtts import gTTS
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import streamlit.components.v1 as components
from  PIL import Image
import pandas as pd

df = pd.read_csv(r"C:\Users\Sagar\Downloads\Copy of Pahari Library - वार्तालाप .csv")

# dropping the first column which was 'S.No.' 
df = df.drop(df.iloc[:,0:1],axis=1)

# dropping the cloumns from index 6 to end
df = df.drop(df.iloc[:,6:],axis = 1)

# setting new columns name as row entries from index 4
df.columns = df.iloc[4]

# dropping the rows knowinf their indeces
df = df.drop([0,1,2,3,4])

# resettig the row idexes .i.e. starting from 0
df.reset_index(inplace=True,drop=True)

framesh = [df['English-H'],df['Hindi']]
hindi = pd.concat(framesh).reset_index(drop=True)

framesm = [df['E-M'],df['Mandyali']]
mand = pd.concat(framesm).reset_index(drop=True)

framese = [df['ENGLISH'],df['ENGLISH']]
eng = pd.concat(framese).reset_index(drop=True)

framesg = [df['E-G'],df['E-G']]
garh = pd.concat(framesg).reset_index(drop=True)

CD=pd.concat([hindi, mand, eng, garh], axis=1)
CD.columns =['HN', 'MN', 'EN', "GH"]


# retrieving indexes of single element
def getIndexes_CD(MD, value):
    ''' Get index positions of value in dataframe i.e. MD.'''
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    val=value
    result = MD.isin([val])
    #print(result)
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
          if 134>row>66:
            row-=67
            listOfPos.append(row)
          elif row>133:
            row-=134
            listOfPos.append(row)
          else:
            listOfPos.append(row)
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos[0]

# functions for translation from Mandyali to others
def translator_M_H(input):
  index = getIndexes_CD(CD,value=input)
  outputm =()
  output1 = df['English-H'].values[index]
  output2 = df['Hindi'].values[index]
  outputm = ('ENGLISH-HINDI --> {}, HINDI--> {}'.format(output1,output2))
  return outputm

def translator_M_E(input):
  index = getIndexes_CD(CD,value=input)
  output1 = df['ENGLISH'].values[index]
  return output1

def translator_M_G(input):
  index = getIndexes_CD(CD,value=input)
  output1 = df['E-G'].values[index]
  return output1

# functions for translation from Hindi to others
def translator_H_E(input):
  index = getIndexes_CD(CD,value=input)
  output1 = df['ENGLISH'].values[index]
  return output1

def translator_H_G(input):
  index = getIndexes_CD(CD,value=input)
  output1 = df['E-G'].values[index]
  return output1

def translator_H_M(input):
  index = getIndexes_CD(CD,value=input)
  outputm =()
  output1 = df['E-M'].values[index]
  output2 = df['Mandyali'].values[index]
  outputm = ('ENGLISH-MANDYALI --> {}, MANDYALI--> {}'.format(output1,output2))
  return outputm

# functions for translation from English to others
def translator_E_H(input):
  index = getIndexes_CD(CD,value=input)
  outputm =()
  output1 = df['Hindi'].values[index]
  output2 = df['English-H'].values[index]
  outputm = ('HINDI ---> {}, ENGLISH-HINDI ---> {}'.format(output1,output2))
  return outputm

def translator_E_G(input):
  index = getIndexes_CD(CD,value=input)
  output1 = df['E-G'].values[index]
  return output1

def translator_E_M(input):
  index = getIndexes_CD(CD,value=input)
  outputm =()
  output1 = df['E-M'].values[index]
  output2 = df['Mandyali'].values[index]
  outputm = ('ENGLISH-MANDYALI --> {}, MANDYALI--> {}'.format(output1,output2))
  return outputm

# functions for translation from Garhwali to others
def translator_G_H(input):
  index = getIndexes_CD(CD,value=input)
  outputm =()
  output1 = df['Hindi'].values[index]
  output2 = df['English-H'].values[index]
  outputm = ('HINDI ---> {}, ENGLISH-HINDI ---> {}'.format(output1,output2))
  return outputm

def translator_G_E(input):
  index = getIndexes_CD(CD,value=input)
  output1 = df['ENGLISH'].values[index]
  return output1

def translator_G_M(input):
  index = getIndexes_CD(CD,value=input)
  outputm =()
  output1 = df['E-M'].values[index]
  output2 = df['Mandyali'].values[index]
  outputm = ('ENGLISH-MANDYALI --> {}, MANDYALI--> {}'.format(output1,output2))
  return outputm

st.markdown(""" # HIMTRADI    """)

#Add a logo (optional) in the sidebar
logo = Image.open(r'C:\Users\Sagar\Downloads\himtri.png')
st.sidebar.image(logo,  width=280,use_column_width=280)

#Add the expander to provide some basic information about the app
st.sidebar.markdown("### Platform to comprehend Tribal Languages")
with st.sidebar.expander("About the Platform"):
     st.write("""
        This language learning Platform is built to work as medium to understand and get to know Tribal languages.
     """)
st.sidebar.markdown("Please use this platform to learn and interpret tribal languages by translating words. These words are commonly used by people in their day to day life")


# main interface CLR - '#273346'

# Background color for the main content area
#backgroundColor = '#F63366'


#Add a horizontal menu bar
choose_from = st.selectbox("Choose a language", ['HINDI','MANDYALI','ENGLISH','GARHWALI'],)

translate_to = st.selectbox("Translate to", ['HINDI','MANDYALI','ENGLISH','GARHWALI'],)


# translating from Mandyali
if choose_from == "MANDYALI":
  # use selectbox for options to choose from
  option = st.selectbox('Enter The Word Here',CD['MN'])
  if translate_to == 'HINDI':
    if st.button("Show Translation"):
      translated_text = translator_M_H(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')
  elif translate_to == 'GARHWALI':
    if st.button("Show Translation"):
      translated_text = translator_M_G(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')
  elif translate_to == 'ENGLISH':
    if st.button("Show Translation"):
      translated_text = translator_M_E(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')


#for converting from hindi words
if choose_from == "HINDI":
  # use selectbox for options to choose from
  option = st.selectbox('Enter The Word Here',CD['HN'])
  if translate_to == 'ENGLISH':
    if st.button("Show Translation"):
      translated_text = translator_H_E(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')
  if translate_to == 'MANDYALI':
    if st.button("Show Translation"):
      translated_text = translator_H_M(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')
  if translate_to == 'GARHWALI':
    if st.button("Show Translation"):
      translated_text = translator_H_G(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')


# For converting from Gharwali
if choose_from == "GARHWALI":
  # use selectbox for options to choose from
  option = st.selectbox('Enter The Word Here',CD['GH'])
  if translate_to == 'HINDI':
    if st.button("Show Translation"):
      translated_text = translator_G_H(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')
  if translate_to == 'ENGLISH':
    if st.button("Show Translation"):
      translated_text = translator_G_E(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')
  if translate_to == 'MANDYALI':
    if st.button("Show Translation"):
      translated_text = translator_G_M(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')
  if translate_to == 'HINDI':
    if st.button("Show Translation"):
      translated_text = translator_G_H(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')


#for converting from ENGLISH words
if choose_from == "ENGLISH":
  # use selectbox for options to choose from
  option = st.selectbox('Enter The Word Here',CD['EN'])
  if translate_to == 'HINDI':
    if st.button("Show Translation"):
      translated_text = translator_E_H(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')
  if translate_to == 'MANDYALI':
    if st.button("Show Translation"):
      translated_text = translator_E_M(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')
  if translate_to == 'GARHWALI':
    if st.button("Show Translation"):
      translated_text = translator_E_G(str(option))

      st.write('  ')
      html_str = f"""
      <style>
      p.a {{
      font: bold {35}px Courier;
      }}
      </style>
      <p class="a">{translated_text}</p>
      """
      st.markdown(html_str, unsafe_allow_html=True)
      st.write('  ')