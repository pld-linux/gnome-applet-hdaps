%define		_realname	gnome-hdaps-applet
%define		_snap		20060120
Summary:	GNOME-based panel applet for monitoring the HDAPS protection status
Summary(pl):	Aplet panelu GNOME do monitorowania stanu zabezpieczenia HDAPS
Name:		gnome-applet-hdaps
Version:	0.1.%{_snap}
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://www.zen24593.zen.co.uk/hdaps/%{_realname}-%{_snap}.tar.gz
# Source0-md5:	43ff308ccf5d15625e9f8f157bfc4bbc
URL:		http://www.zen24593.zen.co.uk/hdaps/
BuildRequires:	gnome-panel-devel >= 2.4.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monitors the /sys/block/xxx/queue/protect file and displays a
graphical representation of the HDAPS protection status. Looks for the
protect file under hda and sda and will use whichever is found first
(lame but works for now).

%description -l pl
Ten aplet monitoruje plik /sys/block/xxx/queue/protect i wy¶wietla
graficzn± reprezentacjê stanu zabezpieczenia HDAPS. Szuka pliku
protect w katalogach hda i sda i u¿ywa tego, który znajdzie jako
pierwszy (prymitywne, ale dzia³a).

%prep
%setup -q -c

%build
%{__cc} %{rpmldflags} %{rpmcflags} $(pkg-config --cflags --libs libpanelapplet-2.0) -o gnome-hdaps-applet gnome-hdaps-applet.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/bonobo/servers/,%{_pixmapsdir}/%{_realname}}
install %{_realname}  $RPM_BUILD_ROOT%{_bindir}
install *.png  $RPM_BUILD_ROOT%{_pixmapsdir}/%{_realname}
install *.server $RPM_BUILD_ROOT%{_libdir}/bonobo/servers

##%%find_lang hdaps-applet --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{_realname}.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall %{_realname}.schemas

%postun
%scrollkeeper_update_postun

%files 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{_realname}
%{_libdir}/bonobo/servers/*.server
%{_pixmapsdir}/%{_realname}
%{_pixmapsdir}/%{_realname}/*.png
