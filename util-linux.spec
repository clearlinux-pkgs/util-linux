#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : util-linux
Version  : 2.32
Release  : 113
URL      : https://www.kernel.org/pub/linux/utils/util-linux/v2.32/util-linux-2.32.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/util-linux/v2.32/util-linux-2.32.tar.xz
Summary  : mount library
Group    : Development/Tools
License  : BSD-3-Clause BSD-4-Clause-UC GPL-2.0 ISC LGPL-2.1
Requires: util-linux-bin
Requires: util-linux-setuid
Requires: util-linux-python3
Requires: util-linux-config
Requires: util-linux-autostart
Requires: util-linux-lib
Requires: util-linux-data
Requires: util-linux-license
Requires: util-linux-locales
Requires: util-linux-man
Requires: util-linux-python
BuildRequires : Linux-PAM-dev
BuildRequires : Linux-PAM-dev32
BuildRequires : bison
BuildRequires : docbook-xml
BuildRequires : e2fsprogs
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
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(tinfow)
BuildRequires : procps-ng
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : readline-dev
BuildRequires : systemd-dev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: 0001-Speed-up-agetty-waits.patch
Patch2: 0002-Clear-out-the-pink-color.patch
Patch3: 0003-Recommend-1M-topology-size-if-none-set.patch
Patch4: 0004-Don-t-unparse-UUID-even-if-we-have-libuuid.patch

%description
util-linux
util-linux is a random collection of Linux utilities
Note: for the years 2006-2010 this project was named "util-linux-ng".

%package autostart
Summary: autostart components for the util-linux package.
Group: Default

%description autostart
autostart components for the util-linux package.


%package bin
Summary: bin components for the util-linux package.
Group: Binaries
Requires: util-linux-data
Requires: util-linux-config
Requires: util-linux-setuid
Requires: util-linux-license
Requires: util-linux-man

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
Requires: util-linux-lib
Requires: util-linux-bin
Requires: util-linux-data
Provides: util-linux-devel

%description dev
dev components for the util-linux package.


%package dev32
Summary: dev32 components for the util-linux package.
Group: Default
Requires: util-linux-lib32
Requires: util-linux-bin
Requires: util-linux-data
Requires: util-linux-dev

%description dev32
dev32 components for the util-linux package.


%package doc
Summary: doc components for the util-linux package.
Group: Documentation
Requires: util-linux-man

%description doc
doc components for the util-linux package.


%package extras
Summary: extras components for the util-linux package.
Group: Default

%description extras
extras components for the util-linux package.


%package lib
Summary: lib components for the util-linux package.
Group: Libraries
Requires: util-linux-data
Requires: util-linux-license

%description lib
lib components for the util-linux package.


%package lib32
Summary: lib32 components for the util-linux package.
Group: Default
Requires: util-linux-data
Requires: util-linux-license

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
Requires: util-linux-python3

%description python
python components for the util-linux package.


%package python3
Summary: python3 components for the util-linux package.
Group: Default
Requires: python3-core

%description python3
python3 components for the util-linux package.


%package setuid
Summary: setuid components for the util-linux package.
Group: Default

%description setuid
setuid components for the util-linux package.


%prep
%setup -q -n util-linux-2.32
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
pushd ..
cp -a util-linux-2.32 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530369571
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure  --disable-use-tty-group \
--disable-makeinstall-chown \
--disable-makeinstall-setuid \
--enable-socket-activation \
--disable-kill \
--disable-chfn-chsh \
--disable-nologin \
--enable-libmount-force-mountinfo \
--disable-plymouth_support \
PYTHON=/usr/bin/python3
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure  --disable-use-tty-group \
--disable-makeinstall-chown \
--disable-makeinstall-setuid \
--enable-socket-activation \
--disable-kill \
--disable-chfn-chsh \
--disable-nologin \
--enable-libmount-force-mountinfo \
--disable-plymouth_support \
PYTHON=/usr/bin/python3 --without-ncurses \
--without-ncursesw \
--without-systemd \
--without-python \
--without-tinfo  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1530369571
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/util-linux
cp COPYING %{buildroot}/usr/share/doc/util-linux/COPYING
cp Documentation/licenses/COPYING.LGPLv2.1 %{buildroot}/usr/share/doc/util-linux/Documentation_licenses_COPYING.LGPLv2.1
cp Documentation/licenses/COPYING.BSD-3 %{buildroot}/usr/share/doc/util-linux/Documentation_licenses_COPYING.BSD-3
cp Documentation/licenses/COPYING.UCB %{buildroot}/usr/share/doc/util-linux/Documentation_licenses_COPYING.UCB
cp Documentation/licenses/COPYING.ISC %{buildroot}/usr/share/doc/util-linux/Documentation_licenses_COPYING.ISC
cp Documentation/licenses/COPYING.GPLv2 %{buildroot}/usr/share/doc/util-linux/Documentation_licenses_COPYING.GPLv2
cp libmount/COPYING %{buildroot}/usr/share/doc/util-linux/libmount_COPYING
cp libfdisk/COPYING %{buildroot}/usr/share/doc/util-linux/libfdisk_COPYING
cp libsmartcols/COPYING %{buildroot}/usr/share/doc/util-linux/libsmartcols_COPYING
cp libuuid/COPYING %{buildroot}/usr/share/doc/util-linux/libuuid_COPYING
cp libblkid/COPYING %{buildroot}/usr/share/doc/util-linux/libblkid_COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang util-linux
## make_install_append content
mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../uuidd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/uuidd.socket
mkdir -p %{buildroot}/usr/lib/systemd/system/timers.target.wants/
ln -sf ../fstrim.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/fstrim.timer
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/sockets.target.wants/uuidd.socket
/usr/lib/systemd/system/timers.target.wants/fstrim.timer

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/fdformat
%exclude /usr/bin/fsck.minix
%exclude /usr/bin/linux32
%exclude /usr/bin/login
%exclude /usr/bin/mkfs.bfs
%exclude /usr/bin/mkfs.cramfs
%exclude /usr/bin/mkfs.minix
%exclude /usr/bin/su
%exclude /usr/bin/zramctl
/usr/bin/addpart
/usr/bin/agetty
/usr/bin/blkdiscard
/usr/bin/blkid
/usr/bin/blkzone
/usr/bin/blockdev
/usr/bin/cal
/usr/bin/cfdisk
/usr/bin/chcpu
/usr/bin/chmem
/usr/bin/chrt
/usr/bin/col
/usr/bin/colcrt
/usr/bin/colrm
/usr/bin/column
/usr/bin/ctrlaltdel
/usr/bin/delpart
/usr/bin/dmesg
/usr/bin/eject
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
/usr/bin/hexdump
/usr/bin/hwclock
/usr/bin/i386
/usr/bin/ionice
/usr/bin/ipcmk
/usr/bin/ipcrm
/usr/bin/ipcs
/usr/bin/isosize
/usr/bin/last
/usr/bin/lastb
/usr/bin/ldattach
/usr/bin/linux64
/usr/bin/logger
/usr/bin/look
/usr/bin/losetup
/usr/bin/lsblk
/usr/bin/lscpu
/usr/bin/lsipc
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
/usr/bin/pivot_root
/usr/bin/prlimit
/usr/bin/raw
/usr/bin/readprofile
/usr/bin/rename
/usr/bin/renice
/usr/bin/resizepart
/usr/bin/rev
/usr/bin/rfkill
/usr/bin/rtcwake
/usr/bin/runuser
/usr/bin/script
/usr/bin/scriptreplay
/usr/bin/setarch
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
/usr/bin/ul
/usr/bin/umount
/usr/bin/uname26
/usr/bin/unshare
/usr/bin/utmpdump
/usr/bin/uuidd
/usr/bin/uuidgen
/usr/bin/uuidparse
/usr/bin/wall
/usr/bin/wdctl
/usr/bin/whereis
/usr/bin/wipefs
/usr/bin/x86_64

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/sockets.target.wants/uuidd.socket
%exclude /usr/lib/systemd/system/timers.target.wants/fstrim.timer
/usr/lib/systemd/system/fstrim.service
/usr/lib/systemd/system/fstrim.timer
/usr/lib/systemd/system/uuidd.service
/usr/lib/systemd/system/uuidd.socket

%files data
%defattr(-,root,root,-)
%exclude /usr/share/bash-completion/completions/addpart
%exclude /usr/share/bash-completion/completions/blkdiscard
%exclude /usr/share/bash-completion/completions/blkid
%exclude /usr/share/bash-completion/completions/blockdev
%exclude /usr/share/bash-completion/completions/cal
%exclude /usr/share/bash-completion/completions/cfdisk
%exclude /usr/share/bash-completion/completions/chcpu
%exclude /usr/share/bash-completion/completions/chmem
%exclude /usr/share/bash-completion/completions/chrt
%exclude /usr/share/bash-completion/completions/col
%exclude /usr/share/bash-completion/completions/colcrt
%exclude /usr/share/bash-completion/completions/colrm
%exclude /usr/share/bash-completion/completions/column
%exclude /usr/share/bash-completion/completions/ctrlaltdel
%exclude /usr/share/bash-completion/completions/delpart
%exclude /usr/share/bash-completion/completions/dmesg
%exclude /usr/share/bash-completion/completions/eject
%exclude /usr/share/bash-completion/completions/fallocate
%exclude /usr/share/bash-completion/completions/fdformat
%exclude /usr/share/bash-completion/completions/fdisk
%exclude /usr/share/bash-completion/completions/fincore
%exclude /usr/share/bash-completion/completions/findfs
%exclude /usr/share/bash-completion/completions/findmnt
%exclude /usr/share/bash-completion/completions/flock
%exclude /usr/share/bash-completion/completions/fsck
%exclude /usr/share/bash-completion/completions/fsck.cramfs
%exclude /usr/share/bash-completion/completions/fsck.minix
%exclude /usr/share/bash-completion/completions/fsfreeze
%exclude /usr/share/bash-completion/completions/fstrim
%exclude /usr/share/bash-completion/completions/getopt
%exclude /usr/share/bash-completion/completions/hexdump
%exclude /usr/share/bash-completion/completions/hwclock
%exclude /usr/share/bash-completion/completions/ionice
%exclude /usr/share/bash-completion/completions/ipcmk
%exclude /usr/share/bash-completion/completions/ipcrm
%exclude /usr/share/bash-completion/completions/ipcs
%exclude /usr/share/bash-completion/completions/isosize
%exclude /usr/share/bash-completion/completions/last
%exclude /usr/share/bash-completion/completions/ldattach
%exclude /usr/share/bash-completion/completions/logger
%exclude /usr/share/bash-completion/completions/look
%exclude /usr/share/bash-completion/completions/losetup
%exclude /usr/share/bash-completion/completions/lsblk
%exclude /usr/share/bash-completion/completions/lscpu
%exclude /usr/share/bash-completion/completions/lsipc
%exclude /usr/share/bash-completion/completions/lslocks
%exclude /usr/share/bash-completion/completions/lslogins
%exclude /usr/share/bash-completion/completions/lsmem
%exclude /usr/share/bash-completion/completions/lsns
%exclude /usr/share/bash-completion/completions/mcookie
%exclude /usr/share/bash-completion/completions/mesg
%exclude /usr/share/bash-completion/completions/mkfs
%exclude /usr/share/bash-completion/completions/mkfs.bfs
%exclude /usr/share/bash-completion/completions/mkfs.cramfs
%exclude /usr/share/bash-completion/completions/mkfs.minix
%exclude /usr/share/bash-completion/completions/mkswap
%exclude /usr/share/bash-completion/completions/more
%exclude /usr/share/bash-completion/completions/mount
%exclude /usr/share/bash-completion/completions/mountpoint
%exclude /usr/share/bash-completion/completions/namei
%exclude /usr/share/bash-completion/completions/nsenter
%exclude /usr/share/bash-completion/completions/partx
%exclude /usr/share/bash-completion/completions/pivot_root
%exclude /usr/share/bash-completion/completions/prlimit
%exclude /usr/share/bash-completion/completions/raw
%exclude /usr/share/bash-completion/completions/readprofile
%exclude /usr/share/bash-completion/completions/rename
%exclude /usr/share/bash-completion/completions/renice
%exclude /usr/share/bash-completion/completions/resizepart
%exclude /usr/share/bash-completion/completions/rev
%exclude /usr/share/bash-completion/completions/rfkill
%exclude /usr/share/bash-completion/completions/rtcwake
%exclude /usr/share/bash-completion/completions/runuser
%exclude /usr/share/bash-completion/completions/script
%exclude /usr/share/bash-completion/completions/scriptreplay
%exclude /usr/share/bash-completion/completions/setarch
%exclude /usr/share/bash-completion/completions/setpriv
%exclude /usr/share/bash-completion/completions/setsid
%exclude /usr/share/bash-completion/completions/setterm
%exclude /usr/share/bash-completion/completions/sfdisk
%exclude /usr/share/bash-completion/completions/su
%exclude /usr/share/bash-completion/completions/swaplabel
%exclude /usr/share/bash-completion/completions/swapoff
%exclude /usr/share/bash-completion/completions/swapon
%exclude /usr/share/bash-completion/completions/taskset
%exclude /usr/share/bash-completion/completions/ul
%exclude /usr/share/bash-completion/completions/umount
%exclude /usr/share/bash-completion/completions/unshare
%exclude /usr/share/bash-completion/completions/utmpdump
%exclude /usr/share/bash-completion/completions/uuidd
%exclude /usr/share/bash-completion/completions/uuidgen
%exclude /usr/share/bash-completion/completions/uuidparse
%exclude /usr/share/bash-completion/completions/wall
%exclude /usr/share/bash-completion/completions/wdctl
%exclude /usr/share/bash-completion/completions/whereis
%exclude /usr/share/bash-completion/completions/wipefs
%exclude /usr/share/bash-completion/completions/zramctl
/usr/share/bash-completion/completions/blkzone

%files dev
%defattr(-,root,root,-)
/usr/include/blkid/blkid.h
/usr/include/libfdisk/libfdisk.h
/usr/include/libmount/libmount.h
/usr/include/libsmartcols/libsmartcols.h
/usr/include/uuid/uuid.h
/usr/lib64/*.a
/usr/lib64/libblkid.so
/usr/lib64/libfdisk.so
/usr/lib64/libmount.so
/usr/lib64/libsmartcols.so
/usr/lib64/libuuid.so
/usr/lib64/pkgconfig/blkid.pc
/usr/lib64/pkgconfig/fdisk.pc
/usr/lib64/pkgconfig/mount.pc
/usr/lib64/pkgconfig/smartcols.pc
/usr/lib64/pkgconfig/uuid.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/*.a
/usr/lib32/libblkid.so
/usr/lib32/libfdisk.so
/usr/lib32/libmount.so
/usr/lib32/libsmartcols.so
/usr/lib32/libuuid.so
/usr/lib32/pkgconfig/32blkid.pc
/usr/lib32/pkgconfig/32fdisk.pc
/usr/lib32/pkgconfig/32mount.pc
/usr/lib32/pkgconfig/32smartcols.pc
/usr/lib32/pkgconfig/32uuid.pc
/usr/lib32/pkgconfig/blkid.pc
/usr/lib32/pkgconfig/fdisk.pc
/usr/lib32/pkgconfig/mount.pc
/usr/lib32/pkgconfig/smartcols.pc
/usr/lib32/pkgconfig/uuid.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/util\-linux/*
%exclude /usr/share/doc/util-linux/getopt/getopt-parse.tcsh

%files extras
%defattr(-,root,root,-)
/usr/bin/mkfs.cramfs
/usr/bin/zramctl
/usr/lib/python3.7/site-packages/libmount/__init__.py
/usr/lib/python3.7/site-packages/libmount/__pycache__/__init__.cpython-37.pyc
/usr/lib/python3.7/site-packages/libmount/pylibmount.so
/usr/share/bash-completion/completions/addpart
/usr/share/bash-completion/completions/blkdiscard
/usr/share/bash-completion/completions/blkid
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
/usr/share/bash-completion/completions/fdformat
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
/usr/share/bash-completion/completions/raw
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libblkid.so.1
/usr/lib64/libblkid.so.1.1.0
/usr/lib64/libfdisk.so.1
/usr/lib64/libfdisk.so.1.1.0
/usr/lib64/libmount.so.1
/usr/lib64/libmount.so.1.1.0
/usr/lib64/libsmartcols.so.1
/usr/lib64/libsmartcols.so.1.1.0
/usr/lib64/libuuid.so.1
/usr/lib64/libuuid.so.1.3.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libblkid.so.1
/usr/lib32/libblkid.so.1.1.0
/usr/lib32/libfdisk.so.1
/usr/lib32/libfdisk.so.1.1.0
/usr/lib32/libmount.so.1
/usr/lib32/libmount.so.1.1.0
/usr/lib32/libsmartcols.so.1
/usr/lib32/libsmartcols.so.1.1.0
/usr/lib32/libuuid.so.1
/usr/lib32/libuuid.so.1.3.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/util-linux/COPYING
/usr/share/doc/util-linux/Documentation_licenses_COPYING.BSD-3
/usr/share/doc/util-linux/Documentation_licenses_COPYING.GPLv2
/usr/share/doc/util-linux/Documentation_licenses_COPYING.ISC
/usr/share/doc/util-linux/Documentation_licenses_COPYING.LGPLv2.1
/usr/share/doc/util-linux/Documentation_licenses_COPYING.UCB
/usr/share/doc/util-linux/libblkid_COPYING
/usr/share/doc/util-linux/libfdisk_COPYING
/usr/share/doc/util-linux/libmount_COPYING
/usr/share/doc/util-linux/libsmartcols_COPYING
/usr/share/doc/util-linux/libuuid_COPYING

%files man
%defattr(-,root,root,-)
%exclude /usr/share/man/man1/login.1
/usr/share/man/man1/cal.1
/usr/share/man/man1/chrt.1
/usr/share/man/man1/col.1
/usr/share/man/man1/colcrt.1
/usr/share/man/man1/colrm.1
/usr/share/man/man1/column.1
/usr/share/man/man1/dmesg.1
/usr/share/man/man1/eject.1
/usr/share/man/man1/fallocate.1
/usr/share/man/man1/fincore.1
/usr/share/man/man1/flock.1
/usr/share/man/man1/getopt.1
/usr/share/man/man1/hexdump.1
/usr/share/man/man1/ionice.1
/usr/share/man/man1/ipcmk.1
/usr/share/man/man1/ipcrm.1
/usr/share/man/man1/ipcs.1
/usr/share/man/man1/last.1
/usr/share/man/man1/lastb.1
/usr/share/man/man1/logger.1
/usr/share/man/man1/look.1
/usr/share/man/man1/lscpu.1
/usr/share/man/man1/lsipc.1
/usr/share/man/man1/lslogins.1
/usr/share/man/man1/lsmem.1
/usr/share/man/man1/mcookie.1
/usr/share/man/man1/mesg.1
/usr/share/man/man1/more.1
/usr/share/man/man1/mountpoint.1
/usr/share/man/man1/namei.1
/usr/share/man/man1/nsenter.1
/usr/share/man/man1/prlimit.1
/usr/share/man/man1/rename.1
/usr/share/man/man1/renice.1
/usr/share/man/man1/rev.1
/usr/share/man/man1/runuser.1
/usr/share/man/man1/script.1
/usr/share/man/man1/scriptreplay.1
/usr/share/man/man1/setpriv.1
/usr/share/man/man1/setsid.1
/usr/share/man/man1/setterm.1
/usr/share/man/man1/su.1
/usr/share/man/man1/taskset.1
/usr/share/man/man1/ul.1
/usr/share/man/man1/unshare.1
/usr/share/man/man1/utmpdump.1
/usr/share/man/man1/uuidgen.1
/usr/share/man/man1/uuidparse.1
/usr/share/man/man1/wall.1
/usr/share/man/man1/whereis.1
/usr/share/man/man3/libblkid.3
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
/usr/share/man/man5/fstab.5
/usr/share/man/man5/terminal-colors.d.5
/usr/share/man/man8/addpart.8
/usr/share/man/man8/agetty.8
/usr/share/man/man8/blkdiscard.8
/usr/share/man/man8/blkid.8
/usr/share/man/man8/blkzone.8
/usr/share/man/man8/blockdev.8
/usr/share/man/man8/cfdisk.8
/usr/share/man/man8/chcpu.8
/usr/share/man/man8/chmem.8
/usr/share/man/man8/ctrlaltdel.8
/usr/share/man/man8/delpart.8
/usr/share/man/man8/fdformat.8
/usr/share/man/man8/fdisk.8
/usr/share/man/man8/findfs.8
/usr/share/man/man8/findmnt.8
/usr/share/man/man8/fsck.8
/usr/share/man/man8/fsck.cramfs.8
/usr/share/man/man8/fsck.minix.8
/usr/share/man/man8/fsfreeze.8
/usr/share/man/man8/fstrim.8
/usr/share/man/man8/hwclock.8
/usr/share/man/man8/i386.8
/usr/share/man/man8/isosize.8
/usr/share/man/man8/ldattach.8
/usr/share/man/man8/linux32.8
/usr/share/man/man8/linux64.8
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
/usr/share/man/man8/partx.8
/usr/share/man/man8/pivot_root.8
/usr/share/man/man8/raw.8
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
/usr/share/man/man8/uname26.8
/usr/share/man/man8/uuidd.8
/usr/share/man/man8/wdctl.8
/usr/share/man/man8/wipefs.8
/usr/share/man/man8/x86_64.8
/usr/share/man/man8/zramctl.8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
%exclude /usr/lib/python3.7/site-packages/libmount/__init__.py
%exclude /usr/lib/python3.7/site-packages/libmount/__pycache__/__init__.cpython-37.pyc
%exclude /usr/lib/python3.7/site-packages/libmount/pylibmount.so

%files setuid
%defattr(-,root,root,-)
%attr(4755, root, root) /usr/bin/su

%files locales -f util-linux.lang
%defattr(-,root,root,-)

