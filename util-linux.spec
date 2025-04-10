#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure_ac
# autospec version: v21
# autospec commit: aacbe1b
#
%define keepstatic 1
Name     : util-linux
Version  : 2.40.4
Release  : 192
URL      : https://mirrors.kernel.org/pub/linux/utils/util-linux/v2.40/util-linux-2.40.4.tar.gz
Source0  : https://mirrors.kernel.org/pub/linux/utils/util-linux/v2.40/util-linux-2.40.4.tar.gz
Summary  : Miscellaneous system utilities for Linux
Group    : Development/Tools
License  : BSD-3-Clause BSD-4-Clause-UC GPL-2.0 GPL-3.0 ISC LGPL-2.1 MIT
Requires: util-linux-bin = %{version}-%{release}
Requires: util-linux-config = %{version}-%{release}
Requires: util-linux-data = %{version}-%{release}
Requires: util-linux-lib = %{version}-%{release}
Requires: util-linux-license = %{version}-%{release}
Requires: util-linux-locales = %{version}-%{release}
Requires: util-linux-man = %{version}-%{release}
Requires: util-linux-services = %{version}-%{release}
Requires: util-linux-setuid = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : Linux-PAM-dev32
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : e2fsprogs
BuildRequires : file
BuildRequires : flex
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libcap-ng-dev
BuildRequires : libcap-ng-dev32
BuildRequires : ncurses-dev
BuildRequires : ncurses-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32sqlite3)
BuildRequires : pkgconfig(libcryptsetup)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(tinfow)
BuildRequires : procps-ng
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : sed
BuildRequires : systemd-dev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Speed-up-agetty-waits.patch
Patch2: 0002-Recommend-1M-topology-size-if-none-set.patch
Patch3: 0003-Trim-all-filesystems-not-just-fstab-ones.patch

%description
util-linux
util-linux is a random collection of Linux utilities
Note: for the years 2006-2010 this project was named "util-linux-ng".

%package bin
Summary: bin components for the util-linux package.
Group: Binaries
Requires: util-linux-data = %{version}-%{release}
Requires: util-linux-setuid = %{version}-%{release}
Requires: util-linux-license = %{version}-%{release}

%description bin
bin components for the util-linux package.


%package config
Summary: config components for the util-linux package.
Group: Default

%description config
config components for the util-linux package.


%package data
Summary: data components for the util-linux package.
Group: Data

%description data
data components for the util-linux package.


%package dev
Summary: dev components for the util-linux package.
Group: Development
Requires: util-linux-lib = %{version}-%{release}
Requires: util-linux-bin = %{version}-%{release}
Requires: util-linux-data = %{version}-%{release}
Provides: util-linux-devel = %{version}-%{release}
Requires: util-linux = %{version}-%{release}

%description dev
dev components for the util-linux package.


%package dev32
Summary: dev32 components for the util-linux package.
Group: Default
Requires: util-linux-lib32 = %{version}-%{release}
Requires: util-linux-bin = %{version}-%{release}
Requires: util-linux-data = %{version}-%{release}
Requires: util-linux-dev = %{version}-%{release}

%description dev32
dev32 components for the util-linux package.


%package doc
Summary: doc components for the util-linux package.
Group: Documentation
Requires: util-linux-man = %{version}-%{release}

%description doc
doc components for the util-linux package.


%package extras
Summary: extras components for the util-linux package.
Group: Default

%description extras
extras components for the util-linux package.


%package extras-uuid-services
Summary: extras-uuid-services components for the util-linux package.
Group: Default

%description extras-uuid-services
extras-uuid-services components for the util-linux package.


%package lib
Summary: lib components for the util-linux package.
Group: Libraries
Requires: util-linux-data = %{version}-%{release}
Requires: util-linux-license = %{version}-%{release}

%description lib
lib components for the util-linux package.


%package lib32
Summary: lib32 components for the util-linux package.
Group: Default
Requires: util-linux-data = %{version}-%{release}
Requires: util-linux-license = %{version}-%{release}

%description lib32
lib32 components for the util-linux package.


%package license
Summary: license components for the util-linux package.
Group: Default

%description license
license components for the util-linux package.


%package locales
Summary: locales components for the util-linux package.
Group: Default

%description locales
locales components for the util-linux package.


%package man
Summary: man components for the util-linux package.
Group: Default

%description man
man components for the util-linux package.


%package python
Summary: python components for the util-linux package.
Group: Default
Requires: util-linux-python3 = %{version}-%{release}

%description python
python components for the util-linux package.


%package python3
Summary: python3 components for the util-linux package.
Group: Default
Requires: python3-core

%description python3
python3 components for the util-linux package.


%package services
Summary: services components for the util-linux package.
Group: Systemd services
Requires: systemd

%description services
services components for the util-linux package.


%package setuid
Summary: setuid components for the util-linux package.
Group: Default

%description setuid
setuid components for the util-linux package.


%package staticdev
Summary: staticdev components for the util-linux package.
Group: Default
Requires: util-linux-dev = %{version}-%{release}

%description staticdev
staticdev components for the util-linux package.


%package staticdev32
Summary: staticdev32 components for the util-linux package.
Group: Default
Requires: util-linux-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the util-linux package.


%prep
%setup -q -n util-linux-2.40.4
cd %{_builddir}/util-linux-2.40.4
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
pushd ..
cp -a util-linux-2.40.4 build32
popd
pushd ..
cp -a util-linux-2.40.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742597336
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure  --disable-use-tty-group \
--disable-makeinstall-chown \
--disable-makeinstall-setuid \
--disable-kill \
--disable-chfn-chsh \
--disable-nologin \
--disable-plymouth_support \
--without-econf \
--without-libmagic \
PYTHON=/usr/bin/python3
make  %{?_smp_mflags}
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure  --disable-use-tty-group \
--disable-makeinstall-chown \
--disable-makeinstall-setuid \
--disable-kill \
--disable-chfn-chsh \
--disable-nologin \
--disable-plymouth_support \
--without-econf \
--without-libmagic \
PYTHON=/usr/bin/python3 --without-ncurses \
--without-ncursesw \
--without-systemd \
--without-python \
--without-tinfo \
--disable-hardlink --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure  --disable-use-tty-group \
--disable-makeinstall-chown \
--disable-makeinstall-setuid \
--disable-kill \
--disable-chfn-chsh \
--disable-nologin \
--disable-plymouth_support \
--without-econf \
--without-libmagic \
PYTHON=/usr/bin/python3
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742597336
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/util-linux
cp %{_builddir}/util-linux-%{version}/COPYING %{buildroot}/usr/share/package-licenses/util-linux/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/util-linux-%{version}/Documentation/licenses/COPYING.BSD-3-Clause %{buildroot}/usr/share/package-licenses/util-linux/e5c9f3867b9251dcd2d97a4d1dffaa38afe6625d || :
cp %{_builddir}/util-linux-%{version}/Documentation/licenses/COPYING.BSD-4-Clause-UC %{buildroot}/usr/share/package-licenses/util-linux/8afe522e7c956a6c19914cd5ffea17a0aa2e4bc7 || :
cp %{_builddir}/util-linux-%{version}/Documentation/licenses/COPYING.GPL-2.0-only %{buildroot}/usr/share/package-licenses/util-linux/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/util-linux-%{version}/Documentation/licenses/COPYING.GPL-2.0-or-later %{buildroot}/usr/share/package-licenses/util-linux/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/util-linux-%{version}/Documentation/licenses/COPYING.GPL-3.0-or-later %{buildroot}/usr/share/package-licenses/util-linux/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/util-linux-%{version}/Documentation/licenses/COPYING.ISC %{buildroot}/usr/share/package-licenses/util-linux/fca052e126f39e97d69d000644b7a462f215c125 || :
cp %{_builddir}/util-linux-%{version}/Documentation/licenses/COPYING.LGPL-2.1-or-later %{buildroot}/usr/share/package-licenses/util-linux/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/util-linux-%{version}/Documentation/licenses/COPYING.MIT %{buildroot}/usr/share/package-licenses/util-linux/b3b0afb867e5845805e356426710a6a2b262b913 || :
cp %{_builddir}/util-linux-%{version}/libblkid/COPYING %{buildroot}/usr/share/package-licenses/util-linux/93e45afdb0d7c3fdd6dfcc951b8a3421660f2811 || :
cp %{_builddir}/util-linux-%{version}/libfdisk/COPYING %{buildroot}/usr/share/package-licenses/util-linux/93e45afdb0d7c3fdd6dfcc951b8a3421660f2811 || :
cp %{_builddir}/util-linux-%{version}/libmount/COPYING %{buildroot}/usr/share/package-licenses/util-linux/66319e97eda8747087e9c5292f31c8bc5153c3c8 || :
cp %{_builddir}/util-linux-%{version}/libsmartcols/COPYING %{buildroot}/usr/share/package-licenses/util-linux/93e45afdb0d7c3fdd6dfcc951b8a3421660f2811 || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang util-linux
## Remove excluded files
rm -f %{buildroot}*/usr/share/getopt/getopt-parse.tcsh
rm -f %{buildroot}*/usr/share/doc/util-linux/getopt/getopt-parse.tcsh
rm -f %{buildroot}*/usr/share/bash-completion/completions/fsck.minix
rm -f %{buildroot}*/usr/share/bash-completion/completions/rfkill
rm -f %{buildroot}*/usr/bin/mkfs.bfs
rm -f %{buildroot}*/usr/bin/linux32
rm -f %{buildroot}*/usr/bin/fdformat
rm -f %{buildroot}*/usr/bin/fsck.minix
rm -f %{buildroot}*/usr/bin/mkfs.minix
## install_append content
#mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
#ln -s ../uuidd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/uuidd.socket
#mkdir -p %{buildroot}/usr/lib/systemd/system/timers.target.wants/
#ln -sf ../fstrim.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/fstrim.timer
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name} --skip-path /usr/bin/su

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/addpart
/V3/usr/bin/agetty
/V3/usr/bin/blkdiscard
/V3/usr/bin/blkid
/V3/usr/bin/blkpr
/V3/usr/bin/blkzone
/V3/usr/bin/blockdev
/V3/usr/bin/cal
/V3/usr/bin/cfdisk
/V3/usr/bin/chcpu
/V3/usr/bin/chmem
/V3/usr/bin/choom
/V3/usr/bin/chrt
/V3/usr/bin/col
/V3/usr/bin/colcrt
/V3/usr/bin/colrm
/V3/usr/bin/column
/V3/usr/bin/ctrlaltdel
/V3/usr/bin/delpart
/V3/usr/bin/dmesg
/V3/usr/bin/eject
/V3/usr/bin/enosys
/V3/usr/bin/exch
/V3/usr/bin/fadvise
/V3/usr/bin/fallocate
/V3/usr/bin/fdisk
/V3/usr/bin/fincore
/V3/usr/bin/findfs
/V3/usr/bin/findmnt
/V3/usr/bin/flock
/V3/usr/bin/fsck
/V3/usr/bin/fsck.cramfs
/V3/usr/bin/fsfreeze
/V3/usr/bin/fstrim
/V3/usr/bin/getopt
/V3/usr/bin/hardlink
/V3/usr/bin/hexdump
/V3/usr/bin/hwclock
/V3/usr/bin/ionice
/V3/usr/bin/ipcmk
/V3/usr/bin/ipcrm
/V3/usr/bin/ipcs
/V3/usr/bin/irqtop
/V3/usr/bin/isosize
/V3/usr/bin/last
/V3/usr/bin/lastlog2
/V3/usr/bin/ldattach
/V3/usr/bin/logger
/V3/usr/bin/login
/V3/usr/bin/look
/V3/usr/bin/losetup
/V3/usr/bin/lsblk
/V3/usr/bin/lsclocks
/V3/usr/bin/lscpu
/V3/usr/bin/lsfd
/V3/usr/bin/lsipc
/V3/usr/bin/lsirq
/V3/usr/bin/lslocks
/V3/usr/bin/lslogins
/V3/usr/bin/lsmem
/V3/usr/bin/lsns
/V3/usr/bin/mcookie
/V3/usr/bin/mesg
/V3/usr/bin/mkfs
/V3/usr/bin/mkswap
/V3/usr/bin/more
/V3/usr/bin/mount
/V3/usr/bin/mountpoint
/V3/usr/bin/namei
/V3/usr/bin/nsenter
/V3/usr/bin/partx
/V3/usr/bin/pipesz
/V3/usr/bin/pivot_root
/V3/usr/bin/prlimit
/V3/usr/bin/readprofile
/V3/usr/bin/rename
/V3/usr/bin/renice
/V3/usr/bin/resizepart
/V3/usr/bin/rev
/V3/usr/bin/rfkill
/V3/usr/bin/rtcwake
/V3/usr/bin/runuser
/V3/usr/bin/script
/V3/usr/bin/scriptlive
/V3/usr/bin/scriptreplay
/V3/usr/bin/setarch
/V3/usr/bin/setpgid
/V3/usr/bin/setpriv
/V3/usr/bin/setsid
/V3/usr/bin/setterm
/V3/usr/bin/sfdisk
/V3/usr/bin/sulogin
/V3/usr/bin/swaplabel
/V3/usr/bin/swapoff
/V3/usr/bin/swapon
/V3/usr/bin/switch_root
/V3/usr/bin/taskset
/V3/usr/bin/uclampset
/V3/usr/bin/ul
/V3/usr/bin/umount
/V3/usr/bin/unshare
/V3/usr/bin/utmpdump
/V3/usr/bin/uuidd
/V3/usr/bin/uuidgen
/V3/usr/bin/uuidparse
/V3/usr/bin/waitpid
/V3/usr/bin/wall
/V3/usr/bin/wdctl
/V3/usr/bin/whereis
/V3/usr/bin/wipefs
/V3/usr/bin/zramctl
/usr/bin/addpart
/usr/bin/agetty
/usr/bin/blkdiscard
/usr/bin/blkid
/usr/bin/blkpr
/usr/bin/blkzone
/usr/bin/blockdev
/usr/bin/cal
/usr/bin/cfdisk
/usr/bin/chcpu
/usr/bin/chmem
/usr/bin/choom
/usr/bin/chrt
/usr/bin/col
/usr/bin/colcrt
/usr/bin/colrm
/usr/bin/column
/usr/bin/ctrlaltdel
/usr/bin/delpart
/usr/bin/dmesg
/usr/bin/eject
/usr/bin/enosys
/usr/bin/exch
/usr/bin/fadvise
/usr/bin/fallocate
/usr/bin/fdisk
/usr/bin/fincore
/usr/bin/findfs
/usr/bin/findmnt
/usr/bin/flock
/usr/bin/fsck
/usr/bin/fsck.cramfs
/usr/bin/fsfreeze
/usr/bin/fstrim
/usr/bin/getopt
/usr/bin/hardlink
/usr/bin/hexdump
/usr/bin/hwclock
/usr/bin/i386
/usr/bin/ionice
/usr/bin/ipcmk
/usr/bin/ipcrm
/usr/bin/ipcs
/usr/bin/irqtop
/usr/bin/isosize
/usr/bin/last
/usr/bin/lastb
/usr/bin/lastlog2
/usr/bin/ldattach
/usr/bin/linux64
/usr/bin/logger
/usr/bin/login
/usr/bin/look
/usr/bin/losetup
/usr/bin/lsblk
/usr/bin/lsclocks
/usr/bin/lscpu
/usr/bin/lsfd
/usr/bin/lsipc
/usr/bin/lsirq
/usr/bin/lslocks
/usr/bin/lslogins
/usr/bin/lsmem
/usr/bin/lsns
/usr/bin/mcookie
/usr/bin/mesg
/usr/bin/mkfs
/usr/bin/mkswap
/usr/bin/more
/usr/bin/mount
/usr/bin/mountpoint
/usr/bin/namei
/usr/bin/nsenter
/usr/bin/partx
/usr/bin/pipesz
/usr/bin/pivot_root
/usr/bin/prlimit
/usr/bin/readprofile
/usr/bin/rename
/usr/bin/renice
/usr/bin/resizepart
/usr/bin/rev
/usr/bin/rfkill
/usr/bin/rtcwake
/usr/bin/runuser
/usr/bin/script
/usr/bin/scriptlive
/usr/bin/scriptreplay
/usr/bin/setarch
/usr/bin/setpgid
/usr/bin/setpriv
/usr/bin/setsid
/usr/bin/setterm
/usr/bin/sfdisk
/usr/bin/sulogin
/usr/bin/swaplabel
/usr/bin/swapoff
/usr/bin/swapon
/usr/bin/switch_root
/usr/bin/taskset
/usr/bin/uclampset
/usr/bin/ul
/usr/bin/umount
/usr/bin/uname26
/usr/bin/unshare
/usr/bin/utmpdump
/usr/bin/uuidd
/usr/bin/uuidgen
/usr/bin/uuidparse
/usr/bin/waitpid
/usr/bin/wall
/usr/bin/wdctl
/usr/bin/whereis
/usr/bin/wipefs
/usr/bin/x86_64
/usr/bin/zramctl

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/lastlog2-tmpfiles.conf
/usr/lib/tmpfiles.d/uuidd-tmpfiles.conf

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/enosys
/usr/share/bash-completion/completions/exch
/usr/share/bash-completion/completions/fadvise
/usr/share/bash-completion/completions/hardlink
/usr/share/bash-completion/completions/irqtop
/usr/share/bash-completion/completions/lastb
/usr/share/bash-completion/completions/lastlog2
/usr/share/bash-completion/completions/lsclocks
/usr/share/bash-completion/completions/lsirq
/usr/share/bash-completion/completions/pipesz
/usr/share/bash-completion/completions/scriptlive
/usr/share/bash-completion/completions/setpgid
/usr/share/bash-completion/completions/uclampset
/usr/share/bash-completion/completions/waitpid

%files dev
%defattr(-,root,root,-)
/usr/include/blkid/blkid.h
/usr/include/libfdisk/libfdisk.h
/usr/include/liblastlog2/lastlog2.h
/usr/include/libmount/libmount.h
/usr/include/libsmartcols/libsmartcols.h
/usr/include/uuid/uuid.h
/usr/lib64/libblkid.so
/usr/lib64/libfdisk.so
/usr/lib64/liblastlog2.so
/usr/lib64/libmount.so
/usr/lib64/libsmartcols.so
/usr/lib64/libuuid.so
/usr/lib64/pkgconfig/blkid.pc
/usr/lib64/pkgconfig/fdisk.pc
/usr/lib64/pkgconfig/lastlog2.pc
/usr/lib64/pkgconfig/mount.pc
/usr/lib64/pkgconfig/smartcols.pc
/usr/lib64/pkgconfig/uuid.pc
/usr/share/man/man3/lastlog2.3
/usr/share/man/man3/libblkid.3
/usr/share/man/man3/ll2_import_lastlog.3
/usr/share/man/man3/ll2_read_all.3
/usr/share/man/man3/ll2_read_entry.3
/usr/share/man/man3/ll2_remove_entry.3
/usr/share/man/man3/ll2_rename_user.3
/usr/share/man/man3/ll2_update_login_time.3
/usr/share/man/man3/ll2_write_entry.3
/usr/share/man/man3/uuid.3
/usr/share/man/man3/uuid_clear.3
/usr/share/man/man3/uuid_compare.3
/usr/share/man/man3/uuid_copy.3
/usr/share/man/man3/uuid_generate.3
/usr/share/man/man3/uuid_generate_random.3
/usr/share/man/man3/uuid_generate_time.3
/usr/share/man/man3/uuid_generate_time_safe.3
/usr/share/man/man3/uuid_is_null.3
/usr/share/man/man3/uuid_parse.3
/usr/share/man/man3/uuid_time.3
/usr/share/man/man3/uuid_unparse.3

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libblkid.so
/usr/lib32/libfdisk.so
/usr/lib32/liblastlog2.so
/usr/lib32/libmount.so
/usr/lib32/libsmartcols.so
/usr/lib32/libuuid.so
/usr/lib32/pkgconfig/32blkid.pc
/usr/lib32/pkgconfig/32fdisk.pc
/usr/lib32/pkgconfig/32lastlog2.pc
/usr/lib32/pkgconfig/32mount.pc
/usr/lib32/pkgconfig/32smartcols.pc
/usr/lib32/pkgconfig/32uuid.pc
/usr/lib32/pkgconfig/blkid.pc
/usr/lib32/pkgconfig/fdisk.pc
/usr/lib32/pkgconfig/lastlog2.pc
/usr/lib32/pkgconfig/mount.pc
/usr/lib32/pkgconfig/smartcols.pc
/usr/lib32/pkgconfig/uuid.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/util\-linux/*

%files extras
%defattr(-,root,root,-)
/V3/usr/bin/mkfs.cramfs
/usr/bin/mkfs.cramfs
/usr/share/bash-completion/completions/addpart
/usr/share/bash-completion/completions/blkdiscard
/usr/share/bash-completion/completions/blkid
/usr/share/bash-completion/completions/blkzone
/usr/share/bash-completion/completions/blockdev
/usr/share/bash-completion/completions/cal
/usr/share/bash-completion/completions/cfdisk
/usr/share/bash-completion/completions/chcpu
/usr/share/bash-completion/completions/chmem
/usr/share/bash-completion/completions/chrt
/usr/share/bash-completion/completions/col
/usr/share/bash-completion/completions/colcrt
/usr/share/bash-completion/completions/colrm
/usr/share/bash-completion/completions/column
/usr/share/bash-completion/completions/ctrlaltdel
/usr/share/bash-completion/completions/delpart
/usr/share/bash-completion/completions/dmesg
/usr/share/bash-completion/completions/eject
/usr/share/bash-completion/completions/fallocate
/usr/share/bash-completion/completions/fdisk
/usr/share/bash-completion/completions/fincore
/usr/share/bash-completion/completions/findfs
/usr/share/bash-completion/completions/findmnt
/usr/share/bash-completion/completions/flock
/usr/share/bash-completion/completions/fsck
/usr/share/bash-completion/completions/fsck.cramfs
/usr/share/bash-completion/completions/fsfreeze
/usr/share/bash-completion/completions/fstrim
/usr/share/bash-completion/completions/getopt
/usr/share/bash-completion/completions/hexdump
/usr/share/bash-completion/completions/hwclock
/usr/share/bash-completion/completions/ionice
/usr/share/bash-completion/completions/ipcmk
/usr/share/bash-completion/completions/ipcrm
/usr/share/bash-completion/completions/ipcs
/usr/share/bash-completion/completions/isosize
/usr/share/bash-completion/completions/last
/usr/share/bash-completion/completions/ldattach
/usr/share/bash-completion/completions/logger
/usr/share/bash-completion/completions/look
/usr/share/bash-completion/completions/losetup
/usr/share/bash-completion/completions/lsblk
/usr/share/bash-completion/completions/lscpu
/usr/share/bash-completion/completions/lsipc
/usr/share/bash-completion/completions/lslocks
/usr/share/bash-completion/completions/lslogins
/usr/share/bash-completion/completions/lsmem
/usr/share/bash-completion/completions/lsns
/usr/share/bash-completion/completions/mcookie
/usr/share/bash-completion/completions/mesg
/usr/share/bash-completion/completions/mkfs
/usr/share/bash-completion/completions/mkfs.bfs
/usr/share/bash-completion/completions/mkfs.cramfs
/usr/share/bash-completion/completions/mkfs.minix
/usr/share/bash-completion/completions/mkswap
/usr/share/bash-completion/completions/more
/usr/share/bash-completion/completions/mount
/usr/share/bash-completion/completions/mountpoint
/usr/share/bash-completion/completions/namei
/usr/share/bash-completion/completions/nsenter
/usr/share/bash-completion/completions/partx
/usr/share/bash-completion/completions/pivot_root
/usr/share/bash-completion/completions/prlimit
/usr/share/bash-completion/completions/readprofile
/usr/share/bash-completion/completions/rename
/usr/share/bash-completion/completions/renice
/usr/share/bash-completion/completions/resizepart
/usr/share/bash-completion/completions/rev
/usr/share/bash-completion/completions/rtcwake
/usr/share/bash-completion/completions/runuser
/usr/share/bash-completion/completions/script
/usr/share/bash-completion/completions/scriptreplay
/usr/share/bash-completion/completions/setarch
/usr/share/bash-completion/completions/setpriv
/usr/share/bash-completion/completions/setsid
/usr/share/bash-completion/completions/setterm
/usr/share/bash-completion/completions/sfdisk
/usr/share/bash-completion/completions/su
/usr/share/bash-completion/completions/swaplabel
/usr/share/bash-completion/completions/swapoff
/usr/share/bash-completion/completions/swapon
/usr/share/bash-completion/completions/taskset
/usr/share/bash-completion/completions/ul
/usr/share/bash-completion/completions/umount
/usr/share/bash-completion/completions/unshare
/usr/share/bash-completion/completions/utmpdump
/usr/share/bash-completion/completions/uuidd
/usr/share/bash-completion/completions/uuidgen
/usr/share/bash-completion/completions/uuidparse
/usr/share/bash-completion/completions/wall
/usr/share/bash-completion/completions/wdctl
/usr/share/bash-completion/completions/whereis
/usr/share/bash-completion/completions/wipefs
/usr/share/bash-completion/completions/zramctl

%files extras-uuid-services
%defattr(-,root,root,-)
/usr/lib/systemd/system/uuidd.service
/usr/lib/systemd/system/uuidd.socket

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libblkid.so.1.1.0
/V3/usr/lib64/libfdisk.so.1.1.0
/V3/usr/lib64/liblastlog2.so.2.0.0
/V3/usr/lib64/libmount.so.1.1.0
/V3/usr/lib64/libsmartcols.so.1.1.0
/V3/usr/lib64/libuuid.so.1.3.0
/V3/usr/lib64/security/pam_lastlog2.so
/usr/lib64/libblkid.so.1
/usr/lib64/libblkid.so.1.1.0
/usr/lib64/libfdisk.so.1
/usr/lib64/libfdisk.so.1.1.0
/usr/lib64/liblastlog2.so.2
/usr/lib64/liblastlog2.so.2.0.0
/usr/lib64/libmount.so.1
/usr/lib64/libmount.so.1.1.0
/usr/lib64/libsmartcols.so.1
/usr/lib64/libsmartcols.so.1.1.0
/usr/lib64/libuuid.so.1
/usr/lib64/libuuid.so.1.3.0
/usr/lib64/security/pam_lastlog2.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libblkid.so.1
/usr/lib32/libblkid.so.1.1.0
/usr/lib32/libfdisk.so.1
/usr/lib32/libfdisk.so.1.1.0
/usr/lib32/liblastlog2.so.2
/usr/lib32/liblastlog2.so.2.0.0
/usr/lib32/libmount.so.1
/usr/lib32/libmount.so.1.1.0
/usr/lib32/libsmartcols.so.1
/usr/lib32/libsmartcols.so.1.1.0
/usr/lib32/libuuid.so.1
/usr/lib32/libuuid.so.1.3.0
/usr/lib32/security/pam_lastlog2.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/util-linux/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/util-linux/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/util-linux/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/util-linux/66319e97eda8747087e9c5292f31c8bc5153c3c8
/usr/share/package-licenses/util-linux/8afe522e7c956a6c19914cd5ffea17a0aa2e4bc7
/usr/share/package-licenses/util-linux/93e45afdb0d7c3fdd6dfcc951b8a3421660f2811
/usr/share/package-licenses/util-linux/b3b0afb867e5845805e356426710a6a2b262b913
/usr/share/package-licenses/util-linux/e5c9f3867b9251dcd2d97a4d1dffaa38afe6625d
/usr/share/package-licenses/util-linux/fca052e126f39e97d69d000644b7a462f215c125

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cal.1
/usr/share/man/man1/choom.1
/usr/share/man/man1/chrt.1
/usr/share/man/man1/col.1
/usr/share/man/man1/colcrt.1
/usr/share/man/man1/colrm.1
/usr/share/man/man1/column.1
/usr/share/man/man1/dmesg.1
/usr/share/man/man1/eject.1
/usr/share/man/man1/enosys.1
/usr/share/man/man1/exch.1
/usr/share/man/man1/fadvise.1
/usr/share/man/man1/fallocate.1
/usr/share/man/man1/fincore.1
/usr/share/man/man1/flock.1
/usr/share/man/man1/getopt.1
/usr/share/man/man1/hardlink.1
/usr/share/man/man1/hexdump.1
/usr/share/man/man1/ionice.1
/usr/share/man/man1/ipcmk.1
/usr/share/man/man1/ipcrm.1
/usr/share/man/man1/ipcs.1
/usr/share/man/man1/irqtop.1
/usr/share/man/man1/last.1
/usr/share/man/man1/lastb.1
/usr/share/man/man1/logger.1
/usr/share/man/man1/login.1
/usr/share/man/man1/look.1
/usr/share/man/man1/lsclocks.1
/usr/share/man/man1/lscpu.1
/usr/share/man/man1/lsfd.1
/usr/share/man/man1/lsipc.1
/usr/share/man/man1/lsirq.1
/usr/share/man/man1/lslogins.1
/usr/share/man/man1/lsmem.1
/usr/share/man/man1/mcookie.1
/usr/share/man/man1/mesg.1
/usr/share/man/man1/more.1
/usr/share/man/man1/mountpoint.1
/usr/share/man/man1/namei.1
/usr/share/man/man1/nsenter.1
/usr/share/man/man1/pipesz.1
/usr/share/man/man1/prlimit.1
/usr/share/man/man1/rename.1
/usr/share/man/man1/renice.1
/usr/share/man/man1/rev.1
/usr/share/man/man1/runuser.1
/usr/share/man/man1/script.1
/usr/share/man/man1/scriptlive.1
/usr/share/man/man1/scriptreplay.1
/usr/share/man/man1/setpgid.1
/usr/share/man/man1/setpriv.1
/usr/share/man/man1/setsid.1
/usr/share/man/man1/setterm.1
/usr/share/man/man1/su.1
/usr/share/man/man1/taskset.1
/usr/share/man/man1/uclampset.1
/usr/share/man/man1/ul.1
/usr/share/man/man1/unshare.1
/usr/share/man/man1/utmpdump.1
/usr/share/man/man1/uuidgen.1
/usr/share/man/man1/uuidparse.1
/usr/share/man/man1/waitpid.1
/usr/share/man/man1/wall.1
/usr/share/man/man1/whereis.1
/usr/share/man/man5/adjtime_config.5
/usr/share/man/man5/fstab.5
/usr/share/man/man5/scols-filter.5
/usr/share/man/man5/terminal-colors.d.5
/usr/share/man/man8/addpart.8
/usr/share/man/man8/agetty.8
/usr/share/man/man8/blkdiscard.8
/usr/share/man/man8/blkid.8
/usr/share/man/man8/blkpr.8
/usr/share/man/man8/blkzone.8
/usr/share/man/man8/blockdev.8
/usr/share/man/man8/cfdisk.8
/usr/share/man/man8/chcpu.8
/usr/share/man/man8/chmem.8
/usr/share/man/man8/ctrlaltdel.8
/usr/share/man/man8/delpart.8
/usr/share/man/man8/fdisk.8
/usr/share/man/man8/findfs.8
/usr/share/man/man8/findmnt.8
/usr/share/man/man8/fsck.8
/usr/share/man/man8/fsck.cramfs.8
/usr/share/man/man8/fsck.minix.8
/usr/share/man/man8/fsfreeze.8
/usr/share/man/man8/fstrim.8
/usr/share/man/man8/hwclock.8
/usr/share/man/man8/isosize.8
/usr/share/man/man8/lastlog2.8
/usr/share/man/man8/ldattach.8
/usr/share/man/man8/losetup.8
/usr/share/man/man8/lsblk.8
/usr/share/man/man8/lslocks.8
/usr/share/man/man8/lsns.8
/usr/share/man/man8/mkfs.8
/usr/share/man/man8/mkfs.bfs.8
/usr/share/man/man8/mkfs.cramfs.8
/usr/share/man/man8/mkfs.minix.8
/usr/share/man/man8/mkswap.8
/usr/share/man/man8/mount.8
/usr/share/man/man8/pam_lastlog2.8
/usr/share/man/man8/partx.8
/usr/share/man/man8/pivot_root.8
/usr/share/man/man8/readprofile.8
/usr/share/man/man8/resizepart.8
/usr/share/man/man8/rfkill.8
/usr/share/man/man8/rtcwake.8
/usr/share/man/man8/setarch.8
/usr/share/man/man8/sfdisk.8
/usr/share/man/man8/sulogin.8
/usr/share/man/man8/swaplabel.8
/usr/share/man/man8/swapoff.8
/usr/share/man/man8/swapon.8
/usr/share/man/man8/switch_root.8
/usr/share/man/man8/umount.8
/usr/share/man/man8/uuidd.8
/usr/share/man/man8/wdctl.8
/usr/share/man/man8/wipefs.8
/usr/share/man/man8/zramctl.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/fstrim.service
/usr/lib/systemd/system/fstrim.timer
/usr/lib/systemd/system/lastlog2-import.service

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/bin/su

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libblkid.a
/usr/lib64/libfdisk.a
/usr/lib64/liblastlog2.a
/usr/lib64/libmount.a
/usr/lib64/libsmartcols.a
/usr/lib64/libuuid.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libblkid.a
/usr/lib32/libfdisk.a
/usr/lib32/liblastlog2.a
/usr/lib32/libmount.a
/usr/lib32/libsmartcols.a
/usr/lib32/libuuid.a

%files locales -f util-linux.lang
%defattr(-,root,root,-)

