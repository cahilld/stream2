pages = {
            'index.html': { 'template': 'templateB.html', 'tags': {'{title}': 'This is the Home page', '{heading}': 'Index Heading', '{body}': 'Index Body', '{footer}': 'Index Footer'}},
            'about.html': { 'template': 'template.html',  'tags': {'{title}': 'This is the About Us.html', '{heading}': 'About Us', '{body}': 'Once Upon a time there was us.', '{footer}': 'About Footer'}}
        }


for page, page_config in pages.items():
    
    with open(page_config['template'], "r+") as file:
        template_text = file.read()

    filedata = template_text
    for tag, text in page_config['tags'].items():
        filedata = filedata.replace(tag, text)
    
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

