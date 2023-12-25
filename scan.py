from pathlib import Path
import normalize
import shutil


our_folders_list = ['images', 'video_files', 'documents', 'music', 'archives', 'others']

unknown = set()

extensions = set()

images = ['.jpeg', '.png', '.jpg', '.svg']
video_files = ['.avi', '.mp4', '.mov', '.mkv']
documents = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
music = ['.mp3', '.ogg', '.wav', '.amr']


archives = ['.zip', '.gz', '.tar']

dict_extension = {
    'images': images,
    'video_files': video_files,
    'documents': documents,
    'music': music,

}


def unpack(archive_path, new_archive_path):

    shutil.unpack_archive(archive_path, new_archive_path)


def move_file(root_path, path_file):
    print('3')
    name = path_file.stem
    suff = path_file.suffix
    category = ''

    name = normalize.normalize(name)
    name_of_file = name + suff
    print(name_of_file)
    category = 0
    for key, values in dict_extension.items():
        print(suff)
        if suff in values:
            category = key
            extensions.add(suff)
            print('3.1.1')
        if suff in archives:
            category = 'archives'
            nev_path_dir = Path(root_path / category)
            if not nev_path_dir.exists():
                print('3.2.1')
                nev_path_dir.mkdir()

                print('Папка успішно створена')
            name_of_file = name_of_file.removesuffix(suff)
            nev_path_dir_for_archive = Path(nev_path_dir / name_of_file)
            nev_path_dir_for_archive.mkdir()
            unpack(path_file, nev_path_dir_for_archive)
            path_file.unlink()
            return None

    if not category:
        category = 'others'
        unknown.add(suff)
        print('3.1.2')
    nev_path_dir = Path(root_path / category)
    print(nev_path_dir)

    if not nev_path_dir.exists():
        print('3.2.1')
        nev_path_dir.mkdir()

        print('Папка успішно створена')
    try:
        path_file.replace(nev_path_dir / name_of_file)
        print('Файл успішно перенесено!!!')

    except:
        print('перемещение не сработало')


def sort_folder(root_path, path):
    print('2')
    for item in path.iterdir():
        print('рекурсирую папки')
        print(item)
        if item.parts[-1] in our_folders_list:
            print('увидел нашу папку')
            continue

        elif item.is_dir():

            sort_folder(root_path, item)
            try:
                print('удаляю папки')

                item.rmdir()
                print('удалил!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            except FileNotFoundError:
                print('КРИТИЧЕСКАЯ ОШИБКА(Удалялка папок не работает)')
                pass
        elif item.is_file():
            move_file(root_path, item)
            print('ПОШЕЛ ДАЛЬШЕ')
