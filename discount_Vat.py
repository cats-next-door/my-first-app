import streamlit as st

st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")
price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0 , value=0.0)
sale = st.number_input("กรอกส่วนลด (%):", min_value=0.0 , max_value=100.0 , value=0.0)

discount = price * (sale / 100)
vat = price * 0.07
netprice = saleprice + vat

st.divider()

showsale = price - discount

st.write(f"• ส่วนลด ({sale}%): **-{showsale:.2f}** บาท")
st.write(f"• ราคาหลังหักส่วนลด: **{saleprice:.2f}** บาท")
