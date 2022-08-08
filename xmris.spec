Name:           xmris
Version:        4.0.5
Release:        18%{?dist}
Summary:        Maze digging and cherry eating game
Group:          Amusements/Games
License:        GPL+
URL:            http://sourceforge.net/projects/xmris/
Source0:        http://downloads.sourceforge.net/xmris/xmris.%{version}.tar.gz
# These were created from screenshots from the game
Source1:        xmris.png
Source2:        xmsit.png
# Various fixes
Patch1:         0001-Fix-xm-exiting-with-a-BadFont-error.patch
Patch2:         0002-Fix-timer-signal-handling-under-Linux.patch
Patch3:         0003-Adjust-Imakefile-for-modern-systems.patch
Patch4:         0004-Catch-the-window-being-deleted.patch
Patch5:         0005-Fix-compiling-of-flock-code-under-Linux.patch
Patch6:         0006-Fix-key-presses-getting-lost.patch
Patch7:         0007-Change-key-binding-defaults-to-something-sane.patch
Patch8:         0008-Fix-compiler-warnings.patch
# Patches for safe global highscore handling
Patch9:        0009-Remove-TRANSPUTER-stuff.patch
Patch10:        0010-Remove-USELOCKFILE-stuff.patch
Patch11:        0011-Remove-seteuid-stuff.patch
Patch12:        0012-Drop-dir-option.patch
Patch13:        0013-Drop-support-for-global-personal-file.patch
Patch14:        0014-Some-renames.patch
Patch15:        0015-Open-score-files-only-once-and-keep-them-open-till-t.patch
Patch16:        0016-Open-the-global-score-file-asap-and-drop-special-rig.patch
# Misc patches
Patch17:        0017-Set-class-to-Xmsit-Xmris-depending-on-how-we-re-laun.patch
Patch18:        0018-Install-manpages-into-section-6-rather-then-1.patch
Patch19:        0019-Add-.desktop-files.patch
BuildRequires:  libXt-devel libXaw-devel groff imake desktop-file-utils
Requires:       hicolor-icon-theme
Requires:       xorg-x11-fonts-ISO8859-1-75dpi
Requires:       xorg-x11-fonts-ISO8859-1-100dpi

%description
You control a gnome, who can walk around a garden, along paths  already
marked,  or  create  new paths wherever you wish. You also have a ball,
which can be thrown in the direction you're facing, towards the gnome's
feet.  Points  are scored for collecting cherries (if you collect eight
cherries without stopping or  pushing  an  apple,  you  get  a  bonus),
killing monsters (by squashing them, or throwing the ball at them), and
collecting the prize left when all the monsters have come out of  their
den.


%package        editor
Summary:        Level editor for %{name}
Requires:       %{name} = %{version}-%{release}

%description    editor
A level editor for %{name}.


%prep
%setup -q -n %{name}.%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1


%build
xmkmf
make %{?_smp_mflags} CDEBUGFLAGS="$RPM_OPT_FLAGS"


%install
make install install.man DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT/usr/lib/X11/app-defaults

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/games
touch $RPM_BUILD_ROOT%{_localstatedir}/games/%{name}.score

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications xm*.desktop


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root,-)
%doc CHANGES* COPYING-2.0 COPYRIGHT README.xmris
%attr(2755,root,games) %{_bindir}/%{name}
%{_bindir}/xmsit
%{_datadir}/%{name}
%{_datadir}/X11/app-defaults/Xm*
%{_datadir}/applications/xmris.desktop
%{_datadir}/applications/xmsit.desktop
%{_datadir}/icons/hicolor/128x128/apps/xm*.png
%{_mandir}/man6/xmris.6*
%{_mandir}/man6/xmsit.6*
%verify(not md5 size mtime) %config(noreplace) %attr(0664,root,games) %{_localstatedir}/games/%{name}.score

%files editor
%defattr(-,root,root,-)
%doc README.xmred
%{_bindir}/xmred
%{_datadir}/applications/xmred.desktop
%{_mandir}/man6/xmred.6*


%changelog
* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.0.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.0.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.5-10
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 4.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 21 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 4.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 4.0.5-4
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat May 21 2011 Hans de Goede <j.w.r.degoede@gmail.com> 4.0.5-2
- Add missing BuildRequires: libXaw-devel groff
- Change font requires to: xorg-x11-fonts-ISO8859-1-75dpi + 100dpi

* Tue May  3 2011 Hans de Goede <j.w.r.degoede@gmail.com> 4.0.5-1
- Initial rpmfusion package
