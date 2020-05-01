import os
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.dirname(CURRENT_PATH)

def main():
    os.chdir(BASE_PATH)
    
    for item in os.listdir():
        if os.path.isdir(item):
            os.chdir(os.path.abspath(item))

            total_files = len(os.listdir())
            if total_files > 2:
                print(f"dir {item} has {total_files} files -- check quality.")

            os.chdir(BASE_PATH)



if __name__ == '__main__':
    main()
