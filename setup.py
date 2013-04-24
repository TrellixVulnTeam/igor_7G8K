from distutils.core import setup
import os
import re

def build_testcases_filelist(dst, path):
    xpat = re.compile("~$")
    lst = []
    for root, dirs, files in os.walk(path):
        lf = []
        for f in files:
            if xpat.search(f):
                continue
            lf.append(os.path.join(root, f))
        lst.append((os.path.join(dst, root), lf))
    return lst

setup(
    name='igor',
    version='0.4.0',
    author='Fabian Deutsch',
    author_email='fabiand@fedoraproject.org',
    packages=['igor', 'igor.backends'],
    package_data={'igor': ['data/*.xsl', 'data/*.sh']},
    scripts=['bin/igord', 'bin/igorc'],
    data_files=[('lib/systemd/system', ['data/igord.service',
                                        'data/igord-event-publisher.service']),
                ('/etc/igord', ['data/igord.cfg.example']),
                ('/etc/igord/hook.d', ['data/notify-event-publisher-hook']),
                ('libexec', ['bin/igord-event-publisher']),
                ('/var/run/igord', []),
                ('lib/igord/testcases', [])], # FIXME testcases are missing
    url='http://www.gitorious.org/ovirt/igord',
    license='LGPLv2',
    description='Testing a Linux distribution',
    long_description=open('README.txt').read(),
)
