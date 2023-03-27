import os
import os.path
import re
import sys
import json
import functools
import argparse

from typing import Union


@functools.lru_cache
def disks() -> dict[str, str]:
    with open(os.path.join(os.path.dirname(__file__), 'disks')) as file:
        return json.load(file)


class MediaItem:
    def __init__(self, path, **kw):
        self.path = path
        self.disk = kw.get('disk', self.get_disk(self.path))
        self.is_valid = kw.get('is_valid', True)
        self.title = os.path.basename(path)

        self.year = None
        self.quality = None

        self.is_movie = kw.get('is_movie', False)
        self.in_directors = kw.get('in_directors', False)
        self.director_name = kw.get('director_name', None)

        self.is_movie_series = kw.get('is_movie_series', False)
        self.movie_series_title = kw.get('movie_series_title', False)

        self.is_tv_series = kw.get('is_tv_series', False)
        self.tv_series_title = kw.get('tv_series_title', None)
        self.number_of_seasons = kw.get('number_of_seasons', None)

        self.is_comedy = kw.get('is_comedy', False)
        self.comedian = kw.get('comedian', None)

        self.files = list()

        # self.parse_path()

        if self.disk is None:
            self.is_valid = False

    def gather_files(self) -> list:
        files = list()
        for _, _, _files in os.walk(self.path):
            files.extend(_files)
        return files

    @classmethod
    def get_disk(cls, path: str) -> Union[str, None]:
        for disk in disks():
            if path.startswith(disk):
                return disk
        return None

    def parse_path(self):
        # Extract title, year, and quality from path
        match = re.match(r'(\d{4}) - (.+) - (.+)', os.path.basename(self.path))
        if match:
            self.year = match.group(1)
            self.title = match.group(2)
            self.quality = match.group(3)
        else:
            self.is_valid = False

        # Check if item is a movie or a TV series
        if 'TV Series' in self.path:
            self.is_series = True
            self.is_season = 'Season' in os.path.basename(os.path.dirname(self.path))
            if self.is_season:
                self.season_number = int(os.path.basename(self.path).replace('Season', ''))
                self.series_title = os.path.basename(os.path.dirname(os.path.dirname(self.path)))
            else:
                self.series_title = os.path.basename(self.path)
        elif 'Stand-Up Comedy' in self.path:
            self.is_comedy = True
            self.director_name = os.path.basename(self.path)
        else:
            self.is_movie = True
            if 'Directors' in self.path:
                self.is_director = True
                self.director_name = os.path.basename(self.path)
            else:
                match = re.match(r'^(\d{4})s', os.path.basename(self.path))
                if match:
                    self.year = match.group(1)

    def __str__(self):
        # return f"{self.path}:\n" \
        #        f"\tvalid: {self.is_valid}\n" \
        #        f"\ttitle: {self.title}\n" \
        #        f"\tyear: {self.year}\n" \
        #        f"\tquality: {self.quality}\n" \
        #        f"\tis_series: {self.is_series}\n" \
        #        f"\tis_comedy: {self.is_comedy}\n" \
        #        f"\tis_movie: {self.is_movie}\n" \
        #        f"\tis_director: {self.is_director}\n" \
        #        f"\tis_season: {self.is_season}\n" \
        #        f"\tseries_title: {self.series_title}\n" \
        #        f"\tseason_number: {self.season_number}\n" \
        #        f"\tdirector_name: {self.director_name}\n"
        return self.title

    def __repr__(self):
        return str(self)


class MediaCollection:
    def __init__(self, paths):
        self.media_items = []
        self.parse_paths(paths)

    def parse_paths(self, paths: dict):
        # todo: error: FileNotFoundError: No such file or directory: e.g. silicon power
        for disk, path in paths.items():
            if not os.path.exists(path) or not os.listdir(path):
                continue
            # todo: before traversing, check if an item is a file or a directory.
            if 'Movies' in os.listdir(path):
                movies_dir = os.path.join(path, 'Movies')
                if 'Directors' in os.listdir(movies_dir):
                    directors_dir = os.path.join(movies_dir, 'Directors')
                    for director in os.listdir(directors_dir):
                        director_dir = os.path.join(directors_dir, director)
                        if not os.path.isdir(director_dir):
                            print(f'report: {director_dir}')
                            continue
                        for movie in os.listdir(director_dir):
                            movie_dir = os.path.join(director_dir, movie)
                            if not os.path.isdir(movie_dir):
                                print(f'report: {movie_dir}')
                                continue
                            self.media_items.append(
                                MediaItem(movie_dir, disk=disk, is_movie=True, in_directors=True,
                                          director_name=director))
                for decade in filter(lambda p: p[:4].isnumeric() and p.endswith('s'), os.listdir(movies_dir)):
                    decade_dir = os.path.join(movies_dir, decade)
                    if not os.path.isdir(decade_dir):
                        print(f'report: {decade_dir}')
                        continue
                    for movie in os.listdir(decade_dir):
                        movie_dir = os.path.join(decade_dir, movie)
                        if not os.path.isdir(movie_dir):
                            print(f'report: {movie_dir}')
                            continue
                        self.media_items.append(MediaItem(movie_dir, disk=disk, is_movie=True))

            if 'Movie Series' in os.listdir(path):
                movie_series_dir = os.path.join(path, 'Movie Series')
                for series in os.listdir(movie_series_dir):
                    series_dir = os.path.join(movie_series_dir, series)
                    if not os.path.isdir(series_dir):
                        print(f'report: {series_dir}')
                        continue
                    for movie in os.listdir(series_dir):
                        movie_dir = os.path.join(series_dir, movie)
                        if not os.path.isdir(movie_dir):
                            print(f'report: {movie_dir}')
                            continue
                        self.media_items.append(
                            MediaItem(movie_dir, disk=disk, is_movie=True, is_movie_series=True,
                                      movie_series_title=series))

            if 'TV Series' in os.listdir(path):
                tv_series_dir = os.path.join(path, 'TV Series')
                for series in os.listdir(tv_series_dir):
                    series_dir = os.path.join(tv_series_dir, series)
                    if not os.path.isdir(series_dir):
                        print(f'report: {series_dir}')
                        continue
                    self.media_items.append(
                        MediaItem(series_dir, disk=disk, is_tv_series=True, tv_series_title=series,
                                  number_of_seasons=len([s for s in os.listdir(series_dir)
                                                         if os.path.isdir(os.path.join(series_dir, s))])))

            if 'Stand-Up Comedy' in os.listdir(path):
                stand_up_dir = os.path.join(path, 'Stand-Up Comedy')
                for comedian in os.listdir(stand_up_dir):
                    comedian_dir = os.path.join(stand_up_dir, comedian)
                    if not os.path.isdir(comedian_dir):
                        continue
                    for special in os.listdir(comedian_dir):
                        special_dir = os.path.join(comedian_dir, special)
                        if not os.path.isdir(special_dir):
                            print(f'report: {special_dir}')
                            continue
                        self.media_items.append(
                            MediaItem(os.path.join(comedian_dir, special),
                                      disk=disk, is_comedy=True, comedian=comedian))

    def __str__(self):
        return '\n'.join([str(item) for item in self.media_items])

collection = MediaCollection(disks())
from random import randint
def randfilm():
    index = randint(0, len(collection.media_items) - 1)
    m = collection.media_items[index]
    print(m.disk, '--', m.title)

def findfilm(subtitle):
    found = False
    for movie in collection.media_items:
        if subtitle.lower() in movie.title.lower():
            print(movie.disk, '--', movie.title)
            found = True
    if not found:
        print('nope')

parser = argparse.ArgumentParser(description="find movies")
parser.add_argument('function', choices=['randfilm', 'findfilm'], help='Choose function')
parser.add_argument('--subtitle', '-t', help='Subtitle for findfilm function')
args = parser.parse_args()

if args.function == 'randfilm':
    randfilm()
elif args.function == 'findfilm':
    if args.subtitle:
        findfilm(args.subtitle)
    else:
        parser.error('The --subtitle argument is required for the findfilm function')
