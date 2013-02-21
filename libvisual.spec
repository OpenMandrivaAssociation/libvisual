%define name libvisual
%define version 0.4.0
%define major 0
%define libname %mklibname visual %major
%define develname %mklibname -d visual

Name: %{name}
Version: %{version}
Release: %mkrel 12
Summary: Audio visualisation framework
Source0: %{name}-%{version}.tar.bz2
Patch0: libvisual-0.4.0-fix-str-fmt.patch
License: LGPLv2+
Group: System/Libraries
Url: http://localhost.nl/~synap/libvisual

%description
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

Libvisual is aimed at developers who have a need for audio
visualisation and those who actually write the visualisation plugins.

#--------------------------------------------------------------------

%package -n %libname
Group: System/Libraries
Summary: Shared library of the audio visualisation framework 
Provides: %name = %version-%release
Obsoletes: libvisual-plugins < 0.4.0
Conflicts: gstreamer0.10-libvisual <= 0.10.7-1mdk
Suggests: libvisual-plugins

%description -n %libname
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

Libvisual is aimed at developers who have a need for audio
visualisation and those who actually write the visualisation plugins.

%files -n %libname -f %name-0.4.lang
%doc README NEWS TODO ChangeLog AUTHORS
%_libdir/libvisual-0.4.so.%{major}*

#--------------------------------------------------------------------

%package -n %develname
Group: Development/C
Summary: Header files of the audio visualisation framework 
Requires: %libname = %version
Provides: libvisual-devel = %version-%release
Obsoletes: %{_lib}visual0-devel < %version-%release

%description -n %develname
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

Libvisual is aimed at developers who have a need for audio
visualisation and those who actually write the visualisation plugins.

%files -n %develname
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %name-0.4




%changelog
* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 0.4.0-12mdv2011.0
+ Revision: 661793
- fix patch apply

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Thu Dec 23 2010 Funda Wang <fwang@mandriva.org> 0.4.0-11mdv2011.0
+ Revision: 623953
- new devel package policy
- tighten BR

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-10mdv2011.0
+ Revision: 602611
- rebuild

* Sun Dec 27 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-9mdv2010.1
+ Revision: 482793
- suggest libvisual-plugins (bug #56679)

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.0-8mdv2010.0
+ Revision: 425874
- rebuild

* Sun Apr 12 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-7mdv2009.1
+ Revision: 366507
- readd format string patch
- readd the patch

* Sun Apr 12 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-6mdv2009.1
+ Revision: 366496
- drop format string patch (bug #49801)
- disable format string Werror
- update license

* Fri Apr 10 2009 Funda Wang <fwang@mandriva.org> 0.4.0-5mdv2009.1
+ Revision: 365704
- fix str fmt

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-5mdv2009.0
+ Revision: 223016
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-4mdv2008.1
+ Revision: 179006
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sat Jan 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.4.0-2mdv2007.0
+ Revision: 108198
- use the right macros

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream version
    - import libvisual-0.2.0-5mdk

* Mon May 01 2006 Stefan van der Eijk <stefan@eijk.nu> 0.2.0-5mdk
- rebuild for sparc

* Tue Aug 23 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.2.0-4mdk
- reconstruct from cvs
- only build lv_video_mmx.c with -mmmx

* Tue Jun 21 2005 Götz Waschk <waschk@mandriva.org> 0.2.0-3mdk
- enable mmx

* Sat Feb 12 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.2.0-2mdk
- Patch1: fix ppc build

* Thu Feb 10 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.2.0-1mdk
- 0.2.0

* Tue Nov 23 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.7-3mdk
- fix provides

* Sat Oct 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.7-2mdk
- fix openGL build

* Sat Oct 16 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.1.7-1mdk
- New release 0.1.7

* Mon Sep 13 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.1.6-1mdk
- New release 0.1.6

* Thu Jul 01 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.5-1mdk
- fix installation
- New release 0.1.5

* Sat Jun 26 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.4-1mdk
- initial package

