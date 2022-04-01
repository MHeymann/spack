# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Flint(Package):
    """FLINT (Fast Library for Number Theory)."""

    homepage = "https://www.flintlib.org"
    url      = "https://www.flintlib.org/flint-2.8.4.tar.gz"
    git      = "https://github.com/wbhart/flint2.git"

    maintainers = ["wbhart", "MHeymann"]


    version('develop', branch='trunk')
    version('2.8.4', sha256='61df92ea8c8e9dc692d46c71d7f50aaa09a33d4ba08d02a1784730a445e5e4be')
    version('2.7.1', sha256='186e2fd9ab67df8a05b122fb018269b382e4babcdb17353c4be1fe364dca481e')
    version('2.6.3', sha256='ce1a750a01fa53715cad934856d4b2ed76f1d1520bac0527ace7d5b53e342ee3')

    # Build dependencies
    depends_on('autoconf', type='build')

    # Other dependencies
    depends_on('gmp')
    depends_on('mpfr')

    phases = ['configure', 'build', 'install']

    def configure_args(self):
        args = [ "--prefix=%s" % self.prefix
               , "--with-gmp=%s" % self.spec['gmp'].prefix
               , "--with-mpfr=%s" % self.spec['mpfr'].prefix
               ]
        return args

    def configure(self, spec, prefix):
        configure_script = Executable("./configure")
        configure_script(*self.configure_args())

    def build(self, spec, prefix):
        make()

    @run_after('build')
    @on_package_attributes(run_tests=True)
    def test(self):
        make("check")

    def install(self, spec, prefix):
        make("install")
