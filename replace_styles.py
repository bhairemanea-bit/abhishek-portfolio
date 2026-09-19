import re

files = ['about.html', 'work.html', 'skills.html', 'contact.html']

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # regex replace style
        content = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="src/styles/secondary.css">', content, flags=re.DOTALL)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Styles replaced in {f}")
    except Exception as e:
        print(f"Error on {f}: {e}")
