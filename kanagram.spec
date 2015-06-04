%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Word learning program
Name:		kanagram
Version:	15.04.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kanagram
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5I18n)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(LibKdeEdu)
BuildRequires:	cmake(LibKEduVocDocument)
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
%{_datadir}/applications/kanagram.desktop
%{_datadir}/kanagram
%{_kde_bindir}/kanagram
%{_sysconfdir}/xdg/kanagram.knsrc
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

