class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if not len(self.photos[page]) >= 4:
                self.photos[page].append(label)
                return f'{label} photo added successfully on page {page+1} slot {len(self.photos[page])}'
        return f'No more free spots'

    def display(self):
        result = f'-----------\n'

        for i in self.photos:
            if not i:
                result += '\n'
            else:
                result += ''.join('[] ' for _ in range(len(i))).strip()
                result += '\n'
            result += f'-----------\n'

        return result