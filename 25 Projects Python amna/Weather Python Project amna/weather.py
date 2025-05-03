import streamlit as st
import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    
    st.write("🔗 URL Used:", url)
    st.write("📦 Status Code:", response.status_code)
    st.write("📄 Raw Response:", response.text)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Condition": data["weather"][0]["description"].title(),
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Wind Speed (m/s)": data["wind"]["speed"]
        }
        return weather
    else:
        return None

def main():
    st.set_page_config(page_title="Weather App 🌤️", page_icon="⛅", layout="centered")
    st.title("🌍 Live Weather Checker")
    st.markdown("Showing weather for **Karachi** using OpenWeatherMap API.")

    # Predefined city and API key
    city = "Karachi"
    api_key = "a8713db04cb4a8502d0ba857eba1ffe5"

    if st.button("Get Weather"):
        with st.spinner("Fetching weather..."):
            weather_data = get_weather(city, api_key)
        if weather_data:
            st.success(f"Weather details for {city.title()}:")
            st.json(weather_data)
        else:
            st.error("City not found or invalid API key!")

if __name__ == "__main__":
    main()
