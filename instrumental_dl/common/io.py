import os

from ..errors import UnknownExtensionError


def get_songs_txt(file_name: str):
    """
    Opens up the provided text file to retrieve a list of all
    the instrumentals that are going to be downloaded.

    :param file_name: The name of the file that contains
                      a list of all the instrumentals to be downloaded.
    :return: song_names: A list of the names of all of the instrumentals
                         to be downloaded.
    """
    with open(file_name, "r") as file:
        song_names = [song.rstrip('\n') for song in file]
    return song_names


def rename_all_files(logger, file_names: list):
    """
    Renames all downloaded instrumentals to remove any unneeded
    keywords in the file name.

    :param logger: The main logger for this program
    :param file_names: A list of the names of all the downloaded files.
                       file_names do not need to have .mp3 as their extension
                       when passed through.
    """
    # Move to output directory
    os.chdir(os.getcwd() + '/../output')
    keywords = _get_keywords()

    for i in range(len(file_names)):
        # Replaces extension in file_name(not actual file name) to .mp3
        if file_names[i][-5:] == '.webm':
            file_names[i] = file_names[i].replace('.webm', '.mp3')
        elif file_names[i][-4:] == '.m4a':
            file_names[i] = file_names[i].replace('.m4a', '.mp3')
        else:
            raise UnknownExtensionError(logger, file_names[i])

        # Removes any unneeded keywords in actual file name
        for keyword in keywords:
            if keyword in file_names[i].lower():
                try:
                    new_file_name = file_names[i].lower().replace(keyword, '').capitalize()
                    os.rename(file_names[i], new_file_name)
                    file_names[i] = new_file_name
                except FileNotFoundError:
                    _file_error(logger, file_names[i])

        # Removes unneeded space at the end of file name
        while file_names[i][-5] == ' ' or file_names[i][-5] == '-':
            try:
                new_file_name = file_names[i][:-5] + '.mp3'
                os.rename(file_names[i], new_file_name)
                file_names[i] = new_file_name
            except FileNotFoundError:
                _file_error(logger, file_names[i])


def _file_error(logger, file_name):
    """Handles FileNotFoundErrors"""
    msg = "Error:", file_name, "not found."
    logger.error(msg)
    print(msg)


def _get_keywords():
    """
    Opens keywords.txt and retrieves all the keywords to
    remove from file names.

    :return: keywords: A list of all the keywords to remove
                       file names.
    """
    keywords = []
    with open('../config/keywords.txt', 'r') as file:
        for keyword in file:
            keywords.append(keyword.rstrip('\n'))

    return keywords