
Name:       xorg-x11-utils-xinput
Summary:    X.Org X11 xinput utility
Version:    1.5.2
Release:    2
Group:      System/X11
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/app/xinput-%{version}.tar.gz
Source1001: packaging/xorg-x11-utils-xinput.manifest 
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(inputproto)
Obsoletes:   xorg-x11-app-xinput


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install





%files
%manifest xorg-x11-utils-xinput.manifest
%defattr(-,root,root,-)
%{_bindir}/xinput
%{_mandir}/man1/xinput.1.gz


