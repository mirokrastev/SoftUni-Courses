class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'

        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name):
        albums_var = [i.name for i in self.albums]

        if album_name not in albums_var:
            return f'Album {album_name} is not found.'

        inx = albums_var.index(album_name)

        if self.albums[inx].published:
            return f'Album has been published. It cannot be removed.'

        self.albums.pop(inx)
        return f'Album {album_name} has been removed.'

    def details(self):
        result = f'Band {self.name}\n'

        for i in self.albums:
            result += f'{i.details()}\n'

        return result