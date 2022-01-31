import setuptools
import os

BUILDING_DIR="D:\\DTPySide"

long_description=""
with open(os.path.join(BUILDING_DIR, 'README.md'), "r", encoding="utf-8") as fh:
    long_description += fh.read()
with open(os.path.join(BUILDING_DIR, 'CHANGELOG.md'), "r", encoding="utf-8") as fh:
    long_description += fh.read()

with open(os.path.join(BUILDING_DIR, 'CHANGELOG.md'), "r", encoding="utf-8") as fh:
    changelog = fh.read()
version=changelog.splitlines()[2][3:]

setuptools.setup(
    name="DTPySide",
    version=version,
    author="Holence",
    author_email="Holence08@gmail.com",
    description="A PySide framework for constructing customizable GUI software.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Holence/DongliTeahousePySide",
    project_urls={
        "Bug Tracker": "https://github.com/Holence/DongliTeahousePySide/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data = True,
    python_requires=">=3.8",
)