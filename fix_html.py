import os

for f in os.listdir('.'):
    if not f.endswith('.html'): continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the bulletproof nav script
    if '<!-- BULLETPROOF NAV' in content:
        start = content.find('<!-- BULLETPROOF NAV')
        end = content.find('</script>', start) + 9
        content = content[:start] + content[end:]
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Fixed {f}")
