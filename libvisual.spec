%define api	0.4
%define major	0
%define libname %mklibname visual %{api} %{major}
%define devname %mklibname -d visual

Summary:	Audio visualisation framework
Name:		libvisual
Version:	0.4.0
Release:	22
License:	LGPLv2+
Group:		System/Libraries
Url:		http://localhost.nl/~synap/libvisual
Source0:	%{name}-%{version}.tar.bz2
Patch0:		libvisual-0.4.0-fix-str-fmt.patch
Patch1:		libvisual-0.4.0-better-altivec-detection.patch
Patch2:		libvisual-0.4.0-inlinedefineconflict.patch

%description
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

Libvisual is aimed at developers who have a need for audio
visualisation and those who actually write the visualisation plugins.

%package -n %{libname}
Summary:	Shared library of the audio visualisation framework 
Group:		System/Libraries
Suggests:	libvisual-plugins
Obsoletes:	%{_lib}visual0 < 0.4.0-14

%description -n %{libname}
Libvisual is a library that acts as a middle layer between
applications that want audio visualisation and audio visualisation
plugins.

Libvisual is aimed at developers who have a need for audio
visualisation and those who actually write the visualisation plugins.

%package -n %{devname}
Summary:	Header files of the audio visualisation framework 
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libvisual-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}-%{api}

%files -n %{libname} -f %{name}-%{api}.lang
%doc README NEWS TODO ChangeLog AUTHORS
%{_libdir}/libvisual-%{api}.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

