# Copyright (C) 2016 SYLEAM (<http://www.syleam.fr>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from setuptools import setup

setup(
    name='odoo-sentinel',
    use_scm_version=True,
    author='Sylvain Garancher',
    author_email='sylvain.garancher@syleam.fr',
    packages=['odoo_sentinel'],
    package_data={'odoo_sentinel': ['i18n/*/LC_MESSAGES/*.mo']},
    install_requires=[
        'odoorpc',
        'halo',
        # 'playsound',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    entry_points={
        'console_scripts': [
            'odoo-sentinel = odoo_sentinel:main',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: POSIX',
    ],
    license='LICENSE.txt',
    description='Odoo custom ncurses client for the stock_scanner module',
    long_description=open('README.txt').read(),
)
