import requests
import zipfile
import os
import shutil
import glob

# URLs, filename
dir = "./temp/"
minecraft = os.getenv("appdata") + '/.minecraft/'
resourcepack = minecraft + '/resourcepacks'

mods_url = "mods.zip"
resource_url = "resource.zip"

url_list = [resource_url, mods_url]
file_extension = '.jar'


def download_file(url):
    filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        return filename


def main():

    print("Downloading requirements files\nwait a sec...\n ")
    for u in url_list:
        filename = download_file(u)
        if filename:
            print('{} is downloaded.\n'.format(filename))

    print("Download complete!\n")
    print("unzipping mods.zip...")

    if os.path.exists(dir):
        shutil.rmtree(dir)

    os.mkdir(dir)
    with zipfile.ZipFile(filename) as obj_zip:
        obj_zip.extractall(dir)

    print("Complete unzipping mods.zip\n")
    print("moving mods...")

    if not os.path.exists(minecraft+'/mods/'):
        shutil.move(dir+'/mods/', minecraft+'/mods/')
    else:
        mod_path = glob.glob('temp/mods/*.jar')
        for i in mod_path:
            print(str(i))
            shutil.move(str(i), str(minecraft+'/mods/'+os.path.basename(i)))
    print("Success!\n")

    print("Copying resourcepack...")
    print(resourcepack)
    if not os.path.exists(resourcepack):
        os.mkdir(resourcepack)

    shutil.move(os.path.basename(resource_url),
                resourcepack + os.path.basename(resource_url))

    print("Success!")


if __name__ == '__main__':
    main()
    while True:
        key = input('Press Enter to exit...')
        if not key:
            break
