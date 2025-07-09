import streamlit as st
import random
from fpdf import FPDF
from io import BytesIO

st.set_page_config(page_title="PackSmart", page_icon="🧳")
st.title("🧳 PackSmart – AI-Based Travel Luggage Planner")
st.markdown("### Plan smart. Pack smarter. Suggests what to pack based on your trip!")

# Packing rules
packing_rules = {
    ('Goa', 'Beach', 'Hot'): ['Shorts', 'T-Shirts', 'Flip-Flops', 'Sunglasses', 'Sunscreen'],
    ('Manali', 'Hiking', 'Cold'): ['Jacket', 'Trekking Shoes', 'Thermals', 'Gloves', 'Woolen Cap'],
    ('Delhi', 'Business', 'Moderate'): ['Formal Shirt', 'Shoes', 'Laptop', 'ID Card'],
    ('Mysore', 'Wedding', 'Warm'): ['Saree / Kurti', 'Jewelry', 'Sandals', 'Moisturizer']
}

# Emoji mapping
emoji_map = {
    'Sunglasses': '🕶️',
    'Sunscreen': '🧴',
    'Shorts': '🩳',
    'Flip-Flops': '🩴',
    'Jacket': '🧥',
    'Laptop': '💻',
    'Jewelry': '💍',
    'Shoes': '👞',
    'Gloves': '🧤',
    'Sandals': '🥿',
    'T-Shirts': '👕',
    'Moisturizer': '🧴',
    'ID Card': '🪪',
    'Thermals': '🧦',
    'Trekking Shoes': '🥾',
    'Saree / Kurti': '👗',
    'Woolen Cap': '🧢',
    'Formal Shirt': '👔'
}

# User Inputs
destination = st.selectbox("📍 Select Destination", ['Goa', 'Manali', 'Delhi', 'Mysore'])
trip_type = st.selectbox("🎯 Trip Type", ['Beach', 'Hiking', 'Business', 'Wedding'])
weather = st.selectbox("☁️ Weather", ['Hot', 'Cold', 'Moderate', 'Warm'])
days = st.slider("🗓️ Trip Duration (in Days)", 1, 14)

# Destination Tips
if destination == "Goa":
    st.markdown("### 🌊 Goa – Beach vibes & sunsets!")
    st.success("☀️ Tip: Don't forget your sunglasses and sunscreen!")

elif destination == "Manali":
    st.markdown("### ❄️ Manali – Chilling in the Himalayan heights!")
    st.info("🧥 Tip: Thermals and gloves are must-haves in the snow!")

elif destination == "Delhi":
    st.markdown("### 🏙️ Delhi – The capital with a royal twist!")
    st.warning("🪪 Tip: Carry your ID for entry into heritage sites.")

elif destination == "Mysore":
    st.markdown("### 🎉 Mysore – Tradition, temples & silk sarees!")
    st.success("💡 Tip: Mysore Palace looks best at night when lit!")

# Packing Suggestion
items = []
if st.button("🎒 Show My Packing List"):
    key = (destination, trip_type, weather)
    if key in packing_rules:
        items = packing_rules[key]
    else:
        all_items = sum(packing_rules.values(), [])
        items = random.sample(all_items, 4)

    st.success("✅ Recommended Packing List:")
    for item in items:
        emoji = emoji_map.get(item, '')
        st.markdown(f"• {item} {emoji}")

# Generate PDF in-memory
def generate_pdf(items):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Your Travel Packing List", ln=True, align='C')
    pdf.ln(10)
    for item in items:
        emoji = emoji_map.get(item, '')
        pdf.cell(200, 10, txt=f"- {item} {emoji}", ln=True)
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output

# Show Download Button
if items:
    pdf_data = generate_pdf(items)
    st.download_button(
        label="📄 Download Packing List as PDF",
        data=pdf_data,
        file_name="Packing_List.pdf",
        mime="application/pdf"
    )
