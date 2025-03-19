import aiohttp

async def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
