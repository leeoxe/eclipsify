from __future__ import print_function
import os
import errno
import sys
import eclipsify_lib
from argparse import ArgumentParser, RawDescriptionHelpFormatter

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else: 
            raise

def main(argv=None):
    if argv is None:
        argv=sys.argv

    usage="""

    This utility creates a new eclipse project."""

    parser = ArgumentParser(description=usage,formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument("package", nargs=1, help="Package to be created.")
    parser.add_argument("src_dir", nargs=1, help="The source directory.")
    parser.add_argument("out_dir", nargs=1, help="The output directory. Where to put the eclipse project.")
    parser.add_argument("build_dir", nargs=1, help="This project's build directory.")
    #parser.add_argument("bin_dir", nargs=1, help="This project's bin directory.")

    options = parser.parse_args(argv)

    package     = options.package[0]
    src_dir     = options.src_dir[0]
    eclipse_dir = options.out_dir[0]
    build_dir   = options.build_dir[0]

    print("eclipsify!")
    print("----------")
    print("-- Creating directories")
    print("-- {0}".format(eclipse_dir))
    mkdir_p( os.path.join( eclipse_dir, '.settings' ) )

    if sys.platform == 'darwin':
        import eclipsify_lib.cproject_osx as cproject
        import eclipsify_lib.project_osx as project
        import eclipsify_lib.language_settings_osx as language_settings
    else:
        raise RuntimeError('Someone has to fill in these templates');

    print("-- Creating .project")
    with open(os.path.join(eclipse_dir,'.project'), 'w') as outfile:
        print(project.get(package, src_dir), file=outfile)

    print("-- Creating .cproject")
    with open(os.path.join(eclipse_dir,'.cproject'), 'w') as outfile:
        print(cproject.get(package,build_dir), file=outfile)

    print("-- Creating .settings/language.settings.xml")
    with open(os.path.join(eclipse_dir,'.settings', 'language_settings.xml'), 'w') as outfile:
        print(language_settings.get(), file=outfile)