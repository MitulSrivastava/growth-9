
import os
import re

files_to_process = [
    "loans.html",
    "business.html",
    "migsun-nehru-detail.html",
    "tech.html",
    "import-export.html",
    "investors.html",
    "terms.html",
    "disclaimer.html",
    "register-idea.html",
    "documents.html",
    "commercial-showroom-detail.html",
    "contact.html",
    "property.html",
    "colony-plots-detail.html",
    "agricultural-land-detail.html",
    "property-list.html",
    "index.html"
]

base_dir = "/Users/mitulsrivastava/Desktop/9 growth"

# Regex to match the phone number paragraph in the footer
# Matches <p class="mb-1"> ... <i ...></i> +91 87918 86474 ... </p>
# allowing for whitespace and newlines
pattern = r'<p\s+class="mb-1">\s*<i\s+class="fas\s+fa-phone\s+me-2">\s*</i>\s*\+91\s*87918\s*86474\s*</p>'

for filename in files_to_process:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Search and replace
    # re.DOTALL is not needed if we handle newlines in the pattern using \s*
    # However, to be safe with multiline matching
    new_content = re.sub(pattern, "", content, flags=re.DOTALL)
    
    if new_content != content:
        print(f"Updating {filename}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        print(f"No match found in {filename}")

