%define major 0
%define libname %mklibname visual %major
%define develname %mklibname -d visual
%define minor 0.4

Name: libvisual
Version: 0.4.0
Release: 13
Summary: Audio visualisation framework
Source0: %{name}-%{version}.tar.bz2
Source1: libvisual.rpmlintrc
Patch0: libvisual-0.4.0-fix-str-fmt.patch
Patch1:         libvisual-0.4.0-better-altivec-detection.patch
Patch2:         libvisual-0.4.0-inlinedefineconflict.patch
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

%files -n %libname -f %name-%{minor}.lang
%doc README NEWS TODO ChangeLog AUTHORS
%_libdir/libvisual-%{minor}.so.%{major}*

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
%patch1 -p1 -b .altivec-detection
%patch2 -p1 -b .inlinedefineconflict

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %name-%{minor}
