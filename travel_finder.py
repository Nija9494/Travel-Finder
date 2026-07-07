import streamlit as st

st.set_page_config(page_title="AI TRAVEL FINDER", page_icon="🌍", layout="wide")

st.title("🌍 AI TRAVEL FINDER")
st.write("Tell me your mood : **adventure,peace,beach,hills,historical**")

# https://loremflickr.com/
# https://loremflickr.com/WIDTH/HEIGHT/KEYWORD1,KEYWORD2
# FREE , OPEN SOURCE , NO API KEY , IMG , ST.IMAGE

places = {
    "adventure": {
        "place": "Ladakh",
        "desc": "🏔️ Perfect for travelling , riding and beautiful lakes",
        "images": [
            "https://loremflickr.com/500/300/ladakh,travel",
            "https://loremflickr.com/500/300/ladakh,lakes"
        ],
        "video_search": "Ladakh travel guide 2025"
    },

    "peace": {
        "place": "Rishikesh",
        "desc": "🧘 Calm place for yoga , meditation and riverside",
        "images": [
            "https://loremflickr.com/500/300/Rishikesh,ganga",
            "https://loremflickr.com/500/300/laxman,jhula,rishikesh"
        ],
        "video_search": "Rishikesh travel guide 2025"
    },

    "beach": {
        "place": "Goa",
        "desc": "🏖️ Enjoy Beaches,nightlife , water sports and seafood",
        "images": [
            "https://loremflickr.com/500/300/goa_beach,india",
            "https://loremflickr.com/500/300/casino,goa"
        ],
        "video_search": "Goa travel guide 2025"
    },

    "hills": {
        "place": "Manali",
        "desc": "🏔️ Best For Trekking, snow",
        "images": [
            "https://loremflickr.com/500/300/manali,hills",
            "https://loremflickr.com/500/300/chandratal,lake,manali"
        ],
        "video_search": "Manali Travel guide 2025"
    },

    "historical": {
        "place": "Jaipur",
        "desc": "🏰 Forts,palaces and royal pink city",
        "images": [
            "https://loremflickr.com/500/300/jaipur,fort",
            "https://loremflickr.com/500/300/amber,fort,jaipur"
        ],
        "video_search": "Jaipur travel guide 2025"
    }
}

# query
query = st.chat_input("Where do you want to go? (e.g. I want adventure)")

if query:
    q = query.lower()

    for mood in places:
        if mood in q:
            data = places[mood]

            st.subheader(f"📍 Recommended Place : {data['place']}")
            st.info(data["desc"])

            # photos
            cols = st.columns(2)
            for i, img_url in enumerate(data["images"]):
                cols[i].image(img_url, use_container_width=True)

            # video
            st.subheader("🎥 Travel Video")
            yt_url = f"https://www.youtube.com/results?search_query={data['video_search'].replace(' ', '+')}"
            st.link_button("▶️ Watch From here", yt_url)

            # map
            st.subheader("📍 Location")
            st.components.v1.iframe(
                f"https://maps.google.com/maps?q={data['place']}&t=&z=12&ie=UTF8&iwloc=&output=embed",
                height=500
            )

            break
    else:
        st.warning("😅 Try Typing : **adventure,hills,beach,peace,historical**")