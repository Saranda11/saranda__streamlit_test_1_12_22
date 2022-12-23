
#1
import streamlit as st
input_txt = st.text_input("Enter the string: ")
#2: Declare a function called “convert_list”  that takes this string..

def convert_list(input_txt):
    str_list = str.split(input_txt)
    return str_list
list = convert_list(input_txt)
list_elements = st.button("Return List")
if list_elements:
    st.write(list)

#3:  Declare another function called “convert_lower”...

def convert_lower(list):
    listt = []
    for element in list:
        listt.append(element.upper())
    return listt
listt = convert_lower(list)
upper_elements = st.button("upper")
if upper_elements:
    st.write(listt)

#4: Declare a function called ‘count” that returns the number of elements in the list ..
def count(list):
    count = 0
    for element in list:
        count += 1
    return count
count_elements = st.button("Print")
length = count(list)
if count_elements:
    st.write("This list has " + str(length) + " elements.")