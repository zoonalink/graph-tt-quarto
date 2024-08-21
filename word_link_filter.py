from pandocfilters import toJSONFilter, Link, Str

def convert_links(key, value, format, meta):
    if key == 'Link' and format == 'docx':
        # Extract link text and target
        link_text, (link_target, link_title) = value

        # Check if the link target is a .qmd file
        if link_target.endswith('.qmd'):
            # Convert to cross-reference format
            new_target = '@' + link_target[:-4]  # Remove .qmd extension
            return Link(link_text, (new_target, link_title))

if __name__ == "__main__":
    toJSONFilter(convert_links)