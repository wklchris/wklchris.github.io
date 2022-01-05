import os, shutil

def external_run(os_cmd):
    print(f"\n--- Running: {os_cmd}")
    errcode = os.system(os_cmd)
    if errcode > 0:
        exit()
    print(f"--- Complete: {os_cmd}")

def copy_dir(dir_src, dir_des, delete_src=False):
    """Overwrite/create the dir_des from the dir_src."""
    if os.path.isdir(dir_des):
        shutil.rmtree(dir_des)
    shutil.copytree(dir_src, dir_des)
    if delete_src:
        shutil.rmtree(dir_src)

def main(dir_src, dir_serve, char_enc='utf-8'):
    docsrc = os.path.join(dir_src)
    docs = os.path.join(dir_serve)
    build_tmp_dir = os.path.join(docsrc, "_build")
    if os.path.isdir(build_tmp_dir):
        shutil.rmtree(build_tmp_dir)
    
    # Build to HTML
    build_cmd = f'sphinx-build -M html {docsrc} {build_tmp_dir}'
    external_run(build_cmd)
    # Copy (Overwrite if exists!) build_tmp_dir to docs
    build_html_dir = os.path.join(build_tmp_dir, "html")
    copy_dir(build_html_dir, docs)

    # Github Pages will be hosted at docs
    ## Create a .nojekyll for Github Pages
    nojekyll = os.path.join(docs, ".nojekyll")
    if not os.path.exists(nojekyll):
        with open(nojekyll, 'w', encoding=char_enc):
            pass


# --- Main ---

dir_src = 'docsrc'
dir_serve = 'docs'

main(dir_src, dir_serve)
