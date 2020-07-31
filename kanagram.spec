%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Word learning program
Name:		kanagram
Version:	20.07.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kanagram
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cmake(ECM)
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
BuildRequires:	cmake(LibKEduVocDocument)
BuildRequires:	cmake(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5TextToSpeech)
Obsoletes:	%{_lib}kanagramengine4 < 4.14
Obsoletes:	kanagram-devel < 4.14

%description
Kanagram is a replacement for KMessedWords. Kanagram mixes up the letters
of a word (creating an anagram), and you have to guess what the mixed up
word is. Kanagram features several built-in word lists, hints, and a cheat
feature which reveals the original word. Kanagram also has a vocabulary
editor, so you can make your own vocabularies, and distribute them through
Kanagram's KNewStuff download service.

%files -f kanagram.lang
%doc ChangeLog TODO COPYING COPYING.DOC
%{_datadir}/applications/org.kde.kanagram.desktop
%{_datadir}/kanagram
%{_bindir}/kanagram
%{_sysconfdir}/xdg/kanagram.knsrc
%{_datadir}/metainfo/org.kde.kanagram.appdata.xml
%{_datadir}/config.kcfg/kanagram.kcfg
%{_iconsdir}/*/*/apps/kanagram*

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kanagram --with-html
