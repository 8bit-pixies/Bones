import os
import markdown, jinja2

SOURCE = "./_posts"
DESTINATION = "./_site/"
TEMPLATE_PATH = "./templates/"
TEMPLATE_OPTIONS = {}
TEMPLATES = {
    'index': "index.html",
    'post': "post.html",
}

def get_tree(source):
    file_list = []
    for root, ds, fs in os.walk(source):
        for filename in fs:
            if filename[0] == ".": continue
            print '\t%s'% filename
            path = os.path.join(root,filename)
            f = open(path,'rU')
            category = f.readline().strip()
            tags = f.readline().strip()

            file_list.append({
                'category': category,
                'tags': [x.strip() for x in tags.split(',')],
                'filename': filename.split('.')[0],
                'title': ' '.join([x.title() for x in filename.split('.')[0].split('-')]),
                'content': markdown.markdown(''.join(f.readlines()[1:]).decode('UTF-8'))
            })
            f.close()

    return file_list

def write_file(url,data):
    path = DESTINATION + url
    dirs = os.path.dirname(path)
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
    file = open(path, "w")
    file.write(data.encode('UTF-8'))
    file.close()


def get_label(f):
    """only for category, must be a way to be refactored"""
    categories = {}
    for files in f:
        if not categories.__contains__(files['category']):
            categories[files['category']]=[]
        categories[files['category']].append({
            'filename':files['filename'],
            'title':files['title']
        })
        print files['filename']
    return categories

def get_tags(f):
    """only for tags, will see if i can get it refactored
        probably using classes
    """
    tags = {}
    for files in f:
        for t in files['tags']:
            if not tags.__contains__(t):
                tags[t]=[]
            tags[t].append({
                'filename':files['filename'],
                'title':files['title']
            })
    return tags


def generate_index(f, e):
    """generate index"""
    template = e.get_template(TEMPLATES['index'])
    print "\tindex.html"
    categories = get_label(f)
    print categories
    write_file("index.html", template.render(category=categories))

def generate_tags(f,e):
    """generate tags"""
    template = e.get_template(TEMPLATES['index'])
    print "\ttags.html"
    tags = get_tags(f)
    print tags
    write_file("tags.html",template.render(category=tags))

def generate_posts(f, e):
    """generate posts"""
    template = e.get_template(TEMPLATES['post'])
    for files in f:
        print "\t%s.html" % files['filename']
        write_file("%s.html" % files['filename'],
                template.render(files=files))

def main():
    print "\nFinding files in %s:" % SOURCE
    files = get_tree(SOURCE)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH), **TEMPLATE_OPTIONS)

    print "\nGenerating files:"
    generate_index(files,env)
    generate_tags(files,env)
    generate_posts(files,env)
    print '\n\n'


if __name__ == '__main__':
    main()

