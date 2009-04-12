%define name libvisual
%define version 0.4.0
%define major 0
%define libname %mklibname visual %major

Name: %{name}
Version: %{version}
Release: %mkrel 6
Summary: Audio visualisation framework
Source0: %{name}-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
Url: http://localhost.nl/~synap/libvisual
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %mdkversion > 200600
BuildRequires:	X11-devel
%else
BuildRequires:	X11-devel
%endif

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

%description -n %libname
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

Libvisual is aimed at developers who have a need for audio
visualisation and those who actually write the visualisation plugins.

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname -f %name-0.4.lang
%defattr(-,root,root)
%doc README NEWS TODO ChangeLog AUTHORS
%_libdir/libvisual-0.4.so.%{major}*

#--------------------------------------------------------------------

%package -n %libname-devel
Group: Development/C
Summary: Header files of the audio visualisation framework 
Requires: %libname = %version
Provides: libvisual-devel = %version-%release

%description -n %libname-devel
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

Libvisual is aimed at developers who have a need for audio
visualisation and those who actually write the visualisation plugins.

%files -n %libname-devel
%defattr(-,root,root)
%_includedir/*
%_libdir/*.so
%_libdir/*.la
%_libdir/pkgconfig/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
#gw the format string patch made gst crash:
# https://qa.mandriva.com/show_bug.cgi?id=49801
%define Werror_cflags %nil
%configure2_5x
%make

%install
rm -rf %buildroot

%makeinstall_std
%find_lang %name-0.4

%clean
rm -rf %buildroot




