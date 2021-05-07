"""Saves all photos in the current folder into smaller files in smaller/."""
import cv2
import threading
import os
from pdftitle.pdftitle import get_title_from_file
from utils import Utils


PRINT_OLD_FILENAME = False
RENAME = True


class RenameByTitle(threading.Thread):
  """Parses a PDF, obtains its title, and renames it."""
  def __init__(self, path, filename):
    threading.Thread.__init__(self)
    self.path = path
    self.filename = filename
    self.old_fullname = os.path.join(self.path, self.filename)

  def run(self):
    if PRINT_OLD_FILENAME:
      print(self.old_fullname)
    try:
      title = get_title_from_file(self.old_fullname)
      new_name = Utils.file_nameable(Utils.capitalize_all(title)) + '.pdf'
      if RENAME:
        os.rename(os.path.join(self.path, self.filename),
          os.path.join(self.path, new_name))
      print('%s => %s.pdf succeed.' % (self.filename, new_name))
    except:
      print('* %s failed ' % self.filename)

if __name__ == '__main__':
  cwd = os.getcwd()
  path_dir_files = os.walk(cwd)
  created_dir = False

  rename_threads = []

  for path, dir_list, file_list in path_dir_files:
    for filename in file_list:
      if filename[-3:].lower() == "pdf":
        # Runs the exporting thread.
        rename_threads.append(RenameByTitle(path, filename))
        rename_threads[-1].start()

  for thread in rename_threads:
    thread.join()
