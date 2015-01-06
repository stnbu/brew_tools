# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
import subprocess
import shutil


class BrewUnusableError(EnvironmentError):
    """
    """

class BrewTools(object):

    def __init__(self, unconditional_link=[]):
        try:
            self.brew_prefix = subprocess.check_output(['brew', '--prefix']).strip()
        except OSError as e:
            raise BrewUnusableError('Brew missing or not properly installed: {0}'.format(e))
        self.gnutools_links_dir_basename = 'gnutools'
        self.brew_bin = os.path.join(self.brew_prefix, 'bin')
        self.gnutools_links_dir = os.path.join(self.brew_bin, '..', self.gnutools_links_dir_basename)
        self.gnutools_links_dir = os.path.realpath(self.gnutools_links_dir)
        self.unconditional_link = unconditional_link
        if self.unconditional_link is None:
            self.unconditional_link = []
        self.unconditional_link = [n.lstrip('g') for n in self.unconditional_link]

    def delete_gnutools_links_dir(self):
        shutil.rmtree(self.gnutools_links_dir, ignore_errors=True)

    def make_gnutools_links(self):
        if not os.path.exists(self.gnutools_links_dir):
            os.mkdir(self.gnutools_links_dir)
        for tool in glob(os.path.join(self.brew_bin, 'g*')):
            for path in '/bin', '/usr/bin':
                realname = os.path.basename(tool)
                realname = realname[1:]
                if os.path.exists('{0}/{1}'.format(path, realname)) or realname in self.unconditional_link:
                    dst = os.path.join(self.gnutools_links_dir, realname)
                    if not os.path.exists(dst):
                        src = os.path.join('..', 'bin', os.path.basename(tool))
                        os.symlink(src, dst)
                        break

    def enable_all_gnutools_links(self):
        for tool in glob(os.path.join(self.gnutools_links_dir, '*')):
            src = os.path.join('..', self.gnutools_links_dir_basename, os.path.basename(tool))
            dst = os.path.join(self.brew_bin, os.path.basename(tool))
            if not os.path.exists(dst):
                os.symlink(src, dst)

    def delete_all_gunutools_links(self):
        for tool in glob(os.path.join(self.brew_bin, '*')):
            if not os.path.islink(tool):
                continue
            link = os.readlink(tool)
            if os.path.dirname(link) == os.path.join('..', self.gnutools_links_dir_basename):
                os.unlink(tool)

    def create(self):
        self.make_gnutools_links()
        self.enable_all_gnutools_links()

    def delete(self):
        self.delete_all_gunutools_links()
        self.delete_gnutools_links_dir()
