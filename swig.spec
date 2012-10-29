Summary:	Interface generator for Perl, Tcl, Guile and Python
Name:		swig
Version:	2.0.7
Release:	2
License:	distributable
Group:		Development/Languages
Source0:	http://downloads.sourceforge.net/swig/%{name}-%{version}.tar.gz
# Source0-md5:	8c2f6a9f51677647a64c8adb1b176299
Patch0:		%{name}-format.patch
Patch1:		swig-id3530078.patch
Patch2:		swig-pyint.patch
URL:		http://www.swig.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	python-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWIG is a compiler that attempts to make it easy to integrate C, C++,
or Objective-C code with scripting languages including Perl, Tcl, and
Python. In a nutshell, you give it a bunch of ANSI C/C++ declarations
and it generates an interface between C and your favorite scripting
language. However, this is only scratching the surface of what SWIG
can do--some of its more advanced features include automatic
documentation generation, module and library management, extensive
customization options, and more.

%package perl
Summary:	SWIG library: Perl
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
SWIG library: perl.

%package python
Summary:	SWIG library: python
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
SWIG library: python.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I Tools/config
%{__autoconf}
%{__automake}
%configure

%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	M4_INSTALL_DIR=$RPM_BUILD_ROOT%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc CHANGES CHANGES.current README ANNOUNCE TODO LICENSE
%attr(755,root,root) %{_bindir}/swig
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/%{version}/perl5
%exclude %{_datadir}/%{name}/%{version}/python

%files perl
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/perl5

%files python
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/python

