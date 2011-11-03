import os
import platform

from ubuntutweak.common.consts import APP, VERSION

def get_distro():
    '''It should be "Ubuntu 10.10 maverick"'''
    return ' '.join(platform.dist())

def get_codename():
    try:
        codename = os.popen('lsb_release -cs').read().strip()
        if codename in ['karmic', 'helena', 'Helena']:
            return 'karmic'
        elif codename in ['lucid', 'isadora', 'Isadora']:
            return 'lucid'
        elif codename in ['maverick', 'julia']:
            return 'maverick'
        elif codename in ['natty', 'katya']:
            return 'natty'
        return codename
    except:
        pass
    return ''

def get_desktop():
    '''
    ubuntu
    ubuntu-2d
    gnome-classic
    gnome-shell
    '''
    return os.getenv('DESKTOP_SESSION')

def get_desktop_fullname():
    desktop_dict = {'ubuntu': 'Unity',
                    'ubuntu-2d': 'Unity 2D',
                    'gnome-classic': _('GNOME Classic'),
                    'gnome-shell': 'GNOME Shell',
                    }

    desktop = get_desktop()

    if desktop in desktop_dict:
        return desktop_dict[desktop]
    else:
        if desktop:
            return _('Unknown (%s)') % desktop
        else:
            return _('Unknown')

def get_app():
    '''Ubuntu Tweak 0.5.x'''
    return " ".join([APP, VERSION])

DISTRO = get_distro()
CODENAME = get_codename()
DESKTOP = get_desktop()
DESKTOP_FULLNAME = get_desktop_fullname()
APP = get_app()
UBUNTU_CODENAMES = ('dapper', 'edgy', 'feisty', 'gutsy', 'hardy', 'intrepid', 'jaunty', 'karmic', 'lucid', 'maverick', 'natty')

def is_supported(codename=CODENAME):
    return codename in ('karmic', 'lucid', 'maverick', 'natty')


if __name__ == '__main__':
    print 'DISTRO: ', DISTRO
    print 'CODENAME: ', CODENAME
    print 'DESKTOP: ', DESKTOP
    print 'DESKTOP_FULLNAME: ', DESKTOP_FULLNAME
    print 'DESKTOP_VERSION: ', DESKTOP_VERSION
    print 'APP: ', APP