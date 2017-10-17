pages = {
            'index.html': {'{title}': 'This is the Home page', '{heading}': 'Index Heading', '{body}': 'Index Body', '{footer}': 'Index Footer'},
            'about.html': {'{title}': 'This is the About Us.html', '{heading}': 'About Us', '{body}': 'Once Upon a time there was us.', '{footer}': 'About Footer'}
        }


with open("template.html", "r+") as file:
    template_text = file.read()

for page, tags in pages.items():
    for tag, text in tags.items():
        filedata = template_text.replace(tag, text)
    
    with open(page, "w") as file:
        file.write(filedata)
    


# '{page}'
# 'index.html'
# 'about.html'

# '{title}'
# 'This is the Home page'
# 'This is the About Us page'

# '{heading}'
# 'Index Heading'
# 'About Us'

# '{body}'
# 'Index Body'
# 'Once Upon a time there was us.'

# '{footer}'
# 'Index Footer'
# 'About Footer'

