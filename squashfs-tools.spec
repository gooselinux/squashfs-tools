Summary: Utility for the creation of squashfs filesystems
Name: squashfs-tools
Version: 4.0
# cvs snapshot from cvs -d:pserver:anonymous@squashfs.cvs.sourceforge.net:/cvsroot/squashfs co squashfs on 2009-01-25
Release: 3%{?dist}
License: GPLv2+
Group: System Environment/Base
URL: http://squashfs.sf.net
Source0: http://cdnetworks-us-2.dl.sourceforge.net/project/squashfs/squashfs/squashfs%{version}/squashfs%{version}.tar.gz
Patch0: squashfs-cflags.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel

%description
Squashfs is a highly compressed read-only filesystem for Linux.  This package
contains the utilities for manipulating squashfs filesystems.

%prep
%setup -q -n squashfs%{version}
%patch0 -p1 -b .cflags

%build
pushd squashfs-tools
make RPM_OPT_FLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin $RPM_BUILD_ROOT/usr/sbin
install -m 755 squashfs-tools/mksquashfs $RPM_BUILD_ROOT/sbin/mksquashfs
install -m 755 squashfs-tools/unsquashfs $RPM_BUILD_ROOT%{_sbindir}/unsquashfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%doc README-4.0
/sbin/mksquashfs
%{_sbindir}/unsquashfs

%changelog
* Thu Feb 18 2010 Kyle McMartin <kyle@redhat.com> - 4.0-3
- Add %{dist} tag to Release.
- Use upstream tarball (instead of CVS snapshot.)
  (There's no code difference.)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 05 2009 Kyle McMartin <kyle@redhat.com> - 4.0-1
- Update to release 4.0

* Tue Mar 16 2009 Kyle McMartin <kyle@redhat.com> - 4.0-0.20090316
- update to cvs snap from 2009-03-16.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.20090126
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 26 2009 Kyle McMartin <kyle@redhat.com> - 4.0-0.20090125
- update to cvs snap that should unbreak big endian machines creating
  little endian fs.

* Mon Jan 12 2009  <katzj@redhat.com> - 4.0-0.20090112
- update to cvs snap that generates v4.0 images

* Tue Sep 30 2008 Jeremy Katz <katzj@redhat.com> - 3.4-1
- update to 3.4

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.3-2
- Autorebuild for GCC 4.3

* Fri Dec 14 2007 Jeremy Katz <katzj@redhat.com> - 3.3-1
- Update to 3.3

* Wed Sep  5 2007 Jeremy Katz <katzj@redhat.com> - 3.2-2
- fixes from package review (#226430)

* Tue Mar 20 2007 Jeremy Katz <katzj@redhat.com> - 3.2-1
- update to 3.2r2

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 3.0-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 18 2006 Jeremy Katz <katzj@redhat.com> - 3.0-3
- updated fragment size patch (#204638)

* Wed Aug 16 2006 Jeremy Katz <katzj@redhat.com> - 3.0-2
- add upstream patch for fragment size problem (#202663)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.0-1.1
- rebuild

* Fri Jun 23 2006 Jeremy Katz <katzj@redhat.com> - 3.0-1
- update to 3.0
- include unsquashfs

* Tue May 16 2006 Jeremy Katz <katzj@redhat.com> 
- add BR on zlib-devel (Andreas Thienemann, #191880)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.2r2-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.2r2-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  1 2005 Jeremy Katz <katzj@redhat.com> - 2.2r2-1
- Initial build

