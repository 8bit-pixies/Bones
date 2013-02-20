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
    category_list = {}
    for root, ds, fs in os.walk(source):
        for filename in fs:
            if filename[0] == ".": continue
            print '\t%s'% filename
            path = os.path.join(root,filename)
            f = open(path,'rU')
            category = f.readline().strip()
            if not category_list.__contains__(category):
                category_list[category]=[]
            category_list[category].append({
                'filename': filename.split('.')[0],
                'title': ' '.join([x.title() for x in filename.split('.')[0].split('-')]),
                'content': markdown.markdown(''.join(f.readlines()[1:]).decode('UTF-8'))
            })
            f.close()

    return category_list

def write_file(url,data):
    path = DESTINATION + url
    dirs = os.path.dirname(path)
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
    file = open(path, "w")
    file.write(data.encode('UTF-8'))
    file.close()


def generate_index(f, e):
    """generate index"""
    template = e.get_template(TEMPLATES['index'])
    print "\tindex.html"
    write_file("index.html", template.render(category=f))

def generate_posts(f, e):
    """generate posts"""
    template = e.get_template(TEMPLATES['post'])
    for files in f:
        for posts in f[files]:
            print "\t%s.html" % posts['filename']
            write_file("%s.html" % posts['filename'],
                    template.render(content=posts['content'],
                                    title=posts['title']))

def main():
    print "\nFinding files in %s:" % SOURCE
    files = get_tree(SOURCE)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH), **TEMPLATE_OPTIONS)

    print "\nGenerating files:"
    generate_index(files,env)
    generate_posts(files,env)

if __name__ == '__main__':
    main()
