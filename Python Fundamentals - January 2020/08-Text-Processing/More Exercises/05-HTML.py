title_article = input()
content_article = input()
div_section = []
while True:
    div_comment = input()
    if div_comment == 'end of comments':
        print('<h1>')
        print(f'    {title_article}')
        print('</h1>')
        print('<article>')
        print(f'    {content_article}')
        print('</article>')
        for i in div_section:
            print('<div>')
            print(f'    {i}')
            print('</div>')
        exit()
    div_section.append(div_comment)