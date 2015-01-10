Summary:	Word learning program
Name:		kanagram
Version:	4.14.3
Release:	3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kanagram
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	libkdeedu-devel >= %{version}
Requires:	libkdeedu = %{version}
Obsoletes:	%{_lib}kanagramengine4 < 4.14
Obsoletes:	kanagram-devel < 4.14

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
%{_kde_applicationsdir}/kanagram.desktop
%{_kde_appsdir}/kanagram
%{_kde_appsdir}/plasma/packages/org.kde.kanagram
%{_kde_bindir}/kanagram
%{_kde_configdir}/kanagram.knsrc
%{_kde_datadir}/appdata/kanagram.appdata.xml
%{_kde_datadir}/config.kcfg/kanagram.kcfg
%{_kde_iconsdir}/*/*/apps/kanagram*

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

