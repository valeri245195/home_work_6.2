import sys
from pathlib import Path
import scan




def main():
    path = Path(sys.argv[1])
    scan.sort_folder(path, path)

    print(f'unknown extensions: {scan.unknown}')
    print(f'known extensions:   {scan.extensions}')


if __name__ == '__main__':
    main()
