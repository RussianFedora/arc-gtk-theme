%global daterev	20151027git42114b

Name:		arc-gtk-theme
Version:	0.0
Release:	0.1.%{?daterev}%{?dist}
Summary:	Flat theme with transparent elements
Group:		User Interface/Desktops

License:	GPLv3
URL:		https://github.com/fdinardo/evopop-gtk-theme
Source0:	%{name}-%{version}-%{?daterev}.tar.xz

BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gtk3-devel

Requires:	gtk-murrine-engine >= 0.98.1.1
Requires:	gtk3 >= 3.14.0

BuildRequires:	git

BuildArch:	noarch

%description
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell.
It supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity,
Budgie, Pantheon, XFCE, Mate, etc.


%prep
%setup -q

%build
autoreconf -fi
%configure

%install
%{make_install}

%files
%defattr(-,root,root)
%doc AUTHORS README.md
%license COPYING
%{_datadir}/themes/Arc*

%changelog
* Sat Oct 31 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0-0.1.20151027git42114b.R
- initial build
