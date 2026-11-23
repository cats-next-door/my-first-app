import streamlit as st

st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")

price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0, value=0.0)
sale = st.number_input("กรอกส่วนลด (%):", min_value=0.0, max_value=100.0, value=0.0)

discount = price * (sale / 100)
saleprice = price - discount
vat = saleprice * 0.07
netprice = saleprice + vat

showsale = sale
showsaleprice = discount
showvat = vat
shownet = netprice

st.divider()

st.write(f"• ส่วนลด ({showsale:.0f}%): -{showsaleprice:.2f} บาท")
st.write(f"• ราคาหลังหักส่วนลด: {saleprice:.2f} บาท")
st.write(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): +{showvat:.2f} บาท")
st.title(f"• ราคาสุทธิที่ต้องจ่าย: {shownet:.2f} บาท")

st.divider()

st.write("นายกลทีบ์ ประทุมทอง เลขที่ 18 ม.4/5")
