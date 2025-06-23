import re

s = """
<p>Everybode<p>
<p>Everybode<p>
<p>Everybode<p>
<p>Everybode<p>
<p>Everybode<p>
<p>Everybode<p>
"""

print(
    re.findall("<p>(.*?)<p>", s)
)  # ['Everybode', 'Everybode', 'Everybode', 'Everybode', 'Everybode', 'Everybode']
print(
    re.search("<p>(.*?)<p>", s)
)  # <re.Match object; span=(1, 16), match='<p>Everybode<p>'>
print(re.search("<p>(.*?)<p>", s).span(0))  # (1, 16) индексы первого вхождения
print(re.search("<p>(.*?)<p>", s).group(0))  # <p>Everybode<p>
print(re.split("<p>\n<p>", s))  # <p>Everybode<p>
print(re.sub("<p>(.*?)<p>", "слово -- \g<1> -- оволс", s))
"""
слово -- Everybode -- оволс
слово -- Everybode -- оволс
слово -- Everybode -- оволс
слово -- Everybode -- оволс
слово -- Everybode -- оволс
слово -- Everybode -- оволс
"""
