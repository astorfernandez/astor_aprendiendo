import os


class FileUtils:
    def write_file(self, content, dir_path, file_path):
        full_path = os.path.join(dir_path, file_path)
        with open(full_path, 'wb') as f:
            f.write(content.encode('utf-8'))

    def read_file(self, dir_path, file_path):
        full_path = os.path.join(dir_path, file_path)
        content = None
        with open(full_path, 'rb') as f:
            content = f.read().decode('utf-8')
        return content

    def delete_file(self, dir_path, file_path):
        full_path = os.path.join(dir_path, file_path)
        os.remove(full_path)