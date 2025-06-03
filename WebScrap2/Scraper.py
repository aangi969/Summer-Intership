from bs4 import BeautifulSoup

# Load local HTML file
with open('sample_news.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all('a', class_='storylink')

print("Top Headlines from Local HTML:")
for i, title in enumerate(titles, start=1):
    print(f"{i}. {title.text}")
