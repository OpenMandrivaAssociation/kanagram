%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Word learning program
Name:		plasma6-kanagram
Version:	24.01.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kanagram
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kanagram-%{version}.tar.xz
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	%{mklibname -d KEduVocDocument6}
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6TextToSpeech)

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
%{_datadir}/metainfo/org.kde.kanagram.appdata.xml
%{_datadir}/config.kcfg/kanagram.kcfg
%{_datadir}/knsrcfiles/kanagram.knsrc
%{_iconsdir}/*/*/apps/kanagram*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kanagram-%{version}
%cmake \
	-DQT_MAJOR_VERSION=6 \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kanagram --with-html
