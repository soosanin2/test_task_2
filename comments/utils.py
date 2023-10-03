import bleach

def clean_html(html):
    allowed_tags = ['a', 'code', 'i', 'strong']  # Разрешенные теги
    cleaned_html = bleach.clean(html, tags=allowed_tags, attributes={})
    return cleaned_html