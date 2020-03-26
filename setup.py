from setuptools import setup
import os
from shutil import rmtree
from glob import glob


packageName = "videoEditor"
try:
    from setuptools.comand.clean import clean as clean_command
except:
    from distutils.command.clean import clean as clean_command

class Clean(clean_command):
    def run(self):
        clean_command.run(self)
        delete_in_root = ['build', 'dist', '*.egg-info', '.tox', '.eggs.', '.cache']
        delete_everywhere = ['__pycache__', '*.pyc']

        for candidate in delete_in_root:
            rmtree_glob(candidate)

        for visible_dir in glob("[A-Za-z0-9]*"):
            for candidate in delete_everywhere:
                rmtree_glob(os.path.join(visible_dir, candidate))
                rmtree_glob(os.path.join(visible_dir, "*", candidate))


def rmtree_glob(candidate):
    for fobj in glob(candidate):
        try:
            rmtree(fobj)
            print("%s/ removed from project" % fobj)
        except OSError:
            try:
                os.remove(fobj)
                print("%s/ removed from project" % fobj)
            except OSError:
                print("Unable to remove the file from the folder")

def read_file(path=None, file_name=None):
    path = path or "."
    file_path = os.path.join(path, file_name)
    print("Reading file %s" % file_path)
    with open(file_path) as fd:
        return fd.read()

exec(read_file(path=os.path.join('.', packageName), file_name="__init__.py"))
version = __version__
projectName = __name__
readmeData = read_file(file_name="README.md")
licenseData = read_file(file_name="LICENSE")

setup(
    name=packageName,
    description="Video editor to cut the videos to apt for youtube",
    version=version,
    packages=[
        packageName,
    ],
    install_requires=[
        "moviepy",
    ],
    license="GNU GENERAL PUBLIC LICENSE",
    long_description_content_type='text/markdown',
    long_description=readmeData,
    author=', '.join(__author__),
    author_emails=', '.join(__author_email__),
    url="https://github.com/sunilk-n/VideoEditor",
    classifiers=[
        # See https://pypi.org/pypi?%3Aaction=list_classifiers
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    data_files=[
        "README.md",
        "LICENSE"
    ],
    entry_points={
        'console_scripts': [
            'srsEdit=%s.__main__:main' % packageName
        ],
    },
    cmdclass={
        "clean": Clean,
    },
    
)
