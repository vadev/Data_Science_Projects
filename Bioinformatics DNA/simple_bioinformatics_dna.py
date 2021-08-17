import pandas as pd
import streamlit as st 
import altair as alt 


# Page title 
st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")

# Input text box
st.header("Enter DNA Sequence: ")

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height= 250) 
sequence = sequence[1:] # this will skip the seq. name (first line only)
sequence = ''.join(sequence) # concats list of strings 

st.write(""" 
*** 
""")

# Prints out the input DNA sequence. 
st.header("OUTPUT (DNA Nucleotide Count)")

# Prints dictionary
st.subheader('1. Print dictionary') 

def DNA_nucleotide_count(seq): 
    d = dict([

        ('A', seq.count('A')), 
        ('T', seq.count('T')), 
        ('G', seq.count('G')), 
        ('C', seq.count('C')), 

    ])
    return d


X = DNA_nucleotide_count(sequence)

# Print the text
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
 
# Display the DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df) 

# Display the bar chart using Altair library 
st.subheader('Display bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide', 
    y='count'
)
p = p.properties(width=alt.Step(80)) # it control the width of the bar 

st.write(p)