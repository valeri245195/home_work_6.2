from pathlib import Path
import normalize
import shutil


our_folders_list = ['images', 'video_files', 'documents', 'music', 'archives', 'others']

unknown = set()

extensions = set()

images = ['.jpeg', '.png', '.jpg', '.svg']
video_files = ['.avi', '.mp4', '.mov', '.mkv', 'aVI']
documents = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
music = ['.mp3', '.ogg', '.wav', '.amr']


archives = ['.zip', '.gz', '.tar']

dict_extension = {
    'images': images,
    'video_files': video_files,
    'documents': documents,
    'music': music,

}
#s

def unpack(archive_path, new_archive_path):

    shutil.unpack_archive(archive_path, new_archive_path)


def move_file(root_path, path_file):

    name = path_file.stem
    suff = path_file.suffix
    category = ''

    name = normalize.normalize(name)
    name_of_file = name + suff.replace('.', '')

    category = 0
    for key, values in dict_extension.items():

        if suff.lower() in values:
            category = key
            extensions.add(suff)

        if suff.lower() in archives:
            category = 'archives'
            nev_path_dir = Path(root_path / category)
            if not nev_path_dir.exists():

                nev_path_dir.mkdir()

            name_of_file = name_of_file.removesuffix(suff)
            nev_path_dir_for_archive = Path(nev_path_dir / name_of_file)
            nev_path_dir_for_archive.mkdir()
            try:
                unpack(path_file, nev_path_dir_for_archive)

            except:
                nev_path_dir.unlink()

            path_file.unlink()
            return None

    if not category:
        category = 'others'
        unknown.add(suff)

    nev_path_dir = Path(root_path / category)


    if not nev_path_dir.exists():

        nev_path_dir.mkdir()


    try:
        path_file.replace(nev_path_dir / name_of_file)

    except:
        x = None

def sort_folder(root_path, path):

    for item in path.iterdir():

        if item.parts[-1] in our_folders_list:

            continue

        elif item.is_dir():

            sort_folder(root_path, item)
            try:


                item.rmdir()

            except FileNotFoundError:

                pass
        elif item.is_file():
            move_file(root_path, item)

