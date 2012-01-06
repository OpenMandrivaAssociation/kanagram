Name: kanagram
Summary: Word learning program
Version: 4.7.97
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 GFDL
URL: http://edu.kde.org/kanagram
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%version
BuildRequires: libkdeedu-devel >= %version

Requires: libkdeedu = %version

Suggests: kanagram-handbook

%description
Kanagram is a replacement for KMessedWords. Kanagram mixes up the letters
of a word (creating an anagram), and you have to guess what the mixed up
word is. Kanagram features several built-in word lists, hints, and a cheat
feature which reveals the original word. Kanagram also has a vocabulary
editor, so you can make your own vocabularies, and distribute them through
Kanagram's KNewStuff download service. 

%files
%_kde_bindir/kanagram
%_kde_appsdir/kanagram
%_kde_iconsdir/*/*/apps/kanagram.*
%_kde_datadir/applications/kde4/kanagram.desktop
%_kde_datadir/config.kcfg/kanagram.kcfg
%_kde_datadir/config/kanagram.knsrc
%doc ChangeLog TODO COPYING COPYING.DOC
%doc %_kde_docdir/HTML/en/kanagram

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

