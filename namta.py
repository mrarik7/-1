import streamlit as st
st.header('এইখানে যেকোনো নাম্বার দিলে ১০ পর্যন্ত তার নামতা বের হবে :)')
a = st.text_input('এইখানে আপনার নাম্বার টি দেনঃ')
if a :
    a=int(a)
if a:
    st.text(f'{a} এর নামতা নিম্নরুপঃ')
    b=0
    while b<=9:
        b=b+1
        c=a*b
        st.text(f'{a}   X   {b}   =   {c}')




st.text('made by')
st.text('-mr.arik7')

