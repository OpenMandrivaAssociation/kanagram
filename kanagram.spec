Name:		kanagram
Summary:	Word learning program
Version: 4.9.3
Release: 1
Group:		Graphical desktop/KDE
License:	GPLv2 GFDL
URL:		http://edu.kde.org/kanagram
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	libkdeedu-devel >= %{version}
Requires:	libkdeedu = %{version}

%description
Kanagram is a replacement for KMessedWords. Kanagram mixes up the letters
of a word (creating an anagram), and you have to guess what the mixed up
word is. Kanagram features several built-in word lists, hints, and a cheat
feature which reveals the original word. Kanagram also has a vocabulary
editor, so you can make your own vocabularies, and distribute them through
Kanagram's KNewStuff download service.

%files
%doc ChangeLog TODO COPYING COPYING.DOC
%doc %{_kde_docdir}/HTML/en/kanagram
%{_kde_bindir}/kanagram
%{_kde_appsdir}/kanagram
%{_kde_iconsdir}/*/*/apps/kanagram*
%{_kde_applicationsdir}/kanagram.desktop
%{_kde_datadir}/config.kcfg/kanagram.kcfg
%{_kde_configdir}/kanagram.knsrc

#----------------------------------------------------------------------------

%define kanagramengine_major 4
%define libkanagramengine %mklibname kanagramengine %{kanagramengine_major}

%package -n %{libkanagramengine}
Summary:	Runtime library for KDE Education Application
Group:		System/Libraries
Conflicts:	%{name} < 4.8.97-2

%description -n %{libkanagramengine}
Runtime library for KDE Education Application.

%files -n %{libkanagramengine}
%{_kde_libdir}/libkanagramengine.so.%{kanagramengine_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkanagramengine} = %{version}-%{release}
Requires:	kdelibs4-devel
Requires:	libkdeedu-devel
Conflicts:	%{name} < 4.8.97-2

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_kde_libdir}/libkanagramengine.so
%{_includedir}/%{name}

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

