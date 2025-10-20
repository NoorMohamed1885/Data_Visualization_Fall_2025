import streamlit as st

st.title("👋 My Bio")

# ---------- TODO: Replace with your own info ----------
NAME = "Noor Mohamed"
PROGRAM = "Computer Science"
INTRO = (
    "I am a computer science student at Metropolitan State University of Denver.: I enjoy learning new things and understanding more about the world of computers., "
    "What excites me about data visualization is being able to make sense of data which at a first glance may look confusing."
)
FUN_FACTS = [
    "I love programming.",
    "I’m learning data visualization.",
    "I want to build a website.",
]
PHOTO_PATH = "photo.jpg"  # Put a file in repo root or set a URL

# ---------- Layout ----------
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    try:
        st.image(PHOTO_PATH, caption=NAME, use_container_width=True)
    except Exception:
        st.info("Add a photo named `your_photo.jpg` to the repo root, or change PHOTO_PATH.")
with col2:
    st.subheader(NAME)
    st.write(PROGRAM)
    st.write(INTRO)

st.markdown("### Fun facts")
for i, f in enumerate(FUN_FACTS, start=1):
    st.write(f"- {f}")

st.divider()
st.caption("Edit `pages/1_Bio.py` to customize this page.")
