%define name libvisual
%define version 0.4.0
%define release %mkrel 2
%define major 0
%define libname %mklibname visual %major

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Audio visualisation framework
Source0: %{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://localhost.nl/~synap/libvisual
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

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

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
%configure2_5x
%make

%install
rm -rf %buildroot

%makeinstall_std
%find_lang %name-0.4

%clean
rm -rf %buildroot




