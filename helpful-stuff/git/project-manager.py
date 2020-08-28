def main():
    import os
    folder = input("Where do you want me to watch: ")
    settings_dir_exists = os.path.exists('{}'.format(f"{folder}/settings/"))

    if folder != "":
        if settings_dir_exists:
            os.system("cls")
            configuration = open(f'{folder}/settings/configurations.txt', 'r')
            content = configuration.readlines()
            git_repository_published_line = content[0].strip()
            process1 = git_repository_published_line.split("=")
            final_git_repository_published = process1[1]

            if final_git_repository_published == "True":
                watch_published(configuration, folder)
            else:
                pass

        elif not settings_dir_exists:
            print("No settings found")
            print("Going through quick-setup of the configurations, please endure ...")

def watch_published(conf, settings_dir="./"):
    import time
    import os
    print("Watching the repository")
    while True:
        settings_folder = os.path.exists(''.format(f"{settings_dir}/settings/"))
        if settings_folder:
            print("Refreshing github repository content (branch=master)")
            remote_name = open(f'{settings_dir}/settings/configurations.txt')
            content = remote_name.readlines()
            print(content)
        elif not settings_folder:
            pass

main()
