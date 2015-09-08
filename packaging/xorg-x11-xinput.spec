%define _unpackaged_files_terminate_build 0

Name:	xorg-x11-xinput
Summary:    X.Org X11 xinput utility
Version: 1.6.0
Release:    2
Group:      System/X11
License:    MIT
URL:        http://www.x.org
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  xorg-x11-xutils-dev
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xinerama)

%description
Description: %{summary}

%prep
%setup -q

%build
%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}

%remove_docs

%make_install

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
%{_bindir}/xinput
#%{_mandir}/man1/xinput.1.gz

