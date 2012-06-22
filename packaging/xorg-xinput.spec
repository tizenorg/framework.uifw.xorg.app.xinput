Name:           xorg-xinput
Version:        1.5.2
Release:        2
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          System/X11
Source0:        http://xorg.freedesktop.org/releases/individual/app/xinput-%{version}.tar.gz
Source1001:     packaging/xorg-xinput.manifest
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-macros)
Obsoletes:      xorg-x11-app-xinput

%description
Description: %{summary}

%prep
%setup -q -n xinput-%{version}


%build
cp %{SOURCE1001} .

%reconfigure --libdir=%{_datadir}

make %{?_smp_mflags}

%install
%make_install





%files
%manifest xorg-xinput.manifest
%{_bindir}/xinput
%{_mandir}/man1/xinput.1.gz
