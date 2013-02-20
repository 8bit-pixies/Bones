# Bones

**Chapman Siu**

Static wiki webpage generator. Heavily influenced by [chisel](https://github.com/dz/chisel)

# Usage

$ python bones.py

# Sample Entry

sample.markdown:

> 	First Line is the Wiki's Category  
> 	(a blank line separates Category from post body)
>   This is the body of the post. It will be evaluated with `markdown`

# Settings 

Change these settings:

### SOURCE:
Location of source files for entries
Must end in slash.  
Example: SOURCE = "./blog/" 

### DESTINATION:
Location to place generated files.
Must end in slash.
Example: DESTINATION = "./explort/"

### HOME_SHOW:
Number of entries to show on homepage
Example: HOME_SHOW = 15

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
