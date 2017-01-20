import os, re
import shutil

# Add Jekyll head strings

fname = "R-clustering"
date = "2017-01-18"

headstr  = '---\n'
headstr += 'layout: post\n'
headstr += 'title: R语言学习与速查（聚类）\n'
headstr += 'category: R\n'
headstr += 'tag: R-learning\n'
headstr += '---\n\n'


# Main
thepath = os.getcwd()
ipynb_path = os.path.join(thepath, 'ipynb')
ipynb_image_path = os.path.join(ipynb_path, r'{}_files'.format(fname))
destination_path = os.path.join(os.path.join(thepath, 'assets'), 'ipynb-images')
post_path = os.path.join(thepath, r'_posts/{}.md').format(date + '-' + fname)

# Convert ipynb to markdown; 
os.system('jupyter nbconvert --to markdown ipynb/{}.ipynb'.format(fname))
# Move it to "/_posts" and renameit
shutil.move(os.path.join(ipynb_path, '{}.md'.format(fname)), os.path.join(thepath, r'_posts/{}.md').format(fname))
if os.path.isfile(post_path):
    os.remove(post_path)
os.rename(os.path.join(thepath, r'_posts/{}.md').format(fname), post_path)

# Move the images under "/ipynb/<fname>_files" to "/assets/ipynb-images"
def moveallfiles(origindir, destinationdir):
    if not os.path.exists(origindir):
        return
    for file in os.listdir(origindir):
        originfile = os.path.join(origindir, file)
        destinationfile = os.path.join(destinationdir, file)
        # If it exists, then delete it and then conduct the movement
        if os.path.isfile(destinationfile):
            os.remove(destinationfile)
        shutil.move(originfile, destinationfile)
    # Delete the origin image path
    shutil.rmtree(ipynb_image_path)

moveallfiles(ipynb_image_path, destination_path)

with open(post_path, 'r', encoding='utf8') as f:
    fstr = f.read()

# Replace the image link strings
fstr = re.compile(r'{}_files'.format(fname)).sub(r'https://wklchris.github.io/assets/ipynb-images', fstr)
fstr = headstr + fstr

# Convert HTML table to markdown table
def transfertable(tablehtml):
    tablehtml = re.compile(r'<table>').sub('', tablehtml)
    tablehtml = re.compile(r'</tbody>[\n]</table>').sub('', tablehtml)

    # Table head
    tablehtml = re.compile(r'<tr><th>').sub(r'#', tablehtml)
    tablehead = re.compile(r'<thead>[\S\s]*?</thead>').findall(tablehtml)
    tablehead = tablehead[0]
    # Headline
    col_num = len(re.compile(r'</th>').findall(tablehead))
    tablehtml = re.compile(r'<tbody>').sub('|' + ' --- |' * col_num, tablehtml)

    headcontent = re.compile(r'(?<=>)[\S]*?(?=</th>)').findall(tablehead)
    newhead = '| ' + ' | '.join(headcontent) + ' |'
    tablehtml = re.compile(tablehead).sub(newhead, tablehtml)

    # First column
    firstcol = re.compile(r'(?<=\s)<tr>[\S\s]*?<td>').findall(tablehtml)
    for cell in firstcol:
        origincell = cell
        cell = re.compile(r'<tr><th[^>]*?>').sub('| **', cell)
        cell = re.compile(r'</th><td>').sub('** | ', cell)
        tablehtml = re.compile('\t' + origincell).sub(cell, tablehtml)

    # Table body
    tablehtml = re.compile(r'<tr><td>').sub('| ', tablehtml)
    tablehtml = re.compile(r'</td></tr>').sub(' |', tablehtml)
    tablehtml = re.compile(r'</th><td>').sub(' | ', tablehtml)
    tablehtml = re.compile(r'</td><td>').sub(' | ', tablehtml)

    return tablehtml

tablehtmllst = re.compile(r'<table>[\s\S]*?</table>').findall(fstr)
if tablehtmllst:
    for table in tablehtmllst:
        fstr = re.compile(table).sub(transfertable(table), fstr)

os.remove(post_path)
with open(post_path, 'w', encoding='utf8') as f:
    f.write(fstr)

