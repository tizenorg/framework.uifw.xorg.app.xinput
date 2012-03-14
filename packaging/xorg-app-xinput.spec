Name:       xorg-app-xinput
Summary:    X.Org X11 xinput utility
Version:    1.5.2
Release:    2
Group:      System/X11
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/app/xinput-%{version}.tar.gz
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(inputproto)


%description
Description: %{summary}



%prep
%setup -q -n xinput-%{version}


%build
%reconfigure --libdir=%{_datadir}
make %{?jobs:-j%jobs}

%install
%make_install



%docs_package


%files
%{_bindir}/xinput


