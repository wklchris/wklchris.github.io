import os, re
import shutil
import datetime
import clipboard

today = datetime.datetime.today()
today = '{}-{:0>2d}-{:0>2d}'.format(today.year, today.month, today.day)
fname = input("Input the file name (DO NOT include '.ipynb'):")

thepath = os.getcwd()
ipynb_path = os.path.join(thepath, 'ipynb')
ipynb_image_path = os.path.join(ipynb_path, r'{}_files'.format(fname))
destination_path = os.path.join(thepath, r'assets/ipynb-images')
post_path = os.path.join(thepath, r'_posts/{}.md').format(today + '-' + fname)

# Convert ipynb to markdown; 
os.system('jupyter nbconvert --to markdown ipynb/{}.ipynb'.format(fname))
# Move it to "/_posts" and renameit
shutil.move(os.path.join(ipynb_path, '{}.md'.format(fname)), os.path.join(thepath, r'_posts/{}.md').format(fname))
if os.path.isfile(post_path):
    os.remove(post_path)
os.rename(os.path.join(thepath, r'_posts/{}.md').format(fname), post_path)

# Move the images under "/ipynb/<fname>_files" to "/assets/ipynb-images"
def moveallfiles(origindir, destinationdir):
    for file in os.listdir(origindir):
        originfile = os.path.join(origindir, file)
        destinationfile = os.path.join(destinationdir, file)
        # If it exists, then delete it and then conduct the movement
        if os.path.isfile(destinationfile):
            os.remove(destinationfile)
        shutil.move(originfile, destinationfile)

moveallfiles(ipynb_image_path, destination_path)
# Delete the origin image path
shutil.rmtree(ipynb_image_path)

# Replace the image link strings
headstr  = '---\n'
headstr += 'layout: post\n'
headstr += 'title: 怎样用 Github Pages 建立博客（3. 绘图/科学计算）\n'
headstr += 'category: Jekylln\n'
headstr += 'tag: 搭建博客\n'
headstr += '---\n\n'

with open(post_path, 'r', encoding='utf8') as f:
    fstr = f.read()

fstr = re.compile(r'{}_files'.format(fname)).sub(r'https://wklchris.github.io/assets/ipynb-images', fstr)
fstr = headstr + fstr

os.remove(post_path)
with open(post_path, 'w', encoding='utf8') as f:
    f.write(fstr)

