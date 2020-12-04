import wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia('en')
page = wiki_wiki.page('International_crisis')

def print_sections(sections, level=0):
    i=0
    for s in sections:
        i = i+1
        if i == 4:
         print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:5000]))
         print_sections(s.sections, level + 1)

print_sections(page.sections)