# Bones

**Chapman Siu**

Static wiki webpage generator. Heavily influenced by [chisel](https://github.com/dz/chisel)

# Usage

$ python bones.py

# Sample Entry

sample.markdown:

	---
	category : category1
	tags : tag1,tag2
	---
	
	Markdown Content here.

# Settings 

Change these settings:

### SOURCE:
Location of source files for entries
Must end in slash.  
Example: SOURCE = "./_post/" 

### DESTINATION:
Location to place generated files.
Must end in slash.
Example: DESTINATION = "./_site/"

### TEMPLATE_PATH:
Path to folder where tempaltes live.
Must end in slash.
Example: TEMPLATE_PATH = "./templates/" 

### TEMPLATE_OPTIONS:
Dictionary of options to give jinja2.
Default: TEMPLATE_OPTIONS = {}

### TEMPLATES:
Dictionary of templates.  
Required keys: 'index', 'post'.
Example: 

    TEMPLATES = {
        'index': "index.html",
        'post': "post.html",
    }
